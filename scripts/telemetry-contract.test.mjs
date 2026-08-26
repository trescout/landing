import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import vm from 'node:vm';

const source = await readFile(new URL('../assets/telemetry.js', import.meta.url), 'utf8');

function harness({ consent = null, va = null, pathname = '/discover/example/', search = '' } = {}) {
  const values = new Map();
  if (consent) values.set('ts_telemetry_consent', consent);
  const calls = [];
  const listeners = new Map();
  const localStorage = {
    getItem: (key) => values.has(key) ? values.get(key) : null,
    setItem: (key, value) => values.set(key, String(value)),
    removeItem: (key) => values.delete(key),
  };
  const document = {
    readyState: 'complete',
    documentElement: { lang: 'tr' },
    querySelectorAll: () => [],
    addEventListener: (name, fn) => listeners.set(name, fn),
  };
  const window = {
    location: { hostname: 'example.test', origin: 'https://example.test', pathname, search },
    localStorage,
    dispatchEvent: () => true,
    addEventListener: (name, fn) => listeners.set(`window:${name}`, fn),
  };
  if (va) window.va = (...args) => calls.push(args);

  const context = {
    window,
    document,
    URL,
    URLSearchParams,
    CustomEvent: class CustomEvent { constructor(type, init) { this.type = type; this.detail = init.detail; } },
    console: { log() {} },
    setTimeout,
    clearTimeout,
    Date,
  };
  vm.runInNewContext(source, context);

  return {
    api: window.TreScoutTelemetry,
    window,
    keys: () => [...values.keys()].sort(),
    calls,
    dispatchStorage: (event) => listeners.get('window:storage')?.(event),
  };
}

test('telemetry does not write state or emit events before explicit consent', () => {
  const app = harness();
  assert.equal(app.api.getConsent(), 'unknown');
  assert.equal(app.api.track('discovery_view'), false);
  assert.deepEqual(app.keys(), []);
  assert.equal(app.api.getPendingCount(), 0);
});

test('consented events wait for provider readiness and flush later', () => {
  const app = harness({ consent: 'granted', va: null });
  assert.equal(app.api.getConsent(), 'granted');
  assert.ok(app.keys().includes('ts_first_seen'));
  assert.ok(app.api.getPendingCount() >= 1);

  const sent = [];
  app.window.va = (...args) => sent.push(args);
  app.api.flush();
  assert.equal(app.api.getPendingCount(), 0);
  assert.ok(sent.length >= 1);
});

test('denying telemetry clears retention state and queued events', () => {
  const app = harness({ consent: 'granted', va: null });
  assert.ok(app.api.getPendingCount() >= 1);
  app.api.setConsent('denied');
  assert.equal(app.api.getConsent(), 'denied');
  assert.deepEqual(app.keys(), ['ts_telemetry_consent']);
  assert.equal(app.api.getPendingCount(), 0);
});

test('telemetry payload is allowlisted and strips PII-like UTM and href values', () => {
  const app = harness({
    consent: 'granted',
    va: true,
    pathname: '/reports/2026-08-25/',
    search: '?utm_source=alice%40example.com&utm_campaign=launch_2026',
  });
  app.api.track('beta_report_open', {
    href: 'https://evil.test/?email=alice%40example.com',
    referrer: 'https://evil.test/private/alice',
  });
  const payload = app.calls.at(-1)[1].data;
  assert.equal(payload.path, '/reports/2026-08-25/');
  assert.equal(payload.href, undefined);
  assert.equal(payload.referrer, undefined);
  assert.equal(payload.utm_source, undefined);
  assert.equal(payload.utm_campaign, 'launch_2026');
});

test('cross-tab denial clears local retention state and pending events', () => {
  const app = harness({ consent: 'granted', va: null });
  assert.ok(app.api.getPendingCount() >= 1);
  app.dispatchStorage({ key: 'ts_telemetry_consent', newValue: 'denied' });
  assert.equal(app.api.getConsent(), 'granted');
  assert.deepEqual(app.keys(), ['ts_telemetry_consent']);
  assert.equal(app.api.getPendingCount(), 0);
  // The storage event changes this runtime immediately; the other tab owns the
  // consent key, so this harness keeps its original storage value.
});
