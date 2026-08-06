#!/usr/bin/env python3
"""
Katalogdaki `cmds` alanını keşif sayfasına basar · Gemini gerektirmez.

Neden gerekti: Komut ekleme akışı `--reprocess` ile sayfayı yeniden ürettiriyordu,
o da Gemini çağrısı demek (kota + anahtar bağımlılığı, anahtar yoksa metni siler).
Sonuç: katkıcıların eklediği komutlar katalogda kaldı, sayfaya hiç düşmedi ·
2026-08-06 denetiminde 15 kayıtta komut yayında görünmüyordu.

Bu betik yalnız komut bölümlerini yazar: mevcut "Kurulum"/"Çalıştırma" bölümlerini
ve "Kaynak:" notunu değiştirir, yoksa "Ne kazandırır?" bölümünün hemen ardına
ekler (discover-sync'teki rich_sections sırasıyla aynı). Diğer içeriğe dokunmaz.

Kullanım: python3 scripts/cmds-render.py [--dry] [--slug=x]
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


def yaz(sayfa, cmds):
    """Mevcut komut bölümlerini kaldır, yenilerini doğru yere koy."""
    # 1. eski komut bölümleri + kaynak notu
    sayfa = re.sub(r'<section class="disc-sec"><h2>(?:Kurulum|Çalıştırma)</h2>.*?</section>\s*', "", sayfa, flags=re.S)
    sayfa = re.sub(r'<p class="disc-note"><strong>Kaynak:</strong>.*?</p>\s*', "", sayfa, flags=re.S)
    yeni = bolumler(cmds)
    if not yeni:
        return sayfa
    # 2. "Ne kazandırır?" bölümünün ardına
    m = re.search(r'<section class="disc-sec"><h2>Ne kazandırır\?</h2>.*?</section>\s*', sayfa, re.S)
    if m:
        return sayfa[:m.end()] + "      " + yeni + sayfa[m.end():]
    # 3. yoksa meta listesinin ardına
    m = re.search(r'<ul class="disc-meta">.*?</ul>\s*', sayfa, re.S)
    if m:
        return sayfa[:m.end()] + "      " + yeni + sayfa[m.end():]
    return sayfa


def main():
    cat = json.load(open(CATALOG, encoding="utf-8"))
    n = 0
    for c in cat:
        cmds = c.get("cmds") or {}
        if not (cmds.get("kurulum") or cmds.get("calistirma")):
            continue
        if ONLY and c["slug"] != ONLY:
            continue
        p = os.path.join(DISC, c["slug"], "index.html")
        if not os.path.exists(p):
            print(f"  ! {c['slug']}: sayfa yok")
            continue
        eski = open(p, encoding="utf-8").read()
        yeni = yaz(eski, cmds)
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
    print(f"{'[--dry] ' if DRY else '✅ '}{n} sayfaya komut bölümü yazıldı")


main()
