#!/usr/bin/env python3
"""
Sözlükte YENİ ikiz terim arar · bulursa GitHub issue açar/günceller.

    python3 scripts/ikiz-tara.py [--dry]

Neden gerekli: `check-birlesmis-terimler.py` yalnız YAPILMIŞ birleşmeleri
koruyor · yenisini bulmuyor. Günlük hat her gün rapor sözlüğünden yeni terim
ekliyor ve tekil/çoğul ikizleri kendiliğinden oluşuyor. Mevcut birleşme tablosu
canonical kararların kaynağıdır. Benzer görünen her çift aynı anlama gelmeyebilir;
bağlam incelemesiyle ayrı tutulması kararlaştırılan çiftler
`assets/dictionary/duplicate-triage.json` içinde kayıtlıdır. Google, gerçekten
aynı içeriği taşıyan sayfaları "standart sayfa olmadan kopya" olarak işaretleyebilir.

Neden guard değil de issue: birleştirme bir İÇERİK kararı · hangi slug kalacak,
metin nasıl ayrışacak. Günlük hattı bunun için düşürmek yayını durdurur. Bu
betik bulguyu görünür kılıyor, kararı insana bırakıyor.

Ölçü: aynı kökten tekil/çoğul slug çifti + gövdelerinin benzerliği. Eşik 0.85 ·
altındakiler gerçekten farklı yazılmış demektir (ör. "agent" kavram,
"agents" çoklu-ajan sistemi anlatıyorsa sorun yok).

Birleştirme kararı verilince: `assets/dictionary/birlesmis.json`'a satır ekleyin,
sayfaları silin, `scripts/redirect-uret.py` çalıştırın.
"""
import difflib
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "assets", "dictionary", "dictionary.json")
BIRLESMIS = os.path.join(ROOT, "assets", "dictionary", "birlesmis.json")
TRIAGE = os.path.join(ROOT, "assets", "dictionary", "duplicate-triage.json")
ESIK = 0.85
TITLE = "Sözlük · birleştirilmesi gereken ikiz terimler"
DRY = "--dry" in sys.argv or not os.environ.get("GH_TOKEN")


def govde(slug):
    p = os.path.join(ROOT, "dictionary", slug, "index.html")
    if not os.path.exists(p):
        return ""
    m = re.search(r"<main[\s\S]*?</main>", open(p, encoding="utf-8").read())
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", m.group(0) if m else "")).strip()


man = json.load(open(MANIFEST, encoding="utf-8"))
sluglar = {t["slug"]: t for t in man}
zaten = set()
if os.path.exists(BIRLESMIS):
    e = json.load(open(BIRLESMIS, encoding="utf-8"))["eslesme"]
    zaten = set(e) | set(e.values())

# İnsan tarafından bağlamı incelenmiş ve ayrı tutulması kararlaştırılmış çiftler.
# Bu kayıt mapping değildir; URL/canonical davranışını değiştirmez.
incelenmis = set()
if os.path.exists(TRIAGE):
    for kayit in json.load(open(TRIAGE, encoding="utf-8")).get("incelenmis", []):
        cift = kayit.get("cift", [])
        if len(cift) == 2:
            incelenmis.add(tuple(sorted(cift)))

bulunan = []
gorulen = set()
for s in sluglar:
    for aday in (s + "s", s.rstrip("s")):
        if aday == s or aday not in sluglar:
            continue
        cift = tuple(sorted((s, aday)))
        if cift in gorulen or cift in incelenmis:
            continue
        gorulen.add(cift)
        a, b = cift
        ga, gb = govde(a), govde(b)
        if not (ga and gb):
            continue
        oran = difflib.SequenceMatcher(None, ga, gb).quick_ratio()
        if oran >= ESIK:
            bulunan.append((a, b, oran))

bulunan.sort(key=lambda x: -x[2])
print(f"{len(gorulen)} tekil/çoğul çifti tarandı · {len(bulunan)} ikiz eşiği aştı (≥{ESIK})")

# Aynı ada çıkan farklı slug'lar: kısaltma/açılım ikizleri (cv ↔ computer-vision, pkm ↔
# personal-knowledge-management). Tekil/çoğul taraması bunları görmüyordu (2026-10-16: sözlük
# dizininde üç çift aynı adla iki kart olarak duruyordu). Aynı ad aynı kavramdır; benzerlik eşiği
# aranmaz, oran bilgi için yazılır. Farklı anlam taşıyan kısaltma çakışması triage'a eklenir.
# DeepLearning.AI "Retrieval Augmented Generation" (bilgi tabanı hijyeni) · R5.
def adlar(t):
    return {re.sub(r"[^a-z0-9]+", " ", (t.get(k) or "").lower()).strip() for k in ("en", "full")} - {""}

