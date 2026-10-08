/**
 * Kayıt durdurma ve bildirim varsayılanları (2026-10-08, #210).
 *
 * Varsayılanlar hukuki koruma: metinler düzelene kadar kayıt alınmaz; kayıt
 * açılınca gelen yönetici bildirimi kişinin e-posta adresini taşımaz. Biri env'i
 * unutursa güvenli tarafta kalınmalı; bu test o varsayılanları kilitler.
 */
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';

process.env.VERCEL_ENV = 'preview';
process.env.RESEND_API_KEY = 'test-resend-key';
process.env.RESEND_AUDIENCE_ID = 'test-audience-id';
delete process.env.UPSTASH_REDIS_REST_URL;
delete process.env.UPSTASH_REDIS_REST_TOKEN;
delete process.env.SUBSCRIBE_PAUSED;
delete process.env.SUBSCRIBE_NOTIFY_ENABLED;

const source = await readFile(new URL('../api/subscribe.js', import.meta.url), 'utf8');
const rateLimitSource = await readFile(new URL('../api/rate-limit.mjs', import.meta.url), 'utf8');
const rateLimitUrl = `data:text/javascript;base64,${Buffer.from(rateLimitSource).toString('base64')}`;
const moduleSource = source
  .replace("import { createRateLimiter } from './rate-limit.mjs';", `const { createRateLimiter } = await import(${JSON.stringify(rateLimitUrl)});`)
  .replace('export default async function handler', 'async function handler')
  + '\nexport { handler };';
const { handler } = await import(`data:text/javascript;base64,${Buffer.from(moduleSource).toString('base64')}`);

const istekler = [];
const govdeler = [];
globalThis.fetch = async (url, init = {}) => {
  istekler.push(String(url));
  govdeler.push(init.body || '');
  return new Response('{}', { status: 200, headers: { 'content-type': 'application/json' } });
};

function kayit(lang = '') {
  return handler(new Request('https://trescout.com/api/subscribe', {
    method: 'POST',
    headers: { origin: 'https://trescout.com', referer: `https://trescout.com/${lang}`, 'content-type': 'application/json' },
    body: JSON.stringify({ email: 'kisi@example.com', consent: true }),
  }));
}

test('env yokken kayıt kapalı: 503 kapali, sağlayıcıya hiç istek yok', async () => {
  istekler.length = 0;
  const res = await kayit();
  assert.equal(res.status, 503);
  const body = await res.json();
  assert.equal(body.code, 'kapali');
  assert.match(body.error, /geçici olarak kapalı/);
  assert.equal(istekler.length, 0);
});

test('kapalı mesajı sayfanın dilinde', async () => {
  const body = await (await kayit('en/')).json();
  assert.equal(body.code, 'kapali');
  assert.match(body.error, /temporarily closed/);
});

test('kayıt açılınca bildirim gider ama kişinin e-posta adresini taşımaz', async () => {
  process.env.SUBSCRIBE_PAUSED = 'false';
  istekler.length = 0;
  govdeler.length = 0;
  const res = await kayit();
  assert.equal(res.status, 200);
  assert.deepEqual(istekler.map((u) => new URL(u).pathname), ['/audiences/test-audience-id/contacts', '/emails']);
  const bildirim = JSON.parse(govdeler[1]);
  assert.ok(!bildirim.subject.includes('kisi@example.com'), 'konu adresi taşımamalı');
  assert.ok(!bildirim.text.includes('kisi@example.com'), 'gövde adresi taşımamalı');
  assert.match(bildirim.text, /Kaynak: /);
  delete process.env.SUBSCRIBE_PAUSED;
});
