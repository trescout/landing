#!/usr/bin/env python3
"""Kaldırılan keşif kayıtları geri gelmesin · kaynak: assets/discover/kaldirilan.json

Hak sahibi bildirimiyle kaldırılan bir kaydın sayfası, kartı, sitemap girdisi ya da
deposuna bağlantı hiçbir yayın dosyasında kalmamalı (bkz. scripts/kaldirilan.py).
Rapor arşivinde (reports/) depo adı geçerse yalnız uyarı verilir: günlük rapor app
reposunda üretiliyor; orada da süzülene kadar hat kırmızıya dönmesin.

Bulgu varsa: python3 scripts/kaldirilan.py --uygula && python3 scripts/llms-txt.py
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kaldirilan import DILLER, ROOT, kayitlar  # noqa: E402

UZANTI = (".html", ".md", ".txt", ".xml", ".json", ".js")
ATLA = {".git", "node_modules", "docs", "scripts", ".vercel"}


def main():
    hatalar, uyarilar = [], []
    kayit = kayitlar()
    for k in kayit:
        s = k["slug"]
        for p in DILLER:
            for yol in (os.path.join(p, "discover", s), os.path.join(p, "discover", s + ".md")):
                if os.path.exists(os.path.join(ROOT, yol)):
                    hatalar.append(f"{yol} hâlâ var")
        cat = json.load(open(os.path.join(ROOT, "assets", "discover", "catalog.json"), encoding="utf-8"))
        if any(c.get("slug") == s for c in cat):
            hatalar.append(f"catalog.json: {s} kaydı hâlâ var")
    desen = re.compile("|".join(
        [r"/discover/" + re.escape(k["slug"]) + r"(?:/|\.md|\b)" for k in kayit] +
        [r"/og/" + re.escape(k["slug"]) + r"(?:-[a-z]{2})?\.webp" for k in kayit] +
        [re.escape(r.split("github.com/", 1)[1]) for k in kayit for r in k["repolar"]]), re.I)
    for kok, dizinler, dosyalar in os.walk(ROOT):
        dizinler[:] = [d for d in dizinler if d not in ATLA]
        for ad in dosyalar:
            if not ad.endswith(UZANTI):
                continue
            yol = os.path.join(kok, ad)
            goreli = os.path.relpath(yol, ROOT)
            if goreli == os.path.join("assets", "discover", "kaldirilan.json"):
                continue
            try:
                t = open(yol, encoding="utf-8").read()
            except (UnicodeDecodeError, OSError):
                continue
            m = desen.search(t)
            if m:
                (uyarilar if goreli.startswith("reports" + os.sep) else hatalar).append(f"{goreli}: '{m.group(0)}'")
    for u in uyarilar:
        print(f"  ⚠ {u}")
    if hatalar:
        print("❌ Kaldırılan keşif kaydının izi kaldı:")
        for h in hatalar:
            print(f"  - {h}")
        print("Düzeltme: python3 scripts/kaldirilan.py --uygula && python3 scripts/llms-txt.py")
        sys.exit(1)
    print(f"✅ Kaldırılan {len(kayit)} kaydın yayında izi yok" + (f" · {len(uyarilar)} rapor uyarısı" if uyarilar else ""))


if __name__ == "__main__":
    main()