ada_gore = {}
for s, t in sluglar.items():
    for ad in adlar(t):
        ada_gore.setdefault(ad, set()).add(s)
ayni_ad = []
for ad, grup in sorted(ada_gore.items()):
    for a in sorted(grup):
        for b in sorted(grup):
            cift = (a, b)
            if a >= b or cift in gorulen or cift in incelenmis:
                continue
            gorulen.add(cift)
            ga, gb = govde(a), govde(b)
            oran = difflib.SequenceMatcher(None, ga, gb).quick_ratio() if ga and gb else 0.0
            ayni_ad.append((a, b, oran, ad))
print(f"{len(ayni_ad)} aynı adlı (kısaltma/açılım) çift")
bulunan += [(a, b, o) for a, b, o, _ in ayni_ad]
for a, b, o in bulunan:
    isaret = " (biri zaten birleşme tablosunda!)" if (a in zaten or b in zaten) else ""
    print(f"   {a} ↔ {b} · benzerlik {o:.2f}{isaret}")

if not bulunan:
    print("✓ yeni ikiz yok")
    sys.exit(0)

satirlar = [
    "Sözlükte aynı metni taşıyan tekil/çoğul ya da aynı adlı (kısaltma/açılım) terim çiftleri bulundu. Google bunlara",
    '"kullanıcı tarafından seçilen standart sayfa olmadan kopya" diyor ve birini dizinden düşürüyor.',
    "",
    f"Tekil/çoğul çiftlerde eşik: gövde benzerliği ≥ {ESIK}. Aynı adlı çiftler eşiksiz listelenir (aynı ad aynı kavram); farklı anlamdaysa `duplicate-triage.json`'a ekleyin.",
    "",
]
for a, b, o in bulunan:
    satirlar.append(
        f"- [ ] **{a}** ↔ **{b}** · benzerlik {o:.2f} · "
        f"[{a}](https://trescout.com/dictionary/{a}/) · "
        f"[{b}](https://trescout.com/dictionary/{b}/)"
    )
satirlar += [
    "",
    "**Nasıl birleştirilir**",
    "1. Kalacak slug'ı seçin (iç bağlantı sayısı > gövde zenginliği > kısa slug)",
    "2. `assets/dictionary/birlesmis.json` → `eslesme`'ye `\"giden\": \"kalan\"` ekleyin",
    "3. Giden slug'ın tüm yapılandırılmış dil sayfalarını silin (`dictionary/`, locale dizinleri · `.md` dahil)",
    "4. `python3 scripts/redirect-uret.py` · 301'leri üretir",
    "5. İç bağlantıları kanonik adrese çevirin, sayfaları yeniden basın",
    "6. `python3 scripts/check-birlesmis-terimler.py` yeşil olmalı",
    "",
    "**Alternatif:** ikisini gerçekten farklı anlamlarla yeniden yazmak da olur "
    "(ör. tekil = kavram, çoğul = sistem). O zaman benzerlik eşiğin altına iner ve liste temizlenir.",
]
body = "\n".join(satirlar)

if DRY:
    print("\n[dry / GH_TOKEN yok] açılacak issue gövdesi:\n")
    print("BAŞLIK:", TITLE, "\n")
    print(body)
    sys.exit(0)

num = None
try:
    out = subprocess.run(["gh", "issue", "list", "--state", "open", "--search", TITLE,
                          "--json", "number,title"], capture_output=True, text=True,
                         cwd=ROOT, check=True)
    for it in json.loads(out.stdout or "[]"):
        if it.get("title") == TITLE:
            num = it["number"]
            break
except Exception as e:
    print("uyarı: mevcut issue aranamadı:", e)

if num:
    subprocess.run(["gh", "issue", "edit", str(num), "--body", body], cwd=ROOT, check=True)
    print(f"issue #{num} güncellendi · {len(bulunan)} ikiz")
else:
    subprocess.run(["gh", "issue", "create", "--title", TITLE, "--body", body], cwd=ROOT, check=True)
    print(f"yeni issue açıldı · {len(bulunan)} ikiz")
