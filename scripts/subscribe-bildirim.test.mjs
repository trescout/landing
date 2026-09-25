/**
 * /api/subscribe · kayıt sonucu ↔ bildirim ayrımı ve gövde doğrulaması.
 *
 * Tamamen mock: global fetch her testte sahte yanıtlarla değiştirilir ve çağrılar
 * kaydedilir. Hiçbir test gerçek Resend, Audience, Upstash veya bildirim isteği
 * göndermez · "sağlayıcıya gidilmedi" iddiası kaydedilen çağrı listesiyle
 * doğrulanır.
 *
 * Modülü scripts/subscribe-contract.test.mjs ile aynı yöntemle yüklüyoruz:
 * kökteki package.json "type": "commonjs" olduğu için api/subscribe.js bir .js
 * ESM dosyası olarak doğrudan import edilemiyor; kaynağı data URL'e çevirip
 * import ediyoruz. Rate limiter modül yüklenirken process.env'i okuduğu için
 * ortam değişkenleri import'tan ÖNCE kuruluyor.
 */
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';

// Preview ortamı · Upstash yok, isolate-local sayaç çalışır (ağ isteği yok).
process.env.VERCEL_ENV = 'preview';
process.env.RESEND_API_KEY = 'test-resend-key';
process.env.RESEND_AUDIENCE_ID = 'test-audience-id';
process.env.TRESCOUT_PREVIEW_ORIGINS = '';
delete process.env.UPSTASH_REDIS_REST_URL;
delete process.env.UPSTASH_REDIS_REST_TOKEN;
// Bildirim kilidi varsayılanı AÇIK · her test kendi durumunu açıkça kurar.
delete process.env.SUBSCRIBE_NOTIFY_ENABLED;

function bildirimKilidiniKapat() {
  process.env.SUBSCRIBE_NOTIFY_ENABLED = 'false';
}

function bildirimKilidiniSifirla() {
  delete process.env.SUBSCRIBE_NOTIFY_ENABLED;
}

const source = await readFile(new URL('../api/subscribe.js', import.meta.url), 'utf8');
const rateLimitSource = await readFile(new URL('../api/rate-limit.mjs', import.meta.url), 'utf8');
const rateLimitUrl = `data:text/javascript;base64,${Buffer.from(rateLimitSource).toString('base64')}`;
const moduleSource = source
  .replace("import { createRateLimiter } from './rate-limit.mjs';", `const { createRateLimiter } = await import(${JSON.stringify(rateLimitUrl)});`)
  .replace('export const config =', 'const config =')
  .replace('export default async function handler', 'async function handler')
  + '\nexport { handler };';
const moduleUrl = `data:text/javascript;base64,${Buffer.from(moduleSource).toString('base64')}`;
const { handler } = await import(moduleUrl);

const realFetch = globalThis.fetch;
let calls = [];

/** Sahte fetch · çağrıları kaydeder, yanıtı responder üretir. */
function stubFetch(responder) {
  calls = [];
  bildirimKilidiniSifirla();
  globalThis.fetch = async (url, init) => {
    calls.push({ url: String(url), init });
    return responder(String(url), init);
  };
}

function reddet() {
  return () => {
    throw new Error('bu testte sağlayıcıya istek gitmemeli');
  };
}

// Rate limiter IP başına 10 dakikada 5 istek sayıyor · testler aynı isolate'i
// paylaştığı için her istek kendi IP'sini alır, yoksa sonraki testler 429 görür.
let ipCounter = 0;
function istek(body, { origin = 'https://trescout.com', raw } = {}) {
  ipCounter += 1;
  return new Request('https://trescout.com/api/subscribe', {
    method: 'POST',
    headers: {
      origin,
      referer: 'https://trescout.com/',
      'content-type': 'application/json',
      'x-forwarded-for': `203.0.113.${(ipCounter % 250) + 1}`,
    },
    body: raw !== undefined ? raw : JSON.stringify(body),
  });
}

test('kayıt başarılıyken bildirim ağ hatası verse de kullanıcıya ok döner', async () => {
  // Regresyon: bildirim fetch'i throw ettiğinde ortak catch kullanıcıya 502
  // döndürüyordu · kişi Audience'a eklenmişken "kayıt olmadı" demek oluyordu.
  stubFetch((url) => {
    if (url.includes('/audiences/')) return new Response('{}', { status: 201 });
    throw new TypeError('fetch failed');
  });

  const response = await handler(istek({ email: 'ok@example.com', consent: true }));

  assert.equal(response.status, 200);
  assert.deepEqual(await response.json(), { ok: true, duplicate: false });
  assert.equal(calls.length, 2);
  assert.ok(calls[1].url.endsWith('/emails'));
});

