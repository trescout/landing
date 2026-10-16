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
    // DOM gibi: zaten çocuksa yerinden alınıp sona taşınır (çoğaltılmaz)
    append(...children) { for (const c of children) { const i = this.children.indexOf(c); if (i >= 0) this.children.splice(i, 1); this.children.push(c); } }
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

// Arama sıralaması (R4) · iki dosyada aynı puan fonksiyonu; gerçek sözlük verisiyle sıra.
function aramaPuaniKaynak(dosya) {
  const src = readFileSync(new URL(`../assets/${dosya}`, import.meta.url), 'utf8');
  return src.match(/  function aramaPuani[\s\S]*?\n  }\n/)?.[0];
}
const katla = (s) => String(s || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/ı/g, 'i');

test('arama puanı sözlükte ve keşifte birebir aynı (kopya ayrışmasın)', () => {
  assert.ok(aramaPuaniKaynak('dictionary.js'));
  assert.equal(aramaPuaniKaynak('discover.js'), aramaPuaniKaynak('dictionary.js'));
});

test('sözlük araması: adı sorguyla başlayan terim kelime içi eşleşmenin önüne geçer (gerçek veri)', () => {
  const aramaPuani = new Function(`${aramaPuaniKaynak('dictionary.js')}; return aramaPuani;`)();
  const html = readFileSync(new URL('../dictionary/index.html', import.meta.url), 'utf8');
  const kartlar = [...html.matchAll(/data-search="([^"]*)"[^>]*><h2 class="dict-card-term">([^<]*)/g)]
    .map(([, metin, ad], sira) => ({ metin: katla(metin), ad: katla(ad), sira }));
  assert.ok(kartlar.length > 500);
  const ilk = (q) => kartlar.map((k) => ({ ...k, p: aramaPuani(k.ad, k.metin, katla(q)) }))
    .filter((k) => k.p > 0).sort((x, y) => y.p - x.p || x.sira - y.sira)[0];
  for (const q of ['RAG', 'API', 'model', 'token', 'LLM']) {
    assert.ok(ilk(q).ad.startsWith(katla(q)), `${q} → ${ilk(q).ad}`);
  }
  // Kelime içi eşleşme kaybolmaz, yalnız sona kalır: "rag" storage içinde
  const storage = kartlar.find((k) => k.ad.startsWith('object storage'));
  if (storage) assert.equal(aramaPuani(storage.ad, storage.metin, 'rag'), 0.5);
  // Çok kelimeli ve sırası farklı sorgu da bulur
  assert.ok(aramaPuani('fine-tuning', 'fine-tuning hazir bir modeli', 'tuning fine') > 0);
});
