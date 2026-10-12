#!/usr/bin/env python3
"""Kaldırılan keşif kayıtları · tek kaynak: assets/discover/kaldirilan.json

2026-10-12 · Web Sheriff (WeMod LLC adına) /en/discover/wand-enhancer için DMCA
bildirimi gönderdi. Keşif hattında hariç tutma yoktu: sayfa silinse bile depo
raporlarda göründükçe discover-sync.py onu yeniden üretirdi. Artık:

  * discover-sync.py rapor öğelerini engelli_mi() ile süzer, kayıt geri gelmez.
  * --uygula listedeki kaydın tüm izlerini siler: 6 dilde sayfa + .md, kapak
    görselleri, katalog/damga/çeviri önbelleği, dizin kartları, sözlük
    "ilgili araçlar" bağlantıları, sitemap, rapor bağlantıları ve rapor JSON
    öğeleri. llms*.txt ardından scripts/llms-txt.py ile yeniden üretilir.
  * scripts/check-kaldirilan.py hiçbir yayın dosyasında iz kalmadığını denetler.

Kullanım: python3 scripts/kaldirilan.py --uygula [--dry]
"""
import glob
import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LISTE = os.path.join(ROOT, "assets", "discover", "kaldirilan.json")
DILLER = ["", "en/", "de/", "fr/", "es/", "pt/"]


def _norm(u):
    return re.sub(r"\.git$", "", (u or "").strip().rstrip("/").lower())


def kayitlar():
    return json.load(open(LISTE, encoding="utf-8"))["kayitlar"]


def slugs():
    return {k["slug"] for k in kayitlar()}


def engelli_mi(url="", slug=""):
    """Rapor öğesi kaldırılan bir kayda mı ait? URL ya da slug eşleşmesi yeter."""
    u = _norm(url)
    for k in kayitlar():
        if slug and slug == k["slug"]:
            return True
        if u and u in {_norm(r) for r in k["repolar"]}:
            return True
        if u and u.rsplit("/", 1)[-1] == k["slug"]:
            return True
    return False


def _yaz(yol, metin, dry):
    if not dry:
        open(yol, "w", encoding="utf-8").write(metin)


def _json_yaz(yol, veri, dry, indent, ham):
    """Dosyanın girintisini ve sondaki satır sonunu korur · diff yalnız silinen kayıt olsun."""
    if not dry:
        with open(yol, "w", encoding="utf-8") as f:
            json.dump(veri, f, ensure_ascii=False, indent=indent)
            if ham.endswith("\n"):
                f.write("\n")


def _girinti(metin):
    m = re.search(r"\n( +)\S", metin)
    return len(m.group(1)) if m else None


def _rapor_suz(d, k):
    """Rapor JSON'unda k (normalize depo URL kümesi) öğelerini iç içe listelerden çıkarır."""
    n = 0
    if isinstance(d, dict):
        for v in d.values():
            n += _rapor_suz(v, k)
    elif isinstance(d, list):
        tut = []
        for it in d:
            if isinstance(it, dict) and _norm(it.get("url", "")) in k:
                n += 1
                continue
            n += _rapor_suz(it, k)
            tut.append(it)
        d[:] = tut
    return n


