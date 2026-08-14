/**
 * Rapor arşivi sayfaları · Türkçe rapordan hedef dilde sayfa üretir.
 *
 *   node scripts/build-reports-en.js            → /en/reports/ + /en/reports/fresh/
 *   node scripts/build-reports-en.js --lang=fr  → /fr/reports/ + /fr/reports/fresh/
 *
 * Dosya adı tarihsel ("en") · tek çağıranı trescout-app/scripts/publish-report.ts
 * olduğu için yeniden adlandırılmadı, iki depoda aynı anda değişirse günlük yayın
 * bir gün düşer. Metinler scripts/diller.py'den geliyor.
 *
 * KURAL · bir tarih için o dilin çevrilmiş arşiv JSON'u yoksa sayfa ÜRETİLMEZ.
 * Yoksa sayfa Türkçe içerikle çıkar. Fransızca arşiv bu yüzden 2026-07-25'te
 * başlıyor · öncesi çevrilmedi, günlük hat ileriye doğru dolduruyor.
 *
 * Aydınlatma bağlantısı sayfanın dilindeki metne gitmeli · burada /privacy.html
 * (Türkçe) yazıyordu ve betik her koştuğunda 128 İngilizce sayfada düzeltmeyi
 * geri alıyordu (2026-08-07). check-consent-consistency.py artık bunu denetliyor.
 */
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const ROOT = path.dirname(__dirname);
const REPORTS_DIR = path.join(ROOT, 'reports');
const LANG = (process.argv.find((a) => a.startsWith('--lang=')) || '--lang=en').split('=')[1];

const D = JSON.parse(
  execFileSync('python3', [path.join(__dirname, 'diller.py'), '--json', LANG], { encoding: 'utf8' })
);
const PRE = D.onek;                       // '/en' · '/fr'
const OUT_ROOT = path.join(ROOT, LANG, 'reports');

/**
 * İki rapor varyantı · normal ve tekrarsız ("fresh only").
 * Türkçe tarafta /reports/ ve /reports/tekrarsiz/ olarak yayınlanıyor.
 */
const VARIANTS = [
  {
    kind: 'normal',
    srcDir: REPORTS_DIR,
    outDir: OUT_ROOT,
    urlBase: `${PRE}/reports`,
    trUrlBase: '/reports',
    ciktiPdf: (d) => `trescout-report-${d}-${LANG}.pdf`,
    trPdf: (d) => `trescout-rapor-${d}.pdf`,
  },
  {
    kind: 'fresh',
    srcDir: path.join(REPORTS_DIR, 'tekrarsiz'),
    outDir: path.join(OUT_ROOT, 'fresh'),
    urlBase: `${PRE}/reports/fresh`,
    trUrlBase: '/reports/tekrarsiz',
    ciktiPdf: (d) => `trescout-report-fresh-${d}-${LANG}.pdf`,
    trPdf: (d) => `trescout-rapor-tekrarsiz-${d}.pdf`,
  },
];

/** Arşiv sekmeleri · Türkçe taraftaki arch-tabs ile aynı desen */
function archiveTabs(active) {
  const tab = (href, label, on) =>
    `<a class="btn ${on ? 'btn-primary' : 'btn-ghost'}" href="${href}"${on ? ' aria-current="page"' : ''}>${label}</a>`;
  return `<div class="arch-tabs">${tab(`${PRE}/reports/`, D.rapor_varyant.normal.geri, active === 'normal')}${tab(`${PRE}/reports/fresh/`, D.rapor_varyant.fresh.geri, active === 'fresh')}</div>`;
}

function tarihYaz(dateStr) {
  const [y, m, d] = dateStr.split('-').map(Number);
  const dt = new Date(Date.UTC(y, m - 1, d));
  return D.rapor_tarih
    .replace('{ay}', D.aylar[m - 1])
    .replace('{gun}', String(d))
    .replace('{yil}', String(y))
    .replace('{gunad}', D.rapor_gunler[dt.getUTCDay()]);
}

/**
 * Nav + footer · o dilin ÜRETİLMİŞ bir sayfasından. Kanonik kaynak İngilizcede
 * fix-all-headers-and-footers.js, diğer dillerde diller.py · her iki hâlde de
 * bu betiğin kendi kabuğunu yazması guard'ları kırardı.
 */

/** Nav'daki dil düğmelerini sayfaya özel yap · hedefi olmayan etiket korunur. */
const dilYaz = (nav, hedefler) => nav.replace(
  /<a href="[^"]*" class="btn btn-ghost" aria-label="[^"]*">(TR|EN|FR|PT)<\/a>/g,
  (m, et) => hedefler[et]
    ? `<a href="${hedefler[et]}" class="btn btn-ghost" aria-label="${et}">${et}</a>`
    : m
);

