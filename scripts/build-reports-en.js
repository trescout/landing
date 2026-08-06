const fs = require('fs');
const path = require('path');

const ROOT = path.dirname(__dirname);
const REPORTS_DIR = path.join(ROOT, 'reports');
const EN_REPORTS_DIR = path.join(ROOT, 'en', 'reports');

/**
 * İki rapor varyantı · normal ve tekrarsız ("fresh only").
 * Türkçe tarafta /reports/ ve /reports/tekrarsiz/ olarak yayınlanıyor;
 * İngilizce tarafta karşılıkları /en/reports/ ve /en/reports/fresh/.
 * Tekrarsız varyantı 2026-08-06'ya kadar İngilizce tarafta hiç yoktu.
 */
const VARIANTS = [
  {
    kind: 'normal',
    srcDir: REPORTS_DIR,
    outDir: EN_REPORTS_DIR,
    urlBase: '/en/reports',
    trUrlBase: '/reports',
    enPdf: (d) => `trescout-report-${d}-en.pdf`,
    trPdf: (d) => `trescout-rapor-${d}.pdf`,
    backLabel: 'All Reports',
    title: 'Daily Technology Reports',
    intro: 'Daily AI-curated summaries of GitHub Trending, Hacker News, HuggingFace and Lobsters. Read online in English or download the English PDF.',
  },
  {
    kind: 'fresh',
    srcDir: path.join(REPORTS_DIR, 'tekrarsiz'),
    outDir: path.join(EN_REPORTS_DIR, 'fresh'),
    urlBase: '/en/reports/fresh',
    trUrlBase: '/reports/tekrarsiz',
    enPdf: (d) => `trescout-report-fresh-${d}-en.pdf`,
    trPdf: (d) => `trescout-rapor-tekrarsiz-${d}.pdf`,
    backLabel: 'Fresh Only',
    title: 'Fresh Only Reports',
    intro: 'Only what is new today. Repositories already covered in the last 30 days are filtered out, so nothing repeats.',
  },
];

/** Arşiv sekmeleri · Türkçe taraftaki arch-tabs ile aynı desen */
function archiveTabs(active) {
  const tab = (href, label, on) =>
    `<a class="btn ${on ? 'btn-primary' : 'btn-ghost'}" href="${href}"${on ? ' aria-current="page"' : ''}>${label}</a>`;
  return `<div class="arch-tabs">${tab('/en/reports/', 'All Reports', active === 'normal')}${tab('/en/reports/fresh/', 'Fresh Only', active === 'fresh')}</div>`;
}

const monthNames = [
  'January', 'February', 'March', 'April', 'May', 'June',
  'July', 'August', 'September', 'October', 'November', 'December'
];

const dayNames = [
  'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'
];

function formatEnDate(dateStr) {
  const [y, m, d] = dateStr.split('-').map(Number);
  const dt = new Date(Date.UTC(y, m - 1, d));
  const dayName = dayNames[dt.getUTCDay()];
  const monthName = monthNames[m - 1];
  return `${monthName} ${d}, ${y} (${dayName})`;
}

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
          <li><a href="/privacy.html" target="_blank" rel="noopener">Privacy Notice</a></li>
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

