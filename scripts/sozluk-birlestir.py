#!/usr/bin/env python3
"""
Sözlük ikizlerini birleştirir · kaynak: assets/dictionary/birlesmis.json (giden → kalan).

2026-10-16 · ikiz taraması aynı adlı kısaltma/açılım çiftlerini buldu (ab, cv, mcp ×3, pkm, stt).
Karar Burhan'ın verdiği yetkiyle verildi; kalan slug birlesmis.json'daki kuralla seçildi (iç
bağlantı sayısı > gövde uzunluğu > kısa slug). Önceki birleşme (#95) elle 426 dosyalık bir PR'dı;
günlük bot commit'leriyle çakışmasın diye uygulama içerik hattında (dict-sync.yml) her koşuda
çalışır, iş kalmadıysa hiçbir dosyaya dokunmaz:

  1. gidenin 6 dilde sayfası, .md'si ve kart görseli silinir
  2. manifestten çıkar; kalanın `full` alanı boşsa gidenin kısaltması yazılır (STT, CV, PKM:
     site araması ve özetleyici dayanağı terimi kısaltmasıyla da bulsun)
  3. çeviri damgalarından gidenin kaydı silinir
  4. dizin sayfalarında gidenin kartı ve JSON-LD DefinedTerm kaydı silinir (kalanınki zaten var);
     kalan html/md/txt/xml'de `/dictionary/giden/` ve `/dictionary/giden.md` kalana çevrilir;
     değişen üretilmiş sayfanın damgası değişiklikten önce tutuyorsa yenilenir (yoksa sayfa
     "elle düzenlenmiş" sayılıp donar, bkz. sayfa_koruma.py)

Hat bu adımdan sonra çapraz bağlantıları, dizinleri, yönlendirmeleri, .md'leri, sitemap'i ve
llms.txt'yi zaten yeniden üretir; check-birlesmis-terimler.py en sonda sıkı denetler.

Kullanım: python3 scripts/sozluk-birlestir.py --uygula [--dry]
          python3 scripts/sozluk-birlestir.py            (yapılacak işi sayar, dokunmaz)
"""
import glob
import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sayfa_koruma import damgalar, damga_yaz, damga_yolu, icerik_damgasi  # noqa: E402

BIRLESMIS = os.path.join(ROOT, "assets", "dictionary", "birlesmis.json")
MANIFEST = os.path.join(ROOT, "assets", "dictionary", "dictionary.json")
DILLER = ["", "en/", "de/", "fr/", "es/", "pt/"]
DAMGALI = ["en", "de", "fr", "es", "pt"]
SAYFA = re.compile(r"^(?:(en|de|fr|es|pt)/)?(dictionary|discover)/([^/]+)/index\.html$")


def eslesme():
    return json.load(open(BIRLESMIS, encoding="utf-8"))["eslesme"]


def kisaltma(giden, kayit):
    """Gidenin kısaltması: büyük harfli `en` (STT) ya da kısa slug (cv → CV)."""
    en = (kayit or {}).get("en", "")
    if re.fullmatch(r"[A-Z0-9]{2,6}", en):
        return en
    if re.fullmatch(r"[a-z]{2,5}", giden):
        return giden.upper()
    return ""


def dosyalar():
    for yol in glob.glob(os.path.join(ROOT, "**", "*"), recursive=True):
        rel = os.path.relpath(yol, ROOT)
        if rel.startswith((".git", "node_modules", "docs" + os.sep)) or not os.path.isfile(yol):
            continue
        if rel.endswith((".html", ".md", ".txt", ".xml")):
            yield yol, rel


def bekleyen(es, man):
    """Henüz uygulanmamış giden slug'lar (manifestte ya da diskte duruyor)."""
    sluglar = {t["slug"] for t in man}
    return sorted(g for g in es if g in sluglar or any(
        os.path.exists(os.path.join(ROOT, d, "dictionary", g)) for d in DILLER))


