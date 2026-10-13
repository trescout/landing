#!/usr/bin/env python3
"""Kaldırılan keşif ve sözlük kayıtları · tek kaynak: assets/discover/kaldirilan.json

2026-10-12 · Web Sheriff (WeMod LLC adına) /en/discover/wand-enhancer için DMCA
bildirimi gönderdi. Keşif hattında hariç tutma yoktu: sayfa silinse bile depo
raporlarda göründükçe discover-sync.py onu yeniden üretirdi. Artık:

  * discover-sync.py ve dict-sync.py rapor/sözlük öğelerini engelli_mi() ve
    terim_engelli_mi() ile süzer, kayıt geri gelmez.
  * --uygula listedeki kaydın tüm izlerini siler: 6 dilde sayfa + .md, kapak
    görselleri, katalog/damga/çeviri önbelleği, dizin kartları, sözlük
    "ilgili araçlar" bağlantıları, sitemap, rapor bağlantıları ve rapor JSON
    öğeleri ile sözlük terimleri. llms*.txt ardından scripts/llms-txt.py ile
    yeniden üretilir.
  * scripts/check-kaldirilan.py hiçbir yayın dosyasında iz kalmadığını denetler.

Kullanım: python3 scripts/kaldirilan.py --uygula [--dry]
"""
import glob
import json
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LISTE = os.path.join(ROOT, "assets", "discover", "kaldirilan.json")
DILLER = ["", "en/", "de/", "fr/", "es/", "pt/"]


def _norm(u):
    if not u:
        return ""
    s = (u or "").strip()
    s = re.sub(r"^[a-zA-Z]+://", "", s)
    s = re.sub(r"^[a-zA-Z]+@github\.com:", "github.com/", s)
    s = re.sub(r"[?#].*$", "", s)
    s = re.sub(r"\.git$", "", s, flags=re.I)
    return s.rstrip("/").lower()


def _repo_bilgi(u):
    norm = _norm(u)
    if not norm:
        return "", "", "", ""
    parts = norm.split("/")
    host = parts[0] if parts else ""
    owner = parts[1] if len(parts) > 1 else ""
    repo = parts[2] if len(parts) > 2 else ""
    is_github = host == "github.com" or ("." not in host and bool(owner) and bool(repo))
    slug = repo if is_github and repo else (parts[-1] if parts else "")
    return norm, is_github, repo, slug


def kayitlar():
    if not os.path.exists(LISTE):
        return []
    with open(LISTE, encoding="utf-8") as f:
        return json.load(f).get("kayitlar", [])


def slugs():
    return {k["slug"].lower() for k in kayitlar() if k.get("slug")}


def sozluk_terimleri():
    """Tüm engelli sözlük terimlerinin normalize edilmiş kümesi."""
    terimler = set()
    for k in kayitlar():
        ham = k.get("sozluk_terimleri", []) + k.get("sozlukTerimleri", [])
        for t in ham:
            if isinstance(t, str) and t.strip():
                terimler.add(t.strip().lower())
    return terimler


def terim_engelli_mi(terim=""):
    """Sözlük terimi kaldırılan bir terim mi? Terim adı ya da slug eşleşir."""
    if not terim:
        return False
    t = str(terim).strip().lower()
    tslug = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    engelliler = sozluk_terimleri()
    if t in engelliler or tslug in engelliler:
        return True
    for e in engelliler:
        eslug = re.sub(r"[^a-z0-9]+", "-", e).strip("-")
        if t == eslug or tslug == eslug:
            return True
    return False


def engelli_mi(url="", slug=""):
    """Rapor öğesi kaldırılan bir kayda mı ait? URL ya da slug eşleşmesi yeter."""
    s = (slug or "").strip().lower()
    norm, is_github, repo, target_slug = _repo_bilgi(url)
    for k in kayitlar():
        kslug = k["slug"].lower()
        if s and s == kslug:
            return True
        if target_slug and target_slug == kslug:
            return True
        for r in k.get("repolar", []):
            rn, r_is_gh, r_repo, _ = _repo_bilgi(r)
            if norm and norm == rn:
                return True
            if norm and norm.startswith(rn + "/"):
                return True
            if is_github and r_is_gh and repo and r_repo and repo == r_repo:
                return True
    return False


def _yaz(yol, metin, dry):
    if not dry:
        with open(yol, "w", encoding="utf-8") as f:
            f.write(metin)


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


