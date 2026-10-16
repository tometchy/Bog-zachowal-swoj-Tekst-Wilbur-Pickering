import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { test } from "node:test";
import { runInContext, createContext } from "node:vm";

const html = readFileSync(new URL("../docs/compare.html", import.meta.url), "utf8");
const inlineScript = html.match(/<script type="module">([\s\S]*?)<\/script>/)?.[1];
assert.ok(inlineScript, "The compare page must contain its application script");
// Execute the actual application, replacing only the browser's PDF.js import.
// Empty .document results keep PDF rendering outside these synchronization tests.
const applicationScript = inlineScript.replace(
  /^\s*import \* as pdfjsLib from "\.\/vendor\/pdfjs\/pdf\.min\.mjs";$/m,
  "const pdfjsLib = { GlobalWorkerOptions: {} };"
);
const prefix = "pdf-comparison:";
const configuration = {
  [`${prefix}sync:owner`]: "test-owner",
  [`${prefix}sync:repository`]: "test-highlights",
  [`${prefix}sync:path`]: "highlights.json",
  [`${prefix}sync:token`]: "fake-test-token",
  [`${prefix}sync:mode`]: "write"
};

class MockElement {
  listeners = new Map();
  children = new Map();
  dataset = {};
  elements = {};
  classList = { toggle() {}, remove() {}, contains() { return false; } };

  addEventListener(type, callback) {
    if (!this.listeners.has(type)) this.listeners.set(type, new Set());
    this.listeners.get(type).add(callback);
  }

  removeEventListener(type, callback) {
    this.listeners.get(type)?.delete(callback);
  }

  dispatchEvent(event) {
    for (const callback of this.listeners.get(event.type) || []) callback(event);
    return !event.defaultPrevented;
  }

  async emit(type, event = {}) {
    for (const callback of this.listeners.get(type) || []) await callback({ type, ...event });
  }

  querySelector(selector) {
    if (!this.children.has(selector)) this.children.set(selector, new MockElement());
    return this.children.get(selector);
  }

  querySelectorAll() { return []; }
  setAttribute() {}
  append() {}
  remove() {}
  close() {}
  showModal() {}
}

function response(status, body = {}) {
  return { status, ok: status >= 200 && status < 300, json: async () => body };
}

function deferred() {
  let resolve;
  const promise = new Promise((done) => { resolve = done; });
  return { promise, resolve };
}

async function createApp(initialStorage = {}) {
  const values = new Map(Object.entries(initialStorage));
  const storage = {
    get length() { return values.size; },
    key: (index) => [...values.keys()][index] ?? null,
    getItem: (key) => values.get(key) ?? null,
    setItem: (key, value) => values.set(key, String(value)),
    removeItem: (key) => values.delete(key)
  };
  const document = new MockElement();
  document.createElement = () => new MockElement();
  document.visibilityState = "visible";
  const form = document.querySelector("#sync-form");
  for (const name of ["owner", "repository", "path", "token", "mode"]) {
    form.elements[name] = { value: "" };
  }
  const window = new MockElement();
  window.location = { href: "https://example.test/compare.html" };
  const requests = [];
  const replies = [];
  let timerId = 0;
  const context = createContext({
    document,
    window,
    localStorage: storage,
    history: { replaceState() {} },
    URL,
    TextEncoder,
    TextDecoder,
    atob,
    btoa,
    CustomEvent: class {
      constructor(type, options = {}) { this.type = type; this.detail = options.detail; }
    },
    console: { error() {} },
    setTimeout: () => ++timerId,
    clearTimeout() {},
    setInterval() {},
    fetch: async (url, options = {}) => {
      requests.push({ url, ...options });
      const next = replies.shift();
      // No real requests are made; an absent remote file is the default.
      if (next instanceof Error) throw next;
      return next ?? response(404);
    }
  });
  runInContext(applicationScript, context, { filename: "docs/compare.html" });
  // Finish the optional startup pull, without advancing any autosync timers.
  await new Promise(setImmediate);
  return {
    context, storage, document, window, requests, replies,
    unload() {
      const event = {
        type: "beforeunload",
        defaultPrevented: false,
        returnValue: undefined,
        preventDefault() { this.defaultPrevented = true; }
      };
      window.dispatchEvent(event);
      return event;
    },
    listenerCount() { return window.listeners.get("beforeunload")?.size ?? 0; }
  };
}

function expectWarning(app, expected) {
  const event = app.unload();
  assert.equal(event.defaultPrevented, expected);
  assert.equal(Boolean(event.returnValue), expected);
  assert.equal(app.listenerCount(), expected ? 1 : 0);
}

function addHighlight(app) {
  app.storage.setItem(`${prefix}polish:highlights:1`, JSON.stringify([
    { tool: "light", points: [[0.1, 0.2], [0.3, 0.2]] }
  ]));
  app.context.highlightDataChanged();
}

