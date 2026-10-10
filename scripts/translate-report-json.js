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

// Kayıt formu bilgilendirme + onay bloğu · tek kaynak scripts/riza-metni.json
// (riza_formu.py ikizi, #210 · KVKK 2026/347: aydınlatma onaylatılmaz).
const RIZA_METNI = JSON.parse(fs.readFileSync(path.join(__dirname, 'riza-metni.json'), 'utf8'));
const RIZA_GIZLILIK = { tr: '/privacy.html', en: '/en/privacy.html', fr: '/fr/privacy.html', pt: '/pt/privacy.html', es: '/es/privacy.html', de: '/de/privacy.html' };
function rizaBlok(dil) {
  const k = RIZA_METNI[String(dil || 'tr').split('-')[0]] ? String(dil || 'tr').split('-')[0] : 'tr';
  const m = RIZA_METNI[k];
  const baglanti = `<a href="${RIZA_GIZLILIK[k]}" target="_blank" rel="noopener">${m.baglanti_metni}</a>`;
  return `<p class="form-notice">${m.bilgi.replace('{baglanti}', baglanti)}</p>`
    + `<label class="form-consent"><input type="checkbox" name="consent" required><span>${m.onay}</span></label>`;
}

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
          <svg width="30" height="30" viewBox="14 15 72 75" aria-hidden="true"><g fill="currentColor"><path d="M 19.16 21.86 A 84.0 84.0 0 0 1 80.84 21.86 A 5.0 5.0 0 0 1 77.16 31.17 A 74.0 74.0 0 0 0 22.84 31.17 A 5.0 5.0 0 0 1 19.16 21.86 Z"/><path d="M 53.00 27.00 C 52.80 28.43 52.79 30.00 52.41 31.30 C 52.03 32.61 51.37 33.78 50.71 34.80 C 50.05 35.83 49.21 36.68 48.45 37.48 C 47.69 38.27 46.86 38.93 46.14 39.58 C 45.42 40.22 44.71 40.80 44.15 41.36 C 43.59 41.92 43.12 42.44 42.79 42.94 C 42.45 43.44 42.25 43.84 42.12 44.35 C 41.99 44.86 41.95 45.61 41.99 46.00 C 42.02 46.39 42.03 46.40 42.33 46.67 C 42.63 46.93 43.01 47.24 43.79 47.58 C 44.56 47.92 45.73 48.34 46.98 48.72 C 48.23 49.10 49.77 49.44 51.28 49.86 C 52.80 50.28 54.46 50.64 56.07 51.24 C 57.67 51.84 59.39 52.39 60.92 53.44 C 62.45 54.49 64.21 55.78 65.25 57.54 C 66.30 59.30 66.93 62.19 67.20 64.00 C 67.46 65.81 67.13 67.00 66.85 68.40 C 66.57 69.80 66.10 71.16 65.53 72.41 C 64.96 73.66 64.22 74.82 63.44 75.88 C 62.66 76.93 61.76 77.88 60.84 78.77 C 59.93 79.65 58.95 80.44 57.97 81.19 C 56.98 81.94 55.96 82.61 54.95 83.27 C 53.94 83.92 52.90 84.52 51.90 85.11 C 50.89 85.70 49.90 86.25 48.91 86.81 A 6.50 6.50 0 0 1 43.09 75.19 C 44.09 74.75 45.12 74.30 46.07 73.87 C 47.02 73.43 47.95 73.01 48.80 72.58 C 49.65 72.15 50.46 71.72 51.19 71.28 C 51.92 70.85 52.58 70.41 53.16 69.98 C 53.73 69.55 54.23 69.12 54.66 68.68 C 55.08 68.25 55.42 67.83 55.72 67.37 C 56.02 66.91 56.25 66.47 56.43 65.90 C 56.61 65.34 56.76 64.51 56.80 64.00 C 56.85 63.49 56.89 63.24 56.69 62.85 C 56.48 62.45 56.24 62.08 55.58 61.62 C 54.92 61.16 53.89 60.59 52.75 60.10 C 51.60 59.60 50.14 59.14 48.72 58.64 C 47.29 58.15 45.71 57.72 44.20 57.13 C 42.70 56.54 41.12 56.02 39.71 55.11 C 38.30 54.19 36.68 53.16 35.73 51.64 C 34.78 50.12 34.15 47.66 34.01 46.00 C 33.87 44.34 34.42 42.94 34.91 41.67 C 35.40 40.39 36.21 39.29 36.96 38.34 C 37.72 37.39 38.63 36.67 39.44 35.98 C 40.26 35.28 41.11 34.74 41.86 34.17 C 42.61 33.61 43.34 33.11 43.96 32.59 C 44.57 32.07 45.10 31.58 45.54 31.04 C 45.97 30.50 46.31 30.01 46.56 29.33 C 46.80 28.66 46.85 27.78 47.00 27.00 A 3.00 3.00 0 0 1 53.00 27.00 Z"/></g></svg>
        </div>
        <p class="footer-tagline">TreScout scans and summarizes, so all you have to do is read.</p>
      </div>
      <div class="footer-col">
        <div class="footer-col-title">Product</div>
        <ul>
          <li><a href="/en/how-it-works/">How It Works</a></li>
          <li><a href="/en/discover/">Discover</a></li>
          <li><a href="/en/dictionary/">Dictionary</a></li>
          <li><a href="/en/reports/">Reports Archive</a></li>
          <li><a href="/en/compare/rss-vs-ai/">Compare</a></li>
          <li><a href="/en/#top">Stay informed</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <div class="footer-col-title">Contact</div>
        <ul>
          <li><a href="mailto:hello@trescout.com">Contact us</a></li><li><a href="mailto:hello@trescout.com?subject=TreScout%20-%20Join%20the%20team">Join the team</a></li>
        </ul>
      </div>
      <div class="footer-col">
          <div class="footer-col-title">Legal</div>
          <ul>
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
<link rel="icon" type="image/x-icon" sizes="16x16 32x32 48x48" href="/favicon.ico"> <link rel="icon" type="image/svg+xml" href="/favicon.svg">
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
  <nav><div class="container nav-inner"><a class="logo-link" href="/en/" aria-label="TreScout Home"><svg width="30" height="30" viewBox="14 15 72 75" aria-hidden="true"><g fill="currentColor"><path d="M 19.16 21.86 A 84.0 84.0 0 0 1 80.84 21.86 A 5.0 5.0 0 0 1 77.16 31.17 A 74.0 74.0 0 0 0 22.84 31.17 A 5.0 5.0 0 0 1 19.16 21.86 Z"/><path d="M 53.00 27.00 C 52.80 28.43 52.79 30.00 52.41 31.30 C 52.03 32.61 51.37 33.78 50.71 34.80 C 50.05 35.83 49.21 36.68 48.45 37.48 C 47.69 38.27 46.86 38.93 46.14 39.58 C 45.42 40.22 44.71 40.80 44.15 41.36 C 43.59 41.92 43.12 42.44 42.79 42.94 C 42.45 43.44 42.25 43.84 42.12 44.35 C 41.99 44.86 41.95 45.61 41.99 46.00 C 42.02 46.39 42.03 46.40 42.33 46.67 C 42.63 46.93 43.01 47.24 43.79 47.58 C 44.56 47.92 45.73 48.34 46.98 48.72 C 48.23 49.10 49.77 49.44 51.28 49.86 C 52.80 50.28 54.46 50.64 56.07 51.24 C 57.67 51.84 59.39 52.39 60.92 53.44 C 62.45 54.49 64.21 55.78 65.25 57.54 C 66.30 59.30 66.93 62.19 67.20 64.00 C 67.46 65.81 67.13 67.00 66.85 68.40 C 66.57 69.80 66.10 71.16 65.53 72.41 C 64.96 73.66 64.22 74.82 63.44 75.88 C 62.66 76.93 61.76 77.88 60.84 78.77 C 59.93 79.65 58.95 80.44 57.97 81.19 C 56.98 81.94 55.96 82.61 54.95 83.27 C 53.94 83.92 52.90 84.52 51.90 85.11 C 50.89 85.70 49.90 86.25 48.91 86.81 A 6.50 6.50 0 0 1 43.09 75.19 C 44.09 74.75 45.12 74.30 46.07 73.87 C 47.02 73.43 47.95 73.01 48.80 72.58 C 49.65 72.15 50.46 71.72 51.19 71.28 C 51.92 70.85 52.58 70.41 53.16 69.98 C 53.73 69.55 54.23 69.12 54.66 68.68 C 55.08 68.25 55.42 67.83 55.72 67.37 C 56.02 66.91 56.25 66.47 56.43 65.90 C 56.61 65.34 56.76 64.51 56.80 64.00 C 56.85 63.49 56.89 63.24 56.69 62.85 C 56.48 62.45 56.24 62.08 55.58 61.62 C 54.92 61.16 53.89 60.59 52.75 60.10 C 51.60 59.60 50.14 59.14 48.72 58.64 C 47.29 58.15 45.71 57.72 44.20 57.13 C 42.70 56.54 41.12 56.02 39.71 55.11 C 38.30 54.19 36.68 53.16 35.73 51.64 C 34.78 50.12 34.15 47.66 34.01 46.00 C 33.87 44.34 34.42 42.94 34.91 41.67 C 35.40 40.39 36.21 39.29 36.96 38.34 C 37.72 37.39 38.63 36.67 39.44 35.98 C 40.26 35.28 41.11 34.74 41.86 34.17 C 42.61 33.61 43.34 33.11 43.96 32.59 C 44.57 32.07 45.10 31.58 45.54 31.04 C 45.97 30.50 46.31 30.01 46.56 29.33 C 46.80 28.66 46.85 27.78 47.00 27.00 A 3.00 3.00 0 0 1 53.00 27.00 Z"/></g></svg></a><div class="nav-actions"><a href="/en/discover/" class="btn btn-ghost">Discover</a><a href="/en/dictionary/" class="btn btn-ghost">Dictionary</a><a href="/en/reports/" class="btn btn-ghost">Reports Archive</a><a href="/reports/${dateStr}/" class="btn btn-ghost" aria-label="Switch to Turkish">TR</a></div></div></nav>

  <main id="main">
    <article class="report-main" style="max-width: 820px; margin: 32px auto; padding: 0 20px;">
      <a class="rep-back" href="/en/reports/">← All Reports</a>
      <div class="rep-eyebrow">Full Daily Technology Intelligence</div>
      <h1 class="rep-title" style="font-size: clamp(32px, 5vw, 48px); margin: 8px 0 16px;">${enDateFormatted}</h1>
      <div class="rep-chips"><span class="chip chip-total">${totalItems} Top Highlights</span></div>
      
      <div style="margin: 24px 0; padding: 18px; background: rgba(95, 168, 211, .08); border-left: 4px solid var(--accent); border-radius: 0 12px 12px 0;">
        <p style="margin: 0; font-size: 16.5px; line-height: 1.6; color: var(--ink);">
          Daily technology intelligence compilation for ${enDateFormatted}. Covering featured developer tools, open-source repositories, and AI research papers across GitHub, Hacker News, and HuggingFace.
        </p>
      </div>

      ${sectionsHtml}

      <aside class="signup-cta" style="margin-top: 44px;">
        <p><strong>Early access list.</strong> You can join the list for early access invitations and launch announcements.</p>
        <form class="cta-form disc-cta-form js-subscribe" data-source="report-detail-en" action="/api/subscribe" method="post">
          <div class="form-row">
            <input class="input" type="email" name="email" placeholder="Enter your email" autocomplete="email" required>
            <button class="btn btn-primary" type="submit">Join Early Access</button>
          </div>
          ${rizaBlok('en')}
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
