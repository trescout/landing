#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const { translateTexts: translateWithProviders } = require('./translation-service');

const ROOT = path.dirname(__dirname);
const DICT_JSON = path.join(ROOT, 'assets', 'dictionary', 'dictionary.json');
const CAT_JSON = path.join(ROOT, 'assets', 'discover', 'catalog.json');

/* Çeviri önbelleği · scripts/discover-en.py ve dictionary-en.py ile AYNI dosya.
   Anahtar kaynak metnin kendisi olduğu için: metin değişmemişse çeviri
   tekrarlanmaz, DEĞİŞMİŞSE yeni anahtar oluşur ve otomatik yenilenir.
   Önceden bu betik her çalıştığında 880 çağrı yapıyordu ve hiçbir iş akışında
   değildi · yeni girdiler İngilizce kartlarda TÜRKÇE görünüyordu (2026-08-07). */
const LANG = (process.argv.find(a => a.startsWith('--lang=')) || '--lang=en').split('=')[1];
// Çıplak argüman sessizce yutulmasın · dict-sync.yml'de bir süre
// `translate-i18n.js fr` yazıyordu ve adım İngilizce koşuyordu (2026-08-08).
const bilinmeyen = process.argv.slice(2).filter(a => !a.startsWith('--'));
if (bilinmeyen.length) {
  console.error(`✗ Tanınmayan argüman: ${bilinmeyen.join(' ')} · dil için --lang=fr kullanın.`);
  process.exit(1);
}
const CACHE_PATH = path.join(ROOT, 'assets', 'discover', `${LANG}-cache.json`);
let cache = {};
try { cache = JSON.parse(fs.readFileSync(CACHE_PATH, 'utf8')); } catch { cache = {}; }
let yeniCeviri = 0;
let basarisizCeviri = 0;

async function batchProcess(items, textGetter, textSetter, batchSize = 12) {
  let completed = 0;
  for (let i = 0; i < items.length; i += batchSize) {
    const chunk = items.slice(i, i + batchSize);
    const pending = [];
    for (const item of chunk) {
      const srcText = (textGetter(item) || '').trim();
      if (srcText && !cache[srcText]) pending.push(srcText);
    }
    const translated = await translateWithProviders(pending, LANG);
    for (const item of chunk) {
      const srcText = (textGetter(item) || '').trim();
      if (!srcText) continue;
      const value = cache[srcText] || translated.get(srcText);
      if (!value) {
        basarisizCeviri++;
        console.warn(`  Translation failed; source text was not written: ${srcText.slice(0, 60)}`);
        continue;
      }
      if (!cache[srcText] && value !== srcText) { cache[srcText] = value; yeniCeviri++; }
      textSetter(item, value);
    }
    completed += chunk.length;
    console.log(`  Processed ${completed}/${items.length}...`);
  }
}

async function main() {
  console.log('Loading data files...');
  const dictionary = JSON.parse(fs.readFileSync(DICT_JSON, 'utf8'));
  const catalog = JSON.parse(fs.readFileSync(CAT_JSON, 'utf8'));

  console.log(`Translating ${dictionary.length} dictionary terms...`);
  await batchProcess(
    dictionary,
    item => item.kisa,
    (item, val) => item[`kisa_${LANG}`] = val
  );
  fs.writeFileSync(DICT_JSON, JSON.stringify(dictionary, null, 2), 'utf8');
  console.log('Dictionary translation saved.');

  const translatableCatalog = catalog.filter(item => !item.tagline_reviewed);
  console.log(`Translating ${translatableCatalog.length}/${catalog.length} catalog items...`);
  // Human-reviewed multilingual taglines are explicit overrides. Keep them
  // stable across daily syncs; remove tagline_reviewed only when a fresh source
  // translation is intentionally requested.
  await batchProcess(
    translatableCatalog,
    item => item.tagline,
    (item, val) => item[`tagline_${LANG}`] = val
  );
  fs.writeFileSync(CAT_JSON, JSON.stringify(catalog, null, 2), 'utf8');
  console.log('Catalog translation saved.');

  fs.writeFileSync(CACHE_PATH, JSON.stringify(cache, null, 1), 'utf8');
  if (basarisizCeviri) {
    throw new Error(`${basarisizCeviri} translation(s) failed; no source-language fallback was written.`);
  }
  console.log(`All translations completed · ${yeniCeviri} new, cache ${Object.keys(cache).length} entries.`);
}

main().catch(err => {
  console.error('Translation error:', err);
  process.exit(1);
});
