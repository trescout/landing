#!/usr/bin/env python3
"""Static guard for consent-gated telemetry, page coverage and disclosures."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
PRIVACY_FILES = (
    ROOT / "privacy.html",
    ROOT / "en/privacy.html",
    ROOT / "fr/privacy.html",
    ROOT / "pt/privacy.html",
    ROOT / "es/privacy.html",
    ROOT / "de/privacy.html",
)
REPORT_SOURCES = (
    "/_vercel/insights/script.js",
    "/_vercel/speed-insights/script.js",
    "/assets/provider-consent.js",
    "/assets/telemetry.js",
)


def fail(messages):
    print("Telemetry consent guard failed:")
    print("\n".join(f"- {message}" for message in messages))
    return 1


def report_detail(path, text):
    return "/reports/" in path.as_posix() and (
        'class="signup-cta"' in text or 'data-page-type="report"' in text
    )


def check_report_scripts(errors):
    for path in ROOT.rglob("*.html"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if not report_detail(path, text):
            continue
        positions = []
        for source in REPORT_SOURCES:
            count = text.count(source)
            if count != 1:
                errors.append(f"{path.relative_to(ROOT)} must contain exactly one {source} tag (found {count})")
            else:
                positions.append((text.find(source), source))
        if len(positions) == len(REPORT_SOURCES) and positions != sorted(positions):
            errors.append(f"{path.relative_to(ROOT)} provider order must be Insights, Speed Insights, telemetry")
        if re.search(r"KVKK uyumlu|GDPR compliant|GDPR uyumludur|SOC 2 uyumlu", text, re.IGNORECASE):
            errors.append(f"{path.relative_to(ROOT)} contains an unqualified generated compliance claim")


def check_form_fallback(errors):
    form_pattern = re.compile(r"<form\b[^>]*>", re.IGNORECASE)
    for path in ROOT.rglob("*.html"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for tag in form_pattern.findall(text):
            if not re.search(r"\bjs-subscribe\b", tag, re.IGNORECASE):
                continue
            if not re.search(r"\baction\s*=\s*[\"']/api/subscribe[\"']", tag, re.IGNORECASE):
                errors.append(f"{path.relative_to(ROOT)} subscription form lacks POST action")
            if not re.search(r"\bmethod\s*=\s*[\"']post[\"']", tag, re.IGNORECASE):
                errors.append(f"{path.relative_to(ROOT)} subscription form lacks method=post")
            if re.search(r"\bnovalidate\b", tag, re.IGNORECASE):
                errors.append(f"{path.relative_to(ROOT)} subscription form still disables native validation")


def main():
    errors = []
    telemetry = (ROOT / "assets/telemetry.js").read_text(encoding="utf-8")
    provider_consent = (ROOT / "assets/provider-consent.js").read_text(encoding="utf-8")
    privacy_js = (ROOT / "assets/privacy.js").read_text(encoding="utf-8")
    home = (ROOT / "index.html").read_text(encoding="utf-8")

    required_runtime_patterns = {
        "track consent gate": r"if \(!eventName \|\| !isGranted\(\)\) return false;",
        "first-seen consent gate": r"function ensureFirstSeen\(\)\s*\{\s*if \(!isGranted\(\)\) return;",
        "retention consent gate": r"function checkRetention\(\)\s*\{\s*if \(!isGranted\(\)\)",
        "granted consent persistence": r"if \(next === 'granted'\)\s*\{\s*storageSet\(STORAGE_KEY_CONSENT, next\);",
        "denied tracking cleanup": r"if \(next === 'denied'\) storageSet\(STORAGE_KEY_CONSENT, next\);[\s\S]{0,180}clearTrackingState\(\);",
        "memory queue bound": r"if \(pendingEvents\.length >= MAX_QUEUE\) pendingEvents\.shift\(\);",
        "custom payload allowlist": r"SAFE_CUSTOM_KEYS",
        "delivery finalization": r"function finalizeDelivery\(item\)",
        "cross-tab consent listener": r"function handleConsentStorageChange\(event\)",
        "path normalization": r"function safePath\(value\)",
        "campaign value normalization": r"function safeCampaignValue\(value\)",
    }
    required_provider_patterns = {
        "provider consent gate": r"if \(!readConsent\(\)\) return;",
        "provider source allowlist": r"function sameOriginProvider\(src\)",
        "provider consent event": r"trescout:telemetry-consent",
    }
    for label, pattern in required_runtime_patterns.items():
        if not re.search(pattern, telemetry):
            errors.append(f"assets/telemetry.js missing {label}")
    for label, pattern in required_provider_patterns.items():
        if not re.search(pattern, provider_consent):
            errors.append(f"assets/provider-consent.js missing {label}")

    direct_provider = re.compile(r'<script\b(?=[^>]*\bsrc=["\']/_vercel/(?:insights|speed-insights)/script\.js["\'])(?![^>]*\bdata-consent-src=)', re.IGNORECASE)
    if direct_provider.search(home):
        errors.append("index.html contains an executable Vercel provider tag before consent")
    if "data-consent-src=\"/_vercel/insights/script.js\"" not in home or "data-consent-src=\"/_vercel/speed-insights/script.js\"" not in home:
        errors.append("index.html missing inert provider consent sources")
    if "<script src=\"/assets/provider-consent.js\" defer></script>" not in home:
        errors.append("index.html missing provider consent loader")

    if "privacy-telemetry-preference" not in privacy_js:
        errors.append("assets/privacy.js missing the standalone telemetry preference panel")
    if "privacy-telemetry-checkbox" not in home or "privacy-telemetry-status" not in home:
        errors.append("index.html missing the static telemetry preference controls")
    provider_pos = home.find('data-consent-src="/_vercel/insights/script.js"')
    loader_pos = home.find('<script src="/assets/provider-consent.js" defer></script>')
    telemetry_pos = home.find('<script src="/assets/telemetry.js" defer></script>')
    if provider_pos < 0 or loader_pos < 0 or telemetry_pos < 0 or not (provider_pos < loader_pos < telemetry_pos):
        errors.append("index.html must keep inert providers, consent loader, then telemetry in order")
    if "ts_telemetry_consent" not in privacy_js or "localStorage" not in privacy_js:
        errors.append("assets/privacy.js missing consent storage handling")
    if "checkbox.checked = readConsent();" not in privacy_js:
        errors.append("assets/privacy.js does not initialize the preference control from consent state")

    check_report_scripts(errors)
    check_form_fallback(errors)

    banned_claims = (
        "GDPR ve KVKK uyumludur",
        "This is GDPR and KVKK compliant",
        "C'est conforme au RGPD et à la KVKK",
        "Isso está de acordo com o GDPR e a KVKK",
        "Esto cumple con el RGPD y la KVKK",
        "Das entspricht der DSGVO und der KVKK",
    )
    telemetry_terms = ("telemetry", "télémétrie", "telemetria", "telemetría", "telemetrie")
    for path in PRIVACY_FILES:
        if not path.exists():
            errors.append(f"missing privacy disclosure: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        lower = text.lower()
        if not any(term in lower for term in telemetry_terms):
            errors.append(f"{path.relative_to(ROOT)} does not disclose optional telemetry")
        if "localstorage" not in lower:
            errors.append(f"{path.relative_to(ROOT)} does not disclose localStorage behavior")
        for claim in banned_claims:
            if claim.lower() in lower:
                errors.append(f"{path.relative_to(ROOT)} retains an unqualified compliance claim: {claim}")

    if errors:
        return fail(errors)

    print(
        "Telemetry consent guard passed: consent gate, bounded/allowlisted runtime, "
        "canonical consent-aware provider/runtime scripts, safe forms and six privacy disclosures are present."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
