#!/usr/bin/env python3
"""Telemetry coverage guard for content and product-conversion pages."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent


def html_files():
    return ROOT.rglob("*.html")


def main():
    checked = 0
    report_checked = 0
    form_checked = 0
    missing = []
    for path in html_files():
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        is_report_page = (
            'data-page-type="report"' in text
            or 'class="signup-cta"' in text
        )
        is_form_page = "js-subscribe" in text
        if not (is_report_page or is_form_page):
            continue

        checked += 1
        has_direct_telemetry = "/assets/telemetry.js" in text
        has_loader = "/assets/subscribe.js" in text or "/assets/index.js" in text

        # Report detail pages have no shared form loader. Keep their analytics
        # dependency explicit so a future generator cannot silently omit it.
        if is_report_page:
            report_checked += 1
            if not has_direct_telemetry:
                missing.append(f"{path.relative_to(ROOT)} (report requires direct telemetry)")
            continue

        form_checked += 1
        if not has_direct_telemetry and not has_loader:
            missing.append(f"{path.relative_to(ROOT)} (form requires direct telemetry or loader)")

    if missing:
        print("Telemetry coverage guard failed:")
        print("\n".join(f"- {item}" for item in missing))
        return 1

    print(
        "Telemetry coverage guard passed: "
        f"{checked} conversion pages checked "
        f"({report_checked} report pages direct, {form_checked} form pages direct/loader)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
