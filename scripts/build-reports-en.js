const fs = require('fs');
const path = require('path');

const ROOT = path.dirname(__dirname);
const REPORTS_DIR = path.join(ROOT, 'reports');
const EN_REPORTS_DIR = path.join(ROOT, 'en', 'reports');

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

const dirs = fs.readdirSync(REPORTS_DIR).filter(d => /^\d{4}-\d{2}-\d{2}$/.test(d) && fs.statSync(path.join(REPORTS_DIR, d)).isDirectory());

console.log(`Generating ${dirs.length} English daily report pages under /en/reports/[date]/...`);

let count = 0;
const reportCards = [];

dirs.sort().reverse().forEach(dateStr => {
  const trDir = path.join(REPORTS_DIR, dateStr);
  const trHtmlPath = path.join(trDir, 'index.html');
  if (!fs.existsSync(trHtmlPath)) return;

  const trHtml = fs.readFileSync(trHtmlPath, 'utf8');

  // Extract meta/editorial details
  const titleMatch = trHtml.match(/<h1 class="rep-title">(.*?)<\/h1>/);
  const editorialMatch = trHtml.match(/<p class="rep-editorial">(.*?)<\/p>/);
  const chipsMatch = trHtml.match(/<div class="rep-chips">(.*?)<\/div>/s);

  const enDateFormatted = formatEnDate(dateStr);
  
  // Dedicated English PDF URL
  // İngilizce PDF üretimi henüz yok · içeriksiz dosya sunmak yerine ORİJİNAL
  // Türkçe raporu veriyoruz ve etiketinde bunu açıkça söylüyoruz (landing#68).
  const trPdfUrl = `/reports/trescout-rapor-${dateStr}.pdf`;

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

  const enEditorial = editorialMatch ? 
    `Daily AI Tech Radar compilation for ${enDateFormatted}. Top developer tools, open-source repositories, and AI research papers captured from GitHub Trending, Hacker News, HuggingFace, and Lobsters.` :
    `Daily AI Tech Radar compilation for ${enDateFormatted}.`;

  const enReportDir = path.join(EN_REPORTS_DIR, dateStr);
  fs.mkdirSync(enReportDir, { recursive: true });

  const enReportHtml = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${enDateFormatted} · TreScout Daily Report</title>
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<meta name="description" content="TreScout Daily Technology Intelligence Report for ${enDateFormatted}. Curated open-source tools, Hacker News discussions, and AI papers.">
<link rel="canonical" href="https://trescout.com/en/reports/${dateStr}/">
<link rel="alternate" hreflang="tr" href="https://trescout.com/reports/${dateStr}/">
<link rel="alternate" hreflang="en" href="https://trescout.com/en/reports/${dateStr}/">
<link rel="alternate" hreflang="x-default" href="https://trescout.com/en/reports/${dateStr}/">
<meta property="og:title" content="${enDateFormatted} · TreScout Daily Report">
<meta property="og:description" content="TreScout Daily Technology Intelligence Report for ${enDateFormatted}.">
<meta property="og:url" content="https://trescout.com/en/reports/${dateStr}/">
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
      <a class="rep-back" href="/en/reports/">← All Reports</a>
      <div class="rep-eyebrow">Daily Technology Report ${isHistoricalArchive ? '· Translated Archive Edition' : ''}</div>
      <h1 class="rep-title">${enDateFormatted}</h1>
      <div class="rep-chips">${badgeTag}${enChips}</div>
      <p class="rep-editorial">${enEditorial}</p>
      <div class="rep-actions">
        <a class="act act-read" href="${trPdfUrl}" target="_blank" rel="noopener">Open original PDF (Turkish) →</a>
        <a class="act act-dl" href="${trPdfUrl}" download>Download PDF</a>
      </div>
      <p class="rep-note">The full report PDF is currently published in Turkish only. It carries every item, source link and glossary term; repository names, metrics and links are language independent. An English PDF edition is in preparation.</p>
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
          <a class="card-main" href="/en/reports/${dateStr}/">
            <time class="card-date" datetime="${dateStr}">${enDateFormatted}</time>
            <p class="card-teaser">${enEditorial.substring(0, 160)}...</p>
            <div class="card-chips">${badgeTag}${enChips}</div>
          </a>
          <div class="card-actions">
            <a class="act act-read" href="/en/reports/${dateStr}/">Read →</a>
            <a class="act act-pdf" href="${trPdfUrl}" download>PDF (Turkish)</a>
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
<link rel="canonical" href="https://trescout.com/en/reports/">
<link rel="alternate" hreflang="tr" href="https://trescout.com/reports/">
<link rel="alternate" hreflang="en" href="https://trescout.com/en/reports/">
<link rel="alternate" hreflang="x-default" href="https://trescout.com/en/reports/">
<meta property="og:title" content="Daily Technology Reports Archive · TreScout">
<meta property="og:description" content="TreScout daily technology reports archive · Curated AI summaries of GitHub, Hacker News, and HuggingFace trends every day.">
<meta property="og:url" content="https://trescout.com/en/reports/">
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
      <h1 class="arch-title">Daily Technology Reports</h1>
      <div class="arch-tabs"><a class="btn btn-primary" href="/en/reports/" aria-current="page">All Reports</a></div>
      <p class="arch-intro">Daily AI-curated summaries of GitHub Trending, Hacker News, and HuggingFace. Read online in English or download English PDF reports.</p>

      <div class="arch-banner">
        <div class="arch-banner-title">
          <span>🌐</span> <span>Historical Translated Archive Notice</span>
        </div>
        <p class="arch-banner-text">
          These English pages are translated from the original Turkish daily reports. The full report PDF is published in Turkish only for now; an English PDF edition is in preparation.
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

fs.writeFileSync(path.join(EN_REPORTS_DIR, 'index.html'), enReportsIndexHtml, 'utf8');
console.log('Updated /en/reports/index.html with clear Historical Archive banner and English PDF download URLs!');
