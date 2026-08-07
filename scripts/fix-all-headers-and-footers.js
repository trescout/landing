const fs = require('fs');
const path = require('path');

function getFiles(dir, fileList = []) {
  const files = fs.readdirSync(dir);
  files.forEach(file => {
    const filePath = path.join(dir, file);
    if (fs.statSync(filePath).isDirectory()) {
      if (file !== 'node_modules' && file !== '.git') {
        getFiles(filePath, fileList);
      }
    } else if (file.endsWith('.html')) {
      fileList.push(filePath);
    }
  });
  return fileList;
}

const allHtmls = getFiles('.');
console.log(`Auditing and fixing clean headers (no Early Access button) & footers across ${allHtmls.length} HTML files...`);

const richTrFooter = `<footer>
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand-block">
        <div class="footer-logo">
          <svg width="32" height="32" viewBox="0 0 100 100" aria-hidden="true"><rect x="0" y="0" width="100" height="100" rx="22" fill="#1B4965"/><path d="M 20 56 A 30 30 0 0 1 80 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.3" stroke-linecap="round"/><path d="M 30 56 A 20 20 0 0 1 70 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.5" stroke-linecap="round"/><path d="M 40 56 A 10 10 0 0 1 60 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.75" stroke-linecap="round"/><rect x="20" y="56" width="60" height="11" rx="2" fill="#F4D35E"/><rect x="44.5" y="56" width="11" height="28" rx="2" fill="#F4D35E"/></svg>
          <span>TreScout</span>
        </div>
        <p class="footer-tagline">TreScout tarar, özetler, gönderir. Siz sadece okursunuz.</p>
      </div>
      <div class="footer-col">
        <div class="footer-col-title">Ürün</div>
        <ul>
          <li><a href="/#how-it-works">Nasıl Çalışır</a></li>
          <li><a href="/discover/">Keşif</a></li>
          <li><a href="/dictionary/">Sözlük</a></li>
          <li><a href="/reports/">Raporlar</a></li>
          <li><a href="/compare/rss-vs-ai/">Karşılaştır</a></li>
          <li><a href="/#top">Erken Erişim</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <div class="footer-col-title">İletişim</div>
        <ul>
          <li><a href="mailto:hello@trescout.com">hello@trescout.com</a></li>
          <li><a href="/privacy.html" target="_blank" rel="noopener">Aydınlatma Metni</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <div class="footer-col-title">Sosyal medya</div>
        <ul>
          <li><a href="https://x.com/GetTreScout" target="_blank" rel="noopener noreferrer">X</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 TreScout · Tüm hakları saklıdır.</span>
    </div>
  </div>
</footer>`;

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

let fixedHeaderCount = 0;
let fixedFooterCount = 0;

/* Üreticiden çıkan diller bu normalize edicinin KAPSAMI DIŞINDA.
   Sebep: bu betik TR/EN ikilisine göre yazılmış · tanımadığı bir dil klasörünü
   "Türkçe" sayıp menüyü Türkçeyle ezerdi. Fransızca sayfaların nav/footer'ı
   scripts/diller.py'den geliyor ve her üretimde yeniden yazılıyor, dolayısıyla
   sapma birikemiyor. Yeni dil eklerken bu listeye de ekleyin. */
const URETILEN_DILLER = ['fr/'];

