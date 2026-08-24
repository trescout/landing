#!/usr/bin/env python3
"""Verify that every discovery index renders the same first-discovery order."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "assets" / "discover" / "catalog.json"
LANGUAGES = {
    "tr": ROOT / "discover" / "index.html",
    "en": ROOT / "en" / "discover" / "index.html",
    "fr": ROOT / "fr" / "discover" / "index.html",
    "pt": ROOT / "pt" / "discover" / "index.html",
    "es": ROOT / "es" / "discover" / "index.html",
    "de": ROOT / "de" / "discover" / "index.html",
}


def expected_slugs(catalog: list[dict[str, object]]) -> list[str]:
    return [
        str(item["slug"])
        for item in sorted(
            catalog,
            key=lambda item: (str(item.get("date") or ""), int(item.get("stars") or 0)),
            reverse=True,
        )
    ]


def rendered_slugs(path: Path, prefix: str) -> list[str]:
    html = path.read_text(encoding="utf-8")
    grid_start = html.find('id="discover-grid"')
    grid_end = html.find('<p class="disc-empty"', grid_start)
    if grid_end < 0:
        grid_end = html.find('disc-cta', grid_start)
    if grid_start < 0 or grid_end < 0:
        raise ValueError(f"{path}: discovery grid boundary not found")
    grid = html[grid_start:grid_end]
    return re.findall(rf'href="{re.escape(prefix)}/discover/([^/]+)/"', grid)


def main() -> int:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    expected = expected_slugs(catalog)
    errors: list[str] = []

    js = (ROOT / "assets" / "discover.js").read_text(encoding="utf-8")
    if "var ad = a.last_seen" in js or "var bd = b.last_seen" in js:
        errors.append("assets/discover.js still sorts the date option by last_seen")

    for language, path in LANGUAGES.items():
        if not path.exists():
            errors.append(f"{language}: missing index {path}")
            continue
        prefix = "" if language == "tr" else f"/{language}"
        actual = rendered_slugs(path, prefix)
        if actual != expected:
            first_difference = next(
                (i for i, (left, right) in enumerate(zip(actual, expected)) if left != right),
                min(len(actual), len(expected)),
            )
            errors.append(
                f"{language}: expected {len(expected)} cards in first-discovery order, "
                f"got {len(actual)}; first difference at position {first_difference + 1}"
            )

    if errors:
        for error in errors:
            print(f"✗ {error}")
        return 1
    print(f"Discovery sort guard passed: {len(expected)} cards × {len(LANGUAGES)} indexes use first discovery date")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
