#!/usr/bin/env node
/**
 * ⚠️ DETAY SAYFALARI ARTIK BURADAN ÜRETİLMİYOR (2026-08-06).
 *
 * Bu betik keşif ve sözlük detay sayfalarını "SEO kabuğu" olarak basıyordu:
 * başlık + tek cümle + sabit kalıp metin. 480 sözlük sayfasında aynı cümle
 * ("Modern software systems leverage <TERİM> to…") yayına çıkmıştı.
 *
 * Detay sayfaları + .md dosyaları artık Türkçesinden üretiliyor:
 *   scripts/discover-en.py      · İngilizce keşif sayfaları
 *   scripts/dictionary-en.py    · İngilizce sözlük sayfaları
 * İkisi de dict-sync.yml hattında çalışıyor.
 *
 * Bu betikte YALNIZ dizin sayfaları (<dil>/discover/index.html,
 * <dil>/dictionary/index.html) üretimi geçerli. Detay sayfası yazan bölümler
 * devre dışı · çalıştırılırsa bugünkü içeriği ezmesin diye.
 *
 * 2026-08-07 · dile göre çalışır:  node scripts/build-en.js --lang=fr
 * Metinler scripts/diller.py'den okunuyor · tablo JS'e ikinci kez yazılmasın diye.
 */
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const LANG = (process.argv.find(a => a.startsWith('--lang=')) || '--lang=en').split('=')[1];

const ROOT = path.dirname(__dirname);
const DICT_JSON = path.join(ROOT, 'assets', 'dictionary', 'dictionary.json');
const CAT_JSON = path.join(ROOT, 'assets', 'discover', 'catalog.json');
const SITEMAP = path.join(ROOT, 'sitemap.xml');
const TODAY = new Date().toISOString().split('T')[0];
const BASE_URL = process.env.SITE_URL || 'https://trescout.com';

let dictionary, catalog;
try {
  dictionary = JSON.parse(fs.readFileSync(DICT_JSON, 'utf8'));
  catalog = JSON.parse(fs.readFileSync(CAT_JSON, 'utf8'));
} catch (err) {
  console.error(`Failed to load data files: ${err.message}`);
  process.exit(1);
}

console.log(`Loaded ${dictionary.length} dictionary terms and ${catalog.length} discover items.`);


const richEnFooter = `<footer>
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand-block">
        <div class="footer-logo">
          <svg width="32" height="32" viewBox="0 0 100 100" aria-hidden="true"><rect x="0" y="0" width="100" height="100" rx="22" fill="#1B4965"/><path d="M 20 56 A 30 30 0 0 1 80 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.3" stroke-linecap="round"/><path d="M 30 56 A 20 20 0 0 1 70 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.5" stroke-linecap="round"/><path d="M 40 56 A 10 10 0 0 1 60 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.75" stroke-linecap="round"/><rect x="20" y="56" width="60" height="11" rx="2" fill="#F4D35E"/><rect x="44.5" y="56" width="11" height="28" rx="2" fill="#F4D35E"/></svg>
          <span>TreScout</span>
        </div>
        <p class="footer-tagline">TreScout scans, summarizes, and delivers. You just read.</p>
      </div>
      <div class="footer-col">
        <div class="footer-col-title">Product</div>
        <ul>
          <li><a href="/en/#how-it-works">How It Works</a></li>
          <li><a href="/en/discover/">Discover</a></li>
          <li><a href="/en/dictionary/">Dictionary</a></li>
          <li><a href="/en/reports/">Reports Archive</a></li>
          <li><a href="/en/compare/rss-vs-ai/">Compare</a></li>
          <li><a href="/en/#top">Early Access</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <div class="footer-col-title">Contact</div>
        <ul>
          <li><a href="mailto:hello@trescout.com">hello@trescout.com</a></li>
          <li><a href="/en/privacy.html" target="_blank" rel="noopener">Privacy Notice</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <div class="footer-col-title">Social</div>
        <ul>
          <li><a href="https://x.com/GetTreScout" target="_blank" rel="noopener noreferrer">X / Twitter</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 TreScout · All rights reserved.</span>
    </div>
  </div>
</footer>`;

