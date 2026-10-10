#!/usr/bin/env python3
"""Keep the ICO fallback before the adaptive SVG icon in pages and generators.

Usage: python3 scripts/sync-favicon.py [--check | --self-test]
The default mode updates static HTML and the source templates that publish it.
--check reports drift without writing; --self-test checks normalization in memory.
"""
import argparse
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
SVG_LINK = '<link rel="icon" type="image/svg+xml" href="/favicon.svg">'
ICO_LINK = '<link rel="icon" type="image/x-icon" sizes="16x16 32x32 48x48" href="/favicon.ico">'
ICON_PAIR = ICO_LINK + " " + SVG_LINK
ICON_BLOCK = re.compile(r"(?:" + re.escape(ICO_LINK) + r"\s*)*" + re.escape(SVG_LINK))
GENERATORS = (
    "build-en.js",
    "build-reports-en.js",
    "dict-sync.py",
    "dictionary-en.py",
    "dil-anasayfa.py",
    "discover-en.py",
    "discover-sync.py",
    "translate-report-json.js",
)


def normalize(text):
    # A space keeps both inline HTML and quoted Python/JS templates valid.
    return ICON_BLOCK.sub(lambda _: ICON_PAIR, text)


def self_test():
    cases = (
        "<head>\n  " + SVG_LINK + "\n</head>",
        "'<head>\\n" + SVG_LINK + "\\n'",
        ICON_PAIR,
        ICO_LINK + "\n  " + SVG_LINK,
        ICO_LINK + ICO_LINK + SVG_LINK,
    )
    for original in cases:
        updated = normalize(original)
        assert updated.count(ICO_LINK) == 1
        assert ICON_PAIR in updated
        assert normalize(updated) == updated
    assert normalize("<head></head>") == "<head></head>"
    print("Favicon normalization: existing pairs, duplicates and repeated runs pass")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="report changes without writing")
    mode.add_argument("--self-test", action="store_true", help="check normalization without file access")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if not (ROOT / "favicon.ico").is_file():
        parser.error("favicon.ico is missing")
    pages = sorted(path for path in ROOT.rglob("*.html") if "node_modules" not in path.parts)
    sources = [ROOT / "scripts" / name for name in GENERATORS]
    changed, declarations = [], 0
    for path in pages + sources:
        original = path.read_text(encoding="utf-8")
        declarations += original.count(SVG_LINK)
        updated = normalize(original)
        if updated == original:
            continue
        changed.append(path.relative_to(ROOT))
        if not args.check:
            path.write_text(updated, encoding="utf-8")
    if args.check and changed:
        for path in changed[:10]:
            print(f"Missing or duplicate ICO fallback: {path}")
    action = "need updates" if args.check else "updated"
    print(f"Favicon declarations: {declarations}; {len(changed)} files {action}")
    return int(args.check and bool(changed))


if __name__ == "__main__":
    raise SystemExit(main())
