#!/usr/bin/env python3
"""Kaldırılan keşif ve sözlük kayıtları geri gelmesin · kaynak: assets/discover/kaldirilan.json

Hak sahibi bildirimiyle kaldırılan bir kaydın sayfası, kartı, sitemap girdisi ya da
deposuna/terimine bağlantı hiçbir yayın dosyasında (HTML, MD, JSON, JS, PDF vb.) kalmamalı.
Rapor arşivindeki (reports/) ve PDF'lerdeki eşleşmeler de artık KESİN HATADIR (fail-closed).

Bulgu varsa: python3 scripts/kaldirilan.py --uygula && python3 scripts/llms-txt.py
"""
import json
import os
import re
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kaldirilan import DILLER, ROOT, kayitlar, sozluk_terimleri, terim_engelli_mi  # noqa: E402

UZANTI = (".html", ".md", ".txt", ".xml", ".json", ".js")
ATLA = {".git", "node_modules", "docs", "scripts", ".vercel"}


def main():
    hatalar = []
    kayit = kayitlar()
    terimler = sozluk_terimleri()

    # 1) Keşif sayfaları ve catalog.json denetimi
    for k in kayit:
        s = k["slug"]
        for p in DILLER:
            for yol in (os.path.join(p, "discover", s), os.path.join(p, "discover", s + ".md")):
                if os.path.exists(os.path.join(ROOT, yol)):
                    hatalar.append(f"{yol} hâlâ var")
        cat_yol = os.path.join(ROOT, "assets", "discover", "catalog.json")
        if os.path.exists(cat_yol):
            cat = json.load(open(cat_yol, encoding="utf-8"))
            if any(c.get("slug") == s for c in cat):
                hatalar.append(f"catalog.json: {s} kaydı hâlâ var")

    # 2) Sözlük sayfaları, manifest ve OG görseli denetimi
    for t in terimler:
        for p in DILLER:
            for yol in (os.path.join(p, "dictionary", t), os.path.join(p, "dictionary", t + ".md")):
                if os.path.exists(os.path.join(ROOT, yol)):
                    hatalar.append(f"{yol} (sözlük) hâlâ var")
        og_yol = os.path.join(ROOT, "assets", "dictionary", "og", f"{t}.webp")
        if os.path.exists(og_yol):
            hatalar.append(f"assets/dictionary/og/{t}.webp hâlâ var")

    dict_man = os.path.join(ROOT, "assets", "dictionary", "dictionary.json")
    if os.path.exists(dict_man):
        man = json.load(open(dict_man, encoding="utf-8"))
        for item in man:
            if terim_engelli_mi(item.get("slug")) or terim_engelli_mi(item.get("en")):
                hatalar.append(f"dictionary.json: {item.get('slug')} terimi hâlâ var")

    # 3) Metin dosyalarında arama deseni
    parcalar = []
    for k in kayit:
        parcalar.append(r"/discover/" + re.escape(k["slug"]) + r"(?:/|\.md|\b)")
        parcalar.append(r"/og/" + re.escape(k["slug"]) + r"(?:-[a-z]{2})?\.webp")
        for r in k.get("repolar", []):
            if "github.com/" in r:
                parcalar.append(re.escape(r.split("github.com/", 1)[1]))
            else:
                parcalar.append(re.escape(r))

    for t in terimler:
        parcalar.append(r"/dictionary/" + re.escape(t) + r"(?:/|\.md|\b)")
        parcalar.append(r"/og/" + re.escape(t) + r"(?:-[a-z]{2})?\.webp")
        parcalar.append(r"\b" + re.escape(t) + r"\b")

    desen = re.compile("|".join(parcalar), re.I)

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
                hatalar.append(f"{goreli}: '{m.group(0)}'")

    # 4) PDF arşivi denetimi
    pdftotext_bin = shutil.which("pdftotext") or ("/opt/homebrew/bin/pdftotext" if os.path.exists("/opt/homebrew/bin/pdftotext") else None)
    if not pdftotext_bin:
        hatalar.append("pdftotext bulunamadı: PDF arşivi denetlenemiyor (fail-closed)")
    else:
        pdf_parcalar = []
        for k in kayit:
            pdf_parcalar.append(re.escape(k["slug"]))
            for r in k.get("repolar", []):
                r_clean = r.split("github.com/", 1)[1] if "github.com/" in r else r
                pdf_parcalar.append(re.escape(r_clean))
        for t in terimler:
            pdf_parcalar.append(r"\b" + re.escape(t) + r"\b")
        desen_pdf = re.compile("|".join(pdf_parcalar), re.I)

        pdf_dosyalari = []
        for kok, dizinler, dosyalar in os.walk(ROOT):
            dizinler[:] = [d for d in dizinler if d not in ATLA]
            for ad in dosyalar:
                if ad.endswith(".pdf"):
                    pdf_dosyalari.append(os.path.join(kok, ad))

        for pdf_yol in sorted(pdf_dosyalari):
            goreli = os.path.relpath(pdf_yol, ROOT)
            try:
                res = subprocess.run([pdftotext_bin, "-layout", pdf_yol, "-"], capture_output=True, text=True, check=True)
                m = desen_pdf.search(res.stdout)
                if m:
                    hatalar.append(f"{goreli} (PDF): '{m.group(0)}'")
            except Exception as exc:
                hatalar.append(f"{goreli} (PDF okunamadı): {exc}")

    if hatalar:
        print("❌ Kaldırılan kayıt ya da sözlük teriminin izi kaldı:")
        for h in hatalar:
            print(f"  - {h}")
        print("Düzeltme: python3 scripts/kaldirilan.py --uygula && python3 scripts/llms-txt.py")
        sys.exit(1)

    print(
        f"✅ Kaldırılan {len(kayit)} kaydın ve {len(terimler)} sözlük teriminin yayında izi yok"
        f" (PDF arşivi doğrulandı)"
    )


if __name__ == "__main__":
    main()