// 1. Generate /en/dictionary/ entries & sync TR hreflang + EN nav button
let enDictCount = 0;
dictionary.forEach(t => {
  const slug = t.slug;
  const enTitle = t.en;
  const full = t.full || '';
  const canonTr = `${BASE_URL}/dictionary/${slug}/`;
  const canonEn = `${BASE_URL}/en/dictionary/${slug}/`;

  // Create EN HTML page
  const enDir = path.join(ROOT, 'en', 'dictionary', slug);
  fs.mkdirSync(enDir, { recursive: true });

  const desc = t.kisa_en || t.kisa || `${enTitle} definition and technical overview.`;
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
<link rel="alternate" hreflang="x-default" href="${canonEn}">
<link rel="alternate" type="text/markdown" href="/en/dictionary/${slug}.md">
<meta property="og:title" content="What is ${enTitle}? · TreScout">
<meta property="og:description" content="${desc}">
<meta property="og:url" content="${canonEn}">
<meta property="og:type" content="article">
<meta property="og:image" content="https://trescout.com/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta property="og:locale" content="en_US">
<link rel="preload" href="/assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css">
<link rel="stylesheet" href="/assets/discover.css">
<link rel="stylesheet" href="/assets/dictionary.css">
<script type="application/ld+json">
${JSON.stringify({
  "@context": "https://schema.org",
  "@type": "DefinedTerm",
  "name": enTitle,
  "description": desc,
  "inDefinedTermSet": {
    "@type": "DefinedTermSet",
    "name": "TreScout Tech Dictionary",
    "url": `${BASE_URL}/en/dictionary/`
  },
  "url": canonEn
})}
</script>
<script type="application/ld+json">
${JSON.stringify({
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": `${BASE_URL}/en/` },
    { "@type": "ListItem", "position": 2, "name": "Dictionary", "item": `${BASE_URL}/en/dictionary/` },
    { "@type": "ListItem", "position": 3, "name": enTitle }
  ]
})}
</script>
</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
<nav><div class="container nav-inner"><a class="logo-link" href="/en/" aria-label="TreScout Home"><svg width="32" height="32" viewBox="0 0 100 100" aria-hidden="true"><rect x="0" y="0" width="100" height="100" rx="22" fill="#1B4965"/><path d="M 20 56 A 30 30 0 0 1 80 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.3" stroke-linecap="round"/><path d="M 30 56 A 20 20 0 0 1 70 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.5" stroke-linecap="round"/><path d="M 40 56 A 10 10 0 0 1 60 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.75" stroke-linecap="round"/><rect x="20" y="56" width="60" height="11" rx="2" fill="#F4D35E"/><rect x="44.5" y="56" width="11" height="28" rx="2" fill="#F4D35E"/></svg><span>TreScout</span></a><div class="nav-actions"><a href="/en/discover/" class="btn btn-ghost">Discover</a><a href="/en/dictionary/" class="btn btn-ghost">Dictionary</a><a href="/en/reports/" class="btn btn-ghost">Reports Archive</a><a href="/en/compare/rss-vs-ai/" class="btn btn-ghost">Compare</a><a href="/dictionary/${slug}/" class="btn btn-ghost" aria-label="Switch to Turkish">TR</a></div></div></nav>
<main id="main">
<article class="disc">
<a class="disc-back" href="/en/dictionary/">← Dictionary</a>
<div class="disc-top"><span class="disc-eyebrow">Dictionary · ${t.cat || 'Tech'}</span></div>
<h1 class="disc-title">What is <span class="disc-accent">${enTitle}</span>?</h1>
${full ? `<p class="dict-en">${full}</p>` : ''}
<p class="disc-lead">${desc}</p>
<section class="disc-sec"><h2>Overview</h2><p>${desc}</p></section>
<div class="dict-analogy"><strong>Analogy:</strong> Think of <strong>${enTitle}</strong> as a core building block in modern AI and software architectures that helps teams move faster with higher precision.</div>
<section class="disc-sec"><h2>How It Works</h2><p>Modern software systems leverage ${enTitle} to streamline data flow, reduce latency, and provide predictable results across production workloads.</p></section>
<section class="disc-sec"><h2>Use Cases</h2><p>Widely adopted in production AI applications, developer tools, cloud infrastructure, and autonomous agent frameworks to improve scalability and reliability.</p></section>
<section class="disc-sec"><h2>Frequently Asked Questions</h2><div class="dict-faq"><div class="dict-faq-item"><p class="dict-faq-q">Why is ${enTitle} important in modern tech stacks?</p><p class="dict-faq-a">It provides clear boundaries, enhances modularity, and enables developers to build maintainable, high-performance systems.</p></div><div class="dict-faq-item"><p class="dict-faq-q">How does TreScout track ${enTitle}?</p><p class="dict-faq-a">TreScout continuously scans open-source repositories on GitHub, research papers on HuggingFace, and engineering discussions on Hacker News.</p></div></div></section>
<section class="disc-sec"><h2>Related Terms</h2><div class="dict-related"><a href="/en/dictionary/rag/">RAG</a><a href="/en/dictionary/llm/">LLM</a><a href="/en/dictionary/vector-database/">Vector Database</a><a href="/en/dictionary/embedding/">Embedding</a><a href="/en/dictionary/agent/">Agent</a></div></section>
<aside class="disc-cta"><p><strong>New tech terms in your inbox every morning.</strong> Join TreScout early access for daily digests.</p><form class="cta-form disc-cta-form js-subscribe" data-source="dictionary-en" novalidate><div class="form-row"><input class="input" type="email" name="email" placeholder="Enter your email" autocomplete="email" required><button class="btn btn-primary" type="submit">Join Early Access</button></div><label class="form-consent"><input type="checkbox" name="consent" required><span>I have read the <a href="/en/privacy.html" target="_blank" rel="noopener">Privacy Notice</a> and consent to my email being processed for this purpose.</span></label><input type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true" class="hp-field"></form><a class="btn btn-ghost disc-cta-all" href="/en/dictionary/">All terms →</a></aside>
<p class="disc-disclaimer">This guide was prepared in plain language for TreScout · If you spot any typo or missing information, let us know at <a href="mailto:hello@trescout.com">hello@trescout.com</a>. TreScout scans GitHub, Hacker News, and HuggingFace daily.</p>
</article>
</main>
${richEnFooter}
<script src="/assets/subscribe.js" defer></script>
</body>
</html>`;

  // DEVRE DIŞI · discover-en.py / dictionary-en.py üretiyor
  // fs.writeFileSync(path.join(enDir, 'index.html'), htmlContent, 'utf8');

  // Create EN Markdown page
  const mdContent = `# What is ${enTitle}?\n\n${full ? `**Full Name:** ${full}\n\n` : ''}**Category:** ${t.cat || 'Tech'}\n\n## Overview\n${desc}\n\n---\nSource: TreScout Tech Dictionary · ${canonEn}\n`;
  // DEVRE DIŞI · yeni üreticiler .md'yi de yazıyor
  // fs.writeFileSync(path.join(ROOT, 'en', 'dictionary', `${slug}.md`), mdContent, 'utf8');
  enDictCount++;
});