function kabuk(hedefler) {
  const aday = [path.join(ROOT, LANG, 'discover'), path.join(ROOT, LANG, 'dictionary')];
  for (const dizin of aday) {
    if (!fs.existsSync(dizin)) continue;
    const ornek = fs.readdirSync(dizin)
      .map((s) => path.join(dizin, s, 'index.html'))
      .find((f) => fs.existsSync(f));
    if (!ornek) continue;
    const html = fs.readFileSync(ornek, 'utf8');
    const al = (etiket) => {
      const m = html.match(new RegExp(`<${etiket}[\\s>][\\s\\S]*?</${etiket}>`));
      if (!m) { console.error(`✗ ${ornek} içinde <${etiket}> yok.`); process.exit(1); }
      return m[0];
    };
    return { nav: dilYaz(al('nav'), hedefler), footer: al('footer') };
  }
  console.error(`✗ ${LANG}/ altında üretilmiş sayfa yok · önce keşif/sözlük sayfalarını basın.`);
  process.exit(1);
}

function buildVariant(V) {
  const dirs = fs.existsSync(V.srcDir)
    ? fs.readdirSync(V.srcDir).filter(
        (d) => /^\d{4}-\d{2}-\d{2}$/.test(d) && fs.statSync(path.join(V.srcDir, d)).isDirectory())
    : [];

  let count = 0;
  let atlanan = 0;
  const reportCards = [];

  dirs.sort().reverse().forEach((dateStr) => {
    const trHtmlPath = path.join(V.srcDir, dateStr, 'index.html');
    if (!fs.existsSync(trHtmlPath)) return;

    // Çevrilmiş arşiv yoksa sayfa üretme · Türkçe içerikli sayfa çıkmasın
    const jsonPath = path.join(ROOT, 'reports', `${V.ciktiPdf(dateStr).replace(/\.pdf$/, '')}.json`);
    if (!fs.existsSync(jsonPath)) { atlanan++; return; }

    let editorial = '';
    try {
      editorial = JSON.parse(fs.readFileSync(jsonPath, 'utf8')).editorial || '';
    } catch { /* bozuk JSON · aşağıda eleniyor */ }
    if (!editorial) { atlanan++; return; }

    const trHtml = fs.readFileSync(trHtmlPath, 'utf8');
    const chipsMatch = trHtml.match(/<div class="rep-chips">(.*?)<\/div>/s);
    const tarih = tarihYaz(dateStr);

    const pdfPath = path.join(ROOT, 'reports', V.ciktiPdf(dateStr));
    const pdfVar = fs.existsSync(pdfPath);
    const pdfUrl = pdfVar ? `/reports/${V.ciktiPdf(dateStr)}` : `/reports/${V.trPdf(dateStr)}`;

    let chips = chipsMatch ? chipsMatch[1] : '';
    for (const [tr, hedef] of Object.entries(D.rapor_cipler)) {
      chips = chips.split(tr).join(hedef);
    }

    const arsiv = dateStr <= D.rapor_arsiv_esigi;
    const badgeTag = arsiv ? `<span class="chip chip-en">${D.rapor_rozet}</span>` : '';
    const enYol = V.kind === 'fresh' ? 'reports/fresh' : 'reports';
    const { nav, footer } = kabuk({
      TR: `${V.trUrlBase}/${dateStr}/`,
      EN: `/en/${enYol}/${dateStr}/`,
      FR: `/fr/${enYol}/${dateStr}/`,
      PT: `/pt/${enYol}/${dateStr}/`,
    });

    const html = `<!DOCTYPE html>
<html lang="${D.html_lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${D.rapor_sayfa_baslik.replace('{tarih}', tarih)}</title>
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<meta name="description" content="${D.rapor_sayfa_aciklama.replace('{tarih}', tarih)}">
<link rel="canonical" href="https://trescout.com${V.urlBase}/${dateStr}/">
<link rel="alternate" hreflang="tr" href="https://trescout.com${V.trUrlBase}/${dateStr}/">
<link rel="alternate" hreflang="en" href="https://trescout.com/en${V.urlBase.slice(PRE.length)}/${dateStr}/">
<link rel="alternate" hreflang="x-default" href="https://trescout.com/en${V.urlBase.slice(PRE.length)}/${dateStr}/">
<meta property="og:title" content="${D.rapor_sayfa_baslik.replace('{tarih}', tarih)}">
<meta property="og:description" content="${D.rapor_sayfa_og.replace('{tarih}', tarih)}">
<meta property="og:url" content="https://trescout.com${V.urlBase}/${dateStr}/">
<meta property="og:type" content="article">
<meta property="og:locale" content="${D.og_locale}">
<link rel="stylesheet" href="/assets/site.css">
<link rel="stylesheet" href="/assets/report-cover.css">
</head>
<body>
  <a class="skip-link" href="#main">${D.atla}</a>
  ${nav}

  <main id="main">
    <article class="report-main">
      <a class="rep-back" href="${V.urlBase}/">← ${D.rapor_varyant[V.kind].geri}</a>
      <div class="rep-eyebrow">${D.rapor_eyebrow}${arsiv ? ' ' + D.rapor_eyebrow_arsiv : ''}</div>
      <h1 class="rep-title">${tarih}</h1>
      <div class="rep-chips">${badgeTag}${chips}</div>
      <p class="rep-editorial">${editorial}</p>
      <div class="rep-actions">
        <a class="act act-read" href="${pdfUrl}" target="_blank" rel="noopener">${D.rapor_ac.replace('{dil}', D.rapor_dil_adi)}</a>
        <a class="act act-dl" href="${pdfUrl}" download>${D.rapor_indir}</a>
      </div>
      <p class="rep-note">${D.rapor_not}</p>
      <aside class="signup-cta">
        <p>${D.rapor_cta}</p>
        <a class="btn btn-primary" href="${PRE}/#top">${D.rapor_cta_dugme}</a>
      </aside>
    </article>
  </main>

  ${footer}
</body>
</html>`;

    const dir = path.join(V.outDir, dateStr);
    fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(path.join(dir, 'index.html'), html, 'utf8');
    count++;

    reportCards.push(`
        <article class="card">
          <a class="card-main" href="${V.urlBase}/${dateStr}/">
            <time class="card-date" datetime="${dateStr}">${tarih}</time>
            <p class="card-teaser">${editorial.substring(0, 160)}...</p>
            <div class="card-chips">${badgeTag}${chips}</div>
          </a>
          <div class="card-actions">
            <a class="act act-read" href="${V.urlBase}/${dateStr}/">${D.rapor_oku}</a>
            <a class="act act-pdf" href="${pdfUrl}" download>${D.rapor_indir}</a>
          </div>
        </article>`);
  });

  const T = D.rapor_varyant[V.kind];
  const dizinYol = V.kind === 'fresh' ? 'reports/fresh' : 'reports';
  const dizinKabuk = kabuk({
    TR: `${V.trUrlBase}/`, EN: `/en/${dizinYol}/`,
    FR: `/fr/${dizinYol}/`, PT: `/pt/${dizinYol}/`,
  });
  const footer = dizinKabuk.footer;
  // Dizin sayfasında menüdeki rapor bağlantısı "bulunduğunuz sayfa" olmalı ·
  // kabuk keşif sayfasından kopyalandığı için bu işaret düşüyordu.
  const nav = dizinKabuk.nav.replace(
    new RegExp(`(<a href="${PRE}/reports/" class="btn btn-ghost")>`),
    '$1 aria-current="page">'
  );
  const indexHtml = `<!DOCTYPE html>
<html lang="${D.html_lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${T.dizin_baslik}</title>
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<meta name="description" content="${T.dizin_aciklama}">
<link rel="canonical" href="https://trescout.com${V.urlBase}/">
<link rel="alternate" hreflang="tr" href="https://trescout.com${V.trUrlBase}/">
<link rel="alternate" hreflang="en" href="https://trescout.com/en${V.urlBase.slice(PRE.length)}/">
<link rel="alternate" hreflang="x-default" href="https://trescout.com/en${V.urlBase.slice(PRE.length)}/">
<meta property="og:title" content="${T.dizin_baslik}">
<meta property="og:description" content="${T.dizin_aciklama}">
<meta property="og:url" content="https://trescout.com${V.urlBase}/">
<meta property="og:type" content="website">
<meta property="og:locale" content="${D.og_locale}">
<link rel="stylesheet" href="/assets/site.css">
<link rel="stylesheet" href="/assets/report-archive.css">
</head>
<body>
  <a class="skip-link" href="#main">${D.atla}</a>
  ${nav}

  <main id="main">
    <div class="archive-main">
      <div class="arch-eyebrow">${D.rapor_arsiv}</div>
      <h1 class="arch-title">${T.baslik}</h1>
      ${archiveTabs(V.kind)}
      <p class="arch-intro">${T.intro}</p>

      <div class="arch-banner">
        <div class="arch-banner-title">
          <span>🌐</span> <span>${D.rapor_banner_baslik}</span>
        </div>
        <p class="arch-banner-text">
          ${D.rapor_banner}
        </p>
      </div>

      <div class="arch-list">
        ${reportCards.join('\n')}
      </div>
    </div>
  </main>

  ${footer}
</body>
</html>`;

  fs.mkdirSync(V.outDir, { recursive: true });
  fs.writeFileSync(path.join(V.outDir, 'index.html'), indexHtml, 'utf8');
  console.log(`  ${V.urlBase}/ · ${count} sayfa${atlanan ? ` · ${atlanan} tarih atlandı (çeviri yok)` : ''}`);
}

for (const V of VARIANTS) buildVariant(V);
console.log(`Rapor sayfaları tamam · dil: ${LANG}`);
