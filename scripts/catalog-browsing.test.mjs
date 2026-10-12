import test from 'node:test';
import assert from 'node:assert/strict';
import vm from 'node:vm';
import { readFileSync } from 'node:fs';

function environment(kind, lang) {
  const created = [];
  let focused;
  class Element {
    constructor() { this.style = {}; this.attrs = {}; this.events = {}; this.children = []; this.hidden = false; this.textContent = ''; this.html = null; }
    setAttribute(k, v) { this.attrs[k] = v; }
    getAttribute(k) { return this.attrs[k]; }
    addEventListener(k, f) { this.events[k] = f; }
    append(...children) { this.children.push(...children); }
    before() {}
    after() {}
    focus() { focused = this; }
    fire(event) { this.events[event](); }
    set innerHTML(value) { this.html = value; }
    get innerHTML() { return this.html ?? this.textContent.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('"', '&quot;'); }
    querySelectorAll() {
      if (this.html === null) return this.children;
      return [...this.html.matchAll(/<a class="disc-card" href="([^"]+)"/g)].map(m => {
        const a = new Element(); a.href = m[1]; a.attrs.href = a.href; return a;
      });
    }
  }
  const prefix = lang === 'tr' ? '' : '/' + (lang === 'pt-BR' ? 'pt' : lang);
  const grid = new Element();
  grid.id = kind === 'dictionary' ? 'dict-grid' : 'discover-grid';
  const cards = Array.from({length: 60}, (_, i) => {
    const a = new Element();
    a.href = `${prefix}/${kind}/item-${i + 1}/`;
    a.attrs = {href: a.href, 'data-search': `item-${i + 1}`, 'data-cat': 'ai'};
    return a;
  });
  grid.children = cards;
  const search = new Element(), sort = new Element(), count = new Element();
  const ids = {[grid.id]: grid, 'dict-search': search, 'disc-search': search, 'disc-sort': sort, 'dict-count': count, 'disc-count': count};
  const doc = {
    documentElement: {lang}, getElementById: id => ids[id] || null,
    querySelectorAll: () => [],
    createElement: () => { const e = new Element(); created.push(e); return e; },
  };
  const items = Array.from({length: 61}, (_, i) => ({slug: `item-${i + 1}`, title: `item-${i + 1}`, date: '2026-01-01', stars: 61-i, tags: []}));
  const math = Object.create(Math); math.random = () => 0.999;
  const context = {document: doc, Math: math, navigator: {}, fetch: async () => ({json: async () => items})};
  vm.runInNewContext(readFileSync(new URL(`../assets/${kind === 'dictionary' ? 'dictionary' : 'discover'}.js`, import.meta.url), 'utf8'), context);
  return {created, grid, cards, search, sort, count, focused: () => focused,
    visible: () => kind === 'dictionary' ? cards.filter(c => c.style.display !== 'none') : grid.querySelectorAll(),
    control: cls => created.find(e => e.className === cls)};
}

for (const kind of ['dictionary', 'discover']) {
  for (const lang of ['tr', 'en', 'fr', 'pt-BR', 'es', 'de']) {
    test(`${kind}/${lang}: batches, full-pool random, search, empty state and focus`, async () => {
      const e = environment(kind, lang);
      await new Promise(resolve => setImmediate(resolve));
      const more = e.control('btn catalog-more'), random = e.control('catalog-random');
      assert.equal(e.visible().length, 16);
      assert.match(random.href, /\/item-60\/$/); // Includes hidden results; excludes unavailable item 61.
      more.fire('click');
      assert.equal(e.visible().length, 32);
      assert.match(e.focused().href, /\/item-17\/$/);
      more.fire('click');
      assert.equal(e.visible().length, 48);
      more.fire('click');
      assert.equal(e.visible().length, 60);
      assert.equal(more.hidden, true);
      e.search.value = 'item-59'; e.search.fire('input');
      assert.equal(e.visible().length, 1);
      assert.match(random.href, /\/item-59\/$/);
      e.search.value = 'no-result'; e.search.fire('input');
      assert.equal(e.visible().length, 0);
      assert.equal(random.hidden, true);
      assert.equal(more.hidden, true);
      e.search.value = ''; e.search.fire('input');
      assert.equal(e.visible().length, 16);
      assert.equal(more.hidden, false);
      if (kind === 'discover') {
        more.fire('click');
        e.sort.value = 'stars'; e.sort.fire('change');
        assert.equal(e.visible().length, 16);
      }
    });
  }
}

test('all locale indexes retain complete static lists when JavaScript is unavailable', () => {
  for (const prefix of ['', 'en/', 'fr/', 'pt/', 'es/', 'de/']) {
    for (const kind of ['dictionary', 'discover']) {
      const html = readFileSync(new URL(`../${prefix}${kind}/index.html`, import.meta.url), 'utf8');
      assert.ok((html.match(kind === 'dictionary' ? /class="dict-card"/g : /class="disc-card"/g) || []).length > 24);
    }
  }
});
