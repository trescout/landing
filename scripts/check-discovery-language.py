#!/usr/bin/env python3
"""Fail when Portuguese discovery taglines leak into non-Portuguese output.

This is intentionally a conservative marker guard, not a general language
classifier. It requires multiple distinctive Portuguese tokens so normal
technology names do not create false positives.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
LANGS = ["tr", "en", "fr", "pt", "es", "de"]
NON_PORTUGUESE = ["tr", "en", "fr", "es", "de"]
PT_MARKERS = re.compile(
    r"\b(?:desenvolvido|desenvolvida|linguagem|aprendizado|roda|coincidência|"
    r"desnecessári[oa]s?|migração|automação|observações|viagem|enxames|"
    r"espaço|ferramenta|serviço|flui|assinaturas|arquivo)\b",
    re.IGNORECASE,
)


def marker_score(value: str) -> int:
    return len({m.group(0).lower() for m in PT_MARKERS.finditer(value or "")})


def page_root(lang: str) -> Path:
    return ROOT / "discover" if lang == "tr" else ROOT / lang / "discover"


def check_catalog(issues: list[str]) -> None:
    catalog = json.loads((ROOT / "assets/discover/catalog.json").read_text(encoding="utf-8"))
    for item in catalog:
        slug = item.get("slug", "")
        source = (item.get("tagline") or "").strip()
        if marker_score(source) >= 2:
            issues.append(f"catalog {slug}: Turkish tagline has Portuguese markers")
        for lang in NON_PORTUGUESE:
            if lang == "tr":
                continue
            value = (item.get(f"tagline_{lang}") or "").strip()
            if marker_score(value) >= 2:
                issues.append(f"catalog {slug}: tagline_{lang} has Portuguese markers")
            if value and source and value == source and marker_score(source) >= 2:
                issues.append(f"catalog {slug}: tagline_{lang} duplicates Portuguese source")


def check_pages(issues: list[str]) -> tuple[int, int]:
    page_count = 0
    checked_fields = 0
    for lang in LANGS:
        base = page_root(lang)
        if not base.exists():
            continue
        for page in sorted(base.glob("*/index.html")):
            page_count += 1
            soup = BeautifulSoup(page.read_text(encoding="utf-8"), "html.parser")
            fields = {
                "meta": (soup.find("meta", attrs={"name": "description"}) or {}).get("content", ""),
                "lead": (soup.find("p", class_="disc-lead") or {}).get_text(" ", strip=True),
            }
            if lang == "pt":
                continue
            for field, value in fields.items():
                checked_fields += 1
                if marker_score(value) >= 2:
                    issues.append(f"page {lang}/{page.parent.name} {field}: Portuguese markers")
    return page_count, checked_fields


def main() -> None:
    issues: list[str] = []
    check_catalog(issues)
    page_count, checked_fields = check_pages(issues)
    print(f"Discovery language guard: {page_count} pages, {checked_fields} non-Portuguese fields checked")
    if issues:
        for issue in issues:
            print(f"FAIL {issue}")
        raise SystemExit(1)
    print("Discovery language guard passed")


if __name__ == "__main__":
    main()
