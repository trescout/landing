#!/usr/bin/env python3
"""CSP inline-content guard.

Strict CSP yürürlükte (`script-src 'self'; style-src 'self'`). Bu yüzden hiçbir
HTML sayfasında şunlar OLMAMALI (tarayıcı bloklar → sayfa stilsiz/işlevsiz kalır):
  • inline <style> bloğu
  • style="..." attribute
  • inline çalıştırılan <script> (harici src yok)

İZİNLİ:
  • <script src="..."> (harici dosya · 'self' kapsar)
  • <script type="application/ld+json"> (data block · CSP'ye tabi değil)

Yerel kullanım:  python3 scripts/check-no-inline-csp.py
Çıkış kodu 1 → ihlal var (CI fail eder).
"""
import sys, re, glob, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

files = set(glob.glob(os.path.join(ROOT, "*.html")))
files |= set(glob.glob(os.path.join(ROOT, "reports", "**", "*.html"), recursive=True))

STYLE_ATTR = re.compile(r'\sstyle\s*=')
SCRIPT_OPEN = re.compile(r'<script\b([^>]*)>', re.IGNORECASE)
LDJSON = re.compile(r'type\s*=\s*["\']application/ld\+json["\']', re.IGNORECASE)

violations = []
for f in sorted(files):
    rel = os.path.relpath(f, ROOT)
    text = open(f, encoding="utf-8").read()

    for i, line in enumerate(text.splitlines(), 1):
        if "<style" in line.lower():
            violations.append((rel, i, "inline <style> bloğu", line.strip()[:90]))
        if STYLE_ATTR.search(line):
            violations.append((rel, i, "inline style= attribute", line.strip()[:90]))

    for m in SCRIPT_OPEN.finditer(text):
        attrs = m.group(1)
        if "src=" in attrs.lower():
            continue                      # harici · izinli
        if LDJSON.search(attrs):
            continue                      # JSON-LD data block · CSP-muaf
        line_no = text[:m.start()].count("\n") + 1
        violations.append((rel, line_no, "inline çalıştırılan <script>", m.group(0)[:90]))

if violations:
    print("❌ CSP guard: inline içerik bulundu — strict CSP bunu bloklar:\n")
    for rel, ln, kind, snippet in violations:
        print(f"  {rel}:{ln} · {kind}")
        print(f"      {snippet}")
    print(f"\nToplam {len(violations)} ihlal. Inline CSS/JS'i /assets/ altında harici dosyaya taşıyın.")
    print("(JSON-LD ve <script src> izinlidir.)")
    sys.exit(1)

print(f"✅ CSP guard: {len(files)} sayfada inline <style>/<script>/style= yok.")
