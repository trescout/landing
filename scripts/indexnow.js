#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const https = require('https');

const ROOT = path.dirname(__dirname);
const SITEMAP = path.join(ROOT, 'sitemap.xml');
const KEY = '4a8f92b1c3d4e5f67890abcdef123456';
const HOST = 'trescout.com';

const sitemapContent = fs.readFileSync(SITEMAP, 'utf8');
const urlMatches = sitemapContent.match(/<loc>(https:\/\/trescout\.com\/[^<]+)<\/loc>/g) || [];
const urlList = urlMatches.map(m => m.replace('<loc>', '').replace('</loc>', ''));

console.log(`Extracted ${urlList.length} URLs from sitemap.xml for IndexNow ping.`);

const payload = JSON.stringify({
  host: HOST,
  key: KEY,
  keyLocation: `https://trescout.com/trescout-indexnow-key.txt`,
  urlList: urlList
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
  console.log(`IndexNow API Response Status: ${res.statusCode} ${res.statusMessage}`);
  let responseData = '';
  res.on('data', (chunk) => { responseData += chunk; });
  res.on('end', () => {
    if (res.statusCode === 200 || res.statusCode === 202) {
      console.log(`Successfully pinged IndexNow with ${urlList.length} URLs in 1 batched payload!`);
    } else {
      console.log(`IndexNow response: ${responseData}`);
    }
  });
});

req.on('error', (e) => {
  console.error(`IndexNow ping request error: ${e.message}`);
});

req.write(payload);
req.end();