console.log(`Generated ${enDictCount} EN dictionary pages & markdown files.`);

// 2. Generate /en/discover/ entries & sync TR hreflang + EN nav button
let enDiscCount = 0;
catalog.forEach(c => {
  const slug = c.slug;
  const title = c.title;
  const canonTr = `${BASE_URL}/discover/${slug}/`;
  const canonEn = `${BASE_URL}/en/discover/${slug}/`;

  // Create EN HTML page
  const enDir = path.join(ROOT, 'en', 'discover', slug);
  fs.mkdirSync(enDir, { recursive: true });

  const tagline = c.tagline_en || c.tagline || `${title} open-source repository overview.`;
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
<link rel="alternate" hreflang="x-default" href="${canonEn}">
<link rel="alternate" type="text/markdown" href="/en/discover/${slug}.md">
<meta property="og:title" content="${title} · TreScout Discover">
<meta property="og:description" content="${tagline}">
<meta property="og:url" content="${canonEn}">
<meta property="og:type" content="article">
<meta property="og:image" content="https://trescout.com/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta property="og:locale" content="en_US">
<link rel="preload" href="/assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css">
<link rel="stylesheet" href="/assets/discover.css">
<script type="application/ld+json">
${JSON.stringify({
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": title,
  "description": tagline,
  "url": canonEn,
  "applicationCategory": "DeveloperApplication",
  ...(c.stars ? { "interactionStatistic": { "@type": "InteractionCounter", "interactionType": "https://schema.org/LikeAction", "userInteractionCount": c.stars } } : {})
})}
</script>
<script type="application/ld+json">
${JSON.stringify({
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": `${BASE_URL}/en/` },
    { "@type": "ListItem", "position": 2, "name": "Discover", "item": `${BASE_URL}/en/discover/` },
    { "@type": "ListItem", "position": 3, "name": title }
  ]
})}
</script>
</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
<nav><div class="container nav-inner"><a class="logo-link" href="/en/" aria-label="TreScout Home"><svg width="32" height="32" viewBox="0 0 100 100" aria-hidden="true"><rect x="0" y="0" width="100" height="100" rx="22" fill="#1B4965"/><path d="M 20 56 A 30 30 0 0 1 80 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.3" stroke-linecap="round"/><path d="M 30 56 A 20 20 0 0 1 70 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.5" stroke-linecap="round"/><path d="M 40 56 A 10 10 0 0 1 60 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.75" stroke-linecap="round"/><rect x="20" y="56" width="60" height="11" rx="2" fill="#F4D35E"/><rect x="44.5" y="56" width="11" height="28" rx="2" fill="#F4D35E"/></svg><span>TreScout</span></a><div class="nav-actions"><a href="/en/discover/" class="btn btn-ghost">Discover</a><a href="/en/dictionary/" class="btn btn-ghost">Dictionary</a><a href="/en/reports/" class="btn btn-ghost">Reports Archive</a><a href="/en/compare/rss-vs-ai/" class="btn btn-ghost">Compare</a><a href="/discover/${slug}/" class="btn btn-ghost" aria-label="Switch to Turkish">TR</a></div></div></nav>
<main id="main">
<article class="disc">
<a class="disc-back" href="/en/discover/">← Discover</a>
<div class="disc-top"><span class="disc-eyebrow">Discover · ${c.source || 'GitHub'}</span></div>
<h1 class="disc-title">${title}</h1>
<p class="disc-lead">${tagline}</p>
<section class="disc-sec"><h2>Project Stats</h2><p>Stars: ${c.stars || 0}${c.date ? ` · Date: ${c.date}` : ''}</p></section>
<aside class="disc-cta"><p><strong>Daily AI-Filtered Tech Radar.</strong> TreScout scans GitHub, Hacker News, and HuggingFace daily to bring you curated insights.</p><a class="btn btn-primary" href="/en/#top">Join Early Access</a></aside>
</article>
</main>
${richEnFooter}
<script src="/assets/subscribe.js" defer></script>
</body>
</html>`;

  // DEVRE DIŞI · discover-en.py / dictionary-en.py üretiyor
  // fs.writeFileSync(path.join(enDir, 'index.html'), htmlContent, 'utf8');

  // Create EN Markdown page
  const mdContent = `# ${title}\n\n> ${tagline}\n\n**Source:** ${c.source || 'GitHub'}  \n**Stars:** ${c.stars || 0}\n\n---\nSource: TreScout Discover · ${canonEn}\n`;
  // DEVRE DIŞI · yeni üreticiler .md'yi de yazıyor
  // fs.writeFileSync(path.join(ROOT, 'en', 'discover', `${slug}.md`), mdContent, 'utf8');
  enDiscCount++;
});

