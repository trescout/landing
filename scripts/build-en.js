#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

const ROOT = path.dirname(__dirname);
const DICT_JSON = path.join(ROOT, 'assets', 'dictionary', 'dictionary.json');
const CAT_JSON = path.join(ROOT, 'assets', 'discover', 'catalog.json');
const SITEMAP = path.join(ROOT, 'sitemap.xml');

const dictionary = JSON.parse(fs.readFileSync(DICT_JSON, 'utf8'));
const catalog = JSON.parse(fs.readFileSync(CAT_JSON, 'utf8'));

console.log(`Loaded ${dictionary.length} dictionary terms and ${catalog.length} discover items.`);

// 1. Generate /en/dictionary/ entries
let enDictCount = 0;
dictionary.forEach(t => {
  const slug = t.slug;
  const enTitle = t.en;
  const full = t.full || '';
  const canonTr = `https://trescout.com/dictionary/${slug}/`;
  const canonEn = `https://trescout.com/en/dictionary/${slug}/`;

  // Update TR page hreflang
  const trHtmlPath = path.join(ROOT, 'dictionary', slug, 'index.html');
  if (fs.existsSync(trHtmlPath)) {
    let trHtml = fs.readFileSync(trHtmlPath, 'utf8');
    if (!trHtml.includes('hreflang="en"')) {
      const hrefTags = `<link rel="alternate" hreflang="tr" href="${canonTr}">\n<link rel="alternate" hreflang="en" href="${canonEn}">\n`;
      trHtml = trHtml.replace('<link rel="canonical"', hrefTags + '<link rel="canonical"');
      fs.writeFileSync(trHtmlPath, trHtml, 'utf8');
    }
  }

  // Create EN HTML page
  const enDir = path.join(ROOT, 'en', 'dictionary', slug);
  fs.mkdirSync(enDir, { recursive: true });

  const desc = t.kisa || `${enTitle} definition and technical overview.`;
  const htmlContent = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${enTitle} · What is it? · TreScout Dictionary</title>
<meta name="description" content="${desc}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="canonical" href="${canonEn}">
<link rel="alternate" hreflang="tr" href="${canonTr}">
<link rel="alternate" hreflang="en" href="${canonEn}">
<link rel="alternate" type="text/markdown" href="/en/dictionary/${slug}.md">
<meta property="og:title" content="What is ${enTitle}? · TreScout">
<meta property="og:description" content="${desc}">
<meta property="og:url" content="${canonEn}">
<meta property="og:type" content="article">
<meta property="og:locale" content="en_US">
<link rel="preload" href="/assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css">
<link rel="stylesheet" href="/assets/discover.css">
<link rel="stylesheet" href="/assets/dictionary.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
<nav><div class="container nav-inner"><a class="logo-link" href="/en/" aria-label="TreScout Home"><svg width="32" height="32" viewBox="0 0 100 100" aria-hidden="true"><rect x="0" y="0" width="100" height="100" rx="22" fill="#1B4965"/><path d="M 20 56 A 30 30 0 0 1 80 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.3" stroke-linecap="round"/><path d="M 30 56 A 20 20 0 0 1 70 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.5" stroke-linecap="round"/><path d="M 40 56 A 10 10 0 0 1 60 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.75" stroke-linecap="round"/><rect x="20" y="56" width="60" height="11" rx="2" fill="#F4D35E"/><rect x="44.5" y="56" width="11" height="28" rx="2" fill="#F4D35E"/></svg><span>TreScout</span></a><div class="nav-actions"><a href="/en/discover/" class="btn btn-ghost">Discover</a><a href="/en/dictionary/" class="btn btn-ghost">Dictionary</a><a href="/compare/rss-vs-ai/" class="btn btn-ghost">Compare</a><a href="/dictionary/${slug}/" class="btn btn-ghost">TR</a></div></div></nav>
<main id="main">
<article class="disc container" style="max-width:800px; margin:40px auto; padding:0 20px;">
<a class="disc-back" href="/en/dictionary/">← Dictionary</a>
<div class="disc-top"><span class="disc-eyebrow">Dictionary · ${t.cat || 'Tech'}</span></div>
<h1 class="disc-title">What is <span class="disc-accent">${enTitle}</span>?</h1>
${full ? `<p class="dict-en">${full}</p>` : ''}
<p class="disc-lead">${desc}</p>
<section class="disc-sec"><h2>Technical Summary</h2><p>${desc}</p></section>
<aside class="disc-cta"><p><strong>Daily AI-Filtered Tech Radar.</strong> TreScout scans GitHub, Hacker News, and HuggingFace daily to bring you curated insights.</p><a class="btn btn-primary" href="/en/">Learn More</a></aside>
</article>
</main>
<footer class="footer"><div class="container footer-inner"><p>© 2026 TreScout · All rights reserved.</p></div></footer>
</body>
</html>`;

  fs.writeFileSync(path.join(enDir, 'index.html'), htmlContent, 'utf8');

  // Create EN Markdown page
  const mdContent = `# What is ${enTitle}?\n\n${full ? `**Full Name:** ${full}\n\n` : ''}**Category:** ${t.cat || 'Tech'}\n\n## Overview\n${desc}\n\n---\nSource: TreScout Tech Dictionary · ${canonEn}\n`;
  fs.writeFileSync(path.join(ROOT, 'en', 'dictionary', `${slug}.md`), mdContent, 'utf8');
  enDictCount++;
});

console.log(`Generated ${enDictCount} EN dictionary pages & markdown files.`);