allHtmls.forEach(relPath => {
  const normPath = relPath.replace(/\\/g, '/');
  if (URETILEN_DILLER.some(o => normPath.startsWith(o))) return;
  const isEn = normPath.startsWith('en/');
  let content = fs.readFileSync(relPath, 'utf8');

  // Compute opposite link for language switcher
  let oppLink = '/';
  if (isEn) {
    if (normPath === 'en/index.html') oppLink = '/';
    else if (normPath === 'en/dictionary/index.html') oppLink = '/dictionary/';
    else if (normPath === 'en/discover/index.html') oppLink = '/discover/';
    else if (normPath === 'en/reports/index.html') oppLink = '/reports/';
    else if (normPath === 'en/compare/rss-vs-ai/index.html') oppLink = '/compare/rss-vs-ai/';
    else if (normPath.startsWith('en/dictionary/')) {
      const slug = normPath.replace('en/dictionary/', '').replace('/index.html', '');
      oppLink = `/dictionary/${slug}/`;
    } else if (normPath.startsWith('en/discover/')) {
      const slug = normPath.replace('en/discover/', '').replace('/index.html', '');
      oppLink = `/discover/${slug}/`;
    } else if (normPath.startsWith('en/reports/')) {
      const dateMatch = normPath.match(/\d{4}-\d{2}-\d{2}/);
      if (dateMatch) oppLink = `/reports/${dateMatch[0]}/`;
      else oppLink = '/reports/';
    } else oppLink = '/';
  } else {
    if (normPath === 'index.html') oppLink = '/en/';
    else if (normPath === 'dictionary/index.html') oppLink = '/en/dictionary/';
    else if (normPath === 'discover/index.html') oppLink = '/en/discover/';
    else if (normPath === 'reports/index.html') oppLink = '/en/reports/';
    else if (normPath === 'compare/rss-vs-ai/index.html') oppLink = '/en/compare/rss-vs-ai/';
    else if (normPath.startsWith('dictionary/')) {
      const slug = normPath.replace('dictionary/', '').replace('/index.html', '');
      oppLink = `/en/dictionary/${slug}/`;
    } else if (normPath.startsWith('discover/')) {
      const slug = normPath.replace('discover/', '').replace('/index.html', '');
      oppLink = `/en/discover/${slug}/`;
    } else if (normPath.startsWith('reports/')) {
      const dateMatch = normPath.match(/\d{4}-\d{2}-\d{2}/);
      if (dateMatch) oppLink = `/en/reports/${dateMatch[0]}/`;
      else oppLink = '/en/reports/';
    } else oppLink = '/en/';
  }

  const expectedNav = isEn ?
`<nav><div class="container nav-inner"><a class="logo-link" href="/en/" aria-label="TreScout Home"><svg width="32" height="32" viewBox="0 0 100 100" aria-hidden="true"><rect x="0" y="0" width="100" height="100" rx="22" fill="#1B4965"/><path d="M 20 56 A 30 30 0 0 1 80 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.3" stroke-linecap="round"/><path d="M 30 56 A 20 20 0 0 1 70 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.5" stroke-linecap="round"/><path d="M 40 56 A 10 10 0 0 1 60 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.75" stroke-linecap="round"/><rect x="20" y="56" width="60" height="11" rx="2" fill="#F4D35E"/><rect x="44.5" y="56" width="11" height="28" rx="2" fill="#F4D35E"/></svg><span>TreScout</span></a><div class="nav-actions"><a href="/en/discover/" class="btn btn-ghost">Discover</a><a href="/en/dictionary/" class="btn btn-ghost">Dictionary</a><a href="/en/reports/" class="btn btn-ghost">Reports Archive</a><a href="/en/compare/rss-vs-ai/" class="btn btn-ghost">Compare</a><a href="${oppLink}" class="btn btn-ghost" aria-label="Switch to Turkish">TR</a></div></div></nav>` :
`<nav><div class="container nav-inner"><a class="logo-link" href="/" aria-label="TreScout anasayfa"><svg width="32" height="32" viewBox="0 0 100 100" aria-hidden="true"><rect x="0" y="0" width="100" height="100" rx="22" fill="#1B4965"/><path d="M 20 56 A 30 30 0 0 1 80 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.3" stroke-linecap="round"/><path d="M 30 56 A 20 20 0 0 1 70 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.5" stroke-linecap="round"/><path d="M 40 56 A 10 10 0 0 1 60 56" fill="none" stroke="#5FA8D3" stroke-width="2.5" opacity="0.75" stroke-linecap="round"/><rect x="20" y="56" width="60" height="11" rx="2" fill="#F4D35E"/><rect x="44.5" y="56" width="11" height="28" rx="2" fill="#F4D35E"/></svg><span>TreScout</span></a><div class="nav-actions"><a href="/discover/" class="btn btn-ghost">Keşif</a><a href="/dictionary/" class="btn btn-ghost">Sözlük</a><a href="/reports/" class="btn btn-ghost">Raporlar</a><a href="/compare/rss-vs-ai/" class="btn btn-ghost">Karşılaştır</a><a href="${oppLink}" class="btn btn-ghost" aria-label="İngilizceye geç">EN</a></div></div></nav>`;

  const expectedFooter = isEn ? richEnFooter : richTrFooter;

  let newContent = content;

  // Replace Nav
  if (newContent.includes('<nav')) {
    newContent = newContent.replace(/<nav[\s\S]*?<\/nav>/, expectedNav);
    if (newContent !== content) fixedHeaderCount++;
  }

  // Replace Footer if needed
  if (newContent.includes('<footer')) {
    const prev = newContent;
    newContent = newContent.replace(/<footer[\s\S]*?<\/footer>/, expectedFooter);
    if (newContent !== prev) fixedFooterCount++;
  }

  if (newContent !== content) {
    fs.writeFileSync(relPath, newContent, 'utf8');
  }
});

console.log(`Completed! Fixed ${fixedHeaderCount} headers and ${fixedFooterCount} footers across all ${allHtmls.length} HTML files.`);
