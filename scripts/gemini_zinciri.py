"""Gemini model zinciri · landing'deki tüm Python Gemini çağrılarının tek girişi.

Free tier'da kota MODEL BAŞINA tutuluyor (ör. 3.5 Flash Lite ve 3.1 Flash Lite
için ayrı ayrı 15 RPM / 500 RPD). Zincir önce daha iyi modeli kullanır, onun
günlük kotası bitince sıradakine geçer. Limitleri koda gömmüyoruz: hangi
hesabın anahtarı kullanılırsa kullanılsın, günlük kotanın bittiğini 429
yanıtındaki quota kimliğinden ("...PerDay...") anlıyoruz.

429 iki türlü:
- dakikalık (RPM): önerilen retryDelay kadar bekleyip AYNI modelle tekrar dene
- günlük (RPD): o model bu koşu için bitti, beklemek anlamsız · sıradakine geç
Eskiden ikisi aynı "duraklat ve tekrar dene" döngüsüne giriyordu; günlük kota
bittiğinde koşu saatlerce boşuna bekliyordu (2026-09-26: iş 180 dk sınırına
takılıp iptal oldu).

Zincir: GEMINI_MODELS (virgülle) > GEMINI_MODEL / TREESCOUT_TRANSLATION_MODEL
(tek model, geriye uyum) > varsayılan.
"""

import json
import os
import re
import time
import urllib.error
import urllib.request

VARSAYILAN_ZINCIR = "gemini-3.5-flash-lite,gemini-3.1-flash-lite"

MODELLER = [m.strip() for m in (
    os.environ.get("GEMINI_MODELS")
    or os.environ.get("GEMINI_MODEL")
    or os.environ.get("TREESCOUT_TRANSLATION_MODEL")
    or VARSAYILAN_ZINCIR
).split(",") if m.strip()]

# İstekler arası asgari süre · 15 RPM = 4 sn. Dakikalık 429'u baştan önler.
ASGARI_ARALIK = float(os.environ.get("GEMINI_MIN_INTERVAL", "4.2"))

_bitenler: set[str] = set()
_son_istek = 0.0
# Yanıtta "PerDay" görünmese de (hesap/tier farkı) bir model üst üste bu kadar
# kez tüm 429 denemelerini tüketirse bitmiş sayılır · koşu boşuna beklemesin.
_ART_ARDA_SINIR = 3
_art_arda_429: dict[str, int] = {}


def aktif_model() -> str | None:
    """Zincirde günlük kotası bitmemiş ilk model · hepsi bittiyse None."""
    return next((m for m in MODELLER if m not in _bitenler), None)


def _birak(model: str, neden: str) -> None:
    _bitenler.add(model)
    sonraki = aktif_model()
    devam = f"{sonraki} ile devam" if sonraki else "zincirde model kalmadı, Gemini bu koşuda kapalı"
    print(f"  ! Gemini {model}: {neden} · {devam}", flush=True)


def _bekle_sira() -> None:
    global _son_istek
    kalan = _son_istek + ASGARI_ARALIK - time.time()
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


def istek(body: dict, key: str, timeout: float = 90, deneme_sayisi: int = 4) -> dict | None:
    """generateContent'i zincir üzerinden çağırır; yanıt JSON'unu ya da None döner.

    None: tüm modellerin günlük kotası bitti, ya da kalıcı hata. Çağıran,
    None'da aynı isteği tekrar denememeli (sonuç değişmez).
    """
    if not key:
        return None
    veri = json.dumps(body, ensure_ascii=False).encode("utf-8")
    deneme = 0
    while True:
        model = aktif_model()
        if not model:
            return None
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
        _bekle_sira()
        try:
            req = urllib.request.Request(
                url, data=veri, method="POST",
                headers={"Content-Type": "application/json", "x-goog-api-key": key},
            )
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                yanit = json.loads(resp.read().decode("utf-8"))
            _art_arda_429[model] = 0
            return yanit
        except urllib.error.HTTPError as e:
            try:
                govde = e.read().decode("utf-8", errors="replace")
            except Exception:
                govde = ""
            if e.code == 429 and "PerDay" in govde:
                _birak(model, "günlük kota doldu")
                deneme = 0
                continue
            if e.code == 404:
                _birak(model, "model bulunamadı (404)")
                deneme = 0
                continue
            if e.code in (429, 500, 502, 503) and deneme < deneme_sayisi - 1:
                time.sleep(_gecikme(e, govde, deneme))
                deneme += 1
                continue
            if e.code == 429:
                _art_arda_429[model] = _art_arda_429.get(model, 0) + 1
                if _art_arda_429[model] >= _ART_ARDA_SINIR:
                    _birak(model, f"üst üste {_ART_ARDA_SINIR} kez 429")
            return None
        except Exception:
            if deneme < deneme_sayisi - 1:
                time.sleep(min(5.0 * (deneme + 1), 30.0))
                deneme += 1
                continue
            return None


def metin(yanit: dict | None) -> str:
    """Yanıttaki ilk adayın metni · yoksa boş string."""
    if not yanit:
        return ""
    adaylar = yanit.get("candidates") or []
    if not adaylar:
        return ""
    parcalar = (adaylar[0].get("content") or {}).get("parts") or []
    return "".join(str(p.get("text") or "") for p in parcalar).strip()
