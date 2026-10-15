#!/usr/bin/env python3
"""Site içi bağlantılar var olan bir dosyaya gidiyor mu (CI).

2026-10-15 taraması: 9.671 sayfada 259 bin site içi bağlantıdan yalnız biri kırıktı
(en/compare/rss-vs-ai olmayan bir .md sürümünü gösteriyordu). Üreticiler sayfa
yolunu kendi kuruyor; bir üretici hatası binlerce sayfaya aynı anda 404 basabilir.
Bu guard o durumu PR'da yakalar.

Kapsam: "/" ile başlayan href/src (dış adresler, /api/ ve /_vercel/ hariç).
"""
import glob
import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HREF = re.compile(r'(?:href|src)="(/[^"#?]*)')
ATLA = ("/api/", "/_vercel", "//")


def var_mi(u):
    p = os.path.join(ROOT, u.lstrip("/"))
    if u.endswith("/"):
        return os.path.exists(os.path.join(p, "index.html"))
    return os.path.exists(p) or os.path.exists(p + ".html") or os.path.exists(os.path.join(p, "index.html"))


def main():
    kirik = defaultdict(set)
    sayfa = 0
    for f in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True):
        rel = os.path.relpath(f, ROOT)
        if rel.startswith(("node_modules", ".git")):
            continue
        sayfa += 1
        for u in set(HREF.findall(open(f, encoding="utf-8").read())):
            if not u.startswith(ATLA) and not var_mi(u):
                kirik[u].add(rel)
    if kirik:
        print(f"✗ {len(kirik)} kırık site içi hedef ({sum(len(v) for v in kirik.values())} sayfada):")
        for u, kaynak in sorted(kirik.items(), key=lambda x: -len(x[1]))[:15]:
            print(f"   {u}  ← {len(kaynak)} sayfa, örn. {sorted(kaynak)[0]}")
        sys.exit(1)
    print(f"✓ site içi bağlantılar sağlam · {sayfa} sayfa")


main()