function buildVariant(V) {
const dirs = fs.existsSync(V.srcDir)
  ? fs.readdirSync(V.srcDir).filter(d => /^\d{4}-\d{2}-\d{2}$/.test(d) && fs.statSync(path.join(V.srcDir, d)).isDirectory())
  : [];

console.log(`Generating ${dirs.length} English ${V.kind} report pages under ${V.urlBase}/[date]/...`);

let count = 0;
const reportCards = [];

dirs.sort().reverse().forEach(dateStr => {
  const trDir = path.join(V.srcDir, dateStr);
  const trHtmlPath = path.join(trDir, 'index.html');
  if (!fs.existsSync(trHtmlPath)) return;

  const trHtml = fs.readFileSync(trHtmlPath, 'utf8');

  // Extract meta/editorial details
  const titleMatch = trHtml.match(/<h1 class="rep-title">(.*?)<\/h1>/);
  const editorialMatch = trHtml.match(/<p class="rep-editorial">(.*?)<\/p>/);
  const chipsMatch = trHtml.match(/<div class="rep-chips">(.*?)<\/div>/s);

  const enDateFormatted = formatEnDate(dateStr);
  
  // Dedicated English PDF URL
  // İngilizce PDF varsa onu ver, yoksa orijinal Türkçe raporu · etiket buna göre
  // değişir (landing#68'de boş EN PDF'ler silinmişti, #69'da gerçeği üretildi).
  const trPdfUrl = `/reports/${V.trPdf(dateStr)}`;
  const enPdfPath = path.join(ROOT, 'reports', V.enPdf(dateStr));
  const enPdfVar = fs.existsSync(enPdfPath);
  const pdfUrl = enPdfVar ? `/reports/${V.enPdf(dateStr)}` : trPdfUrl;

  // Translate chips
  let enChips = chipsMatch ? chipsMatch[1] : '<span class="chip">Daily Tech Radar</span>';
  enChips = enChips
    .replace(/Günün Modelleri/g, 'Daily Models')
    .replace(/Günün Makaleleri/g, 'Daily Papers')
    .replace(/öne çıkan/g, 'highlights');

  // Add historical translated archive badge for dates <= 2026-08-05
  const isHistoricalArchive = dateStr <= '2026-08-05';
  const badgeTag = isHistoricalArchive ? 
    `<span class="chip chip-en">Translated Archive</span>` : '';

  // Gün sayfasının açılışı · İngilizce arşiv JSON'undaki GERÇEK editöryel.
  // Önceden her gün için aynı tanıtım cümlesi basılıyordu ("Daily AI Tech Radar
  // compilation for …") · 127 sayfa birbirinin kopyasıydı ve o günün raporu
  // hakkında hiçbir şey söylemiyordu. Artık build-en-report.ts'in çevirdiği
  // açılış metni kullanılıyor; yoksa eski tanıtım cümlesine düşer.
  const enJsonPath = path.join(ROOT, 'reports', `${V.enPdf(dateStr).replace(/\.pdf$/, '')}.json`);
  let enEditorial = `Daily AI Tech Radar compilation for ${enDateFormatted}.`;
  if (fs.existsSync(enJsonPath)) {
    try {
      const enArchive = JSON.parse(fs.readFileSync(enJsonPath, 'utf8'));
      if (enArchive.editorial) enEditorial = enArchive.editorial;
    } catch { /* bozuk JSON · tanıtım cümlesi kalsın */ }
  }

  const enReportDir = path.join(V.outDir, dateStr);
  fs.mkdirSync(enReportDir, { recursive: true });

  const enReportHtml = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${enDateFormatted} · TreScout Daily Report</title>
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<meta name="description" content="TreScout Daily Technology Intelligence Report for ${enDateFormatted}. Curated open-source tools, Hacker News discussions, and AI papers.">
<link rel="canonical" href="https://trescout.com${V.urlBase}/${dateStr}/">
<link rel="alternate" hreflang="tr" href="https://trescout.com${V.trUrlBase}/${dateStr}/">
<link rel="alternate" hreflang="en" href="https://trescout.com${V.urlBase}/${dateStr}/">
<link rel="alternate" hreflang="x-default" href="https://trescout.com${V.urlBase}/${dateStr}/">
<meta property="og:title" content="${enDateFormatted} · TreScout Daily Report">
<meta property="og:description" content="TreScout Daily Technology Intelligence Report for ${enDateFormatted}.">
<meta property="og:url" content="https://trescout.com${V.urlBase}/${dateStr}/">
<meta property="og:type" content="article">
<meta property="og:locale" content="en_US">
<link rel="stylesheet" href="/assets/site.css">
<link rel="stylesheet" href="/assets/report-cover.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>
  <nav><div class="container nav-inner"><a class="logo-link" href="/en/" aria-label="TreScout Home"><svg width="32" height="32" viewBox="0 0 100 100" aria-hidden="true"><rect x="0" y="0" width="100" height="100" rx="22" fill="#1B4965"/><path d="M 20 56 A 30 30 0 0 1 80 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.3" stroke-linecap="round"/><path d="M 30 56 A 20 20 0 0 1 70 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.5" stroke-linecap="round"/><path d="M 40 56 A 10 10 0 0 1 60 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.75" stroke-linecap="round"/><rect x="20" y="56" width="60" height="11" rx="2" fill="#F4D35E"/><rect x="44.5" y="56" width="11" height="28" rx="2" fill="#F4D35E"/></svg><span>TreScout</span></a><div class="nav-actions"><a href="/en/discover/" class="btn btn-ghost">Discover</a><a href="/en/dictionary/" class="btn btn-ghost">Dictionary</a><a href="/en/reports/" class="btn btn-ghost">Reports Archive</a><a href="/en/compare/rss-vs-ai/" class="btn btn-ghost">Compare</a><a href="/reports/${dateStr}/" class="btn btn-ghost" aria-label="Switch to Turkish">TR</a></div></div></nav>

  <main id="main">
    <article class="report-main">
      <a class="rep-back" href="${V.urlBase}/">← ${V.backLabel}</a>
      <div class="rep-eyebrow">Daily Technology Report ${isHistoricalArchive ? '· Translated Archive Edition' : ''}</div>
      <h1 class="rep-title">${enDateFormatted}</h1>
      <div class="rep-chips">${badgeTag}${enChips}</div>
      <p class="rep-editorial">${enEditorial}</p>
      <div class="rep-actions">
        <a class="act act-read" href="${pdfUrl}" target="_blank" rel="noopener">${enPdfVar ? 'Open English PDF →' : 'Open original PDF (Turkish) →'}</a>
        <a class="act act-dl" href="${pdfUrl}" download>Download PDF</a>
      </div>
      <p class="rep-note">${enPdfVar
        ? 'Full report PDF: every item with its summary, source links and the glossary of terms. Translated from the original Turkish edition.'
        : 'The full report PDF is currently published in Turkish only. Repository names, metrics and links are language independent. An English PDF edition is in preparation.'}</p>
      <aside class="signup-cta">
        <p><strong>Get daily technology reports in your inbox.</strong> TreScout scans, summarizes, and delivers. You just read.</p>
        <a class="btn btn-primary" href="/en/#top">Join Early Access List →</a>
      </aside>
    </article>
  </main>

  ${richEnFooter}
</body>
</html>`;

  fs.writeFileSync(path.join(enReportDir, 'index.html'), enReportHtml, 'utf8');
  count++;

  reportCards.push(`
        <article class="card">
          <a class="card-main" href="${V.urlBase}/${dateStr}/">
            <time class="card-date" datetime="${dateStr}">${enDateFormatted}</time>
            <p class="card-teaser">${enEditorial.substring(0, 160)}...</p>
            <div class="card-chips">${badgeTag}${enChips}</div>
          </a>
          <div class="card-actions">
            <a class="act act-read" href="${V.urlBase}/${dateStr}/">Read →</a>
            <a class="act act-pdf" href="${pdfUrl}" download>${enPdfVar ? 'Download PDF' : 'PDF (Turkish)'}</a>
          </div>
        </article>`);
});

console.log(`Generated ${count} English daily report pages!`);

// Update /en/reports/index.html with clear banner distinguishing historical translated archives vs future live reports
const enReportsIndexHtml = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Daily Technology Reports Archive · TreScout</title>
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<meta name="description" content="TreScout daily technology reports archive · Curated AI summaries of GitHub, Hacker News, and HuggingFace trends every day.">
<link rel="canonical" href="https://trescout.com${V.urlBase}/">
<link rel="alternate" hreflang="tr" href="https://trescout.com${V.trUrlBase}/">
<link rel="alternate" hreflang="en" href="https://trescout.com${V.urlBase}/">
<link rel="alternate" hreflang="x-default" href="https://trescout.com${V.urlBase}/">
<meta property="og:title" content="Daily Technology Reports Archive · TreScout">
<meta property="og:description" content="TreScout daily technology reports archive · Curated AI summaries of GitHub, Hacker News, and HuggingFace trends every day.">
<meta property="og:url" content="https://trescout.com${V.urlBase}/">
<meta property="og:type" content="website">
<meta property="og:locale" content="en_US">
<link rel="stylesheet" href="/assets/site.css">
<link rel="stylesheet" href="/assets/report-archive.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>
  <nav><div class="container nav-inner"><a class="logo-link" href="/en/" aria-label="TreScout Home"><svg width="32" height="32" viewBox="0 0 100 100" aria-hidden="true"><rect x="0" y="0" width="100" height="100" rx="22" fill="#1B4965"/><path d="M 20 56 A 30 30 0 0 1 80 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.3" stroke-linecap="round"/><path d="M 30 56 A 20 20 0 0 1 70 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.5" stroke-linecap="round"/><path d="M 40 56 A 10 10 0 0 1 60 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.75" stroke-linecap="round"/><rect x="20" y="56" width="60" height="11" rx="2" fill="#F4D35E"/><rect x="44.5" y="56" width="11" height="28" rx="2" fill="#F4D35E"/></svg><span>TreScout</span></a><div class="nav-actions"><a href="/en/discover/" class="btn btn-ghost">Discover</a><a href="/en/dictionary/" class="btn btn-ghost">Dictionary</a><a href="/en/reports/" class="btn btn-ghost" aria-current="page">Reports Archive</a><a href="/en/compare/rss-vs-ai/" class="btn btn-ghost">Compare</a><a href="/reports/" class="btn btn-ghost" aria-label="Switch to Turkish">TR</a></div></div></nav>

  <main id="main">
    <div class="archive-main">
      <div class="arch-eyebrow">Archive</div>
      <h1 class="arch-title">${V.title}</h1>
      ${archiveTabs(V.kind)}
      <p class="arch-intro">${V.intro}</p>

      <div class="arch-banner">
        <div class="arch-banner-title">
          <span>🌐</span> <span>Historical Translated Archive Notice</span>
        </div>
        <p class="arch-banner-text">
          These English pages and report PDFs are translated from the original Turkish daily reports. Item selection, metrics and links are identical to the Turkish edition.
        </p>
      </div>

      <div class="arch-list">
        ${reportCards.join('\n')}
      </div>
    </div>
  </main>

  ${richEnFooter}
</body>
</html>`;

fs.mkdirSync(V.outDir, { recursive: true });
fs.writeFileSync(path.join(V.outDir, 'index.html'), enReportsIndexHtml, 'utf8');
console.log(`Updated ${V.urlBase}/index.html · ${count} pages`);
}

for (const V of VARIANTS) buildVariant(V);
console.log('English report pages: done.');
