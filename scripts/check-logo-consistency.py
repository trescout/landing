#!/usr/bin/env python3
"""Check canonical logo geometry in page chrome, generators and the favicon.

Every size uses the same filled horizon and tapering S from brand-kit logos/v2.
Check every logo container independently, so a valid footer cannot conceal a
missing or altered navigation mark. Retired thick and v1 paths are rejected.
"""
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
STANDARD_PATHS = (
    "M 19.16 21.86 A 84.0 84.0 0 0 1 80.84 21.86 A 5.0 5.0 0 0 1 77.16 31.17 A 74.0 74.0 0 0 0 22.84 31.17 A 5.0 5.0 0 0 1 19.16 21.86 Z",
    "M 53.00 27.00 C 52.80 28.43 52.79 30.00 52.41 31.30 C 52.03 32.61 51.37 33.78 50.71 34.80 C 50.05 35.83 49.21 36.68 48.45 37.48 C 47.69 38.27 46.86 38.93 46.14 39.58 C 45.42 40.22 44.71 40.80 44.15 41.36 C 43.59 41.92 43.12 42.44 42.79 42.94 C 42.45 43.44 42.25 43.84 42.12 44.35 C 41.99 44.86 41.95 45.61 41.99 46.00 C 42.02 46.39 42.03 46.40 42.33 46.67 C 42.63 46.93 43.01 47.24 43.79 47.58 C 44.56 47.92 45.73 48.34 46.98 48.72 C 48.23 49.10 49.77 49.44 51.28 49.86 C 52.80 50.28 54.46 50.64 56.07 51.24 C 57.67 51.84 59.39 52.39 60.92 53.44 C 62.45 54.49 64.21 55.78 65.25 57.54 C 66.30 59.30 66.93 62.19 67.20 64.00 C 67.46 65.81 67.13 67.00 66.85 68.40 C 66.57 69.80 66.10 71.16 65.53 72.41 C 64.96 73.66 64.22 74.82 63.44 75.88 C 62.66 76.93 61.76 77.88 60.84 78.77 C 59.93 79.65 58.95 80.44 57.97 81.19 C 56.98 81.94 55.96 82.61 54.95 83.27 C 53.94 83.92 52.90 84.52 51.90 85.11 C 50.89 85.70 49.90 86.25 48.91 86.81 A 6.50 6.50 0 0 1 43.09 75.19 C 44.09 74.75 45.12 74.30 46.07 73.87 C 47.02 73.43 47.95 73.01 48.80 72.58 C 49.65 72.15 50.46 71.72 51.19 71.28 C 51.92 70.85 52.58 70.41 53.16 69.98 C 53.73 69.55 54.23 69.12 54.66 68.68 C 55.08 68.25 55.42 67.83 55.72 67.37 C 56.02 66.91 56.25 66.47 56.43 65.90 C 56.61 65.34 56.76 64.51 56.80 64.00 C 56.85 63.49 56.89 63.24 56.69 62.85 C 56.48 62.45 56.24 62.08 55.58 61.62 C 54.92 61.16 53.89 60.59 52.75 60.10 C 51.60 59.60 50.14 59.14 48.72 58.64 C 47.29 58.15 45.71 57.72 44.20 57.13 C 42.70 56.54 41.12 56.02 39.71 55.11 C 38.30 54.19 36.68 53.16 35.73 51.64 C 34.78 50.12 34.15 47.66 34.01 46.00 C 33.87 44.34 34.42 42.94 34.91 41.67 C 35.40 40.39 36.21 39.29 36.96 38.34 C 37.72 37.39 38.63 36.67 39.44 35.98 C 40.26 35.28 41.11 34.74 41.86 34.17 C 42.61 33.61 43.34 33.11 43.96 32.59 C 44.57 32.07 45.10 31.58 45.54 31.04 C 45.97 30.50 46.31 30.01 46.56 29.33 C 46.80 28.66 46.85 27.78 47.00 27.00 A 3.00 3.00 0 0 1 53.00 27.00 Z",
)
RETIRED = (
    "M 20 56 A 30 30 0 0 1 80 56",  # v1 radar
    'rect x="16" y="16" width="68" height="13" rx="6.5"',  # flat horizon
    "M 50 29 C 50 41, 35 40, 35 51",  # thick small-size S
    "M 22.50 27.54 A 77.5 77.5 0 0 1 77.50 27.54",  # thick horizon
)
SVG = re.compile(r"<svg\b.*?</svg>", re.S)
CHROME = re.compile(r'<(a|div)\b[^>]*\bclass="(?:logo-link|footer-logo)"[^>]*>(.*?)</\1>', re.S)


def geometry_issues(svg, favicon=False):
    try:
        root = ET.fromstring(svg)
    except ET.ParseError:
        return ["invalid SVG"]
    paths = [element for element in root.iter() if element.tag.rsplit("}", 1)[-1] == "path"]
    issues = []
    if tuple(path.get("d") for path in paths) != STANDARD_PATHS:
        issues.append("non-canonical horizon or S path")
    expected_viewbox = "12.5 15 75 75" if favicon else "14 15 72 75"
    if root.get("viewBox") != expected_viewbox:
        issues.append("incorrect viewBox")
    if any("transform" in element.attrib or "stroke" in element.attrib for element in root.iter()):
        issues.append("transformed or stroked logo")
    if not favicon:
        groups = list(root)
        if len(groups) != 1 or groups[0].tag != "g" or groups[0].attrib != {"fill": "currentColor"}:
            issues.append("missing currentColor fill group")
        elif len(list(groups[0])) != 2 or any(path.attrib != {"d": expected} for path, expected in zip(paths, STANDARD_PATHS)):
            issues.append("unexpected logo elements or attributes")
    return issues


def main():
    failures, pages, count = [], 0, 0
    for path in sorted(ROOT.rglob("*.html")):
        if "node_modules" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        rel = str(path.relative_to(ROOT))
        if any(signature in text for signature in RETIRED):
            failures.append((rel, "retired logo geometry"))
        containers = CHROME.findall(text)
        pages += bool(containers)
        for _, container in containers:
            marks = SVG.findall(container)
            if len(marks) != 1:
                failures.append((rel, "logo container must contain exactly one SVG"))
            for mark in marks:
                count += 1
                issues = geometry_issues(mark)
                if issues:
                    failures.append((rel, ", ".join(issues)))

    for path in sorted((ROOT / "scripts").glob("*")):
        if path.suffix not in (".py", ".js") or path.name == Path(__file__).name:
            continue
        text = path.read_text(encoding="utf-8")
        rel = str(path.relative_to(ROOT))
        if any(signature in text for signature in RETIRED):
            failures.append((rel, "generator still contains retired geometry"))
        for mark in SVG.findall(text):
            if STANDARD_PATHS[0] in mark or STANDARD_PATHS[1][:25] in mark:
                issues = geometry_issues(mark)
                if issues:
                    failures.append((rel, ", ".join(issues)))

    favicon = ROOT / "favicon.svg"
    if not favicon.is_file():
        failures.append(("favicon.svg", "missing favicon"))
    else:
        issues = geometry_issues(favicon.read_text(encoding="utf-8"), favicon=True)
        if issues:
            failures.append(("favicon.svg", ", ".join(issues)))

    if not count:
        failures.append((".", "no logo marks found"))
    if failures:
        for rel, issue in failures[:20]:
            print(f"FAIL {rel}: {issue}")
        print(f"Logo geometry check failed: {len(failures)} violations")
        sys.exit(1)
    print(f"Logo geometry consistent: {count} marks on {pages} pages; generators and favicon match")


if __name__ == "__main__":
    main()
