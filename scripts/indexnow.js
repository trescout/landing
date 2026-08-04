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
const urlList = urlMatches.map(m => m.replace('<loc>', '').replace('</loc>', ''));

console.log(`Extracted ${urlList.length} URLs from sitemap.xml for IndexNow ping.`);

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
