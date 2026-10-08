"""Üretilen çeviri sayfası mevcut sayfayı ZAYIFLATMASIN.

2026-09-27 · hat 19 Eylül'den beri ilk kez push etti ve dictionary-en.py 40
çeviri sözlük sayfasını ezdi. 25 Eylül'de elle/ajanla zenginleştirilmiş sayfalar
(etimoloji, teknik derinlik, sık hatalar...) üreticinin tanımadığı bölümler
taşıyordu; üretici onları hiç çevirmedi, çevrilecek metin kalmadığı için "çeviri
eksik" koruması da devreye girmedi ve en/dictionary/llm, rag, transformer gibi
sayfalar 7 bölümden 1'e düştü.

Kural: diskte bir sayfa varsa, yeni çıktı ondan daha az bölüm (<h2>) taşıyorsa ya
da ana metni %40'tan fazla kısalıyorsa yazılmaz, mevcut hali korunur. Çağıran
loglar. Bedeli: elle zenginleştirilmiş çeviri sayfaları üreticiden güncelleme
almaz, elle bakılır.

2026-10-03 · ÜRETİCİ DAMGASI. Miktar kuralı yetmedi: #281'den sonra çeviri tam
bölüm oldu, aynı bölüm sayısında ve benzer uzunluktaki makine çevirisi elle
düzeltilmiş başlık/ifadeleri ezdi (168 sayfa; 15'i #255'te bir kez geri
yüklenmişti). Artık köken ölçülüyor: üretici yazdığı her sayfanın içerik
damgasını assets/<tur>/<dil>-damga.json'a kaydeder. Diskteki sayfanın damgası
kayıtla tutmuyorsa (ya da kayıt yoksa) sayfa elle düzenlenmiştir, üretilmez.
zayiflatir() üretici-sahipli sayfalarda ikinci kat olarak kalır.

Damgaya GİRMEYEN bölgeler (buralardaki elle düzenleme korunmaz, toplu yönetilir):
nav/footer/<head> (hreflang, og:, JSON-LD), ilgili çip kutuları (ilgili-temizle.py),
kayıt/rıza formu (diller.py, check-consent-consistency.py) ve makine çevirisi notu.

Frenler: toplu donma (damga dosyası silinir/bozulursa) ve kayma (KAYMA_ESIGI, eskimiş
damga) koşuyu kırmızıya döndürür; sayfalar sessizce donmaz.

Bakım: python3 scripts/sayfa_koruma.py --liste            korunan sayfalar
        python3 scripts/sayfa_koruma.py --birak en/dictionary/rag   üreticiye bırak
        python3 scripts/sayfa_koruma.py --baslat [--dry]   damgaları git geçmişinden kur
"""
import hashlib
import json
import os
import re
import subprocess
import sys

_KABUK = re.compile(r"<(nav|footer|script|svg)[\s\S]*?</\1>")
_BASLIK = re.compile(r"<h2[^>]*>")
ASGARI_METIN_ORANI = 0.6


def _olcu(html):
    govde = _KABUK.sub("", html)
    ana = (govde.split("<main", 1) + [""])[1].split("</main>")[0] or govde
    kelime = len(re.sub(r"<[^>]+>", " ", ana).split())
    return len(_BASLIK.findall(govde)), kelime


