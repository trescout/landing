import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import vm from 'node:vm';

const source = await readFile(new URL('../assets/provider-consent.js', import.meta.url), 'utf8');

function harness(initialConsent = null) {
  const values = new Map();
  if (initialConsent) values.set('ts_telemetry_consent', initialConsent);
  const listeners = new Map();
  const appended = [];
  const inert = [
    '/_vercel/insights/script.js',
    '/_vercel/speed-insights/script.js',
    'https://attacker.example/provider.js',
  ].map((src) => ({
    attributes: { 'data-consent-src': src },
    getAttribute(name) { return this.attributes[name] || null; },
    parentNode: { insertBefore(node) { appended.push(node); } },
  }));
  const localStorage = {
    getItem: (key) => values.has(key) ? values.get(key) : null,
    setItem: (key, value) => values.set(key, String(value)),
    removeItem: (key) => values.delete(key),
  };
  const document = {
    querySelectorAll: () => inert,
    createElement: () => ({
      setAttribute() {},
    }),
  };
  const window = {
    location: { origin: 'https://example.test' },
    localStorage,
    addEventListener: (name, fn) => listeners.set(name, fn),
  };
  const context = { window, document, URL, console: { log() {} } };
  vm.runInNewContext(source, context);

  return {
    values,
    appended,
    consentEvent: () => listeners.get('trescout:telemetry-consent')?.({}),
    storageEvent: (event) => listeners.get('storage')?.(event),
  };
}

test('does not append provider scripts without explicit consent', () => {
  const app = harness();
  assert.equal(app.appended.length, 0);
});

test('loads only same-origin allowlisted providers after consent and stays idempotent', () => {
  const app = harness();
  app.values.set('ts_telemetry_consent', 'granted');
  app.consentEvent();
  assert.deepEqual(app.appended.map((script) => script.src), [
    '/_vercel/insights/script.js',
    '/_vercel/speed-insights/script.js',
  ]);
  app.consentEvent();
  assert.equal(app.appended.length, 2);
});

test('loads providers when another tab grants consent', () => {
  const app = harness();
  app.values.set('ts_telemetry_consent', 'granted');
  app.storageEvent({ key: 'ts_telemetry_consent', newValue: 'granted' });
  assert.equal(app.appended.length, 2);
});
