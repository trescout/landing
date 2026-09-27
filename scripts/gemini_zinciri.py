"""Gemini model zinciri · landing'deki tüm Python Gemini çağrılarının tek girişi.

Free tier'da kota MODEL BAŞINA tutuluyor. Zincir en iyi modelden başlar, onun
günlük kotası bitince sıradakine geçer. Sıra KALİTEYE göre; kapasite sıradan
bağımsız (toplam ~1120 istek/gün). Limitler AI Studio Rate Limit tablosu
(2026-09-27, free tier):
  3.8 / 3.7 / 3.6 / 3.5 Flash  · 5 RPM / 20 RPD   (günde 80)
  3.5 Flash-Lite               · 15 RPM / 500 RPD  · Google: "3 Flash'ı birçok
                                 değerlendirmede geçiyor", 2.5 ve 3 Flash
                                 iş yüklerine alternatif (blog, 3.6 duyurusu)
  3 Flash (preview), 2.5 Flash · 5 RPM / 20 RPD   (günde 40)
  3.1 Flash-Lite               · 15 RPM / 500 RPD  · en zayıf, en sonda
Günlük normal hacim ~80-150 istek (5 dil): çoğu gün ilk dört Flash + 3.5 Lite ile
biter; 3 Flash, 2.5 Flash ve 3.1 Lite yalnız birikmiş iş günlerinde devreye girer.

Zincir öğesi "model:rpm" biçiminde · rpm istekler arası aralığı belirler
(60/rpm sn). Günlük limiti koda gömmüyoruz: hangi hesabın anahtarı kullanılırsa
kullanılsın, kotanın bittiği yanıttan anlaşılır.

Hata sınıfları (https://ai.google.dev/gemini-api/docs/api-errors):
- günlük kota (429 quota_exceeded / "PerDay") ve model yok (404) ya da modele
  erişim yok (403) → model bu koşuda bırakılır, sıradakine geçilir
- anahtar/hesap (401 kimlik, 402 kredi, 400 FAILED_PRECONDITION, API_KEY_INVALID)
  → hiçbir model çalışmaz, Gemini bu koşuda kapatılır
- geçici (429 dakikalık, 408, 500, 503, 504, ağ) → beklenip aynı modelle denenir
- istek hatası (400 INVALID_ARGUMENT) → bu istek başarısız, model kalır
- 200 ama engellendi / yarıda kesildi (blockReason, finishReason != STOP) →
  bu istek başarısız sayılır; yarım çeviri asla dönmez
Aynı model üst üste _ART_ARDA_SINIR kez başarısız olursa (sınıf ne olursa olsun)
bırakılır · bilinmeyen bir hata biçimi koşuyu saatlerce oyalamasın.

Zincir: GEMINI_MODELS (virgülle) > GEMINI_MODEL / TREESCOUT_TRANSLATION_MODEL
(tek model, geriye uyum) > varsayılan.
"""

import datetime
import json
import os
import re
import tempfile
import time
import urllib.error
import urllib.request

VARSAYILAN_ZINCIR = ("gemini-3.8-flash:5,gemini-3.7-flash:5,gemini-3.6-flash:5,gemini-3.5-flash:5,"
                     "gemini-3.5-flash-lite:15,"
                     "gemini-3-flash-preview:5,gemini-2.5-flash:5,"
                     "gemini-3.1-flash-lite:15")


def _zincir_coz(metin: str) -> list[tuple[str, float]]:
    zincir = []
    for oge in metin.split(","):
        oge = oge.strip()
        if not oge:
            continue
        model, _, rpm = oge.partition(":")
        zincir.append((model.strip(), float(rpm) if rpm.strip() else 15.0))
    return zincir


ZINCIR = _zincir_coz(
    os.environ.get("GEMINI_MODELS")
    or os.environ.get("GEMINI_MODEL")
    or os.environ.get("TREESCOUT_TRANSLATION_MODEL")
    or VARSAYILAN_ZINCIR
)
MODELLER = [m for m, _ in ZINCIR]
_RPM = dict(ZINCIR)

_ART_ARDA_SINIR = 3
ASGARI_CIKTI = 8192

