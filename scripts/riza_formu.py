#!/usr/bin/env python3
"""Kayıt formunun bilgilendirme + onay bloğu · TEK KAYNAK (2026-10-08, #210).

KVKK Kurulu'nun 2026/347 sayılı ilke kararı (RG 24.03.2026): aydınlatma ile
açık rıza ayrı düzenlenir, aydınlatma yapıldığına dair onay istenmez. Eski
form "Aydınlatma Metni'ni okudum, ... onaylıyorum" diyordu ve ana sayfadaki
pencere "Okudum, onaylıyorum" düğmesine basılmadan kutuyu açmıyordu.

Yeni yapı, her `form.js-subscribe` içinde:
  <p class="form-notice">Bilgilendirme cümlesi + Aydınlatma Metni bağlantısı</p>
  <label class="form-consent"><input type="checkbox" name="consent" required>
    <span>Belirli amaca yönelik onay cümlesi (metne atıf yok)</span></label>

Metinler scripts/riza-metni.json'da. Python üreticiler `blok()` çağırır, JS
üreticiler JSON'u okur. Bot commit'leri [skip ci] ile guard'ı atladığı için
üreticilerin kendisi doğru metni basmalı; bu betik ayrıca günlük hatta
düzeltici olarak koşar ve CI'da denetler.

Kullanım:
  python3 scripts/riza_formu.py           tüm sayfaları kanonik bloğa çevirir
  python3 scripts/riza_formu.py --check   sapma varsa listeler, 1 ile çıkar
"""
import glob
import json
import os
import re
import sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
METIN = json.load(open(os.path.join(KOK, "scripts", "riza-metni.json"), encoding="utf-8"))
GIZLILIK = {"tr": "/privacy.html", "en": "/en/privacy.html", "fr": "/fr/privacy.html",
            "pt": "/pt/privacy.html", "es": "/es/privacy.html", "de": "/de/privacy.html"}

FORM = re.compile(r'(<form[^>]*class="[^"]*js-subscribe[^"]*"[^>]*>)([\s\S]*?)(</form>)')
# Eski ya da yeni blok: varsa önündeki bilgilendirme paragrafı + onay etiketi.
BLOK = re.compile(r'(?:<p class="form-notice">[\s\S]*?</p>\s*)?<label class="form-consent">[\s\S]*?</label>')
HTML_LANG = re.compile(r'<html[^>]*\blang="([a-zA-Z-]+)"')


def dil_kodu(lang):
    kod = (lang or "tr").split("-")[0].lower()
    return kod if kod in METIN else "tr"


def blok(dil, modal=False):
    """Kanonik bilgilendirme + onay bloğu. modal=True: bağlantı ana sayfadaki pencereyi açar."""
    m = METIN[dil_kodu(dil)]
    nitelik = " data-privacy-modal" if modal else ' target="_blank" rel="noopener"'
    baglanti = f'<a href="{GIZLILIK[dil_kodu(dil)]}"{nitelik}>{m["baglanti_metni"]}</a>'
    return (f'<p class="form-notice">{m["bilgi"].format(baglanti=baglanti)}</p>'
            f'<label class="form-consent"><input type="checkbox" name="consent" required>'
            f'<span>{m["onay"]}</span></label>')


def sayfa_dili(html):
    m = HTML_LANG.search(html)
    return dil_kodu(m.group(1) if m else "tr")


def duzelt(html):
    """Sayfadaki her kayıt formunun bloğunu kanoniğe çevirir. (yeni_html, değişen_form_sayısı)"""
    dil = sayfa_dili(html)
    modal = 'id="privacy-modal"' in html
    hedef = blok(dil, modal)
    say = 0

    def form_duzelt(m):
        nonlocal say
        govde = m.group(2)
        if BLOK.search(govde):
            yeni = BLOK.sub(lambda _: hedef, govde, count=1)
        else:
            # Blok hiç yoksa honeypot'tan önce ekle, o da yoksa formun sonuna.
            hp = govde.find('<input type="text" name="website"')
            yeni = govde[:hp] + hedef + govde[hp:] if hp >= 0 else govde + hedef
        if yeni != govde:
            say += 1
        return m.group(1) + yeni + m.group(3)

    return FORM.sub(form_duzelt, html), say


def sayfalar():
    for p in sorted(glob.glob(os.path.join(KOK, "**", "*.html"), recursive=True)):
        if "/node_modules/" in p:
            continue
        yield p


def main():
    kontrol = "--check" in sys.argv
    sapma, degisen_sayfa, form_say = [], 0, 0
    for p in sayfalar():
        html = open(p, encoding="utf-8").read()
        if "js-subscribe" not in html:
            continue
        form_say += len(FORM.findall(html))
        yeni, say = duzelt(html)
        if not say:
            continue
        rel = os.path.relpath(p, KOK)
        if kontrol:
            sapma.append(rel)
        else:
            open(p, "w", encoding="utf-8").write(yeni)
            degisen_sayfa += 1
    if kontrol:
        if sapma:
            print(f"✗ {len(sapma)} sayfada kayıt formu kanonik bilgilendirme/onay bloğunu taşımıyor "
                  f"(düzeltmek için: python3 scripts/riza_formu.py)")
            for r in sapma[:10]:
                print("  ", r)
            sys.exit(1)
        print(f"✓ rıza formu · {form_say} formun hepsi kanonik blokta")
    else:
        print(f"rıza formu · {form_say} form · {degisen_sayfa} sayfa güncellendi")


if __name__ == "__main__":
    main()
