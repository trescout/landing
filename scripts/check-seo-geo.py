#!/usr/bin/env python3
"""Read-only SEO/GEO checks for TreScout's static landing output.

The guard validates generated metadata, locale signals, directory hreflang
coverage, report-description uniqueness, catalogue claims, and the early-access
subscription endpoint without invoking any network endpoint.
"""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://trescout.com"
REQUIRED_HREFLANG = ("tr", "en", "fr", "pt-BR", "es", "de", "x-default")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def first(pattern: str, text: str) -> str | None:
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else None


def schema_text(value: object | None) -> str:
    """Compare schema and visible copy after HTML/entity/whitespace normalization."""
    return re.sub(r"\s+", " ", html.unescape(str(value or ""))).strip()


def visible_text(value: str | None) -> str:
    if not value:
        return ""
    return schema_text(re.sub(r"<[^>]+>", " ", value))


def route_for(path: Path) -> str:
    rel = path.parent.relative_to(ROOT).as_posix()
    return "/" if rel == "." else f"/{rel}/"


def scripts_jsonld(text: str) -> list[dict]:
    blocks = re.findall(
        r'<script\s+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
        text,
        re.IGNORECASE | re.DOTALL,
    )
    result: list[dict] = []
    for block in blocks:
        try:
            value = json.loads(block.strip())
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict):
            result.append(value)
    return result


