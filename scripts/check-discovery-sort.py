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


from html.parser import HTMLParser


class DiscoverGridParser(HTMLParser):
    def __init__(self, prefix: str) -> None:
        super().__init__()
        self.prefix = prefix
        self.in_grid = False
        self.grid_depth = 0
        self.found_grid = False
        self.slugs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_dict = dict(attrs)
        if attr_dict.get("id") == "discover-grid":
            self.in_grid = True
            self.found_grid = True
            self.grid_depth = 1
            return
        if self.in_grid:
            self.grid_depth += 1
            if tag == "a":
                classes = (attr_dict.get("class") or "").split()
                if "disc-card" in classes:
                    href = attr_dict.get("href") or ""
                    m = re.match(rf"^{re.escape(self.prefix)}/discover/([^/]+)/?$", href)
                    if m:
                        self.slugs.append(m.group(1))

    def handle_endtag(self, tag: str) -> None:
        if self.in_grid:
            self.grid_depth -= 1
            if self.grid_depth == 0:
                self.in_grid = False


def extract_grid_slugs(html: str, prefix: str) -> list[str]:
    parser = DiscoverGridParser(prefix)
    parser.feed(html)
    if not parser.found_grid:
        raise ValueError("discovery grid boundary not found")
    return parser.slugs


def rendered_slugs(path: Path, prefix: str) -> list[str]:
    html = path.read_text(encoding="utf-8")
    try:
        return extract_grid_slugs(html, prefix)
    except ValueError as exc:
        raise ValueError(f"{path}: {exc}") from exc


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
        # Dizin yalnız o dilde sayfası OLAN araçlara kart basıyor (build-en.js
        # sayfaVar · çevirisi eksik sayfa yazılmıyor). Sıra kuralı aynı, beklenen
        # küme o dilde var olan sayfalar.
        dil_kok = ROOT if language == "tr" else ROOT / language
        beklenen = [s for s in expected if (dil_kok / "discover" / s / "index.html").exists()]
        if actual != beklenen:
            first_difference = next(
                (i for i, (left, right) in enumerate(zip(actual, beklenen)) if left != right),
                min(len(actual), len(beklenen)),
            )
            errors.append(
                f"{language}: expected {len(beklenen)} cards in first-discovery order, "
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
