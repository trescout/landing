import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import helper from './catalog-layout.js';

test('legacy generator wrappers retain content and replace the old signup once', () => {
  for (const wrapper of ['container container-pad', 'archive-main']) {
    for (const old of ['', '<aside class="disc-cta"><form>old</form></aside>', '<aside class="signup-cta">old</aside>']) {
      const input = `<html><head></head><body><main id="main"><div class="${wrapper}"><h1>Title</h1><div id="results"><a href="/item/">Item</a></div>${old}</div></main></body></html>`;
      const output = helper.layout(input, '', 'reports');
      assert.match(output, /<h1>Title<\/h1><div id="results"><a href="\/item\/">Item<\/a><\/div>/);
      assert.equal((output.match(/<form /g) || []).length, 1);
      assert.equal(helper.layout(output, '', 'reports'), output);
    }
  }
});

for (const locale of ['', 'en', 'fr', 'pt', 'es', 'de']) {
  for (const kind of ['dictionary', 'discover', 'reports', `reports/${locale ? 'fresh' : 'tekrarsiz'}`]) {
    test(`${locale || 'tr'}/${kind}: sidebar, consent, static content and repeatable generation`, () => {
      const html = readFileSync(new URL(`../${locale ? locale + '/' : ''}${kind}/index.html`, import.meta.url), 'utf8');
      assert.equal((html.match(/class="catalog-sidebar"/g) || []).length, 1);
      assert.equal((html.match(/<form /g) || []).length, 1);
      assert.match(html, /name="consent" required/);
      assert.match(html, /name="website"/);
      assert.match(html, /src="\/assets\/subscribe.js"/);
      assert.match(html, new RegExp(`href="/${locale ? locale + '/' : ''}privacy.html"`));
      assert.ok(html.indexOf('<!-- /catalog-content -->') < html.indexOf('class="catalog-sidebar"'));
      assert.equal(helper.layout(html, locale, kind.startsWith('reports') ? 'reports' : kind), html);
      assert.doesNotMatch(html, /<aside class="(?:disc-cta|signup-cta)"/);
      assert.match(html, /data-cta-placement="catalog_sidebar"/);
    });
  }
}