def main() -> int:
    errors: list[str] = []
    pages = sorted(ROOT.rglob("index.html"))
    report_descriptions: list[tuple[str, str]] = []

    for page in pages:
        text = page.read_text(encoding="utf-8")
        rel = page.relative_to(ROOT).as_posix()
        route = route_for(page)
        lang = first(r"<html\s+lang=[\"']([^\"']+)", text)
        title = first(r"<title>(.*?)</title>", text)
        description = first(r'<meta\s+name=["\']description["\']\s+content=["\']([^\"]+)', text)
        canonical = first(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)', text)

        if not lang:
            fail(errors, f"{rel}: html lang missing")
        if not title:
            fail(errors, f"{rel}: title missing")
        if not description or len(description) < 50:
            fail(errors, f"{rel}: meta description missing or too short")
        if canonical != f"{BASE}{route}":
            fail(errors, f"{rel}: canonical is {canonical!r}, expected {BASE}{route!r}")
        if not re.search(r"<h1\b", text, re.IGNORECASE):
            fail(errors, f"{rel}: h1 missing")

        # Social metadata is also a machine-readable preview contract. Keep
        # it present on every indexable HTML page so localized/index routes do
        # not silently lose their share preview during generation.
        for marker in (
            'property="og:image"',
            'name="twitter:card"',
            'name="twitter:title"',
            'name="twitter:description"',
            'name="twitter:image"',
        ):
            if marker not in text:
                fail(errors, f"{rel}: social metadata {marker} missing")

        # Discovery detail pages expose an Article entity. Its fields must
        # describe the visible page, not only the underlying repository record.
        if "/discover/" in route and not route.endswith("/discover/"):
            articles = [item for item in scripts_jsonld(text) if item.get("@type") == "Article"]
            if not articles:
                fail(errors, f"{rel}: discovery Article JSON-LD missing")
            else:
                article = articles[0]
                visible_headline = visible_text(first(r'<h1 class="disc-title">(.*?)</h1>', text))
                visible_lead = visible_text(first(r'<p class="disc-lead">(.*?)</p>', text))
                if schema_text(article.get("headline")) != schema_text(visible_headline):
                    fail(errors, f"{rel}: Article headline does not match visible H1")
                if schema_text(article.get("description")) != schema_text(visible_lead):
                    fail(errors, f"{rel}: Article description does not match visible lead")
                article_lang = str(article.get("inLanguage", ""))
                if article_lang.split("-")[0].lower() != (lang or "").split("-")[0].lower():
                    fail(errors, f"{rel}: Article inLanguage is {article_lang!r}, expected {lang!r}")
                if article.get("url") != canonical:
                    fail(errors, f"{rel}: Article url does not match canonical")

        if "/reports/" in route and re.search(r"/reports/(?:fresh/)?\d{4}-\d{2}-\d{2}/$", route):
            if description:
                report_descriptions.append((rel, description))

        if route.endswith(("/discover/", "/dictionary/")):
            for code in REQUIRED_HREFLANG:
                if f'hreflang="{code}"' not in text:
                    fail(errors, f"{rel}: hreflang {code} missing")

        if route in {"/", "/en/", "/fr/", "/pt/", "/es/", "/de/"}:
            graph_items: list[dict] = []
            for block in scripts_jsonld(text):
                graph = block.get("@graph")
                graph_items.extend(graph if isinstance(graph, list) else [block])
            websites = [item for item in graph_items if item.get("@type") == "WebSite"]
            if not websites:
                fail(errors, f"{rel}: WebSite JSON-LD missing or invalid")
            else:
                website = websites[0]
                if website.get("url", "").rstrip("/") != (canonical or "").rstrip("/"):
                    fail(errors, f"{rel}: WebSite JSON-LD url is {website.get('url')!r}")
                jsonld_lang = str(website.get("inLanguage", ""))
                if lang and jsonld_lang.split("-")[0].lower() != lang.split("-")[0].lower():
                    fail(errors, f"{rel}: WebSite JSON-LD inLanguage is {jsonld_lang!r}, expected language {lang!r}")

    compare_files = [ROOT / "compare/rss-vs-ai.md"] + sorted(ROOT.glob("**/compare/rss-vs-ai/index.html"))
    for path in compare_files:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if re.search(r"\b494\b|\b407\b", text):
            fail(errors, f"{path.relative_to(ROOT)}: stale catalogue count remains")

    home = (ROOT / "index.html").read_text(encoding="utf-8")
    if "HuggingFace ve daha fazlası yakında" in home:
        fail(errors, "index.html: stale 'HuggingFace yakında' claim remains")

    robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
    for agent in ("OAI-SearchBot", "Claude-SearchBot", "Claude-User", "PerplexityBot"):
        if not re.search(rf"^User-agent:\s*{re.escape(agent)}\s*$", robots, re.MULTILINE):
            fail(errors, f"robots.txt: official AI search agent {agent} missing")

    catalog = json.loads((ROOT / "assets/discover/catalog.json").read_text(encoding="utf-8"))
    dictionary = json.loads((ROOT / "assets/dictionary/dictionary.json").read_text(encoding="utf-8"))
    llms = (ROOT / "llms.txt").read_text(encoding="utf-8")
    expected_counts = f"{len(catalog)} araç · {len(dictionary)} terim"
    if expected_counts not in llms:
        fail(errors, f"llms.txt: expected manifest count {expected_counts!r} not found")

    if report_descriptions:
        descriptions = [description for _, description in report_descriptions]
        if len(set(descriptions)) != len(descriptions):
            duplicates = len(descriptions) - len(set(descriptions))
            fail(errors, f"report pages: {duplicates} duplicate meta descriptions")

    # This endpoint is intentionally checked, never called. It must keep
    # collecting registrations and notifying the owner about new registrations.
    subscribe = (ROOT / "api/subscribe.js").read_text(encoding="utf-8")
    for marker in ("https://api.resend.com", "NOTIFY_TO", "audiences", "emails"):
        if marker not in subscribe:
            fail(errors, f"api/subscribe.js: expected registration marker {marker!r} missing")

    if errors:
        print(f"✗ SEO/GEO guard · {len(errors)} hata")
        for error in errors[:80]:
            print(f"  - {error}")
        return 1

    print(
        f"✓ SEO/GEO guard · {len(pages)} HTML sayfa · "
        f"{len(catalog)} araç · {len(dictionary)} terim · "
        f"{len(report_descriptions)} benzersiz rapor açıklaması"
    )
    print("✓ Erken erişim endpoint'i doğrulandı; hiçbir istek gönderilmedi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# AI Traceability
# Plan Agent: SEO/GEO audit report and landing AGENTS.md.
# Skills Agent: static landing SEO/GEO guard workflow.
# Turkish content: no new user-facing Turkish copy generated here.
# Manual: validation logic and repository integration.
