#!/usr/bin/env python3
"""Sözlük sayfalarında "Sıkça sorulanlar" başlığı "Sorular ve yanıtlar" olur.

2026-10-22 · Burhan (5 Ekim kaydı): bölümdeki sorular okurlardan gelmedi, "sıkça sorulan"
demek yanıltıcı. Başlık Gemini'den geçti. Yeni sayfalar yeni başlıkla doğar (dict-sync.py);
mevcut Türkçe sayfaları (html ve .md, 589 "Sıkça sorulanlar" + 146 "Sıkça Sorulanlar")
içerik hattı bu betikle günceller. Çeviri sayfalarına burada dokunulmaz: üretici
(dictionary-en.py) yeniden yazarken diller.py'deki karşılığı basar ve damgayı kendisi
yeniler (bkz. landing toplu düzenleme notu: dışarıdan değişen çeviri sayfası donar).

Kullanım:
  python3 scripts/sss-baslik.py             # sıkı: hiçbir Türkçe sözlük dosyasında eski başlık yok
  python3 scripts/sss-baslik.py --uygula    # eski başlığı yenisiyle değiştirir
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YENI = "Sorular ve yanıtlar"
ESKI_HTML = re.compile(r"<h2([^>]*)>Sıkça [sS]orulanlar</h2>")
ESKI_MD = re.compile(r"^(#{2,3}) Sıkça [sS]orulanlar[ \t]*$", re.M)


def dosyalar():
    yield from sorted(glob.glob(os.path.join(ROOT, "dictionary", "*", "index.html")))
    yield from sorted(glob.glob(os.path.join(ROOT, "dictionary", "*.md")))


def main():
    uygula = "--uygula" in sys.argv
    eski, degisen = [], 0
    for yol in dosyalar():
        md = yol.endswith(".md")
        rx = ESKI_MD if md else ESKI_HTML
        s = open(yol, encoding="utf-8").read()
        if not rx.search(s):
            continue
        if not uygula:
            eski.append(os.path.relpath(yol, ROOT))
            continue
        yeni = rx.sub(lambda m: f"{m.group(1)} {YENI}" if md else f"<h2{m.group(1)}>{YENI}</h2>", s)
        open(yol, "w", encoding="utf-8").write(yeni)
        degisen += 1
    if uygula:
        print(f"✓ SSS başlığı: {degisen} Türkçe sözlük dosyası güncellendi")
        return
    if eski:
        print(f"✗ {len(eski)} Türkçe sözlük dosyasında eski başlık (Sıkça sorulanlar): {', '.join(eski[:5])}"
              " · python3 scripts/sss-baslik.py --uygula")
        sys.exit(1)
    print("✓ SSS başlığı kontrolü: Türkçe sözlükte eski başlık yok")


if __name__ == "__main__":
    main()
