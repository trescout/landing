#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const https = require('https');

const ROOT = path.dirname(__dirname);
const SITEMAP = path.join(ROOT, 'sitemap.xml');
const KEY = process.env.INDEXNOW_KEY || '4a8f92b1c3d4e5f67890abcdef123456';
const SITE_URL = process.env.SITE_URL || 'https://trescout.com';
const HOST = SITE_URL.replace(/^https?:\/\//, '').replace(/\/+$/, '');
const CHUNK_SIZE = 10000; // IndexNow max URLs per request
const MAX_RETRIES = 3;
const RETRY_DELAY_MS = 2000;

let sitemapContent;
try {
  sitemapContent = fs.readFileSync(SITEMAP, 'utf8');
} catch (err) {
  console.error(`Failed to read sitemap: ${err.message}`);
  process.exit(1);
}

const escapedHost = HOST.replace(/\./g, '\\.');
const urlRegex = new RegExp(`<loc>(https://${escapedHost}/[^<]+)</loc>`, 'g');
const urlMatches = sitemapContent.match(urlRegex) || [];
const sitemapUrls = urlMatches.map(m => m.replace('<loc>', '').replace('</loc>', ''));

/*
 * YALNIZ DEĞİŞENLERİ bildir · IndexNow'ın amacı bu.
 *
 * 2026-08-20'ye kadar her gün sitemap'in TAMAMI gönderiliyordu (6782 URL).
 * Uç nokta 200 dönüyor, yani "çalışıyor" görünüyor · ama protokolün beklediği
 * şey "şu sayfalar değişti" demek. Her gün her şeyi bildirmek sinyali
 * gürültüye çeviriyor ve arama motorları böyle göndericileri kısıtlıyor.
 *
 * Adım commit'ten SONRA koştuğu için son commit'in diff'i tam olarak o günün
 * değişikliği. Diff alınamazsa (sığ klon, ilk commit) hiçbir şey gönderilmez ·
 * "emin değilsem her şeyi bildireyim" yanlış varsayılan. Elle tam gönderim
 * gerekirse --all var.
 */
function degisenUrller() {
  const { execFileSync } = require('child_process');
  let dosyalar;
  try {
    dosyalar = execFileSync('git', ['diff', '--name-only', 'HEAD~1', 'HEAD'],
      { cwd: ROOT, encoding: 'utf8' }).split('\n').filter(Boolean);
  } catch (err) {
    console.log(`Git diff alınamadı (${err.message.split('\n')[0]}) · bildirim atlandı.`);
    return [];
  }
  const bilinen = new Set(sitemapUrls);
  const out = new Set();
  for (const f of dosyalar) {
    if (!f.endsWith('.html')) continue;
    const url = f === 'index.html'
      ? `https://${HOST}/`
      : f.endsWith('/index.html')
        ? `https://${HOST}/${f.slice(0, -'index.html'.length)}`
        : `https://${HOST}/${f}`;
    if (bilinen.has(url)) out.add(url);
  }
  return [...out];
}

const TUMU = process.argv.includes('--all');
// --dry · ne göndereceğini yaz, İSTEK ATMA. Betikte yoktu; 2026-08-20'de
// değişiklik test edilirken uç noktaya gereksiz iki tam gönderim yapıldı.
const DRY = process.argv.includes('--dry');
const urlList = TUMU ? sitemapUrls : degisenUrller();

console.log(TUMU
  ? `[--all] Sitemap'in tamamı bildirilecek: ${urlList.length} URL.`
  : `Son commit'te değişen ${urlList.length} sayfa bildirilecek (sitemap ${sitemapUrls.length} URL).`);

if (urlList.length === 0) {
  console.log('No URLs found, skipping IndexNow ping.');
  process.exit(0);
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function sendBatch(urls, batchIndex, totalBatches) {
  return new Promise((resolve, reject) => {
    const payload = JSON.stringify({
      host: HOST,
      key: KEY,
      keyLocation: `https://${HOST}/${KEY}.txt`,
      urlList: urls
    });

    const options = {
      hostname: 'api.indexnow.org',
      path: '/indexnow',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json; charset=utf-8',
        'Content-Length': Buffer.byteLength(payload)
      }
    };

    const req = https.request(options, (res) => {
      let responseData = '';
      res.on('data', (chunk) => { responseData += chunk; });
      res.on('end', () => {
        const status = res.statusCode;
        console.log(`  Batch ${batchIndex + 1}/${totalBatches}: ${status} ${res.statusMessage} (${urls.length} URLs)`);

        if (status === 200 || status === 202) {
          resolve({ success: true, status });
        } else if (status === 429) {
          console.warn(`  Rate limited — will retry after delay.`);
          resolve({ success: false, status, retryable: true });
        } else if (status >= 500) {
          console.warn(`  Server error — will retry after delay.`);
          resolve({ success: false, status, retryable: true, body: responseData });
        } else {
          console.error(`  Rejected: ${responseData}`);
          resolve({ success: false, status, retryable: false, body: responseData });
        }
      });
    });

    req.on('error', (e) => {
      console.error(`  Network error: ${e.message}`);
      resolve({ success: false, retryable: true, error: e.message });
    });

    req.write(payload);
    req.end();
  });
}

async function main() {
  // Chunk URLs into batches of CHUNK_SIZE
  const chunks = [];
  for (let i = 0; i < urlList.length; i += CHUNK_SIZE) {
    chunks.push(urlList.slice(i, i + CHUNK_SIZE));
  }

  if (DRY) {
    console.log(`[--dry] ${urlList.length} URL, ${chunks.length} istek · gönderilmedi.`);
    console.log('  örnek:', urlList.slice(0, 4));
    return;
  }

  console.log(`Sending ${urlList.length} URLs in ${chunks.length} batch(es)...`);

  let totalSuccess = 0;
  let totalFailed = 0;

  for (let i = 0; i < chunks.length; i++) {
    let retries = 0;
    let result;

    while (retries <= MAX_RETRIES) {
      result = await sendBatch(chunks[i], i, chunks.length);

      if (result.success) {
        totalSuccess += chunks[i].length;
        break;
      }

      if (!result.retryable || retries >= MAX_RETRIES) {
        totalFailed += chunks[i].length;
        console.error(`  Batch ${i + 1} failed permanently after ${retries} retries.`);
        break;
      }

      retries++;
      const delay = RETRY_DELAY_MS * Math.pow(2, retries - 1); // exponential backoff
      console.log(`  Retrying batch ${i + 1} in ${delay}ms (attempt ${retries}/${MAX_RETRIES})...`);
      await sleep(delay);
    }

    // Small delay between batches to be polite
    if (i < chunks.length - 1) {
      await sleep(1000);
    }
  }

  console.log(`\nIndexNow ping complete: ${totalSuccess} succeeded, ${totalFailed} failed.`);
  if (totalFailed > 0) {
    process.exit(1);
  }
}

main().catch(err => {
  console.error(`Unexpected error: ${err.message}`);
  process.exit(1);
});
