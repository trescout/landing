#!/usr/bin/env python3
"""
Katalogdaki alanları (`cmds`, `trescout_notu`, `shot`) keşif sayfasına basar ·
Gemini gerektirmez.

Neden gerekti: Komut ekleme akışı `--reprocess` ile sayfayı yeniden ürettiriyordu,
o da Gemini çağrısı demek (kota + anahtar bağımlılığı, anahtar yoksa metni siler).
Sonuç: katkıcıların eklediği komutlar katalogda kaldı, sayfaya hiç düşmedi ·
2026-08-06 denetiminde 15 kayıtta komut yayında görünmüyordu.

Cerrahi çalışır: yalnız ilgili blokları değiştirir, diğer içeriğe dokunmaz.
Sıralama discover-sync'teki build_page ile aynı · not ve görsel meta listesinin
ardında, komutlar "Ne kazandırır?" bölümünün ardında.

Kullanım: python3 scripts/catalog-render.py [--dry] [--slug=x]
"""
import os, re, sys, json, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG = os.path.join(ROOT, "assets", "discover", "catalog.json")
DISC = os.path.join(ROOT, "discover")
DRY = "--dry" in sys.argv
ONLY = next((a.split("=")[1] for a in sys.argv if a.startswith("--slug=")), None)


def esc(s):
    return (str(s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace('"', "&quot;").replace("'", "&#x27;"))


def cmd_block(it):
    """discover-sync.cmd_block ile birebir aynı biçim."""
    return ('<div class="disc-cmd"><div class="disc-cmd-head"><span>' + esc(it.get("baslik", "Komut")) + '</span>'
            '<button type="button" class="disc-copy" aria-label="Komutu kopyala">Kopyala</button></div>'
            '<pre><code>' + esc(it.get("komut", "")) + '</code></pre></div>')


def bolumler(cmds):
    s = ""
    for grp, h in (("kurulum", "Kurulum"), ("calistirma", "Çalıştırma")):
        its = cmds.get(grp) or []
        if its:
            s += f'<section class="disc-sec"><h2>{h}</h2>' + "".join(cmd_block(i) for i in its) + '</section>\n      '
    if cmds.get("kaynak"):
        s += f'<p class="disc-note"><strong>Kaynak:</strong> {esc(cmds["kaynak"])}</p>\n      '
    return s


def not_html(c):
    n = (c.get("trescout_notu") or "").strip()
    return (f'<aside class="disc-note"><p><strong>TreScout notu:</strong> {esc(n)}</p></aside>\n      ') if n else ""


def shot_html(c):
    sh = c.get("shot")
    if not sh:
        return ""
    return (f'<figure class="disc-shot"><img src="{esc(sh["src"])}" width="{sh.get("w","")}" '
            f'height="{sh.get("h","")}" loading="lazy" decoding="async" alt="{esc(sh.get("alt",""))}">'
            f'<figcaption>{esc(sh.get("credit",""))}</figcaption></figure>\n      ')


def meta_sonrasi(sayfa, c):
    """TreScout notu + ekran görüntüsü · meta listesinin hemen ardında (build_page sırası)."""
    sayfa = re.sub(r'<aside class="disc-note">.*?</aside>\s*', "", sayfa, flags=re.S)
    sayfa = re.sub(r'<figure class="disc-shot">.*?</figure>\s*', "", sayfa, flags=re.S)
    yeni = not_html(c) + shot_html(c)
    if not yeni:
        return sayfa
    m = re.search(r'<ul class="disc-meta">.*?</ul>\s*', sayfa, re.S)
    return sayfa[:m.end()] + yeni + sayfa[m.end():] if m else sayfa


def temizle_eski_komut_bloklari(sayfa):
    """Yeni catalog komutları basılmadan önce stale embedded command bloklarını kaldır.

    Bazı legacy sayfalarda aynı komutlar `disc-how` içindeki AI prompt’unun altında,
    ayrıca catalog-render’ın eklediği Kurulum/Çalıştırma bölümlerinde bulunuyordu.
    Yeni catalog komutları güncellenirken eski bloklar kalırsa Turkish ve locale
    sayfalarda iki farklı kurulum akışı görünür. AI prompt korunur.
    """
    def temizle(m):
        sec = m.group(0)
        if 'class="disc-cmd"' not in sec:
            return sec
        sec = re.sub(r'<div class="disc-cmd">.*?<pre><code>.*?</code></pre>\s*</div>\s*', '', sec, flags=re.S)
        # Komut dışında anlamlı bir içerik veya AI prompt yoksa boş başlık bırakma.
        if 'class="disc-ai"' not in sec and not re.search(r'<(?:p|ul|ol|aside|figure)\b', sec):
            return ''
        return sec
    return re.sub(r'<section class="disc-sec[^"]*">.*?</section>\s*', temizle, sayfa, flags=re.S)


def yaz(sayfa, cmds):
    """Mevcut komut bölümlerini kaldır, yenilerini doğru yere koy."""
    # Yeni catalog komutu varsa legacy embedded blokları da temizle.
    if cmds.get("kurulum") or cmds.get("calistirma"):
        sayfa = temizle_eski_komut_bloklari(sayfa)
    # 1. eski komut bölümleri + kaynak notu
    sayfa = re.sub(r'<section class="disc-sec"><h2>(?:Kurulum|Çalıştırma)</h2>.*?</section>\s*', "", sayfa, flags=re.S)
    sayfa = re.sub(r'<p class="disc-note"><strong>Kaynak:</strong>.*?</p>\s*', "", sayfa, flags=re.S)
    yeni = bolumler(cmds)
    if not yeni:
        return sayfa
    # 2. "Ne kazandırır?" bölümünün ardına
    m = re.search(r'<section class="disc-sec"><h2>Ne kazandırır\?</h2>.*?</section>\s*', sayfa, re.S)
    if m:
        return sayfa[:m.end()] + yeni + sayfa[m.end():]
    # 3. yoksa meta listesinin ardına
    m = re.search(r'<ul class="disc-meta">.*?</ul>\s*', sayfa, re.S)
    if m:
        return sayfa[:m.end()] + yeni + sayfa[m.end():]
    return sayfa


def main():
    cat = json.load(open(CATALOG, encoding="utf-8"))
    n = 0
    for c in cat:
        cmds = c.get("cmds") or {}
        if not (cmds.get("kurulum") or cmds.get("calistirma") or c.get("trescout_notu") or c.get("shot")):
            continue
        if ONLY and c["slug"] != ONLY:
            continue
        p = os.path.join(DISC, c["slug"], "index.html")
        if not os.path.exists(p):
            print(f"  ! {c['slug']}: sayfa yok")
            continue
        eski = open(p, encoding="utf-8").read()
        yeni = meta_sonrasi(yaz(eski, cmds), c)
        # komut kopyalama düğmesi discover.js'e bağlı · sayfada yoksa ekle
        if 'src="/assets/discover.js"' not in yeni:
            yeni = yeni.replace('<script src="/assets/subscribe.js" defer></script>',
                                '<script src="/assets/discover.js" defer></script>\n<script src="/assets/subscribe.js" defer></script>', 1)
        if yeni == eski:
            continue
        n += 1
        if DRY:
            print(f"  ~ {c['slug']}")
            continue
        open(p, "w", encoding="utf-8").write(yeni)
    print(f"{'[--dry] ' if DRY else '✅ '}{n} sayfa güncellendi (komut · not · görsel)")


main()
