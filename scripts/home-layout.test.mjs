import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

for (const locale of ['', 'en/', 'fr/', 'pt/', 'es/', 'de/']) {
  test(`homepage layout and signup contract: ${locale || 'tr'}`, () => {
    const html = readFileSync(new URL(`../${locale}index.html`, import.meta.url), 'utf8');
    const main = html.match(/<main id="main">([\s\S]*?)<\/main>/)[1];
    assert.equal((main.match(/<form\b/g) || []).length, 1);
    const band = main.slice(0, main.indexOf('<div class="container ana-govde">'));
    assert.ok(band.includes('<div class="ana-bant-sag"><section class="ana-erken" id="cta">'));
    assert.ok(main.indexOf('class="ana-tarih"') < main.indexOf('class="ana-gun"'));
    assert.ok(band.includes('<h1 id="ana-baslik">'));
    assert.ok(!band.includes('class="ana-tarih"'));
    assert.ok(main.includes('<div class="ana-icerik"><section class="ana-rapor-bilgisi"'));
    assert.ok(band.includes('id="top"'));
    assert.ok(band.includes('action="/api/subscribe" method="post"'));
    assert.ok(band.includes('name="consent" required'));
    assert.ok(band.includes('name="website"'));
    assert.ok(band.includes('data-source="final-cta"'));
    assert.ok(!band.includes('ana-gecmis'));
    const sidebar = main.match(/<aside class="ana-yan">([\s\S]*?)<\/aside>/)[1];
    assert.ok(sidebar.indexOf('ana-yan-baglanti') < sidebar.indexOf('ana-tamami'));
    assert.ok(sidebar.indexOf('ana-tamami') < sidebar.indexOf('ana-yz'));
    assert.ok(sidebar.indexOf('ana-yz') < sidebar.indexOf('ana-gecmis'));
    assert.ok(sidebar.endsWith('</svg></div>'));
    assert.equal((main.match(/class="ana-tamami"/g) || []).length, 1);
    assert.match(main, /ana-serit-dar[^>]+role="img" aria-label="[^"]+"/);
    assert.ok(!main.includes('ana-alt'));
  });
}