test('bildirim HTTP hatası verse de kullanıcıya ok döner', async () => {
  stubFetch((url) => {
    if (url.includes('/audiences/')) return new Response('{}', { status: 201 });
    return new Response('rate limited', { status: 429 });
  });

  const response = await handler(istek({ email: 'ok2@example.com', consent: true }));

  assert.equal(response.status, 200);
  assert.deepEqual(await response.json(), { ok: true, duplicate: false });
});

test('tekrar kayıtta (409) duplicate bayrağı döner, bildirim konusu buna göre kurulur', async () => {
  stubFetch((url) => {
    if (url.includes('/audiences/')) return new Response('exists', { status: 409 });
    return new Response('{}', { status: 200 });
  });

  const response = await handler(istek({ email: 'dup@example.com', consent: true }));

  assert.equal(response.status, 200);
  assert.deepEqual(await response.json(), { ok: true, duplicate: true });
  assert.match(JSON.parse(calls[1].init.body).subject, /^Tekrar kayıt:/);
});

test('Audience isteği ağ hatası verirse 502 döner ve bildirim denenmez', async () => {
  stubFetch(() => {
    throw new TypeError('fetch failed');
  });

  const response = await handler(istek({ email: 'net@example.com', consent: true }));

  assert.equal(response.status, 502);
  assert.equal((await response.json()).code, 'baglanti');
  assert.equal(calls.length, 1);
});

test('Audience HTTP hatası verirse 502 kayit döner ve bildirim denenmez', async () => {
  stubFetch(() => new Response('nope', { status: 422 }));

  const response = await handler(istek({ email: 'bad@example.com', consent: true }));

  assert.equal(response.status, 502);
  assert.equal((await response.json()).code, 'kayit');
  assert.equal(calls.length, 1);
});

test('JSON null gövdesi çökmek yerine 400 format döner', async () => {
  // Regresyon: body null olduğunda body.hp erişimi runtime hatası veriyordu.
  stubFetch(reddet());

  const response = await handler(istek(null, { raw: 'null' }));

  assert.equal(response.status, 400);
  assert.equal((await response.json()).code, 'format');
  assert.equal(calls.length, 0);
});

test('nesne olmayan JSON gövdeleri 400 format döner', async () => {
  stubFetch(reddet());

  for (const raw of ['[]', '"metin"', '42', 'true']) {
    const response = await handler(istek(null, { raw }));
    assert.equal(response.status, 400, `gövde: ${raw}`);
    assert.equal((await response.json()).code, 'format', `gövde: ${raw}`);
  }
  assert.equal(calls.length, 0);
});

test('honeypot dolu gelirse sessizce ok döner ve sağlayıcıya gidilmez', async () => {
  stubFetch(reddet());

  const response = await handler(istek({ email: 'bot@example.com', consent: true, hp: 'spam' }));

  assert.equal(response.status, 200);
  assert.deepEqual(await response.json(), { ok: true });
  assert.equal(calls.length, 0);
});

test('onay yoksa veya e-posta geçersizse sağlayıcıya gidilmez', async () => {
  stubFetch(reddet());

  const onaysiz = await handler(istek({ email: 'a@example.com' }));
  assert.equal(onaysiz.status, 400);
  assert.equal((await onaysiz.json()).code, 'onay');

  const bozukEposta = await handler(istek({ email: 'not-an-email', consent: true }));
  assert.equal(bozukEposta.status, 400);
  assert.equal((await bozukEposta.json()).code, 'eposta');

  assert.equal(calls.length, 0);
});

test('tek kullanımlık e-posta alanı sağlayıcıya gitmeden 400 döner', async () => {
  stubFetch(reddet());

  const response = await handler(istek({ email: 'x@mailinator.com', consent: true }));

  assert.equal(response.status, 400);
  assert.equal((await response.json()).code, 'gecici');
  assert.equal(calls.length, 0);
});

test('izin verilmeyen origin 403 döner ve sağlayıcıya gidilmez', async () => {
  stubFetch(reddet());

  const response = await handler(
    istek({ email: 'a@example.com', consent: true }, { origin: 'https://saldirgan.example' }),
  );

  assert.equal(response.status, 403);
  assert.equal(calls.length, 0);
});

