import assert from 'node:assert/strict';
import { test } from 'node:test';
import { createRateLimiter } from '../api/rate-limit.mjs';

function makeClock() {
  let current = 1_700_000_000_000;
  return {
    now: () => current,
    advance(milliseconds) {
      current += milliseconds;
    },
  };
}

test('uses isolate-local fallback when distributed protection is not configured', async () => {
  const clock = makeClock();
  const limiter = createRateLimiter({
    env: { VERCEL_ENV: 'production' },
    now: clock.now,
  });

  const statuses = [];
  for (let index = 0; index < 6; index += 1) {
    statuses.push((await limiter.check('203.0.113.20')).limited);
  }
  assert.deepEqual(statuses, [false, false, false, false, false, true]);

  clock.advance(10 * 60 * 1000 + 1);
  assert.equal((await limiter.check('203.0.113.20')).limited, false);
});

test('uses an atomic Upstash transaction and enforces the distributed count', async () => {
  const calls = [];
  const limiter = createRateLimiter({
    env: {
      VERCEL_ENV: 'production',
      UPSTASH_REDIS_REST_URL: 'https://example.upstash.io/',
      UPSTASH_REDIS_REST_TOKEN: 'test-token',
    },
    fetchImpl: async (url, init) => {
      calls.push({ url: String(url), init });
      return new Response(JSON.stringify([
        { result: 'OK' },
        { result: 6 },
      ]), { status: 200 });
    },
  });

  assert.deepEqual(await limiter.check('203.0.113.22'), {
    limited: true,
    unavailable: false,
  });
  assert.equal(calls.length, 1);
  assert.equal(calls[0].url, 'https://example.upstash.io/multi-exec');
  assert.equal(calls[0].init.method, 'POST');
  assert.equal(calls[0].init.headers.Authorization, 'Bearer test-token');
  const transaction = JSON.parse(calls[0].init.body);
  assert.deepEqual(transaction[0].slice(0, 5), [
    'SET',
    'trescout:subscribe:rate:203.0.113.22',
    '0',
    'EX',
    '600',
  ]);
  assert.deepEqual(transaction[1], [
    'INCR',
    'trescout:subscribe:rate:203.0.113.22',
  ]);
});

test('falls back to local rate limiting when Upstash returns an error', async () => {
  const clock = makeClock();
  const limiter = createRateLimiter({
    env: {
      VERCEL_ENV: 'production',
      UPSTASH_REDIS_REST_URL: 'https://example.upstash.io',
      UPSTASH_REDIS_REST_TOKEN: 'test-token',
    },
    fetchImpl: async () => new Response('', { status: 503 }),
    now: clock.now,
  });

  assert.deepEqual(await limiter.check('203.0.113.23'), {
    limited: false,
    unavailable: false,
  });
});
