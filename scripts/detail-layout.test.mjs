import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync, readdirSync, existsSync} from 'node:fs';
import vm from 'node:vm';
import helper from './detail-layout.js';

const root = new URL('../', import.meta.url);
const script = readFileSync(new URL('assets/detail-layout.js', root), 'utf8');
const include = '<script src="/assets/detail-layout.js" defer></script>';

test('normalization changes no editorial content and is idempotent', () => {
  const old = '<main><article class="disc"><h1>Title</h1><aside class="disc-cta"><form>Consent</form></aside></article></main><script src="/assets/subscribe.js" defer></script>';
  const next = helper.normalize(old);
  assert.equal(next.replace(include + '\n', ''), old);
  assert.equal(helper.normalize(next), next);
  assert.equal(helper.normalize('<main>Index</main>'), '<main>Index</main>');
});

test('non-detail pages are not touched at runtime', () => {
  vm.runInNewContext(script, {document: {querySelector: () => null}});
});

for (const locale of ['', 'en', 'fr', 'pt', 'es', 'de']) {
  test(`${locale || 'tr'}: homepage copy matches and every detail keeps static content and one form`, () => {
    const copy = vm.runInNewContext('(' + script.match(/var copy = (\{[\s\S]*?\n  \});/)[1] + ')')[locale || 'tr'];
    const home = readFileSync(new URL(`${locale ? locale + '/' : ''}index.html`, root), 'utf8').replaceAll('&#x27;', "'");
    for (const text of copy) assert.ok(home.includes(text), `Homepage copy drift: ${text}`);
    let count = 0;
    for (const kind of ['dictionary', 'discover']) {
      const directory = new URL(`${locale ? locale + '/' : ''}${kind}/`, root);
      for (const entry of readdirSync(directory, {withFileTypes: true})) {
        if (!entry.isDirectory()) continue;
        const file = new URL(`${entry.name}/index.html`, directory);
        if (!existsSync(file)) continue;
        const html = readFileSync(file, 'utf8');
        if (!html.includes('<article class="disc">') || !html.includes('class="disc-cta"')) continue;
        count++;
        assert.equal(html.split(include).length - 1, 1, file.pathname);
        assert.equal((html.match(/<form\b/g) || []).length, 1, file.pathname);
        assert.match(html, /name="consent" required/, file.pathname);
        assert.match(html, /button[^>]*type="submit"/, file.pathname);
        assert.match(html, /<h1\b/, file.pathname);
        assert.equal(helper.normalize(html), html);
      }
    }
    assert.ok(count > 1000);
  });
}
