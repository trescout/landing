import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';

const source = await readFile(new URL('../api/subscribe.js', import.meta.url), 'utf8');
const moduleSource = source
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
  const expected = {
    tr: 'Aydınlatma Metni onayı gerekli',
    en: 'Please accept the privacy notice to continue',
    fr: 'Veuillez accepter la notice de confidentialité pour continuer',
    pt: 'Aceite o aviso de privacidade para continuar',
    es: 'Acepte el aviso de privacidad para continuar',
    de: 'Stimmen Sie dem Datenschutzhinweis zu, um fortzufahren',
  };

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