// 2. Generate /en/discover/ entries
let enDiscCount = 0;
catalog.forEach(c => {
  const slug = c.slug;
  const title = c.title;
  const canonTr = `https://trescout.com/discover/${slug}/`;
  const canonEn = `https://trescout.com/en/discover/${slug}/`;

  // Update TR page hreflang
  const trHtmlPath = path.join(ROOT, 'discover', slug, 'index.html');
  if (fs.existsSync(trHtmlPath)) {
    let trHtml = fs.readFileSync(trHtmlPath, 'utf8');
    if (!trHtml.includes('hreflang="en"')) {
      const hrefTags = `<link rel="alternate" hreflang="tr" href="${canonTr}">\n<link rel="alternate" hreflang="en" href="${canonEn}">\n`;
      trHtml = trHtml.replace('<link rel="canonical"', hrefTags + '<link rel="canonical"');
      fs.writeFileSync(trHtmlPath, trHtml, 'utf8');
    }
  }

  // Create EN HTML page
  const enDir = path.join(ROOT, 'en', 'discover', slug);
  fs.mkdirSync(enDir, { recursive: true });

  const tagline = c.tagline || `${title} open-source repository overview.`;
  const htmlContent = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${title} · Discover · TreScout</title>
<meta name="description" content="${tagline}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="canonical" href="${canonEn}">
<link rel="alternate" hreflang="tr" href="${canonTr}">
<link rel="alternate" hreflang="en" href="${canonEn}">
<link rel="alternate" type="text/markdown" href="/en/discover/${slug}.md">
<meta property="og:title" content="${title} · TreScout Discover">
<meta property="og:description" content="${tagline}">
<meta property="og:url" content="${canonEn}">
<meta property="og:type" content="article">
<meta property="og:locale" content="en_US">
<link rel="preload" href="/assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css">
<link rel="stylesheet" href="/assets/discover.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
<nav><div class="container nav-inner"><a class="logo-link" href="/en/" aria-label="TreScout Home"><svg width="32" height="32" viewBox="0 0 100 100" aria-hidden="true"><rect x="0" y="0" width="100" height="100" rx="22" fill="#1B4965"/><path d="M 20 56 A 30 30 0 0 1 80 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.3" stroke-linecap="round"/><path d="M 30 56 A 20 20 0 0 1 70 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.5" stroke-linecap="round"/><path d="M 40 56 A 10 10 0 0 1 60 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.75" stroke-linecap="round"/><rect x="20" y="56" width="60" height="11" rx="2" fill="#F4D35E"/><rect x="44.5" y="56" width="11" height="28" rx="2" fill="#F4D35E"/></svg><span>TreScout</span></a><div class="nav-actions"><a href="/en/discover/" class="btn btn-ghost">Discover</a><a href="/en/dictionary/" class="btn btn-ghost">Dictionary</a><a href="/compare/rss-vs-ai/" class="btn btn-ghost">Compare</a><a href="/discover/${slug}/" class="btn btn-ghost">TR</a></div></div></nav>
<main id="main">
<article class="disc container" style="max-width:800px; margin:40px auto; padding:0 20px;">
<a class="disc-back" href="/en/discover/">← Discover</a>
<div class="disc-top"><span class="disc-eyebrow">Discover · ${c.source || 'GitHub'}</span></div>
<h1 class="disc-title">${title}</h1>
<p class="disc-lead">${tagline}</p>
<section class="disc-sec"><h2>Project Stats</h2><p>Stars: ${c.stars || 0} · Date: ${c.date || ''}</p></section>
<aside class="disc-cta"><p><strong>Daily AI-Filtered Tech Radar.</strong> TreScout scans GitHub, Hacker News, and HuggingFace daily to bring you curated insights.</p><a class="btn btn-primary" href="/en/">Learn More</a></aside>
</article>
</main>
<footer class="footer"><div class="container footer-inner"><p>© 2026 TreScout · All rights reserved.</p></div></footer>
</body>
</html>`;

  fs.writeFileSync(path.join(enDir, 'index.html'), htmlContent, 'utf8');

  // Create EN Markdown page
  const mdContent = `# ${title}\n\n> ${tagline}\n\n**Source:** ${c.source || 'GitHub'}  \n**Stars:** ${c.stars || 0}\n\n---\nSource: TreScout Discover · ${canonEn}\n`;
  fs.writeFileSync(path.join(ROOT, 'en', 'discover', `${slug}.md`), mdContent, 'utf8');
  enDiscCount++;
});

console.log(`Generated ${enDiscCount} EN discover pages & markdown files.`);

// 3. Update sitemap.xml with all new EN URLs
let sm = fs.readFileSync(SITEMAP, 'utf8');
let smLines = [];

dictionary.forEach(t => {
  const url = `https://trescout.com/en/dictionary/${t.slug}/`;
  if (!sm.includes(url)) {
    smLines.push(`  <url>\n    <loc>${url}</loc>\n    <lastmod>2026-08-04</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.6</priority>\n  </url>`);
  }
});

catalog.forEach(c => {
  const url = `https://trescout.com/en/discover/${c.slug}/`;
  if (!sm.includes(url)) {
    smLines.push(`  <url>\n    <loc>${url}</loc>\n    <lastmod>2026-08-04</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.6</priority>\n  </url>`);
  }
});

if (smLines.length > 0) {
  sm = sm.replace('</urlset>', smLines.join('\n') + '\n</urlset>');
  fs.writeFileSync(SITEMAP, sm, 'utf8');
  console.log(`Added ${smLines.length} EN URLs to sitemap.xml.`);
}

console.log('Build EN script completed successfully!');
