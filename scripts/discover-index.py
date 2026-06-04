#!/usr/bin/env python3
"""
TreScout Keşif · index server-render (AI/non-JS botlar için)
===========================================================
discover/index.html'deki #discover-grid önceden boştu (JS ile doluyordu) → JS
çalıştırmayan crawler'lara / çoğu AI botuna BOŞ görünüyordu. Bu script grid'i
catalog'dan server-render eder (discover.js markup'ıyla birebir, yıldıza göre).
discover.js JS kullanıcıları için aynı içeriği yeniden render eder + arama/filtre
ekler (progressive enhancement). Idempotent · Action'da discover-sync sonrası çalışır.
Kullanım: python3 scripts/discover-index.py
"""
import os, re, json, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAT = os.path.join(ROOT, "assets", "discover", "catalog.json")
IDX = os.path.join(ROOT, "discover", "index.html")

def esc(s): return html.escape("" if s is None else str(s), quote=True)

def card(it):  # discover.js card() ile birebir aynı markup
    img = f'<img class="disc-card-img" src="{esc(it.get("image",""))}" alt="" loading="lazy" decoding="async">' if it.get("image") else ''
    meta = f'<span class="disc-card-meta">{esc(it.get("meta",""))}</span>' if it.get("meta") else ''
    tags = "".join(f'<span class="disc-card-tagchip">{esc(t)}</span>' for t in (it.get("tags") or []))
    tagsdiv = f'<div class="disc-card-tags">{tags}</div>' if tags else ''
    return (f'<a class="disc-card" href="/discover/{esc(it["slug"])}/">{img}'
            f'<div class="disc-card-body"><h2 class="disc-card-title">{esc(it["title"])}</h2>'
            f'<p class="disc-card-tag">{esc(it.get("tagline",""))}</p>'
            f'{tagsdiv}{meta}</div></a>')

def main():
    cat = json.load(open(CAT, encoding="utf-8"))
    items = sorted(cat, key=lambda c: -(c.get("stars") or 0))
    grid = "\n        " + "\n        ".join(card(c) for c in items) + "\n      "
    t = open(IDX, encoding="utf-8").read()
    # grid'i değiştir · bitişi <aside class="disc-cta"> ile çapala (iç içe </div>'lere takılmaz, idempotent)
    t2 = re.sub(r'(<div id="discover-grid"[^>]*>).*?(</div>)(\s*<aside class="disc-cta")',
                lambda m: m.group(1) + grid + m.group(2) + m.group(3), t, count=1, flags=re.S)
    # sayaç
    t2 = re.sub(r'(<p id="disc-count" class="disc-count">).*?(</p>)',
                lambda m: m.group(1) + f"{len(items)} araç" + m.group(2), t2, count=1, flags=re.S)
    if t2 == t:
        print("discover index: değişiklik yok (grid/sayaç bulunamadı?)"); return
    open(IDX, "w", encoding="utf-8").write(t2)
    print(f"discover index server-render: {len(items)} kart gömüldü (yıldıza göre)")

if __name__ == "__main__":
    main()