console.log(`Generated ${enDiscCount} EN discover pages & markdown files.`);

const D = JSON.parse(
  execFileSync('python3', [path.join(__dirname, 'diller.py'), '--json', LANG], { encoding: 'utf8' })
);
const PRE = D.onek;              // '/en' · '/fr'
const tagTranslationMap = D.etiketler;

/**
 * Türkçe binlik ayırıcıyı sayfanın diline çevir · 77.021 → 77,021 (en) ·
 * 77 021 (fr, bölünmez boşluk). Kartlardaki yıldız sayısı katalogdan Türkçe
 * biçimde geliyordu ve İngilizce dizinde de öyle basılıyordu (2026-08-07) ·
 * İngiliz okur 77.021'i ondalık sanar. Detay sayfalarındaki kural (discover-en.py
 * sayi_en) ile aynı.
 */
const sayi = (s) => String(s ?? '').replace(/\d{1,3}(?:\.\d{3})+/g, (n) => n.replace(/\./g, D.binlik));

/**
 * Nav + footer'ı o dilin ÜRETİLMİŞ bir detay sayfasından alır.
 * Kanonik kaynak fix-all-headers-and-footers.js · dizin sayfası kendi kabuğunu
 * yazarsa guard'lar kırılır, bu yüzden kopyalıyoruz. TR bağlantısı sayfaya özel
 * olduğu için (o sayfanın Türkçe karşılığı) burada hedefe göre düzeltiliyor.
 */

