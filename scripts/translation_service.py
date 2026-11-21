"""Reliable Turkish-to-locale translation for generated landing content.

Gemini is preferred when GEMINI_API_KEY is available. The anonymous GTX endpoint
is retained as a fallback. A failed call returns None: callers must preserve an
existing page or stop the generation, never write Turkish into another locale.
"""

import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gemini_zinciri  # noqa: E402 · model zinciri, 429 ayrımı, istek aralığı

# Rate-limit pause state. A quota wall is a property of the whole process, not
# of one passage: once the provider has refused every retry of a call, later
# calls in the same run will be refused too. Without this, each of thousands of
# passages paid the full retry ladder on its own (2026-08-26: a run sat in the
# page-generation step for five hours before it was cancelled). The pause window
# doubles on each consecutive exhaustion so a run that has truly hit the daily
# quota parks itself instead of probing every ninety seconds.
# Okura hitap (2026-10-16): Türkçe kaynak okura "siz" diye hitap ediyor; istem
# yalnız "register natural for the target locale" diyordu. İspanyolcada sözlük
# sayfalarının ~%30'u "tú", geri kalanı "usted" çıktı, bazı sayfalarda ikisi bir
# arada (kota bitince devreye giren GTX hitabı hiç seçemiyor). Kural artık istemde
# açık; çıktı da kodla sınanıyor: resmî kaynağın samimi çevirisi önbelleğe girmez,
# Gemini'den bir kez düzeltme istenir, olmazsa metin çevrilmemiş sayılır.
# Ajan istemleri (okurun yapay zekâ asistanına yazdığı metin) samimi kalabilir.
HITAP = {
    "es": 'Address the reader formally with "usted" (singular), its verb forms and "su/sus"; never use "tú", "tu" or "vosotros".',
    "fr": 'Address the reader formally with "vous"; never use "tu".',
    "de": 'Address the reader formally with "Sie"; never use "du".',
    "pt": 'Address the reader with "você" (Brazilian Portuguese); never use "tu".',
}
_HITAP_ISTISNA = ("Exception: if the Turkish text is a message the reader writes to an AI assistant "
                  "(informal \"sen\" forms), keep it informal.")
# Türkçede okura resmî hitap: "-ınız/-iniz/-unuz/-ünüz", "-sınız/-siniz..." ve "siz/size/sizin".
_TR_RESMI = re.compile(r"\b\w*(?:[aeıioöuü]n[ıiuü]z|s[ıiuü]n[ıiuü]z)(?:[ıiuüae]|[dt][ae]n?|l[ae]|[ıiuü]n|c[ae])?\b"
                       r"|\bsiz(?:e|i|in|den|ce|inle)?\b", re.I)
_SAMIMI = {
    "es": re.compile(r"\b(?:tú|tu|tus|contigo|puedes|quieres|tienes|necesitas|debes|sabes|estás|eres)\b", re.I),
    "fr": re.compile(r"\b(?:tu|toi|te|tes)\b", re.I),
    "de": re.compile(r"\b(?:du|dich|dir|dein|deine|deinen|deinem|deiner|deines)\b"),
    "pt": re.compile(r"\b(?:tu|teu|tua|teus|tuas|contigo)\b", re.I),
}


def hitap_ihlali(kaynak: str, ceviri: str, lang: str) -> bool:
    """Okura resmî hitap eden Türkçe kaynak samimi hitapla çevrildiyse True."""
    rx = _SAMIMI.get(lang)
    return bool(rx and _TR_RESMI.search(kaynak or "") and rx.search(ceviri or ""))


def _hitap_kurali(lang: str) -> str:
    kural = HITAP.get(lang)
    return f" {kural} {_HITAP_ISTISNA}" if kural else ""


_PAUSE_CAP = 600.0
_GTX_PAUSED_UNTIL = 0.0
_GTX_PAUSE_STREAK = 0


def _retry_delay(attempt: int) -> float:
    return min(2.0 * (2**attempt), 12.0)


def _http_retry_delay(error: urllib.error.HTTPError, attempt: int) -> float:
    """Honor provider Retry-After/retryDelay without exposing response bodies."""
    header = error.headers.get('Retry-After') if error.headers else None
    if header:
        try:
            return min(max(float(header), 1.0), 90.0)
        except ValueError:
            pass
    try:
        body = error.read().decode('utf-8', errors='replace')
        match = re.search(r'"retryDelay"\s*:\s*"([0-9.]+)s"', body)
        if match:
            return min(max(float(match.group(1)), 1.0), 90.0)
    except Exception:
        pass
    return _retry_delay(attempt)