def uygula(dry):
    es = eslesme()
    ham_man = open(MANIFEST, encoding="utf-8").read()
    man = json.loads(ham_man)
    isler = bekleyen(es, man)
    if not isler:
        print("✓ birleştirilecek ikiz kalmadı")
        return 0
    print(f"· {len(isler)} giden slug: {', '.join(f'{g} → {es[g]}' for g in isler)}")

    # 1) sayfalar, .md, kart görselleri
    for g in isler:
        for d in DILLER:
            for yol in (os.path.join(ROOT, d, "dictionary", g), os.path.join(ROOT, d, "dictionary", g + ".md")):
                if os.path.isdir(yol):
                    print(f"  sil {os.path.relpath(yol, ROOT)}/")
                    dry or shutil.rmtree(yol)
                elif os.path.exists(yol):
                    print(f"  sil {os.path.relpath(yol, ROOT)}")
                    dry or os.remove(yol)
        for yol in glob.glob(os.path.join(ROOT, "assets", "dictionary", "og", g + ".webp")) + \
                glob.glob(os.path.join(ROOT, "assets", "dictionary", "og", g + "-*.webp")):
            print(f"  sil {os.path.relpath(yol, ROOT)}")
            dry or os.remove(yol)

    # 2) manifest · kalanın boş `full` alanına gidenin kısaltması
    kayit = {t["slug"]: t for t in man}
    for g in isler:
        kalan = kayit.get(es[g])
        k = kisaltma(g, kayit.get(g))
        if kalan is not None and not kalan.get("full") and k and k.lower() != kalan.get("en", "").lower():
            kalan["full"] = k
            print(f"  {es[g]}: full = {k!r}")
    yeni_man = [t for t in man if t["slug"] not in es]
    print(f"  dictionary.json −{len(man) - len(yeni_man)}")
    if not dry:
        with open(MANIFEST, "w", encoding="utf-8") as f:
            json.dump(yeni_man, f, ensure_ascii=False, indent=2)
            f.write("\n" if ham_man.endswith("\n") else "")

    # 3) + 4) damgalar ve bağlantılar
    damga = {(tur, dil): damgalar(damga_yolu(tur, dil)) for tur in ("dictionary", "discover") for dil in DAMGALI}
    degisen_damga = set()
    for dil in DAMGALI:
        for g in isler:
            if g in damga[("dictionary", dil)]:
                del damga[("dictionary", dil)][g]
                degisen_damga.add(("dictionary", dil))
    rx = re.compile(r"/dictionary/(" + "|".join(map(re.escape, isler)) + r")(/|\.md)")
    adlar = "|".join(map(re.escape, isler))
    kart_rx = re.compile(r'<a class="dict-card"[^>]*href="(?:/[a-z]{2})?/dictionary/(?:' + adlar + r')/"[^>]*>.*?</a>\s*', re.S)
    ld_rx = re.compile(r'[\t ]*\{\s*"@type":\s*"DefinedTerm",\s*"name":\s*"[^"]*",\s*"url":\s*"https://trescout\.com'
                       r'(?:/[a-z]{2})?/dictionary/(?:' + adlar + r')/"\s*\},?\n?', re.S)
    duzelen = 0
    for yol, rel in dosyalar():
        t = open(yol, encoding="utf-8").read()
        if "/dictionary/" not in t or not rx.search(t):
            continue
        y = rx.sub(lambda m: f"/dictionary/{es[m.group(1)]}{m.group(2)}", ld_rx.sub("", kart_rx.sub("", t)))
        m = SAYFA.match(rel.replace(os.sep, "/"))
        if m and m.group(1):
            d = damga[(m.group(2), m.group(1))]
            if d.get(m.group(3)) == icerik_damgasi(t):
                d[m.group(3)] = icerik_damgasi(y)
                degisen_damga.add((m.group(2), m.group(1)))
        if not dry:
            with open(yol, "w", encoding="utf-8") as f:
                f.write(y)
        duzelen += 1
    print(f"  {duzelen} dosyada bağlantı kalana çevrildi")
    if not dry:
        for tur, dil in sorted(degisen_damga):
            damga_yaz(damga_yolu(tur, dil), damga[(tur, dil)])
    print(f"  {len(degisen_damga)} damga dosyası güncellendi")
    return 0


if __name__ == "__main__":
    if "--uygula" in sys.argv:
        sys.exit(uygula("--dry" in sys.argv))
    es = eslesme()
    isler = bekleyen(es, json.load(open(MANIFEST, encoding="utf-8")))
    print(f"{len(isler)} giden slug uygulanmayı bekliyor" + (f": {', '.join(isler)}" if isler else ""))
