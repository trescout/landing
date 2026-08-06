#!/usr/bin/env python3
"""
TreScout · İngilizce keşif sayfalarını Türkçesinden üretir.
============================================================

Neden gerekti: İngilizce keşif sayfaları `build-en.js` ile üretiliyordu ve o
betik Türkçe sayfalar zenginleşmeden önce yazılmış bir **SEO kabuğu**: yalnız
başlık + tek cümle + "Project Stats". 2026-08-06 denetimi: Türkçe sayfa medyanı
314 kelime, İngilizce 100 kelime. Kurulum komutları (kod · çeviri bile
gerektirmez) İngilizce tarafta hiç yoktu.

Yöntem · İngilizce raporlarda işe yarayanın aynısı: Türkçe sayfanın içerik
bloklarını okur, düzyazıyı ücretsiz çeviri uç noktasından geçirir (Gemini
kotasından harcamaz), kodu OLDUĞU GİBİ kopyalar, aynı CSS sınıflarıyla basar ·
tasarım paritesi böyle kendiliğinden geliyor.

Çeviriler `assets/discover/en-cache.json`'da saklanır: tekrar çalıştırmak
neredeyse bedava, çeviri değişimi diff'te görünür.

Kullanım:
  python3 scripts/discover-en.py            # tümü (önbellekten)
  python3 scripts/discover-en.py --limit=5  # ilk 5 sayfa
  python3 scripts/discover-en.py --slug=k-skill
  python3 scripts/discover-en.py --dry
"""
import os, re, sys, json, html, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TR_DIR = os.path.join(ROOT, "discover")
EN_DIR = os.path.join(ROOT, "en", "discover")
CATALOG = os.path.join(ROOT, "assets", "discover", "catalog.json")
CACHE = os.path.join(ROOT, "assets", "discover", "en-cache.json")
BASE = "https://trescout.com"

DRY = "--dry" in sys.argv
LIMIT = next((int(a.split("=")[1]) for a in sys.argv if a.startswith("--limit=")), None)
ONLY = next((a.split("=")[1] for a in sys.argv if a.startswith("--slug=")), None)

