import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';

// Doğrulama sözleşmesi kayıt AÇIKKEN sınanır; durdurma davranışı ayrı testte.
process.env.SUBSCRIBE_PAUSED = 'false';

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

async function responseFor(language, method = 'POST') {
  const headers = {
    origin: 'https://trescout.com',
    referer: `https://trescout.com/${language === 'tr' ? '' : `${language}/`}`,
  };
  const init = { method, headers };
  if (method === 'POST') {
    headers['content-type'] = 'application/json';
    init.body = JSON.stringify({ consent: false });
  }
  const response = await handler(new Request('https://trescout.com/api/subscribe', init));
  return { response, body: await response.json() };
}

test('localized validation errors use a stable code for every supported language', async () => {
  // Beklenen metinler tek kaynaktan (riza-metni.json, #210): API ile form
  // aynı mesajı göstermeli.
  const riza = JSON.parse(await readFile(new URL('./riza-metni.json', import.meta.url), 'utf8'));
  const expected = Object.fromEntries(
    Object.entries(riza).filter(([k]) => !k.startsWith('_')).map(([k, v]) => [k, v.onay_hata]),
  );

  for (const [language, message] of Object.entries(expected)) {
    const { response, body } = await responseFor(language);
    assert.equal(response.status, 400, language);
    assert.equal(body.code, 'onay', language);
    assert.equal(body.error, message, language);
  }
});

test('method errors are localized from the referer path', async () => {
  const { response, body } = await responseFor('fr', 'GET');
  assert.equal(response.status, 405);
  assert.equal(body.code, 'method');
  assert.equal(body.error, 'Méthode non autorisée');
});

test('lookalike Vercel preview origins are rejected', async () => {
  const response = await handler(new Request('https://trescout.com/api/subscribe', {
    method: 'POST',
    headers: {
      origin: 'https://trescout-landing-attacker.vercel.app',
      referer: 'https://trescout.com/',
      'content-type': 'application/json',
    },
    body: JSON.stringify({ consent: false }),
  }));
  const body = await response.json();
  assert.equal(response.status, 403);
  assert.equal(body.code, 'istek');
});

test('urlencoded forms still reach consent validation without JSON parsing', async () => {
  const response = await handler(new Request('https://trescout.com/api/subscribe', {
    method: 'POST',
    headers: {
      origin: 'https://trescout.com',
      referer: 'https://trescout.com/',
      'content-type': 'application/x-www-form-urlencoded',
    },
    body: 'email=test%40example.com',
  }));
  const body = await response.json();
  assert.equal(response.status, 400);
  assert.equal(body.code, 'onay');
});