test('bildirim kilidi varsayılan olarak AÇIK · /emails çağrısı yapılır', async () => {
  stubFetch((url) => {
    if (url.includes('/audiences/')) return new Response('{}', { status: 201 });
    if (url.endsWith('/emails')) return new Response('{}', { status: 200 });
    throw new Error('beklenmeyen istek: ' + url);
  });

  const response = await handler(istek({ email: 'varsayilan@example.com', consent: true }));

  assert.equal(response.status, 200);
  assert.deepEqual(await response.json(), { ok: true, duplicate: false });
  assert.equal(calls.length, 2);
  assert.ok(calls[0].url.includes('/audiences/'));
  assert.ok(calls[1].url.endsWith('/emails'));
});

test('SUBSCRIBE_NOTIFY_ENABLED="false" yapıldığında /emails çağrısı hiç yapılmaz', async () => {
  stubFetch((url) => {
    if (url.includes('/audiences/')) return new Response('{}', { status: 201 });
    throw new Error('kilit kapalıyken /emails çağrılmamalı');
  });
  bildirimKilidiniKapat();

  const response = await handler(istek({ email: 'kilit@example.com', consent: true }));

  assert.equal(response.status, 200);
  assert.deepEqual(await response.json(), { ok: true, duplicate: false });
  assert.equal(calls.length, 1);
  assert.ok(calls[0].url.includes('/audiences/'));
  bildirimKilidiniSifirla();
});

test('kilit kapalıyken ("false") tekrar kayıt da (409) sağlayıcıya gitmez', async () => {
  stubFetch((url) => {
    if (url.includes('/audiences/')) return new Response('exists', { status: 409 });
    throw new Error('kilit kapalıyken /emails çağrılmamalı');
  });
  bildirimKilidiniKapat();

  const response = await handler(istek({ email: 'kilitdup@example.com', consent: true }));

  assert.equal(response.status, 200);
  assert.deepEqual(await response.json(), { ok: true, duplicate: true });
  assert.equal(calls.length, 1);
  bildirimKilidiniSifirla();
});

test('gövdede source/path yokken Referer başlığından kaynak ve sayfa yedeklenir', async () => {
  stubFetch((url) => {
    if (url.includes('/audiences/')) return new Response('{}', { status: 201 });
    if (url.endsWith('/emails')) return new Response('{}', { status: 200 });
    throw new Error('beklenmeyen istek: ' + url);
  });

  ipCounter += 1;
  const req = new Request('https://trescout.com/api/subscribe', {
    method: 'POST',
    headers: {
      origin: 'https://trescout.com',
      referer: 'https://trescout.com/dictionary/local/',
      'content-type': 'application/json',
      'x-forwarded-for': `203.0.113.${(ipCounter % 250) + 1}`,
    },
    body: JSON.stringify({ email: 'referer-test@example.com', consent: true }),
  });

  const response = await handler(req);
  assert.equal(response.status, 200);
  assert.equal(calls.length, 2);

  const emailBody = JSON.parse(calls[1].init.body);
  assert.ok(emailBody.text.includes('Kaynak: dictionary'));
  assert.ok(emailBody.text.includes('Sayfa: https://trescout.com/dictionary/local/'));
});

test('İngilizce sayfadan urlencoded form geldiğinde Referer başlığından kaynak ve sayfa çıkarılır', async () => {
  stubFetch((url) => {
    if (url.includes('/audiences/')) return new Response('{}', { status: 201 });
    if (url.endsWith('/emails')) return new Response('{}', { status: 200 });
    throw new Error('beklenmeyen istek: ' + url);
  });

  ipCounter += 1;
  const req = new Request('https://trescout.com/api/subscribe', {
    method: 'POST',
    headers: {
      origin: 'https://trescout.com',
      referer: 'https://trescout.com/en/dictionary/open-weight/',
      'content-type': 'application/x-www-form-urlencoded',
      'x-forwarded-for': `203.0.113.${(ipCounter % 250) + 1}`,
    },
    body: 'email=en-test%40example.com&consent=on',
  });

  const response = await handler(req);
  assert.equal(response.status, 200);
  assert.equal(calls.length, 2);

  const emailBody = JSON.parse(calls[1].init.body);
  assert.ok(emailBody.text.includes('Kaynak: dictionary-en'));
  assert.ok(emailBody.text.includes('Sayfa: https://trescout.com/en/dictionary/open-weight/'));
});

test.after(() => {
  globalThis.fetch = realFetch;
  delete process.env.SUBSCRIBE_NOTIFY_ENABLED;
});
