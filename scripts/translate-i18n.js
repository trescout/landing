#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const https = require('https');

const ROOT = path.dirname(__dirname);
const DICT_JSON = path.join(ROOT, 'assets', 'dictionary', 'dictionary.json');
const CAT_JSON = path.join(ROOT, 'assets', 'discover', 'catalog.json');

function translateText(text) {
  if (!text) return Promise.resolve('');
  return new Promise((resolve) => {
    const url = `https://translate.googleapis.com/translate_a/single?client=gtx&sl=tr&tl=en&dt=t&q=${encodeURIComponent(text)}`;
    https.get(url, { headers: { 'User-Agent': 'Mozilla/5.0' } }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          const parsed = JSON.parse(data);
          const translated = parsed[0].map(sentence => sentence[0]).join('');
          resolve(translated || text);
        } catch (e) {
          resolve(text);
        }
      });
    }).on('error', () => resolve(text));
  });
}

async function batchProcess(items, textGetter, textSetter, batchSize = 25) {
  let completed = 0;
  for (let i = 0; i < items.length; i += batchSize) {
    const chunk = items.slice(i, i + batchSize);
    await Promise.all(chunk.map(async (item) => {
      const srcText = textGetter(item);
      const translated = await translateText(srcText);
      textSetter(item, translated);
    }));
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
    (item, val) => item.kisa_en = val
  );
  fs.writeFileSync(DICT_JSON, JSON.stringify(dictionary, null, 2), 'utf8');
  console.log('Dictionary translation saved.');

  console.log(`Translating ${catalog.length} catalog items...`);
  await batchProcess(
    catalog,
    item => item.tagline,
    (item, val) => item.tagline_en = val
  );
  fs.writeFileSync(CAT_JSON, JSON.stringify(catalog, null, 2), 'utf8');
  console.log('Catalog translation saved.');

  console.log('All translations completed successfully!');
}

main().catch(err => {
  console.error('Translation error:', err);
  process.exit(1);
});