def uygula(dry=False):
    for k in kayitlar():
        s = k["slug"]
        print(f"· {s}")
        # 1) sayfalar ve kapaklar
        for p in DILLER:
            for yol in (os.path.join(ROOT, p, "discover", s), os.path.join(ROOT, p, "discover", s + ".md")):
                if os.path.isdir(yol):
                    print(f"  sil {os.path.relpath(yol, ROOT)}/")
                    dry or shutil.rmtree(yol)
                elif os.path.exists(yol):
                    print(f"  sil {os.path.relpath(yol, ROOT)}")
                    dry or os.remove(yol)
        for yol in glob.glob(os.path.join(ROOT, "assets", "discover", "og", s + ".webp")) + \
                glob.glob(os.path.join(ROOT, "assets", "discover", "og", s + "-*.webp")):
            print(f"  sil {os.path.relpath(yol, ROOT)}")
            dry or os.remove(yol)

        ad = re.compile(re.escape(s), re.I)
        # 2) katalog, damga, kapak metni, çeviri önbellekleri
        cat_yol = os.path.join(ROOT, "assets", "discover", "catalog.json")
        ham_cat = open(cat_yol, encoding="utf-8").read()
        cat = json.loads(ham_cat)
        yeni = [c for c in cat if c.get("slug") != s]
        if len(yeni) != len(cat):
            print(f"  catalog.json −{len(cat) - len(yeni)}")
            _json_yaz(cat_yol, yeni, dry, 2, ham_cat)
        for yol in glob.glob(os.path.join(ROOT, "assets", "discover", "*-damga.json")) + \
                glob.glob(os.path.join(ROOT, "assets", "discover", "*-cache.json")) + \
                glob.glob(os.path.join(ROOT, "assets", "dictionary", "*-cache.json")) + \
                [os.path.join(ROOT, "assets", "discover", "og", "kapak-metinleri.json")]:
            ham = open(yol, encoding="utf-8").read()
            if not ad.search(ham):
                continue
            d = json.loads(ham)
            yeni = {a: v for a, v in d.items() if not (ad.search(a) or ad.search(json.dumps(v, ensure_ascii=False)))}
            print(f"  {os.path.relpath(yol, ROOT)} −{len(d) - len(yeni)}")
            _json_yaz(yol, yeni, dry, _girinti(ham), ham)

        # 3) HTML bağlantıları (dizin kartları, sözlük ilgili araçlar, rapor bağlantıları)
        a_rx = re.compile(r'<a\b[^>]*href="(?:/[a-z]{2})?/discover/' + re.escape(s) + r'/"[^>]*>.*?</a>\s*', re.S)
        bos_rx = re.compile(r'<section class="disc-sec"><h2>[^<]*</h2><div class="dict-related"></div></section>\n?')
        for yol in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True):
            if "/.git/" in yol or "/node_modules/" in yol:
                continue
            t = open(yol, encoding="utf-8").read()
            if f"/discover/{s}/" not in t:
                continue
            y = bos_rx.sub("", a_rx.sub("", t))
            print(f"  {os.path.relpath(yol, ROOT)} bağlantı temizlendi")
            _yaz(yol, y, dry)

        # 4) markdown liste satırları ve boş kalan "ilgili araçlar" başlıkları
        satir_rx = re.compile(r"^- \[[^\]]*\]\(https://trescout\.com(?:/[a-z]{2})?/discover/" + re.escape(s) + r"/\)\n", re.M)
        for yol in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True):
            if "/.git/" in yol or "/node_modules/" in yol or "/docs/" in yol:
                continue
            t = open(yol, encoding="utf-8").read()
            if f"/discover/{s}/" not in t:
                continue
            y = satir_rx.sub("", t)
            y = re.sub(r"\n\n## [^\n]+\n\n(?=\n)", "\n", y)  # listesi tümden boşalan başlık (yalnız silmenin bıraktığı üçlü satır sonu)
            print(f"  {os.path.relpath(yol, ROOT)} satır temizlendi")
            _yaz(yol, y, dry)

        # 5) sitemap
        sm = os.path.join(ROOT, "sitemap.xml")
        t = open(sm, encoding="utf-8").read()
        y = re.sub(r"\s*<url>\s*<loc>https://trescout\.com(?:/[a-z]{2})?/discover/" + re.escape(s) + r"/</loc>.*?</url>", "", t, flags=re.S)
        if y != t:
            print("  sitemap.xml temizlendi")
            _yaz(sm, y, dry)

        # 6) rapor JSON öğeleri
        for yol in glob.glob(os.path.join(ROOT, "reports", "*.json")):
            ham = open(yol, encoding="utf-8").read()
            if not ad.search(ham):
                continue
            d = json.loads(ham)
            n = _rapor_suz(d, {_norm(r) for r in k["repolar"]})
            if n:
                print(f"  {os.path.relpath(yol, ROOT)} −{n} öğe")
                _json_yaz(yol, d, dry, _girinti(ham), ham)
    print("Sonra: python3 scripts/llms-txt.py && python3 scripts/check-kaldirilan.py")


if __name__ == "__main__":
    if "--uygula" in sys.argv:
        uygula(dry="--dry" in sys.argv)
    else:
        print(__doc__)
