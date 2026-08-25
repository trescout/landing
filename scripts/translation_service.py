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

GEMINI_MODEL = os.environ.get("TREESCOUT_TRANSLATION_MODEL", "gemini-3.1-flash-lite")


def _retry_delay(attempt: int) -> float:
    return min(2.0 * (2**attempt), 12.0)


def _gemini(text: str, lang: str, key: str) -> str | None:
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
            if error.code not in (429, 500, 502, 503) or attempt == 3:
                return None
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
            if error.code not in (429, 500, 502, 503) or attempt == 2:
                return None
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
