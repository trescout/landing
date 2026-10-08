#!/usr/bin/env python3
"""
TreScout · .md uç noktaları (LLM/yapay zekâ için temiz markdown) · HTML'den türetilir.

Kapsam: tüm dillerde (Türkçe dahil) sözlük ve keşif sayfaları. Her
<tur>/<slug>/index.html → <tur>/<slug>.md · tek kaynak sayfanın kendisi.

Neden (2026-10-08): .md'ler yalnız üretici sayfayı yazarken üretiliyordu.
Elle düzenlenmiş (korunan) sayfalar hiç yeniden üretilmediği için .md'leri
HTML'den geride kaldı (tools.md 5 dilde "What is Tools?" bot sürümündeydi);
üreticiler de bölümlerin yalnız bir kısmını alıyordu. Türkçe sözlük .md'leri
dict-sync.py verisinden bir kez yazılıyordu · sonradan eklenen "İlgili araçlar"
ve elle zenginleştirilen bölümler 493 sayfada .md'ye hiç girmemişti. Artık her koşuda tüm
.md'ler sayfanın son hâlinden, ortak dönüştürücüyle (html_md.py) yeniden
yazılır. Eski discover-md.py'nin (yalnız Türkçe keşif) yerini aldı.

Kullanım:
  python3 scripts/md-uret.py           # yaz (idempotent · içerik aynıysa dosya değişmez)
  python3 scripts/md-uret.py --check   # guard · güncel olmayan .md varsa exit 1
"""
import os, sys, glob

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from html_md import md_dosyasi
from diller import DILLER

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://trescout.com"
CHECK = "--check" in sys.argv
TR_SON = "TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler."


def hedefler():
    """(sayfa yolu, .md yolu, kaynak satırı, Türkçe keşif mi) dörtlüleri."""
    for tur, ad in (("dictionary", "TreScout Teknoloji Sözlüğü"), ("discover", "TreScout Keşif")):
        for f in sorted(glob.glob(os.path.join(ROOT, tur, "*", "index.html"))):
            slug = os.path.basename(os.path.dirname(f))
            yield f, os.path.join(ROOT, tur, slug + ".md"), \
                f"Kaynak: {ad} · {BASE}/{tur}/{slug}/\n{TR_SON}", tur == "discover"
    for kod, D in DILLER.items():
        dizin = D["onek"].strip("/")
        if not dizin:
            continue
        for tur, anahtar in (("dictionary", "md_kaynak_sozluk"), ("discover", "md_kaynak_kesif")):
            for f in sorted(glob.glob(os.path.join(ROOT, dizin, tur, "*", "index.html"))):
                slug = os.path.basename(os.path.dirname(f))
                yield f, os.path.join(ROOT, dizin, tur, slug + ".md"), \
                    D[anahtar].format(url=f"{BASE}{D['onek']}/{tur}/{slug}/"), False


def main():
    yazilan = eski = toplam = 0
    bayat = []
    for sayfa, mdyol, kaynak, tr_kesif in hedefler():
        t = open(sayfa, encoding="utf-8").read()
        md = md_dosyasi(t, kaynak, BASE)
        if md is None:
            continue
        toplam += 1
        onceki = open(mdyol, encoding="utf-8").read() if os.path.exists(mdyol) else None
        if md != onceki:
            bayat.append(os.path.relpath(mdyol, ROOT))
            if not CHECK:
                open(mdyol, "w", encoding="utf-8").write(md)
                yazilan += 1
        # Türkçe keşif sayfasına rel=alternate (çeviri üreticileri kendileri basıyor)
        if tr_kesif and not CHECK and 'type="text/markdown"' not in t:
            slug = os.path.basename(os.path.dirname(sayfa))
            link = f'<link rel="alternate" type="text/markdown" href="/discover/{slug}.md">\n'
            open(sayfa, "w", encoding="utf-8").write(t.replace('<link rel="canonical"', link + '<link rel="canonical"', 1))
            eski += 1
    if CHECK:
        if bayat:
            print(f"✗ {len(bayat)} .md sayfasının HTML'inden geride · python3 scripts/md-uret.py")
            for b in bayat[:20]:
                print("   ", b)
            raise SystemExit(1)
        print(f"✓ .md uç noktaları güncel · {toplam} sayfa (Türkçe + {sum(1 for D in DILLER.values() if D["onek"])} dil · sözlük ve keşif)")
        return
    print(f".md: {toplam} sayfa · {yazilan} yazıldı/güncellendi · rel=alternate: {eski} sayfaya eklendi")


if __name__ == "__main__":
    main()
