/**
 * ⚠️ KULLANIM DIŞI · yayın hattında ÇAĞRILMIYOR.
 *
 * Yayın hattı (app/scripts/publish-report.ts) yalnız build-en.js ve
 * build-reports-en.js çalıştırıyor. Bu betik eski bir yoldan kalma.
 *
 * Elle çalıştırmayın: İçinde 11 inline style= var, CSP guard'ını düşürür ve
 * canlıda stiller uygulanmaz (site başlığı style-src 'self'). Yeniden
 * kullanılacaksa önce stilleri sınıfa taşıyın (bkz. landing#57).
 */

const fs = require('fs');
const path = require('path');

const ROOT = path.dirname(__dirname);
const REPORTS_DIR = path.join(ROOT, 'reports');

// Source name mappings
const sourceTitleMap = {
  'github': 'GitHub Trending',
  'hackernews': 'Hacker News',
  'huggingface': 'HuggingFace Daily Models',
  'hfpapers': 'HuggingFace Daily Papers',
  'lobsters': 'Lobsters Tech Discussions'
};

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

// Dynamically scan all available JSON report files
const targetDates = fs.readdirSync(REPORTS_DIR)
  .filter(f => /^trescout-rapor-\d{4}-\d{2}-\d{2}\.json$/.test(f))
  .map(f => f.replace('trescout-rapor-', '').replace('.json', ''));

targetDates.forEach(dateStr => {
  const jsonPath = path.join(REPORTS_DIR, `trescout-rapor-${dateStr}.json`);
  if (!fs.existsSync(jsonPath)) return;

  const data = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
  const enDateFormatted = formatEnDate(dateStr);

  let totalItems = 0;
  const sectionsHtml = data.sections.map(sec => {
    const sName = sourceTitleMap[sec.sourceName] || sec.sourceName;
    const itemsHtml = sec.items.map(item => {
      totalItems++;
      const metaClean = (item.meta || '').replace(/bugün/g, 'today');
      return `
      <div style="margin-bottom: 20px; padding: 18px; background: var(--bg-elevated); border: 1px solid rgba(95, 168, 211, .15); border-radius: 12px;">
        <h3 style="margin: 0 0 6px; font-size: 17px; font-weight: 700;"><a href="${item.url}" target="_blank" rel="noopener" style="color: #fff; text-decoration: none;">${item.title} ↗</a></h3>
        <p style="margin: 0 0 8px; font-size: 15px; color: var(--ink); line-height: 1.55;">${item.summary}</p>
        <span style="font-size: 12.5px; color: var(--brand-light); opacity: .85;">${metaClean}</span>
      </div>`;
    }).join('\n');

    return `
    <section class="disc-sec" style="margin-top: 36px;">
      <h2 style="font-size: 22px; margin-bottom: 16px; border-bottom: 1px solid rgba(95, 168, 211, .2); padding-bottom: 8px; color: var(--accent);">${sName}</h2>
      ${itemsHtml}
    </section>`;
  }).join('\n');

  const enReportDir = path.join(ROOT, 'en', 'reports', dateStr);
  fs.mkdirSync(enReportDir, { recursive: true });

  const enReportHtml = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${enDateFormatted} · TreScout Full Daily Technology Intelligence</title>
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<meta name="description" content="TreScout Daily Technology Intelligence Report for ${enDateFormatted}. Featuring ${totalItems} top highlights across GitHub, Hacker News, and HuggingFace.">
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
<link rel="stylesheet" href="/assets/discover.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>
  <nav><div class="container nav-inner"><a class="logo-link" href="/en/" aria-label="TreScout Home"><svg width="32" height="32" viewBox="0 0 100 100" aria-hidden="true"><rect x="0" y="0" width="100" height="100" rx="22" fill="#1B4965"/><path d="M 20 56 A 30 30 0 0 1 80 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.3" stroke-linecap="round"/><path d="M 30 56 A 20 20 0 0 1 70 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.5" stroke-linecap="round"/><path d="M 40 56 A 10 10 0 0 1 60 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.75" stroke-linecap="round"/><rect x="20" y="56" width="60" height="11" rx="2" fill="#F4D35E"/><rect x="44.5" y="56" width="11" height="28" rx="2" fill="#F4D35E"/></svg><span>TreScout</span></a><div class="nav-actions"><a href="/en/discover/" class="btn btn-ghost">Discover</a><a href="/en/dictionary/" class="btn btn-ghost">Dictionary</a><a href="/en/reports/" class="btn btn-ghost">Reports Archive</a><a href="/en/compare/rss-vs-ai/" class="btn btn-ghost">Compare</a><a href="/reports/${dateStr}/" class="btn btn-ghost" aria-label="Switch to Turkish">TR</a></div></div></nav>

  <main id="main">
    <article class="report-main" style="max-width: 820px; margin: 32px auto; padding: 0 20px;">
      <a class="rep-back" href="/en/reports/">← All Reports</a>
      <div class="rep-eyebrow">Full Daily Technology Intelligence</div>
      <h1 class="rep-title" style="font-size: clamp(32px, 5vw, 48px); margin: 8px 0 16px;">${enDateFormatted}</h1>
      <div class="rep-chips"><span class="chip chip-total">${totalItems} Top Highlights</span></div>
      
      <div style="margin: 24px 0; padding: 18px; background: rgba(95, 168, 211, .08); border-left: 4px solid var(--accent); border-radius: 0 12px 12px 0;">
        <p style="margin: 0; font-size: 16.5px; line-height: 1.6; color: var(--ink);">
          Daily technology intelligence compilation for ${enDateFormatted}. Covering featured developer tools, open-source repositories, and AI research papers across GitHub, Hacker News, HuggingFace, and Lobsters.
        </p>
      </div>

      ${sectionsHtml}

      <aside class="signup-cta" style="margin-top: 44px;">
        <p><strong>Get daily technology reports in your inbox.</strong> TreScout scans, summarizes, and delivers. You just read.</p>
        <form class="cta-form disc-cta-form js-subscribe" data-source="report-detail-en" novalidate>
          <div class="form-row">
            <input class="input" type="email" name="email" placeholder="Enter your email" autocomplete="email" required>
            <button class="btn btn-primary" type="submit">Join Early Access</button>
          </div>
          <label class="form-consent">
            <input type="checkbox" name="consent" required>
            <span>I agree to receive daily tech updates from TreScout. No spam ever.</span>
          </label>
          <input type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true" class="hp-field">
        </form>
      </aside>
    </article>
  </main>

  ${richEnFooter}
</body>
</html>`;

  fs.writeFileSync(path.join(enReportDir, 'index.html'), enReportHtml, 'utf8');
  console.log(`Generated full English daily web report for ${dateStr} with ${totalItems} items!`);
});

console.log('Daily reports English translation build complete!');
