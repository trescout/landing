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

GEMINI_MODEL = os.environ.get("GEMINI_MODEL") or os.environ.get("TREESCOUT_TRANSLATION_MODEL") or "gemini-2.5-flash"
_GEMINI_PAUSED_UNTIL = 0.0


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


def _pause_gemini(delay: float) -> None:
    global _GEMINI_PAUSED_UNTIL
    _GEMINI_PAUSED_UNTIL = max(_GEMINI_PAUSED_UNTIL, time.time() + delay)


def _gemini_is_paused() -> bool:
    return time.time() < _GEMINI_PAUSED_UNTIL


def _gemini(text: str, lang: str, key: str) -> str | None:
    if _gemini_is_paused():
        return None
    body = {
        "systemInstruction": {
            "parts": [{
                "text": (
                    "You are a precise professional translator. Translate Turkish into the requested language. "
                    "Return only the translation, with no quotation marks, commentary, markdown, or language label. "
                    "Do not summarize, omit, or add claims. Preserve product names, repository names, URLs and numbers."
                )
            }]
        },
        "contents": [{
            "parts": [{
                "text": (
                    f"Translate this Turkish technology-site text into {lang}. "
                    "Keep the meaning and register natural for the target locale.\n\n{text}"
                )
            }]
        }],
        "generationConfig": {
            "temperature": 0.1,
            "maxOutputTokens": 2048,
        },
    }
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"
    request = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json", "x-goog-api-key": key},
        method="POST",
    )
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                payload = json.loads(response.read().decode("utf-8"))
            candidates = payload.get("candidates") or []
            parts = (candidates[0].get("content") or {}).get("parts") or []
            result = "".join(str(part.get("text") or "") for part in parts).strip()
            if result:
                if result.startswith("```") and result.endswith("```"):
                    result = result.split("\n", 1)[-1][:-3].strip()
                return result or None
            raise ValueError("Gemini empty translation response")
        except urllib.error.HTTPError as error:
            if error.code == 429:
                _pause_gemini(_http_retry_delay(error, attempt))
                return None
            if error.code not in (500, 502, 503) or attempt == 3:
                return None
            time.sleep(_http_retry_delay(error, attempt))
            continue
        except Exception:
            if attempt == 3:
                return None
        time.sleep(_retry_delay(attempt))
    return None


def _gtx(text: str, lang: str) -> str | None:
    url = (
        "https://translate.googleapis.com/translate_a/single?client=gtx&sl=tr&"
        f"tl={urllib.parse.quote(lang)}&dt=t&q={urllib.parse.quote(text)}"
    )
    request = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "TreScout/1.0"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                payload = json.loads(response.read().decode("utf-8"))
            if not isinstance(payload, list) or not payload or not isinstance(payload[0], list):
                return None
            result = "".join(str(part[0]) for part in payload[0] if isinstance(part, list) and part).strip()
            return result or None
        except urllib.error.HTTPError as error:
            if error.code == 429:
                _pause_gemini(_http_retry_delay(error, attempt))
                return None
            if error.code not in (429, 500, 502, 503) or attempt == 2:
                return None
            time.sleep(_http_retry_delay(error, attempt))
            continue
        except Exception:
            if attempt == 2:
                return None
        time.sleep(_retry_delay(attempt))
    return None


def translate_text(text: str, lang: str) -> str | None:
    clean = (text or "").strip()
    if not clean:
        return ""
    key = os.environ.get("GEMINI_API_KEY", "").strip()
    if key:
        translated = _gemini(clean, lang, key)
        if translated:
            return translated
    return _gtx(clean, lang)


def _gemini_batch(texts: list[str], lang: str, key: str) -> dict[str, str] | None:
    items = [{"id": str(index), "text": text} for index, text in enumerate(texts)]
    body = {
        "systemInstruction": {
            "parts": [{
                "text": (
                    "You are a precise professional translator. Output valid JSON only. Translate each Turkish "
                    "item into the requested language. Preserve every id exactly, do not summarize, omit, merge, "
                    "or add items, and preserve proper nouns, URLs, numbers, and technical meaning."
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
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"
    request = urllib.request.Request(
        url,
        data=json.dumps(body, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json", "x-goog-api-key": key},
        method="POST",
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=90) as response:
                payload = json.loads(response.read().decode("utf-8"))
            candidates = payload.get("candidates") or []
            parts = (candidates[0].get("content") or {}).get("parts") or []
            raw = "".join(str(part.get("text") or "") for part in parts).strip()
            if raw.startswith("```"):
                raw = raw.split("\n", 1)[-1].removesuffix("```").strip()
            parsed = json.loads(raw)
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
            if len(result) != len(items):
                raise ValueError("Gemini batch ids are not unique")
            return result
        except urllib.error.HTTPError as error:
            if error.code == 429:
                _pause_gemini(_http_retry_delay(error, attempt))
                return None
            if error.code not in (429, 500, 502, 503) or attempt == 2:
                return None
            time.sleep(_http_retry_delay(error, attempt))
            continue
        except Exception:
            if attempt == 2:
                return None
        time.sleep(_retry_delay(attempt))
    return None


def translate_texts(texts: list[str], lang: str) -> dict[str, str | None]:
    """Translate passages in paced batches; never return source text on failure."""
    unique = list(dict.fromkeys((text or "").strip() for text in texts if (text or "").strip()))
    result: dict[str, str | None] = {}
    key = os.environ.get("GEMINI_API_KEY", "").strip()
    batch_size = 12
    for start in range(0, len(unique), batch_size):
        batch = unique[start:start + batch_size]
        translated = _gemini_batch(batch, lang, key) if key else None
        if translated is None:
            # Do not immediately fire Gemini once per item after a batch quota
            # failure. GTX is bounded and failures remain explicit as None.
            translated = {}
            for text in batch:
                value = _gtx(text, lang)
                if value:
                    translated[text] = value
        for text in batch:
            result[text] = translated.get(text)
        if start + batch_size < len(unique):
            time.sleep(5.0)
    return result
