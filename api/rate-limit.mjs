const RATE_WINDOW_SECONDS = 10 * 60;
const RATE_WINDOW_MS = RATE_WINDOW_SECONDS * 1000;
const RATE_MAX = 5;

function isLocalRateLimited(rateHits, ip, now) {
  if (!ip) return false;
  const cutoff = now - RATE_WINDOW_MS;
  const hits = (rateHits.get(ip) || []).filter((timestamp) => timestamp > cutoff);
  hits.push(now);
  rateHits.set(ip, hits);

  if (rateHits.size > 5000) {
    for (const [key, values] of rateHits) {
      if (values.every((timestamp) => timestamp <= cutoff)) rateHits.delete(key);
    }
  }

  return hits.length > RATE_MAX;
}

export function createRateLimiter({
  env = process.env,
  fetchImpl = globalThis.fetch,
  now = () => Date.now(),
} = {}) {
  const redisUrl = (env.UPSTASH_REDIS_REST_URL || '').replace(/\/+$/, '');
  const redisToken = env.UPSTASH_REDIS_REST_TOKEN || '';
  // Production'da dağıtık sayaç yoksa isolate-local Map koruma sayılmaz:
  // her isolate kendi sayacını tutar, saldırgan yeni isolate'lerle limiti
  // sessizce atlatır. Bu yüzden production fail-closed davranır (docs/ENV.md §4,
  // docs/BETA-MEASUREMENT.md). Local/preview'da fallback yeterli.
  const failClosed = env.VERCEL_ENV === 'production';
  const rateHits = new Map();

  async function checkDistributed(ip) {
    const key = `trescout:subscribe:rate:${encodeURIComponent(ip)}`;
    const response = await fetchImpl(`${redisUrl}/multi-exec`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${redisToken}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify([
        ['SET', key, '0', 'EX', String(RATE_WINDOW_SECONDS), 'NX'],
        ['INCR', key],
      ]),
    });

    if (!response.ok) {
      throw new Error(`Upstash rate limit HTTP ${response.status}`);
    }

    const results = await response.json();
    const count = Number(results?.[1]?.result);
    if (!Number.isFinite(count)) {
      throw new Error('Upstash rate limit response is invalid');
    }

    return count > RATE_MAX;
  }

  return {
    async check(ip) {
      if (!ip) return { limited: false, unavailable: false };

      if (!redisUrl || !redisToken) {
        if (failClosed) {
          console.error('Distributed rate limit is not configured in production');
          return { limited: false, unavailable: true };
        }
        return {
          limited: isLocalRateLimited(rateHits, ip, now()),
          unavailable: false,
        };
      }

      try {
        return { limited: await checkDistributed(ip), unavailable: false };
      } catch (error) {
        if (failClosed) {
          console.error(
            'Distributed rate limit unavailable in production:',
            error instanceof Error ? error.message : 'unknown',
          );
          return { limited: false, unavailable: true };
        }
        console.warn('Distributed rate limit unavailable, using local rate limit fallback:', error);
        return {
          limited: isLocalRateLimited(rateHits, ip, now()),
          unavailable: false,
        };
      }
    },
  };
}

export { RATE_MAX, RATE_WINDOW_SECONDS };