/** Nav'daki dil düğmelerini sayfaya özel yap · hedefi olmayan etiket korunur. */
const dilYaz = (nav, hedefler) => nav.replace(
  /<a href="[^"]*" class="btn btn-ghost" aria-label="[^"]*">(TR|EN|FR)<\/a>/g,
  (m, et) => hedefler[et]
    ? `<a href="${hedefler[et]}" class="btn btn-ghost" aria-label="${et}">${et}</a>`
    : m
);

function kabuk(bolum, hedefler) {
  const dizin = path.join(ROOT, LANG, bolum);
  const ornek = fs.readdirSync(dizin)
    .map(s => path.join(dizin, s, 'index.html'))
    .find(f => fs.existsSync(f));
  if (!ornek) {
    console.error(`✗ ${LANG}/${bolum} altında üretilmiş sayfa yok · önce detay sayfalarını basın.`);
    process.exit(1);
  }
  const html = fs.readFileSync(ornek, 'utf8');
  const al = (etiket) => {
    const m = html.match(new RegExp(`<${etiket}[\\s>][\\s\\S]*?</${etiket}>`));
    if (!m) { console.error(`✗ ${ornek} içinde <${etiket}> bulunamadı.`); process.exit(1); }
    return m[0];
  };
  return { nav: dilYaz(al('nav'), hedefler), footer: al('footer') };
}

const kafa = (kanonik) => `<link rel="preload" href="/assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css">
<link rel="stylesheet" href="/assets/discover.css">`;

// Kayıt formu · detay sayfalarındakiyle aynı kalıp (discover-en.py · CTA_FORM)
const form = (kaynak) => `<form class="cta-form disc-cta-form js-subscribe" data-source="${kaynak}" novalidate><div class="form-row"><input class="input" type="email" name="email" placeholder="${D.form_yer_tutucu}" autocomplete="email" required><button class="btn btn-primary" type="submit">${D.form_dugme}</button></div><label class="form-consent"><input type="checkbox" name="consent" required><span>${D.form_onay.replace('{gizlilik}', D.gizlilik_yolu)}</span></label><input type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true" class="hp-field"></form>`;

const hreflang = (trYol, hedefYol) => `<link rel="alternate" hreflang="tr" href="${BASE_URL}${trYol}">
<link rel="alternate" hreflang="en" href="${BASE_URL}/en${hedefYol}">
<link rel="alternate" hreflang="fr" href="${BASE_URL}/fr${hedefYol}">
<link rel="alternate" hreflang="x-default" href="${BASE_URL}/en${hedefYol}">`;