# Biten modeller süreçler arasında paylaşılır · dict-sync günde ~20 ayrı süreç
# başlatıyor; her biri zincire baştan başlasaydı kotası bitmiş her Flash'ı bir
# kez daha dener (günde ~120 boş istek, 12 sn aralıkla ~25 dk). Kota Pasifik
# gece yarısı sıfırlandığı için kayıt o güne ait. Dosya repo DIŞINDA
# (dict-sync `git add -A` ile commit'lemesin).
DURUM_DOSYASI = os.environ.get("GEMINI_ZINCIR_DURUM") or os.path.join(
    os.environ.get("RUNNER_TEMP") or tempfile.gettempdir(), "trescout-gemini-zinciri.json")


def _kota_gunu() -> str:
    try:
        from zoneinfo import ZoneInfo
        return datetime.datetime.now(ZoneInfo("America/Los_Angeles")).date().isoformat()
    except Exception:
        return (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=8)).date().isoformat()


def _durum_oku() -> set[str]:
    try:
        with open(DURUM_DOSYASI, encoding="utf-8") as f:
            d = json.load(f)
        return set(d.get("bitenler") or []) if d.get("gun") == _kota_gunu() else set()
    except Exception:
        return set()


def _durum_yaz(model: str) -> None:
    try:
        bitenler = _durum_oku() | {model}
        with open(DURUM_DOSYASI, "w", encoding="utf-8") as f:
            json.dump({"gun": _kota_gunu(), "bitenler": sorted(bitenler)}, f)
    except Exception:
        pass  # durum dosyası yalnız hız kazancı; yazılamazsa zincir yine çalışır


_bitenler: set[str] = _durum_oku() & set(MODELLER)
if _bitenler:
    import sys as _sys
    print(f"  · Gemini: bugün kotası biten modeller atlanıyor ({', '.join(sorted(_bitenler))})", file=_sys.stderr, flush=True)
_art_arda_hata: dict[str, int] = {}
_kapali = False
_son_istek = 0.0


def aktif_model() -> str | None:
    """Zincirde bırakılmamış ilk model · hepsi bittiyse ya da Gemini kapalıysa None."""
    if _kapali:
        return None
    return next((m for m in MODELLER if m not in _bitenler), None)


def _birak(model: str, neden: str, kalici: bool = True) -> None:
    _bitenler.add(model)
    if kalici:
        _durum_yaz(model)
    sonraki = aktif_model()
    devam = f"{sonraki} ile devam" if sonraki else "zincirde model kalmadı, Gemini bu koşuda kapalı"
    print(f"  ! Gemini {model}: {neden} · {devam}", flush=True)


def _kapat(neden: str) -> None:
    global _kapali
    if not _kapali:
        _kapali = True
        print(f"  ! Gemini kapatıldı: {neden} · anahtar/hesap sorunu, hiçbir model denenmeyecek", flush=True)


def _basarisiz(model: str) -> None:
    _art_arda_hata[model] = _art_arda_hata.get(model, 0) + 1
    if _art_arda_hata[model] >= _ART_ARDA_SINIR and model not in _bitenler:
        # Kalıcı değil: sebep kota değil, ertesi süreç modeli yeniden denesin
        _birak(model, f"üst üste {_ART_ARDA_SINIR} başarısız istek", kalici=False)


def _bekle_sira(model: str) -> None:
    global _son_istek
    aralik = float(os.environ.get("GEMINI_MIN_INTERVAL") or (60.0 / _RPM.get(model, 15.0)) * 1.05)
    kalan = _son_istek + aralik - time.time()
    if kalan > 0:
        time.sleep(kalan)
    _son_istek = time.time()


def _gecikme(error: urllib.error.HTTPError, govde: str, deneme: int) -> float:
    header = error.headers.get("Retry-After") if error.headers else None
    if header:
        try:
            return min(max(float(header), 1.0), 90.0)
        except ValueError:
            pass
    m = re.search(r'"retryDelay"\s*:\s*"([0-9.]+)s"', govde)
    if m:
        return min(max(float(m.group(1)), 1.0), 90.0)
    return min(5.0 * (deneme + 1), 60.0)


def siniflandir(kod: int, govde: str) -> str:
    """HTTP hatasını sınıflandır: gunluk | model | anahtar | gecici | istek."""
    if kod == 429:
        if re.search(r"PerDay|quota_exceeded|daily quota", govde, re.I):
            return "gunluk"
        return "gecici"
    # Anahtar kontrolü 403'ten önce: sızdırılmış anahtar 403 + "leaked" döner,
    # "model" sayılsaydı zincirdeki her model boşuna denenirdi.
    if kod in (401, 402) or re.search(r"API_KEY_INVALID|FAILED_PRECONDITION|failed_precondition|leaked", govde):
        return "anahtar"
    if kod in (404, 403):
        return "model"
    if kod in (408, 500, 502, 503, 504):
        return "gecici"
    return "istek"


