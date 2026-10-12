/** Shared index layout. Reuses published homepage copy and consent verbatim. */
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const locales = ['', 'en', 'fr', 'pt', 'es', 'de'];

function layout(html, locale, kind) {
  const home = fs.readFileSync(path.join(ROOT, locale, 'index.html'), 'utf8');
  const signup = home.match(/<section class="ana-erken"[^>]*>([\s\S]*?)<\/section>/);
  if (!signup) throw new Error(`Homepage signup missing: ${locale}`);
  const source = `${kind}${locale ? '-' + locale : ''}`;
  const form = signup[1].replace(/<span id="top"[^>]*><\/span>/, '')
    .replaceAll('email-final-', 'email-catalog-')
    .replace('data-source="final-cta"', `data-source="${source}" data-page-type="${kind}" data-cta-placement="catalog_sidebar"`)
    .replace(' data-privacy-modal', ' target="_blank" rel="noopener"');
  const aside = `<aside class="catalog-sidebar" aria-labelledby="catalog-signup-title">${form.replace('<h2>', '<h2 id="catalog-signup-title">')}</aside>`;
  const main = html.match(/<main id="main">([\s\S]*?)<\/main>/);
  if (!main) throw new Error('Index main missing');
  let body;
  if (main[1].includes('<!-- catalog-content -->')) {
    body = main[1].split('<!-- catalog-content -->')[1].split('<!-- /catalog-content -->')[0];
  } else {
    body = main[1].trim();
    if (!/^<div\b[^>]*>/.test(body) || !body.endsWith('</div>')) throw new Error('Unexpected index wrapper');
    body = body.replace(/^<div\b[^>]*>/, '').replace(/<\/div>$/, '');
    body = body.replace(/[ \t]*<aside class="(?:disc-cta|signup-cta)"[^>]*>[\s\S]*?<\/aside>/g, '');
  }
  html = html.replace(main[0], `<main id="main"><div class="container catalog-shell"><div class="catalog-content"><!-- catalog-content -->${body}<!-- /catalog-content --></div>${aside}</div></main>`);
  if (!html.includes('href="/assets/catalog-layout.css"')) html = html.replace('</head>', '<link rel="stylesheet" href="/assets/catalog-layout.css">\n</head>');
  if (!html.includes('src="/assets/subscribe.js"')) html = html.replace('</body>', '<script src="/assets/subscribe.js" defer></script>\n</body>');
  return html;
}

function updateAll() {
  for (const locale of locales) {
    for (const kind of ['dictionary', 'discover', 'reports', `reports/${locale ? 'fresh' : 'tekrarsiz'}`]) {
      const file = path.join(ROOT, locale, kind, 'index.html');
      if (!fs.existsSync(file)) continue;
      const before = fs.readFileSync(file, 'utf8');
      const after = layout(before, locale, kind.startsWith('reports') ? 'reports' : kind);
      if (after !== before) fs.writeFileSync(file, after);
    }
  }
}
module.exports = {layout, updateAll};
if (require.main === module) updateAll();