// ── 3. Sözlük dizini ────────────────────────────────────────────────────────
const dictIndexDir = path.join(ROOT, LANG, 'dictionary');
fs.mkdirSync(dictIndexDir, { recursive: true });
const dictKabuk = kabuk('dictionary', { TR: '/dictionary/', EN: '/en/dictionary/', FR: '/fr/dictionary/' });

const dictCards = dictionary.map(t => {
  const desc = t[D.kisa_alan] || t.kisa || '';
  const full = t.full ? `<p class="dict-card-en">${t.full}</p>` : '';
  const cat = t.cat || 'ai';
  const searchAttr = `${t.en} ${t.full || ''} ${desc} ${t.slug}`.replace(/"/g, '&quot;');
  return `<a class="dict-card" data-cat="${cat}" data-search="${searchAttr}" href="${PRE}/dictionary/${t.slug}/"><h2 class="dict-card-term">${t.en}</h2>${full}<p class="dict-card-kisa">${desc}</p></a>`;
}).join('\n');

const dictChips = D.sozluk_dizin_cipler.map(([cat, ad], i) =>
  `<button type="button" class="dict-chip${i === 0 ? ' dict-chip-active' : ''}" data-cat="${cat}">${ad}</button>`
).join('');

const dictIndexHtml = `<!DOCTYPE html>
<html lang="${D.html_lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${D.sozluk_dizin_baslik}</title>
<meta name="description" content="${D.sozluk_dizin_aciklama}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="canonical" href="${BASE_URL}${PRE}/dictionary/">
${hreflang('/dictionary/', '/dictionary/')}
<meta property="og:title" content="${D.sozluk_dizin_baslik}">
<meta property="og:description" content="${D.sozluk_dizin_aciklama}">
<meta property="og:url" content="${BASE_URL}${PRE}/dictionary/">
<meta property="og:type" content="website">
<meta property="og:locale" content="${D.og_locale}">
${kafa()}
<link rel="stylesheet" href="/assets/dictionary.css">
</head>
<body>
<a class="skip-link" href="#main">${D.atla}</a>
${dictKabuk.nav}
<main id="main">
<div class="container container-pad">
<div class="dict-index-hero"><span class="disc-eyebrow">${D.sozluk}</span><h1 class="dict-index-title">${D.sozluk_dizin_h1}</h1><p class="dict-index-lead">${D.sozluk_dizin_lead}</p></div>
<div class="dict-controls"><input type="search" id="dict-search" class="dict-search" placeholder="${D.sozluk_dizin_ara}" aria-label="${D.sozluk_dizin_ara_etiket}"></div>
<div class="dict-tags" id="dict-tags">${dictChips}</div>
<p class="dict-count" id="dict-count">${dictionary.length} ${D.sozluk_dizin_birim}</p>
<div class="dict-grid" id="dict-grid">
${dictCards}
</div>
<p class="dict-empty" id="dict-empty">${D.sozluk_dizin_bos}</p>
<aside class="disc-cta"><p><strong>${D.sozluk_cta_baslik}</strong> ${D.sozluk_cta_metin}</p>${form(`dictionary-${LANG}`)}</aside>
</div>
</main>
${dictKabuk.footer}
<script src="/assets/dictionary.js" defer></script>
<script src="/assets/subscribe.js" defer></script>
</body>
</html>`;
fs.writeFileSync(path.join(dictIndexDir, 'index.html'), dictIndexHtml, 'utf8');
console.log(`Üretildi · ${PRE}/dictionary/index.html (${dictionary.length} terim)`);

// ── 4. Keşif dizini ─────────────────────────────────────────────────────────
const discIndexDir = path.join(ROOT, LANG, 'discover');
fs.mkdirSync(discIndexDir, { recursive: true });
const discKabuk = kabuk('discover', { TR: '/discover/', EN: '/en/discover/', FR: '/fr/discover/' });

const discCards = catalog.map(c => {
  const tagline = c[D.tagline_alan] || c.tagline || '';
  const searchAttr = `${c.title} ${tagline} ${c.slug}`.replace(/"/g, '&quot;');
  const imgHtml = c.image ? `<img class="disc-card-img" src="${c.image}" alt="" loading="lazy" decoding="async">` : '';
  const tagChips = (c.tags || []).map(t => `<span class="disc-card-tagchip">${tagTranslationMap[t] || t}</span>`).join('');
  const tagChipsHtml = tagChips ? `<div class="disc-card-tags">${tagChips}</div>` : '';
  const metaStr = c.meta ? sayi(c.meta) : `★ ${sayi((c.stars || 0).toLocaleString('tr-TR'))}`;
  return `<a class="disc-card" data-cat="all" data-search="${searchAttr}" href="${PRE}/discover/${c.slug}/">
    ${imgHtml}
    <div class="disc-card-body">
      <h2 class="disc-card-title">${c.title}</h2>
      <p class="disc-card-tag">${tagline}</p>
      ${tagChipsHtml}
      <span class="disc-card-meta">${metaStr}</span>
    </div>
  </a>`;
}).join('\n');

const discSort = D.kesif_dizin_siralar.map(([v, ad]) => `<option value="${v}">${ad}</option>`).join('');

const discIndexHtml = `<!DOCTYPE html>
<html lang="${D.html_lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${D.kesif_dizin_baslik}</title>
<meta name="description" content="${D.kesif_dizin_aciklama}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="canonical" href="${BASE_URL}${PRE}/discover/">
${hreflang('/discover/', '/discover/')}
<meta property="og:title" content="${D.kesif_dizin_baslik}">
<meta property="og:description" content="${D.kesif_dizin_aciklama}">
<meta property="og:url" content="${BASE_URL}${PRE}/discover/">
<meta property="og:type" content="website">
<meta property="og:locale" content="${D.og_locale}">
${kafa()}
</head>
<body>
<a class="skip-link" href="#main">${D.atla}</a>
${discKabuk.nav}
<main id="main">
<div class="container">
  <div class="disc-index-hero">
    <div class="disc-eyebrow">${D.kesif}</div>
    <h1 class="disc-index-title">${D.kesif_dizin_h1}</h1>
    <p class="disc-index-lead">${D.kesif_dizin_lead}</p>
  </div>

  <div class="disc-controls">
    <input id="disc-search" class="disc-search" type="search" placeholder="${D.kesif_dizin_ara}" aria-label="${D.kesif_dizin_ara_etiket}">
    <div class="disc-sortwrap">
      <label for="disc-sort">${D.kesif_dizin_sirala}</label>
      <select id="disc-sort" class="disc-sort">${discSort}</select>
    </div>
  </div>
  <!-- Kategori çipleri discover.js tarafından kart etiketlerinden kuruluyor ·
       Türkçe dizinde olan bu iki kontrol İngilizcede eksikti (2026-08-07). -->
  <div id="disc-tags" class="disc-tags" role="group" aria-label="${D.kesif_dizin_kategori}"></div>

  <p class="disc-count" id="disc-count">${catalog.length} ${D.kesif_dizin_birim}</p>
  <!-- id discover-grid · discover.js bu id'yi arıyor. Önce disc-grid yazıyordu,
       betik erken çıkıyor ve İngilizce dizinde arama hiç çalışmıyordu. -->
  <div class="disc-grid" id="discover-grid">
    ${discCards}
  </div>
  <p class="disc-empty" id="disc-empty">${D.kesif_dizin_bos}</p>
</div>
</main>
${discKabuk.footer}
<script src="/assets/discover.js" defer></script>
<script src="/assets/subscribe.js" defer></script>
</body>
</html>`;
fs.writeFileSync(path.join(discIndexDir, 'index.html'), discIndexHtml, 'utf8');
console.log(`Üretildi · ${PRE}/discover/index.html (${catalog.length} kayıt)`);

console.log(`build-en.js tamamlandı · dil: ${LANG}`);
