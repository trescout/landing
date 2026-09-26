#!/usr/bin/env python3
"""
Gemini model zinciri guard'ı (CI).
Landing'de Gemini dört ayrı betikten çağrılıyordu ve her biri model adını ve
429 davranışını kendi içinde tutuyordu. Zincir artık iki yerde:
  - scripts/gemini_zinciri.py   (Python: translation_service, dict-sync, discover-sync)
  - scripts/translation-service.js (JS: translate-i18n ve rapor çevirileri)
Bu guard iki kaymayı yakalar:
  1. Bu iki dosya dışında Gemini adresi ya da sabit model adı yazılması
     (yeni bir betik zinciri atlayıp tek modele bağlanmasın).
  2. İki dosyadaki varsayılan zincirin birbirinden ayrılması.
Kullanım: python3 scripts/check-gemini-zinciri.py
"""
import os, re, glob, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = os.path.join(ROOT, "scripts", "gemini_zinciri.py")
JS = os.path.join(ROOT, "scripts", "translation-service.js")
IZINLI = {os.path.abspath(PY), os.path.abspath(JS), os.path.abspath(__file__)}
DESEN = re.compile(r"generativelanguage\.googleapis\.com|[\"']gemini-\d[\w.-]*[\"']")

hatalar = []
for p in sorted(glob.glob(os.path.join(ROOT, "scripts", "*.py")) + glob.glob(os.path.join(ROOT, "scripts", "*.js"))
                + glob.glob(os.path.join(ROOT, "scripts", "*.mjs")) + glob.glob(os.path.join(ROOT, "api", "**", "*.*"), recursive=True)):
    if os.path.abspath(p) in IZINLI or ".test." in p:
        continue
    for no, satir in enumerate(open(p, encoding="utf-8", errors="replace"), 1):
        if DESEN.search(satir):
            hatalar.append(f"{os.path.relpath(p, ROOT)}:{no}: Gemini adresi/modeli zincir dışında · gemini_zinciri.py kullanın")

def varsayilan(yol, desen):
    """Atamadaki tüm string parçalarını birleştir (zincir birden çok satıra bölünüyor)."""
    m = re.search(desen, open(yol, encoding="utf-8").read(), re.S)
    return "".join(re.findall(r"[\"']([^\"']*)[\"']", m.group(1))) if m else None

py_zincir = varsayilan(PY, r"VARSAYILAN_ZINCIR = \((.*?)\)\n")
js_zincir = varsayilan(JS, r"const DEFAULT_CHAIN = (.*?);\n")
if not py_zincir or not js_zincir:
    hatalar.append("varsayılan zincir iki dosyadan birinde bulunamadı (guard deseni güncellenmeli)")
elif py_zincir != js_zincir:
    hatalar.append(f"varsayılan zincir ayrıştı · py={py_zincir} js={js_zincir}")

if hatalar:
    print("❌ Gemini zincir guard'ı:")
    for h in hatalar:
        print("  -", h)
    sys.exit(1)
print(f"✅ Gemini zinciri tek yerde · varsayılan: {py_zincir}")