test("a clean page has no unload warning or beforeunload listener", async () => {
  const app = await createApp(configuration);
  expectWarning(app, false);
});

test("local changes warn, persist their pending state, and do not duplicate the listener", async () => {
  const app = await createApp(configuration);
  addHighlight(app);
  app.context.highlightDataChanged();
  expectWarning(app, true);
  assert.equal(app.storage.getItem(`${prefix}sync:pending`), "true");
  // Cancelling a navigation must not clear changes or remove the protection.
  expectWarning(app, true);
  assert.equal(app.storage.getItem(`${prefix}sync:pending`), "true");
});

test("pending changes restored from storage are protected immediately", async () => {
  const app = await createApp({ ...configuration, [`${prefix}sync:pending`]: "true" });
  expectWarning(app, true);
  assert.equal(app.requests.length, 0, "startup must wait for the retry timer");
});

test("the warning stays during upload and disappears only after successful completion", async () => {
  const app = await createApp(configuration);
  addHighlight(app);
  const upload = deferred();
  app.replies.push(response(404), upload.promise);
  const pushing = app.context.pushHighlights();
  await new Promise(setImmediate);
  assert.equal(app.requests.at(-1).method, "PUT");
  expectWarning(app, true);
  upload.resolve(response(200, { content: { sha: "uploaded-sha" } }));
  assert.equal(await pushing, true);
  expectWarning(app, false);
  assert.equal(app.storage.getItem(`${prefix}sync:pending`), "false");
});

test("an unsuccessful GitHub response leaves changes protected", async () => {
  const app = await createApp(configuration);
  addHighlight(app);
  app.replies.push(response(404), response(500));
  assert.equal(await app.context.pushHighlights(), false);
  expectWarning(app, true);
  assert.equal(app.storage.getItem(`${prefix}sync:pending`), "true");
});

test("a network failure leaves the warning until a successful retry", async () => {
  const app = await createApp(configuration);
  addHighlight(app);
  app.replies.push(new Error("offline"));
  assert.equal(await app.context.pushHighlights(), false);
  expectWarning(app, true);
  app.replies.push(response(404), response(200, { content: { sha: "retry-sha" } }));
  assert.equal(await app.context.pushHighlights(), true);
  expectWarning(app, false);
});

test("new changes made during upload remain protected after the older upload succeeds", async () => {
  const app = await createApp(configuration);
  addHighlight(app);
  const upload = deferred();
  app.replies.push(response(404), upload.promise);
  const pushing = app.context.pushHighlights();
  await new Promise(setImmediate);
  assert.equal(app.requests.at(-1).method, "PUT");
  app.context.highlightDataChanged();
  upload.resolve(response(200, { content: { sha: "older-version" } }));
  assert.equal(await pushing, true);
  expectWarning(app, true);
  assert.equal(app.storage.getItem(`${prefix}sync:pending`), "true");
  app.replies.push(response(404), response(200, { content: { sha: "latest-version" } }));
  assert.equal(await app.context.pushHighlights(), true);
  expectWarning(app, false);
});

test("deleting the last highlight is an unsent change even when no strokes remain", async () => {
  const app = await createApp(configuration);
  app.storage.setItem(`${prefix}polish:highlights:1`, "[]");
  app.context.highlightDataChanged();
  assert.equal(Object.keys(app.context.localHighlightData().highlights.polish).length, 0);
  expectWarning(app, true);
});

test("applying remote highlights clears the warning", async () => {
  const app = await createApp(configuration);
  addHighlight(app);
  app.context.applyHighlightData({ version: 1, highlights: { english: {}, polish: {} } });
  expectWarning(app, false);
  assert.equal(app.storage.getItem(`${prefix}sync:pending`), "false");
});

test("disabling synchronization removes the warning without deleting local highlights", async () => {
  const app = await createApp(configuration);
  addHighlight(app);
  await app.document.querySelector("#sync-disable").emit("click");
  expectWarning(app, false);
  assert.ok(app.storage.getItem(`${prefix}polish:highlights:1`));
  assert.equal(app.storage.getItem(`${prefix}sync:token`), null);
});

test("read-only mode does not produce a false unsent-changes warning", async () => {
  const app = await createApp({ ...configuration, [`${prefix}sync:mode`]: "read" });
  app.context.highlightDataChanged();
  expectWarning(app, false);
  assert.equal(await app.context.pushHighlights(), false);
});

test("unconfigured local-only mode does not produce a false synchronization warning", async () => {
  const app = await createApp();
  addHighlight(app);
  expectWarning(app, false);
  assert.equal(await app.context.pushHighlights(), false);
  assert.equal(app.requests.length, 0);
});