def zayiflatir(yeni_html, mevcut_yol, kaynak_yol=None):
    """Yeni çıktı mevcut sayfayı zayıflatıyorsa gerekçe döner, yoksa None.

    kaynak_yol: Türkçe kaynak sayfa. Yeni çıktı kaynağın bölüm sayısına
    ulaşıyorsa küçülme meşrudur (kaynak yeniden işlenip kısalmış), engellenmez.
    2026-09-28: archify yeniden işlendi, Türkçesi 7 → 6 bölüm oldu; koruma
    6 bölümlük çevirileri engelledi, eski 7 bölümlük sayfalar kaldı ve bölüm
    paritesi guard'ı "fazla bölüm" diye düştü.
    """
    if not os.path.exists(mevcut_yol):
        return None
    try:
        eski = open(mevcut_yol, encoding="utf-8").read()
    except OSError:
        return None
    eski_bolum, eski_kelime = _olcu(eski)
    yeni_bolum, yeni_kelime = _olcu(yeni_html)
    # Kaynağın bölüm sayısına ulaşan çıktı için YALNIZ bölüm kuralı esner;
    # metin kuralı her zaman geçerli (elle zenginleştirilmiş, Türkçesinden uzun
    # çeviri sayfası daha kısa bir makine çevirisiyle ezilmesin).
    kaynak_yeterli = False
    if kaynak_yol and os.path.exists(kaynak_yol):
        try:
            kaynak_bolum, _ = _olcu(open(kaynak_yol, encoding="utf-8").read())
            kaynak_yeterli = yeni_bolum >= kaynak_bolum
        except OSError:
            pass
    if yeni_bolum < eski_bolum and not kaynak_yeterli:
        return f"bölüm {eski_bolum}→{yeni_bolum}"
    if eski_kelime and yeni_kelime < eski_kelime * ASGARI_METIN_ORANI:
        return f"metin {eski_kelime}→{yeni_kelime} kelime"
    return None


# ---------- üretici damgası ----------
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TURLER = ("dictionary", "discover")
BOT_EPOSTA = {"hello@trescout.com", "bot@trescout.com"}  # TreScout Bot, trescout-bot
_OZET = (re.compile(r"<main\b.*?</main>", re.S), re.compile(r"<title>.*?</title>", re.S),
         re.compile(r'<meta name="description"[^>]*>'))
_KALIP = re.compile(
    r'<section class="disc-sec">\s*<h2>[^<]*</h2>\s*<div class="(?:dict|disc)-related">.*?</div>\s*</section>\n?[ \t]*'  # ilgili-temizle.py
    r'|<form[^>]*class="[^"]*js-subscribe[^"]*"[\s\S]*?</form>'  # check-consent-consistency.py FORM_DESEN ikizi
    r'|<p class="disc-disclaimer">.*?</p>', re.S)


def icerik_damgasi(html):
    """<main> + <title> + meta description, kalıp bloklar hariç (sitemap-sync.py icerik_ozeti ikizi)."""
    ozet = "".join(m.group(0) for m in (p.search(html) for p in _OZET) if m)
    return hashlib.sha256(_KALIP.sub("", ozet).encode("utf-8")).hexdigest()[:16]


def damga_yolu(tur, dil):
    return os.path.join(ROOT, "assets", tur, f"{dil}-damga.json")


def damgalar(yol):
    """Dosya yoksa {} (yeni dil). Bozuk JSON sessizce {} dönmez, düşer: o dilin tüm
    sayfaları korunur görünüp donmasın."""
    if not os.path.exists(yol):
        return {}
    return json.load(open(yol, encoding="utf-8"))