def _pause_span(delay: float, streak: int) -> float:
    return min(max(delay, 30.0) * (2 ** max(streak - 1, 0)), _PAUSE_CAP)


def _duyur(saglayici: str, span: float, streak: int) -> None:
    """Kota duvarını loga yaz · yoksa koşu "neden çeviremedi" diye okunamıyor.

    27 Ağustos koşusunda en/fr/pt sıfır hatayla bitti, es ortasında tükendi.
    Duraklatma çalıştı ama log bunu söylemediği için tükenme mi yoksa başka
    bir hata mı olduğu ancak zaman damgalarından çıkarılabildi.
    """
    if streak == 1:
        print(f"  ! {saglayici} kota duvarı · çeviri {span:.0f} sn duraklatıldı "
              f"(tekrarında pencere ikiye katlanır)", flush=True)


def _pause_gtx(delay: float) -> None:
    global _GTX_PAUSED_UNTIL, _GTX_PAUSE_STREAK
    _GTX_PAUSE_STREAK += 1
    span = _pause_span(delay, _GTX_PAUSE_STREAK)
    _duyur("GTX", span, _GTX_PAUSE_STREAK)
    _GTX_PAUSED_UNTIL = max(_GTX_PAUSED_UNTIL, time.time() + span)


def _gtx_is_paused() -> bool:
    return time.time() < _GTX_PAUSED_UNTIL


def _gemini(text: str, lang: str, key: str, duzeltme: bool = False) -> str | None:
    not_ = ("\n\nYour previous translation addressed the reader informally. Use the formal address "
            "required above." if duzeltme else "")
    body = {
        "systemInstruction": {
            "parts": [{
                "text": (
                    "You are a precise professional translator. Translate Turkish into the requested language. "
                    "Return only the translation, with no quotation marks, commentary, markdown, or language label. "
                    "Do not summarize, omit, or add claims. Preserve product names, repository names, URLs and numbers."
                    + _hitap_kurali(lang)
                )
            }]
        },
        "contents": [{
            "parts": [{
                "text": (
                    f"Translate this Turkish technology-site text into {lang}. "
                    f"Keep the meaning and register natural for the target locale.{not_}\n\n{text}"
                )
            }]
        }],
        "generationConfig": {
            "temperature": 0.1,
            "maxOutputTokens": 2048,
        },
    }
    result = gemini_zinciri.metin(gemini_zinciri.istek(body, key, timeout=60))
    if result.startswith("```") and result.endswith("```"):
        result = result.split("\n", 1)[-1][:-3].strip()
    return result or None


def _gtx(text: str, lang: str) -> str | None:
    url = (
        "https://translate.googleapis.com/translate_a/single?client=gtx&sl=tr&"
        f"tl={urllib.parse.quote(lang)}&dt=t&q={urllib.parse.quote(text)}"
    )
    # Yumuşak süre sınırı GTX yedeğini de kapsar: Gemini None dönünce çeviri
    # buraya düşüyor ve sınırdan sonra iş yavaş GTX ile sürüyordu (2026-09-27).
    if _gtx_is_paused() or gemini_zinciri.sure_doldu():
        return None
    for attempt in range(3):
        try:
            request = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "TreScout/1.0"})
            with urllib.request.urlopen(request, timeout=20) as response:
                payload = json.loads(response.read().decode("utf-8"))
            if not isinstance(payload, list) or not payload or not isinstance(payload[0], list):
                return None
            result = "".join(str(part[0]) for part in payload[0] if isinstance(part, list) and part).strip()
            return result or None
        except urllib.error.HTTPError as error:
            if error.code == 429:
                delay = max(_http_retry_delay(error, attempt), (attempt + 1) * 2.0)
                if attempt == 2:
                    _pause_gtx(delay)
                    return None
                time.sleep(delay)
                continue
            if error.code not in (500, 502, 503) or attempt == 2:
                return None
            time.sleep(_http_retry_delay(error, attempt))
            continue
        except Exception:
            if attempt == 2:
                return None
            time.sleep(_retry_delay(attempt))
    return None