def istek(body: dict, key: str, timeout: float = 90, deneme_sayisi: int = 4) -> dict | None:
    """generateContent'i zincir üzerinden çağırır; kullanılabilir yanıt JSON'u ya da None.

    None: istek başarısız, tüm modeller bitti ya da Gemini kapalı. Çağıran,
    None'da aynı isteği tekrar denememeli (sonuç değişmez).
    """
    if not key:
        return None
    # Flash ailesinde düşünme varsayılan açık (medium) ve düşünme token'ları
    # maxOutputTokens'a sayılıyor (ai.google.dev/gemini-api/docs/thinking).
    # Küçük sınır (ör. başlıkta 64) cevaba yer bırakmıyor, MAX_TOKENS ile boş
    # dönüyordu. thinkingLevel göndermiyoruz: modeller arasında destek tutarsız.
    ayar = dict(body.get("generationConfig") or {})
    ayar["maxOutputTokens"] = max(int(ayar.get("maxOutputTokens") or 0), ASGARI_CIKTI)
    veri = json.dumps({**body, "generationConfig": ayar}, ensure_ascii=False).encode("utf-8")
    deneme = 0
    while True:
        model = aktif_model()
        if not model:
            return None
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
        _bekle_sira(model)
        try:
            req = urllib.request.Request(
                url, data=veri, method="POST",
                headers={"Content-Type": "application/json", "x-goog-api-key": key},
            )
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                yanit = json.loads(resp.read().decode("utf-8"))
            if not metin(yanit):
                # 200 ama engellendi ya da yarıda kesildi · sebebi logla (2026-09-27:
                # sözlük çağrısı sessizce None döndü, sebep okunamadı)
                aday = (yanit.get("candidates") or [{}])[0]
                sebep = ((yanit.get("promptFeedback") or {}).get("blockReason")
                         or aday.get("finishReason") or "boş yanıt")
                print(f"  ! Gemini {model}: yanıt kullanılamadı ({sebep})", flush=True)
                _basarisiz(model)
                return None
            _art_arda_hata[model] = 0
            return yanit
        except urllib.error.HTTPError as e:
            try:
                govde = e.read().decode("utf-8", errors="replace")
            except Exception:
                govde = ""
            sinif = siniflandir(e.code, govde)
            if sinif == "gunluk":
                # Hangi kotanın bittiğini logla · 2026-09-27'de 8 model 4 dk'da
                # "günlük kota" dedi, gövde loglanmadığı için sebep okunamadı.
                kota = re.search(r'"quotaId"\s*:\s*"([^"]+)"', govde)
                _birak(model, f"günlük kota doldu ({kota.group(1) if kota else 'quotaId yok'})")
                deneme = 0
                continue
            if sinif == "model":
                _birak(model, f"model kullanılamıyor ({e.code})")
                deneme = 0
                continue
            if sinif == "anahtar":
                _kapat(f"HTTP {e.code}")
                return None
            if sinif == "gecici" and deneme < deneme_sayisi - 1:
                time.sleep(_gecikme(e, govde, deneme))
                deneme += 1
                continue
            durum = re.search(r'"status"\s*:\s*"([A-Z_]+)"', govde)
            print(f"  ! Gemini {model}: istek başarısız (HTTP {e.code}{' ' + durum.group(1) if durum else ''})", flush=True)
            _basarisiz(model)
            return None
        except Exception:
            if deneme < deneme_sayisi - 1:
                time.sleep(min(5.0 * (deneme + 1), 30.0))
                deneme += 1
                continue
            _basarisiz(model)
            return None


def metin(yanit: dict | None) -> str:
    """Yanıttaki ilk adayın TAM metni · engellendi/yarıda kesildiyse boş string."""
    if not yanit:
        return ""
    if (yanit.get("promptFeedback") or {}).get("blockReason"):
        return ""
    adaylar = yanit.get("candidates") or []
    if not adaylar:
        return ""
    bitis = adaylar[0].get("finishReason")
    if bitis and bitis != "STOP":
        return ""
    parcalar = (adaylar[0].get("content") or {}).get("parts") or []
    return "".join(str(p.get("text") or "") for p in parcalar if not p.get("thought")).strip()