def damga_yaz(yol, d):
    """Atomik: süre sınırında öldürülen süreç yarım JSON bırakıp ertesi koşuyu düşürmesin."""
    gecici = yol + ".tmp"
    with open(gecici, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")
    os.replace(gecici, yol)


def elle_duzenlenmis(sayfa_yolu, damga):
    """Sayfa diskte varsa ve damgası üreticinin son yazdığıyla tutmuyorsa True."""
    try:
        html = open(sayfa_yolu, encoding="utf-8").read()
    except OSError:
        return False  # sayfa yok · üretilir
    if "</main>" not in html:
        return False  # yarım yazılmış sayfa korunmaz, onarılır
    return damga is None or icerik_damgasi(html) != damga


# KAYMA FRENİ · 2026-10-08: #286 bir gün beklerken bot 390 keşif sayfasını yeniden
# üretti, damgalar eskide kaldı. Öyle merge edilseydi bu sayfalar "elle" sayılıp
# donacaktı; toplu donma freni (dil başına max(50, %25) ≈ 155) dizin başına 78'i
# yakalamıyordu. Damgası KAYITLI ama tutmayan sayfa ayrı sayılır: meşru elle içerik
# düzenlemesi dizin başına ~10 sayfa (geçmiş commit'ler; nav/hreflang gibi toplu
# değişiklikler damgaya girmez), eskimiş damga ise onlarca sayfa.
KAYMA_ESIGI = 25


def kayma_freni(kayma, tur, dil):
    """Damgası kayıtlı ama tutmayan sayfa sayısı eşiği aşarsa gerekçe döner, yoksa None."""
    if kayma <= KAYMA_ESIGI:
        return None
    return (f"✗ {dil}/{tur} · {kayma} sayfanın damgası kayıtlı ama tutmuyor (eşik {KAYMA_ESIGI}) · "
            f"damgalar eskimiş olabilir (üretici dışında toplu <main>/title/description değişikliği ya da "
            f"damga dosyası güncellenmeden yapılan merge). Kontrol: python3 scripts/sayfa_koruma.py --baslat --dry · "
            f"değişiklikler bot'unsa ya da kasıtlı elle düzenlemeyse --baslat ile damgaları yenileyin")


def _sayfalar():
    """(tur, dil, slug, yol) · diller.py'deki her çeviri dili."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from diller import DILLER
    for dil in DILLER:
        for tur in TURLER:
            kok = os.path.join(ROOT, dil, tur)
            if not os.path.isdir(kok):
                continue
            for slug in sorted(os.listdir(kok)):
                yol = os.path.join(kok, slug, "index.html")
                if os.path.isfile(yol):
                    yield tur, dil, slug, yol


def baslat(dry):
    """Her çeviri sayfası için içerik damgasını DEĞİŞTİREN son commit'i bulur. O
    commit bot commit'iyse ve disk hâlâ o içerikteyse damga basılır; değilse sayfa
    elle sayılır. Yalnız nav/hreflang/çip/form değiştiren commit'ler sayılmaz."""
    if subprocess.check_output(["git", "rev-parse", "--is-shallow-repository"], cwd=ROOT, text=True).strip() == "true":
        sys.exit("✗ sığ klon · önce `git fetch --unshallow`")
    sayfalar = list(_sayfalar())
    yollar = {os.path.relpath(y, ROOT).replace(os.sep, "/"): (t, d, s) for t, d, s, y in sayfalar}
    dizinler = sorted({f"{d}/{t}" for t, d, _, _ in sayfalar})
    log = subprocess.check_output(["git", "log", "--format=%x00%H%x09%ae", "--raw", "--no-abbrev",
                                   "--no-renames", "--no-merges", "HEAD", "--", *dizinler], cwd=ROOT, text=True)
    gecmis = {}  # yol → [(commit, eposta, eski_blob, yeni_blob)] yeniden eskiye
    commit = eposta = None
    for satir in log.splitlines():
        if satir.startswith("\x00"):
            commit, eposta = satir[1:].split("\t")
        elif satir.startswith(":"):
            bilgi, yol = satir.split("\t", 1)
            if yol in yollar:
                p = bilgi.split()
                gecmis.setdefault(yol, []).append((commit, eposta, p[2], p[3]))
    cat = subprocess.Popen(["git", "cat-file", "--batch"], cwd=ROOT, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    onbellek = {}

    def blob_damga(sha):
        if set(sha) == {"0"}:
            return None  # dosya yok (eklenme öncesi)
        if sha not in onbellek:
            cat.stdin.write(f"{sha}\n".encode())
            cat.stdin.flush()
            n = int(cat.stdout.readline().split()[2])
            onbellek[sha] = icerik_damgasi(cat.stdout.read(n).decode("utf-8", "replace"))
            cat.stdout.read(1)
        return onbellek[sha]

    yeni = {}
    elle = {}  # commit → [yol]
    for yol, (tur, dil, slug) in sorted(yollar.items()):
        disk = icerik_damgasi(open(os.path.join(ROOT, yol), encoding="utf-8").read())
        sahip = None
        for c, e, eski, yeni_blob in gecmis.get(yol, []):
            if blob_damga(eski) != blob_damga(yeni_blob):
                sahip = (c, e, blob_damga(yeni_blob))
                break
        if sahip and sahip[1] in BOT_EPOSTA and sahip[2] == disk:
            yeni.setdefault((tur, dil), {})[slug] = disk
        else:
            elle.setdefault(sahip[0][:10] if sahip else "geçmişsiz", []).append(yol)
    cat.stdin.close()
    toplam = sum(len(v) for v in yeni.values())
    print(f"damga · {len(yollar)} çeviri sayfası · üretici-sahipli {toplam} · elle {sum(len(v) for v in elle.values())}")
    for c, ys in sorted(elle.items(), key=lambda x: -len(x[1])):
        konu = "" if c == "geçmişsiz" else subprocess.check_output(["git", "log", "-1", "--format=%an · %s", c], cwd=ROOT, text=True).strip()
        print(f"  elle {len(ys):4} · {c} {konu[:90]}")
    if dry:
        print("[--dry] yazılmadı.")
        return
    from diller import DILLER
    for dil in DILLER:
        for tur in TURLER:
            if os.path.isdir(os.path.join(ROOT, dil, tur)):
                damga_yaz(damga_yolu(tur, dil), yeni.get((tur, dil), {}))
    print("✅ damga dosyaları yazıldı")


def liste():
    """Korunan (elle) sayfalar · h2 sayısı Türkçesiyle yan yana. Sığ klonda çalışır."""
    say, okunan = 0, {}
    for tur, dil, slug, yol in _sayfalar():
        if (tur, dil) not in okunan:
            okunan[(tur, dil)] = damgalar(damga_yolu(tur, dil))
        if not elle_duzenlenmis(yol, okunan[(tur, dil)].get(slug)):
            continue
        say += 1
        h2 = len(_BASLIK.findall(open(yol, encoding="utf-8").read()))
        tr = os.path.join(ROOT, tur, slug, "index.html")
        tr_h2 = len(_BASLIK.findall(open(tr, encoding="utf-8").read())) if os.path.exists(tr) else "-"
        print(f"  {dil}/{tur}/{slug}  h2 {h2} · tr {tr_h2}")
    print(f"{say} korunan çeviri sayfası")


def birak(hedefler):
    """Sayfanın ŞU ANKİ damgasını kaydeder · üretici ertesi koşuda yeniden üretir.
    Yalnız açıkça verilen <dil>/<tur>/<slug> yolları (toplu bırakma yok). Türkçesinden
    fazla bölüm taşıyan sayfayı zayiflatir() yine yazdırmayabilir."""
    for h in hedefler:
        p = h.strip("/").split("/")
        if len(p) != 3 or p[1] not in TURLER or "*" in h:
            sys.exit(f"✗ {h}: <dil>/<dictionary|discover>/<slug> biçiminde olmalı")
        dil, tur, slug = p
        yol = os.path.join(ROOT, dil, tur, slug, "index.html")
        if not os.path.isfile(yol):
            sys.exit(f"✗ {h}: sayfa yok")
        dy = damga_yolu(tur, dil)
        d = damgalar(dy)
        d[slug] = icerik_damgasi(open(yol, encoding="utf-8").read())
        damga_yaz(dy, d)
        print(f"✅ {h} üreticiye bırakıldı")


if __name__ == "__main__":
    if "--baslat" in sys.argv:
        baslat("--dry" in sys.argv)
    elif "--liste" in sys.argv:
        liste()
    elif "--birak" in sys.argv:
        birak([a for a in sys.argv[1:] if not a.startswith("--")])
    else:
        sys.exit(__doc__)