def _tekli(text: str, lang: str, key: str, gemini_ok: bool) -> str | None:
    """Tek metin: Gemini (hitap tutmazsa bir düzeltme turu), olmazsa GTX. Hitabı
    tutmayan çıktı dönmez (None = çevrilemedi, sayfa ertesi koşuya kalır)."""
    if gemini_ok:
        translated = _gemini(text, lang, key)
        if translated and hitap_ihlali(text, translated, lang):
            translated = _gemini(text, lang, key, duzeltme=True)
        if translated and not hitap_ihlali(text, translated, lang):
            return translated
    translated = _gtx(text, lang)
    return None if translated and hitap_ihlali(text, translated, lang) else translated


def translate_text(text: str, lang: str) -> str | None:
    clean = (text or "").strip()
    if not clean:
        return ""
    key = os.environ.get("GEMINI_API_KEY", "").strip()
    return _tekli(clean, lang, key, bool(key))


def _gemini_batch(texts: list[str], lang: str, key: str) -> dict[str, str] | None:
    items = [{"id": str(index), "text": text} for index, text in enumerate(texts)]
    body = {
        "systemInstruction": {
            "parts": [{
                "text": (
                    "You are a precise professional translator. Output valid JSON only. Translate each Turkish "
                    "item into the requested language. Preserve every id exactly, do not summarize, omit, merge, "
                    "or add items, and preserve proper nouns, URLs, numbers, and technical meaning."
                    + _hitap_kurali(lang)
                )
            }]
        },
        "contents": [{
            "parts": [{
                "text": (
                    f"Translate every item into {lang}. Return a JSON array with exactly one object per input, "
                    "using the same id and the translated text in the text field.\n\n" + json.dumps(items, ensure_ascii=False)
                )
            }]
        }],
        "generationConfig": {
            "temperature": 0.1,
            "maxOutputTokens": 8192,
            "responseMimeType": "application/json",
        },
    }
    # Biçim hatasında bir kez daha dene; kota/erişim hatasında (None) tekrar
    # denemek sonucu değiştirmez, zincir zaten sıradaki modele geçti.
    for attempt in range(2):
        raw = gemini_zinciri.metin(gemini_zinciri.istek(body, key, timeout=90))
        if not raw:
            return None
        try:
            return _batch_coz(raw, items)
        except Exception:
            continue
    return None


def _batch_coz(raw: str, items: list[dict]) -> dict[str, str]:
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[-1].removesuffix("```").strip()
    try:
        parsed = json.loads(raw)
    except Exception:
        fence = re.search(r'```(?:json)?\s*([\s\S]*?)\s*```', raw)
        if fence:
            parsed = json.loads(fence.group(1).strip())
        else:
            arr = re.search(r'\[\s*\{[\s\S]*\}\s*\]', raw)
            if arr:
                parsed = json.loads(arr.group(0).strip())
            else:
                raise
    rows = parsed if isinstance(parsed, list) else parsed.get("translations")
    if not isinstance(rows, list) or len(rows) != len(items):
        raise ValueError("Gemini batch translation shape mismatch")
    result: dict[str, str] = {}
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("Gemini batch row is not an object")
        index = int(str(row.get("id", "")))
        if index < 0 or index >= len(items):
            raise ValueError("Gemini batch id is invalid")
        value = str(row.get("text") or "").strip()
        if not value:
            raise ValueError("Gemini batch item is empty")
        result[items[index]["text"]] = value
    return result


def translate_texts(texts: list[str], lang: str) -> dict[str, str | None]:
    """Translate passages in paced batches; never return source text on failure."""
    unique = list(dict.fromkeys((text or "").strip() for text in texts if (text or "").strip()))
    result: dict[str, str | None] = {}
    key = os.environ.get("GEMINI_API_KEY", "").strip()
    batch_size = 12
    for start in range(0, len(unique), batch_size):
        batch = unique[start:start + batch_size]
        translated = _gemini_batch(batch, lang, key) if key else {}
        translated = translated or {}
        for text in batch:
            if translated.get(text) and not hitap_ihlali(text, translated[text], lang):
                result[text] = translated[text]
            else:
                result[text] = _tekli(text, lang, key, bool(key and gemini_zinciri.aktif_model()))
    return result
