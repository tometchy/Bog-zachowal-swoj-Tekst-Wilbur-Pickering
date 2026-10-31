// Keep drawing and GitHub snapshots independent of browser storage write failures.
// Only highlights use IndexedDB; the small UI/sync settings stay in localStorage.
export async function createHighlightStore({ storage, databaseFactory, onChange = () => {}, onError = () => {} }) {
  const prefix = "pdf-comparison:";
  const legacyPattern = /^pdf-comparison:(english|polish):highlights:(\d+)$/;
  const pages = new Map();
  const dirty = new Map();
  let revision = 0;
  let database;
  let queue = Promise.resolve();

  function transaction(write, action) {
    return new Promise((resolve, reject) => {
      const tx = database.transaction("pages", write ? "readwrite" : "readonly");
      tx.oncomplete = resolve;
      tx.onabort = () => reject(tx.error || new Error("Przerwano zapis zakreśleń."));
      tx.onerror = () => {}; // onabort reports the final transaction outcome.
      action(tx.objectStore("pages"));
    });
  }

  const legacy = new Map();
  try {
    for (let index = 0; index < storage.length; index += 1) {
      const key = storage.key(index);
      const match = key?.match(legacyPattern);
      if (!match) continue;
      const strokes = JSON.parse(storage.getItem(key) || "[]");
      if (Array.isArray(strokes)) legacy.set(key, strokes);
    }
  } catch (error) { onError(error); }

  try {
    if (!databaseFactory) throw new Error("IndexedDB jest niedostępne.");
    database = await new Promise((resolve, reject) => {
      const request = databaseFactory.open("pdf-comparison-highlights", 1);
      request.onupgradeneeded = () => request.result.createObjectStore("pages");
      request.onsuccess = () => resolve(request.result);
      request.onerror = () => reject(request.error);
      request.onblocked = () => reject(new Error("Baza zakreśleń jest zablokowana przez inną kartę."));
    });
    let migrated = false;
    await transaction(false, (store) => {
      const cursor = store.openCursor();
      cursor.onsuccess = () => {
        const entry = cursor.result;
        if (!entry) return;
        if (entry.key === "migrated") migrated = true;
        else pages.set(entry.key, entry.value);
        entry.continue();
      };
    });
    if (!migrated) {
      for (const [key, strokes] of legacy) {
        const match = key.match(legacyPattern);
        pages.set(`${match[1]}:${match[2]}`, strokes);
      }
      await transaction(true, (store) => {
        for (const [key, strokes] of pages) store.put(strokes, key);
        store.put(true, "migrated");
      });
    }
    // Remove old copies only after the migration transaction has committed.
    // The marker prevents leftover copies resurrecting erased strokes later.
    for (const key of legacy.keys()) {
      try { storage.removeItem(key); } catch (_) { /* Already safe in IndexedDB. */ }
    }
  } catch (error) {
    database?.close();
    database = undefined;
    for (const [key, strokes] of legacy) {
      const match = key.match(legacyPattern);
      pages.set(`${match[1]}:${match[2]}`, strokes);
    }
    onError(error);
  }

  function persist() {
    onChange();
    const task = queue.then(async () => {
      const changes = new Map(dirty);
      if (database) {
        await transaction(true, (store) => {
          for (const key of changes.keys()) store.put(pages.get(key), key);
        });
      } else {
        for (const key of changes.keys()) {
          const [name, page] = key.split(":");
          storage.setItem(`${prefix}${name}:highlights:${page}`, JSON.stringify(pages.get(key)));
        }
      }
      for (const [key, version] of changes) {
        if (dirty.get(key) === version) dirty.delete(key);
      }
    });
    queue = task.catch(onError).finally(onChange);
    return task;
  }

  return {
    get unsaved() { return dirty.size > 0; },
    get(name, page) { return pages.get(`${name}:${page}`) || []; },
    snapshot() {
      const highlights = { english: {}, polish: {} };
      for (const [key, strokes] of pages) {
        const [name, page] = key.split(":");
        if (strokes.length) highlights[name][page] = strokes;
      }
      return highlights;
    },
    set(name, page, strokes) {
      const key = `${name}:${page}`;
      pages.set(key, strokes);
      dirty.set(key, ++revision);
      return persist();
    },
    replace(highlights) {
      // Empty pages are tombstones too, so a reload cannot restore old strokes.
      for (const key of pages.keys()) {
        pages.set(key, []);
        dirty.set(key, ++revision);
      }
      for (const name of ["english", "polish"]) {
        for (const [page, strokes] of Object.entries(highlights[name] || {})) {
          if (!/^\d+$/.test(page) || !Array.isArray(strokes)) continue;
          const key = `${name}:${page}`;
          pages.set(key, strokes);
          dirty.set(key, ++revision);
        }
      }
      return persist();
    }
  };
}