# ── çeviri ────────────────────────────────────────────────────────────────────
_cache = json.load(open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {}
_yeni = 0


def tr2en(s):
    """Ücretsiz uç nokta (translate-i18n.js ile aynı) · önbellekli, hata olursa Türkçesini bırakır."""
    global _yeni
    s = (s or "").strip()
    if not s:
        return ""
    if s in _cache:
        return _cache[s]
    url = ("https://translate.googleapis.com/translate_a/single?client=gtx&sl=tr&tl=en&dt=t&q="
           + urllib.parse.quote(s))
    out, oldu = s, False
    for deneme in range(3):
        try:
            with urllib.request.urlopen(url, timeout=25) as r:
                d = json.loads(r.read().decode())
            out = "".join(p[0] for p in d[0])
            oldu = True
            break
        except Exception:
            time.sleep(1 + deneme * 2)
    # Başarısız çeviriyi ÖNBELLEĞE YAZMA · yoksa Türkçe metin kalıcı olarak
    # İngilizce sayfaya yapışır, sonraki çalıştırmalar da onu kullanır.
    if oldu:
        _cache[s] = out
        _yeni += 1
    else:
        print(f"  ! çeviri başarısız (önbelleğe yazılmadı): {s[:60]}")
    time.sleep(0.15)  # uç noktaya nazik ol
    return out


# ── Türkçe sayfadan blok çıkarma ──────────────────────────────────────────────
def blok(pat, t, flags=re.S):
    m = re.search(pat, t, flags)
    return m.group(1) if m else ""


def metin(h):
    """HTML parçasından düz metin · &#x27; gibi kaçışları çözer."""
    return html.unescape(re.sub(r"<[^>]+>", "", h)).strip()


def esc(s):
    return (html.escape(s or "", quote=True).replace("&#x27;", "&#39;"))


def sayi_en(s):
    """Türkçe binlik ayırıcı → İngilizce · 6.780 → 6,780 (rapor tarafındaki metaEn ile aynı kural)."""
    return re.sub(r"\d{1,3}(?:\.\d{3})+", lambda m: m.group(0).replace(".", ","), s)


BASLIK_MAP = {
    "Ne kazandırır?": "What you get",
    "Kurulum": "Installation",
    "Çalıştırma": "Running it",
    "Nasıl başlanır?": "Getting started",
    "Kod bilmiyorsanız": "If you don't write code",
    "İlgili sözlük terimleri": "Related dictionary terms",
    "Bağlantılar": "Links",
}


def cmd_bloklari(sec_html):
    """disc-cmd blokları · başlık çevrilir, KOD olduğu gibi kalır."""
    out = ""
    for m in re.finditer(r'<div class="disc-cmd">.*?<span>(.*?)</span>.*?<pre><code>(.*?)</code></pre>\s*</div>',
                         sec_html, re.S):
        baslik = tr2en(metin(m.group(1)))
        kod = m.group(2)  # zaten kaçışlı · dokunma
        out += ('<div class="disc-cmd"><div class="disc-cmd-head"><span>' + esc(baslik) + '</span>'
                '<button type="button" class="disc-copy" aria-label="Copy command">Copy</button></div>'
                '<pre><code>' + kod + '</code></pre></div>')
    return out


def bolumler(t):
    """Türkçe sayfadaki disc-sec bölümlerini İngilizceye çevirerek yeniden kur."""
    out = ""
    for m in re.finditer(r'<section class="disc-sec"><h2>(.*?)</h2>(.*?)</section>', t, re.S):
        h2, govde = metin(m.group(1)), m.group(2)
        if h2 == "Bağlantılar":
            continue  # bağlantı bölümünü aşağıda kendimiz kuruyoruz
        yeni_h2 = BASLIK_MAP.get(h2) or tr2en(h2)
        if 'class="disc-wins"' in govde:
            maddeler = "".join(f"<li>{esc(tr2en(metin(x)))}</li>"
                               for x in re.findall(r"<li>(.*?)</li>", govde, re.S))
            out += f'<section class="disc-sec"><h2>{esc(yeni_h2)}</h2><ul class="disc-wins">{maddeler}</ul></section>\n      '
        elif 'class="disc-cmd"' in govde:
            out += f'<section class="disc-sec"><h2>{esc(yeni_h2)}</h2>{cmd_bloklari(govde)}</section>\n      '
        elif 'class="disc-ai"' in govde:
            istem = tr2en(metin(blok(r'<p class="disc-ai-text">(.*?)</p>', govde)))
            out += ('<section class="disc-sec"><h2>' + esc(yeni_h2) + '</h2><div class="disc-ai"><div class="disc-ai-head">'
                    '<span>🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)</span>'
                    '<button type="button" class="disc-copy" aria-label="Copy prompt">Copy</button></div>'
                    '<p class="disc-ai-text">' + esc(istem) + '</p></div></section>\n      ')
        elif 'class="disc-related"' in govde:
            cips = "".join(f'<a href="/en/dictionary/{s}/">{esc(metin(a))}</a>'
                           for s, a in re.findall(r'<a href="/dictionary/([^/]+)/">(.*?)</a>', govde, re.S)
                           if os.path.isdir(os.path.join(ROOT, "en", "dictionary", s)))
            if cips:
                out += f'<section class="disc-sec"><h2>{esc(yeni_h2)}</h2><div class="disc-related">{cips}</div></section>\n      '
        else:
            p = metin(blok(r"<p>(.*?)</p>", govde))
            link = blok(r'(<ul class="disc-links">.*?</ul>)', govde)
            link = link.replace("Resmî kaynak →", "Official source →")
            if p:
                out += f'<section class="disc-sec"><h2>{esc(yeni_h2)}</h2><p>{esc(tr2en(p))}</p>{link}</section>\n      '
    return out


def olgular(t):
    """disc-facts · 'Kimin için' / 'Lisans'. Lisans adı çevrilmez (SPDX)."""
    govde = blok(r'<div class="disc-facts">(.*?)</div>\s*(?:<section|<p class="disc-disclaimer")', t)
    if not govde:
        return ""
    out = ""
    for k, v in re.findall(r'<span class="disc-fact-k">(.*?)</span><span class="disc-fact-v">(.*?)</span>', govde, re.S):
        k, v = metin(k), metin(v)
        if k == "Lisans":
            out += f'<div class="disc-fact"><span class="disc-fact-k">License</span><span class="disc-fact-v">{esc(v)}</span></div>'
        else:
            out += (f'<div class="disc-fact"><span class="disc-fact-k">{esc(tr2en(k))}</span>'
                    f'<span class="disc-fact-v">{esc(tr2en(v))}</span></div>')
    return f'<div class="disc-facts">{out}</div>\n      ' if out else ""


def guncelleme_en(gs):
    """Katalogdaki yapısal güncelleme katmanları · sayılar ve tarihler veriden, metin sabit."""
    if not gs:
        return ""
    aylar = ["January", "February", "March", "April", "May", "June",
             "July", "August", "September", "October", "November", "December"]

    def tarih(iso):
        try:
            y, a, g = iso.split("-")
            return f"{aylar[int(a)-1]} {int(g)}, {y}"
        except Exception:
            return iso

    li = []
    for g in reversed(gs[-4:]):
        p = []
        if g.get("onceki_yildiz") and g.get("yildiz"):
            p.append(f"Stars {g['onceki_yildiz']:,} → {g['yildiz']:,}")
        elif g.get("yildiz"):
            p.append(f"Stars {g['yildiz']:,}")
        if g.get("surum"):
            t = f" ({tarih(g['surum_tarihi'])})" if g.get("surum_tarihi") else ""
            p.append(f"latest release {esc(g['surum'])}{t}")
        if g.get("tasindi"):
            p.append(f"repository moved, new address {esc(g['tasindi'])}")
        if g.get("arsiv"):
            p.append("repository archived, development stopped")
        if p:
            li.append(f"<li><strong>{tarih(g['tarih'])}:</strong> " + ", ".join(p) + ".</li>")
    if not li:
        return ""
    return ('<section class="disc-sec disc-updates"><h2>Updates</h2><ul class="disc-update-list">'
            + "".join(li) + "</ul></section>\n      ")


# ── sayfa kurulumu ────────────────────────────────────────────────────────────
def en_chrome():
    """Mevcut İngilizce sayfadan nav + footer al · guard'lar kanonik seti bekliyor."""
    ornek = next((os.path.join(EN_DIR, d, "index.html") for d in sorted(os.listdir(EN_DIR))
                  if os.path.isdir(os.path.join(EN_DIR, d))
                  and os.path.exists(os.path.join(EN_DIR, d, "index.html"))), None)
    t = open(ornek, encoding="utf-8").read()
    nav = re.search(r"<nav>.*?</nav>", t, re.S).group(0)
    footer = re.search(r"<footer>.*?</footer>", t, re.S).group(0)
    form = re.search(r'<form class="cta-form.*?</form>', t, re.S)
    vercel = "".join(re.findall(r'<script[^>]*src="/_vercel[^>]*></script>', t))
    return nav, footer, (form.group(0) if form else ""), vercel


def build(slug, cat, chrome):
    nav, footer, form, vercel = chrome
    tp = os.path.join(TR_DIR, slug, "index.html")
    if not os.path.exists(tp):
        return None
    t = open(tp, encoding="utf-8").read()
    c = cat.get(slug, {})
    title = metin(blok(r"<title>(.*?)</title>", t)).split(" · ")[0]
    headline = tr2en(metin(blok(r'<h1 class="disc-title">(.*?)</h1>', t)))
    lead = tr2en(metin(blok(r'<p class="disc-lead">(.*?)</p>', t)))
    url = blok(r'<ul class="disc-links"><li><a href="([^"]+)"', t)
    date = c.get("date", "")
    mom = metin(blok(r'<span class="disc-momentum">(.*?)</span>', t))
    mom_en = sayi_en(mom).replace("bugün", "today")
    metas = ""
    for li in re.findall(r"<li>(.*?)</li>", blok(r'<ul class="disc-meta">(.*?)</ul>', t), re.S):
        v = sayi_en(metin(li))
        metas += f"<li>{esc(v)}</li>"
    notu = metin(blok(r'<aside class="disc-note"><p><strong>TreScout notu:</strong>(.*?)</p></aside>', t))
    not_html = (f'<aside class="disc-note"><p><strong>TreScout note:</strong> {esc(tr2en(notu))}</p></aside>\n      '
                if notu else "")
    shot = blok(r'(<figure class="disc-shot">.*?</figure>)', t)
    if shot:
        alt = re.search(r'alt="([^"]*)"', shot)
        if alt and alt.group(1):
            shot = shot.replace(f'alt="{alt.group(1)}"', f'alt="{esc(tr2en(html.unescape(alt.group(1))))}"')
        shot += "\n      "

    canon_en = f"{BASE}/en/discover/{slug}/"
    canon_tr = f"{BASE}/discover/{slug}/"
    ogimg = f"{BASE}/assets/discover/og/{slug}.webp"
    tagline_en = c.get("tagline_en") or lead
    ld = json.dumps({
        "@context": "https://schema.org", "@type": "Article", "headline": title, "inLanguage": "en",
        "description": tagline_en,
        "author": {"@type": "Organization", "name": "TreScout", "url": BASE},
        "publisher": {"@type": "Organization", "name": "TreScout"},
        "image": ogimg, "url": canon_en,
        "about": {"@type": "SoftwareSourceCode", "name": title, "codeRepository": url},
    }, ensure_ascii=False, indent=2)

    head = ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<title>{esc(title)} · Discover · TreScout</title>\n'
            f'<meta name="description" content="{esc(tagline_en)}">\n'
            '<link rel="icon" type="image/svg+xml" href="/favicon.svg">\n'
            f'<link rel="alternate" type="text/markdown" href="/en/discover/{slug}.md">\n'
            f'<link rel="canonical" href="{canon_en}">\n'
            f'<link rel="alternate" hreflang="tr" href="{canon_tr}">\n'
            f'<link rel="alternate" hreflang="en" href="{canon_en}">\n'
            f'<link rel="alternate" hreflang="x-default" href="{canon_en}">\n'
            f'<meta property="og:title" content="{esc(title)}">\n'
            f'<meta property="og:description" content="{esc(tagline_en)}">\n'
            f'<meta property="og:url" content="{canon_en}">\n<meta property="og:type" content="article">\n'
            '<meta property="og:locale" content="en_US">\n'
            f'<meta property="og:image" content="{ogimg}">\n'
            '<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n'
            '<meta name="twitter:card" content="summary_large_image">\n'
            '<meta name="twitter:site" content="@GetTreScout">\n'
            f'<meta name="twitter:title" content="{esc(title)}">\n'
            f'<meta name="twitter:image" content="{ogimg}">\n'
            f'<script type="application/ld+json">\n{ld}\n</script>\n'
            '<link rel="preload" href="/assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>\n'
            '<link rel="stylesheet" href="/assets/site.css">\n'
            '<link rel="stylesheet" href="/assets/discover.css">\n</head>\n')

    eyebrow = f"Discover · GitHub · {esc(title)}" if headline.strip().lower() != title.strip().lower() else "Discover · GitHub"
    govde = ('<body>\n<a class="skip-link" href="#main">Skip to main content</a>\n' + nav +
             '\n<main id="main">\n<article class="disc">\n'
             '<a class="disc-back" href="/en/discover/">← Discover</a>\n'
             f'<div class="disc-top"><span class="disc-eyebrow">{eyebrow}</span>'
             + (f'<span class="disc-momentum">{esc(mom_en)}</span>' if mom_en else "") + '</div>\n'
             f'<h1 class="disc-title">{esc(headline)}</h1>\n<p class="disc-lead">{esc(lead)}</p>\n'
             f'<ul class="disc-meta">{metas}</ul>\n      '
             + not_html + guncelleme_en(c.get("guncellemeler")) + shot + bolumler(t) + olgular(t) +
             '<section class="disc-sec"><h2>Links</h2><ul class="disc-links">'
             f'<li><a href="{esc(url)}" target="_blank" rel="noopener">GitHub repository →</a></li>'
             f'<li><a href="{canon_tr}">Read in Turkish →</a></li></ul></section>\n'
             f'<p class="disc-disclaimer">TreScout did not build this tool · we found it in GitHub trends and wrote it up. '
             f'This page describes the repository as of {date}: The star count and our text belong to that day, the repository '
             f'may have changed since. Check the repository link for the current state.</p>\n'
             '<aside class="disc-cta"><p><strong>TreScout catches tools like this every day.</strong> '
             'GitHub, Hacker News and HuggingFace are scanned, the highlights are summarized for you.</p>'
             + form + '<a class="btn btn-ghost disc-cta-all" href="/en/discover/">All discoveries →</a></aside>\n'
             '</article>\n</main>\n' + footer + '\n<script src="/assets/discover.js" defer></script>\n'
             '<script src="/assets/subscribe.js" defer></script>\n' + vercel + '</body>\n</html>\n')
    return head + govde


def main():
    cat = {c["slug"]: c for c in json.load(open(CATALOG, encoding="utf-8"))}
    chrome = en_chrome()
    sluglar = [ONLY] if ONLY else sorted(cat)
    if LIMIT:
        sluglar = sluglar[:LIMIT]
    yazilan = 0
    for i, slug in enumerate(sluglar, 1):
        h = build(slug, cat, chrome)
        if not h:
            print(f"  ! {slug}: Türkçe sayfa yok · atlandı")
            continue
        if DRY:
            print(f"  ~ {slug}: {len(h.split())} kelime")
            continue
        d = os.path.join(EN_DIR, slug)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(h)
        yazilan += 1
        if i % 25 == 0:
            json.dump(_cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
            print(f"  · {i}/{len(sluglar)} sayfa · önbellek {len(_cache)} kayıt")
    if not DRY:
        json.dump(_cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
    print(f"✅ {yazilan} İngilizce keşif sayfası · {_yeni} yeni çeviri · önbellek {len(_cache)} kayıt")


main()
