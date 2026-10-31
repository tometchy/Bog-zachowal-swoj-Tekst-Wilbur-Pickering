import assert from "node:assert/strict";
import { test } from "node:test";
import { IDBFactory } from "fake-indexeddb";
import { createHighlightStore } from "../docs/highlight-store.mjs";

const stroke = { tool: "light", points: [[0.1, 0.2], [0.3, 0.2]] };
const key = (name, page) => `pdf-comparison:${name}:highlights:${page}`;

function storage(initial = {}) {
  const values = new Map(Object.entries(initial));
  return {
    full: false,
    get length() { return values.size; },
    key: (index) => [...values.keys()][index],
    getItem: (key) => values.get(key) ?? null,
    setItem(key, value) {
      if (this.full) throw new DOMException("Storage full", "QuotaExceededError");
      values.set(key, String(value));
    },
    removeItem: (key) => values.delete(key)
  };
}

test("full localStorage migrates both PDFs, preserves precision and reloads new strokes", async () => {
  const legacy = { ...stroke, points: [[0.1234567890123456, 0.9876543210987654]] };
  const local = storage({ [key("english", 2)]: JSON.stringify([legacy]), [key("polish", 3)]: JSON.stringify([stroke]) });
  local.full = true;
  const databaseFactory = new IDBFactory();
  const store = await createHighlightStore({ storage: local, databaseFactory });
  assert.equal(local.length, 0, "legacy copies are freed after migration commits");
  assert.deepEqual(store.get("english", 2), [legacy]);
  assert.deepEqual(store.get("polish", 3), [stroke]);
  await store.set("english", 2, [...store.get("english", 2), stroke]);
  await store.set("polish", 3, [...store.get("polish", 3), stroke]);
  const reloaded = await createHighlightStore({ storage: local, databaseFactory });
  assert.deepEqual(reloaded.get("english", 2), [legacy, stroke]);
  assert.equal(reloaded.get("polish", 3).length, 2);
  assert.equal(store.unsaved, false);
});

test("a failed migration retains all legacy data and still allows drawing", async () => {
  const local = storage({ [key("english", 2)]: JSON.stringify([stroke]), [key("polish", 3)]: JSON.stringify([stroke]) });
  const errors = [];
  const databaseFactory = { open() { throw new Error("Database unavailable"); } };
  const store = await createHighlightStore({ storage: local, databaseFactory, onError: (error) => errors.push(error) });
  assert.equal(local.length, 2);
  assert.equal(errors.length, 1);
  await store.set("polish", 3, [stroke, stroke]);
  assert.equal(JSON.parse(local.getItem(key("polish", 3))).length, 2);
});

test("aborting the migration transaction keeps legacy copies intact for a later retry", async () => {
  const local = storage({ [key("english", 2)]: JSON.stringify([stroke]), [key("polish", 3)]: JSON.stringify([stroke]) });
  const factory = new IDBFactory();
  const failingFactory = {
    open(...args) {
      const request = factory.open(...args);
      request.addEventListener("success", () => {
        const database = request.result;
        const original = database.transaction.bind(database);
        database.transaction = (...args) => {
          const tx = original(...args);
          if (args[1] === "readwrite") queueMicrotask(() => tx.abort());
          return tx;
        };
      });
      return request;
    }
  };
  const store = await createHighlightStore({ storage: local, databaseFactory: failingFactory });
  assert.equal(local.length, 2);
  assert.equal(store.get("english", 2).length, 1);
  assert.equal(store.get("polish", 3).length, 1);
  const retried = await createHighlightStore({ storage: local, databaseFactory: factory });
  assert.equal(local.length, 0);
  assert.equal(retried.get("english", 2).length, 1);
  assert.equal(retried.get("polish", 3).length, 1);
});

test("quota failures preserve consecutive strokes for drawing and GitHub, retry saves all pages", async () => {
  const local = storage();
  const errors = [];
  const store = await createHighlightStore({ storage: local, onError: (error) => errors.push(error) });
  local.full = true;
  await assert.rejects(store.set("english", 1, [stroke]), { name: "QuotaExceededError" });
  await assert.rejects(store.set("polish", 2, [stroke]), { name: "QuotaExceededError" });
  await assert.rejects(store.set("english", 1, [...store.get("english", 1), stroke]));
  assert.equal(store.unsaved, true);
  assert.equal(store.get("english", 1).length, 2);
  assert.equal(store.snapshot().english[1].length, 2);
  assert.equal(store.snapshot().polish[2].length, 1);
  local.full = false;
  await store.set("polish", 2, [stroke, stroke]);
  assert.equal(store.unsaved, false);
  const reloaded = await createHighlightStore({ storage: local });
  assert.equal(reloaded.get("english", 1).length, 2);
  assert.equal(reloaded.get("polish", 2).length, 2);
});

test("remote replacement removes old pages durably and retains the sync JSON format", async () => {
  const options = { storage: storage(), databaseFactory: new IDBFactory() };
  const store = await createHighlightStore(options);
  await store.set("english", 10, [stroke]);
  await store.set("polish", 20, [stroke]);
  const remote = { english: { 2: [stroke] }, polish: { 3: [stroke] } };
  await store.replace(remote);
  assert.deepEqual(store.snapshot(), remote);
  const reloaded = await createHighlightStore(options);
  assert.deepEqual(reloaded.snapshot(), remote);
});

test("legacy copies left after migration cannot resurrect erased strokes", async () => {
  const local = storage({ [key("english", 2)]: JSON.stringify([stroke]) });
  local.removeItem = () => { throw new Error("Removal unavailable"); };
  const options = { storage: local, databaseFactory: new IDBFactory() };
  const store = await createHighlightStore(options);
  await store.set("english", 2, []);
  const reloaded = await createHighlightStore(options);
  assert.deepEqual(reloaded.get("english", 2), []);
});

test("overlapping saves keep the latest page version and never clear a pending write early", async () => {
  const options = { storage: storage(), databaseFactory: new IDBFactory() };
  const store = await createHighlightStore(options);
  const first = store.set("english", 2, [stroke]);
  const second = store.set("english", 2, [stroke, stroke]);
  assert.equal(store.unsaved, true);
  await Promise.all([first, second]);
  assert.equal(store.unsaved, false);
  const reloaded = await createHighlightStore(options);
  assert.equal(reloaded.get("english", 2).length, 2);
});