def _rapor_suz(d, engelli_fonk):
    """Rapor JSON'unda engelli depoları iç içe listelerden çıkarır."""
    n = 0
    if isinstance(d, dict):
        for v in d.values():
            n += _rapor_suz(v, engelli_fonk)
    elif isinstance(d, list):
        tut = []
        for it in d:
            if isinstance(it, dict) and (
                engelli_fonk(it.get("url", ""), it.get("slug", ""))
                or engelli_fonk(it.get("title", ""))
            ):
                n += 1
                continue
            n += _rapor_suz(it, engelli_fonk)
            tut.append(it)
        d[:] = tut
    return n


def _glossary_suz(d):
    """Rapor JSON'unun glossary alanından engelli terimleri çıkarır."""
    if not isinstance(d, dict) or "glossary" not in d:
        return 0
    g = d.get("glossary")
    if not isinstance(g, list):
        return 0
    yeni = [item for item in g if not (isinstance(item, dict) and terim_engelli_mi(item.get("term", "")))]
    n = len(g) - len(yeni)
    if n > 0:
        d["glossary"] = yeni
    return n


def uygula(dry=False):
    # ─── A) Keşif kayıtları takedown ───
    for k in kayitlar():
        s = k["slug"]
        print(f"· keşif: {s}")
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
        if os.path.exists(cat_yol):
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
            if not os.path.exists(yol):
                continue
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
            print(f"  {os.path.relpath(yol, ROOT)} keşif bağlantısı temizlendi")
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
            y = re.sub(r"\n\n## [^\n]+\n\n(?=\n)", "\n", y)
            print(f"  {os.path.relpath(yol, ROOT)} markdown satırı temizlendi")
            _yaz(yol, y, dry)

        # 5) sitemap
        sm = os.path.join(ROOT, "sitemap.xml")
        if os.path.exists(sm):
            t = open(sm, encoding="utf-8").read()
            y = re.sub(r"\s*<url>\s*<loc>https://trescout\.com(?:/[a-z]{2})?/discover/" + re.escape(s) + r"/</loc>.*?</url>", "", t, flags=re.S)
            if y != t:
                print("  sitemap.xml keşif girdisi temizlendi")
                _yaz(sm, y, dry)

        # 6) rapor JSON öğeleri
        for yol in glob.glob(os.path.join(ROOT, "reports", "*.json")):
            ham = open(yol, encoding="utf-8").read()
            if not ad.search(ham):
                continue
            d = json.loads(ham)
            n = _rapor_suz(d, lambda u, sl="": engelli_mi(url=u, slug=sl))
            if n:
                print(f"  {os.path.relpath(yol, ROOT)} −{n} öğe")
                _json_yaz(yol, d, dry, _girinti(ham), ham)

    # ─── B) Sözlük terimleri takedown ───
    engelli_sozluk = sozluk_terimleri()
    for t in sorted(engelli_sozluk):
        print(f"· sözlük: {t}")
        # 1) sayfalar ve .md
        for p in DILLER:
            for yol in (
                os.path.join(ROOT, p, "dictionary", t),
                os.path.join(ROOT, p, "dictionary", t + ".md"),
            ):
                if os.path.isdir(yol):
                    print(f"  sil {os.path.relpath(yol, ROOT)}/")
                    dry or shutil.rmtree(yol)
                elif os.path.exists(yol):
                    print(f"  sil {os.path.relpath(yol, ROOT)}")
                    dry or os.remove(yol)

        # 2) og görselleri
        for yol in glob.glob(os.path.join(ROOT, "assets", "dictionary", "og", t + ".webp")) + \
                glob.glob(os.path.join(ROOT, "assets", "dictionary", "og", t + "-*.webp")):
            print(f"  sil {os.path.relpath(yol, ROOT)}")
            dry or os.remove(yol)

        # 3) dictionary.json manifesti
        man_yol = os.path.join(ROOT, "assets", "dictionary", "dictionary.json")
        if os.path.exists(man_yol):
            ham_man = open(man_yol, encoding="utf-8").read()
            man = json.loads(ham_man)
            yeni_man = [m for m in man if not (terim_engelli_mi(m.get("slug")) or terim_engelli_mi(m.get("en")))]
            if len(yeni_man) != len(man):
                print(f"  dictionary.json −{len(man) - len(yeni_man)}")
                _json_yaz(man_yol, yeni_man, dry, 2, ham_man)

        # 4) damga, önbellek ve birlesmis.json
        t_rx = re.compile(r"\b" + re.escape(t) + r"\b", re.I)
        for yol in (
            glob.glob(os.path.join(ROOT, "assets", "dictionary", "*-damga.json")) +
            glob.glob(os.path.join(ROOT, "assets", "dictionary", "*-cache.json")) +
            glob.glob(os.path.join(ROOT, "assets", "discover", "*-cache.json")) +
            [os.path.join(ROOT, "assets", "dictionary", "birlesmis.json")]
        ):
            if not os.path.exists(yol):
                continue
            ham = open(yol, encoding="utf-8").read()
            if not t_rx.search(ham):
                continue
            d = json.loads(ham)
            if isinstance(d, dict):
                if "eslesme" in d and isinstance(d["eslesme"], dict):
                    es = {k: v for k, v in d["eslesme"].items() if not (t_rx.search(k) or t_rx.search(str(v)))}
                    d["eslesme"] = es
                    yeni = d
                else:
                    yeni = {k: v for k, v in d.items() if not (t_rx.search(k) or t_rx.search(json.dumps(v, ensure_ascii=False)))}
            elif isinstance(d, list):
                yeni = [x for x in d if not t_rx.search(json.dumps(x, ensure_ascii=False))]
            else:
                yeni = d
            print(f"  {os.path.relpath(yol, ROOT)} önbellek temizlendi")
            _json_yaz(yol, yeni, dry, _girinti(ham), ham)

        # 5) HTML bağlantı, kart ve JSON-LD DefinedTerm temizliği (dictionary/index.html, reports/*.html vb.)
        dict_a_rx = re.compile(r'<a\b[^>]*href="(?:/[a-z]{2})?/dictionary/' + re.escape(t) + r'/"[^>]*>.*?</a>\s*', re.S)
        ld_rx = re.compile(
            r'[\t ]*\{\s*"@type":\s*"DefinedTerm",\s*"name":\s*"[^"]*",\s*"url":\s*"https://trescout\.com(?:/[a-z]{2})?/dictionary/' +
            re.escape(t) + r'/"\s*\},?\n?',
            re.S
        )
        for yol in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True):
            if "/.git/" in yol or "/node_modules/" in yol:
                continue
            tekst = open(yol, encoding="utf-8").read()
            if f"/dictionary/{t}/" not in tekst:
                continue
            y = ld_rx.sub("", dict_a_rx.sub("", tekst))
            print(f"  {os.path.relpath(yol, ROOT)} sözlük bağlantısı temizlendi")
            _yaz(yol, y, dry)

        # 6) Markdown bağlantıları
        dict_md_rx = re.compile(r"^- \[[^\]]*\]\(https://trescout\.com(?:/[a-z]{2})?/dictionary/" + re.escape(t) + r"/\)\n", re.M)
        for yol in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True):
            if "/.git/" in yol or "/node_modules/" in yol or "/docs/" in yol:
                continue
            tekst = open(yol, encoding="utf-8").read()
            if f"/dictionary/{t}/" not in tekst:
                continue
            y = dict_md_rx.sub("", tekst)
            print(f"  {os.path.relpath(yol, ROOT)} sözlük satırı temizlendi")
            _yaz(yol, y, dry)

        # 7) sitemap
        sm = os.path.join(ROOT, "sitemap.xml")
        if os.path.exists(sm):
            tekst = open(sm, encoding="utf-8").read()
            y = re.sub(
                r"\s*<url>\s*<loc>https://trescout\.com(?:/[a-z]{2})?/dictionary/" + re.escape(t) + r"/</loc>.*?</url>",
                "",
                tekst,
                flags=re.S,
            )
            if y != tekst:
                print("  sitemap.xml sözlük girdisi temizlendi")
                _yaz(sm, y, dry)

    # 8) Rapor JSON glossary temizliği
    if engelli_sozluk:
        for yol in glob.glob(os.path.join(ROOT, "reports", "*.json")):
            ham = open(yol, encoding="utf-8").read()
            try:
                d = json.loads(ham)
            except Exception:
                continue
            n = _glossary_suz(d)
            if n:
                print(f"  {os.path.relpath(yol, ROOT)} −{n} glossary terimi")
                _json_yaz(yol, d, dry, _girinti(ham), ham)

    # 9) llms.txt yeniden üretimi
    if not dry:
        llms_script = os.path.join(ROOT, "scripts", "llms-txt.py")
        if os.path.exists(llms_script):
            print("· llms.txt yeniden üretiliyor...")
            subprocess.run([sys.executable, llms_script], check=True)

    print("Sonra: python3 scripts/check-kaldirilan.py")


if __name__ == "__main__":
    if "--uygula" in sys.argv:
        uygula(dry="--dry" in sys.argv)
    else:
        print(__doc__)
