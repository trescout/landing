#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TreScout · 1 Dakikalık Sesli Günlük Teknoloji Özeti Üreticisi
============================================================
Günlük teknoloji raporunu (reports/{tarih}/index.html) alarak 60-90 saniyelik
doğal radyo/podcast tarzı bir Türkçe sesli bülten metni ve ses dosyası üretir.

Kullanım:
    python3 scripts/generate-audio-digest.py [--date YYYY-MM-DD] [--voice tr-TR-AhmetNeural]
"""

import os
import re
import sys
import json
import argparse
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS_DIR = os.path.join(ROOT, "reports")


def en_son_rapor_tarihi():
    if not os.path.isdir(REPORTS_DIR):
        return None
    dates = [d for d in os.listdir(REPORTS_DIR) if re.match(r"^\d{4}-\d{2}-\d{2}$", d)]
    return sorted(dates, reverse=True)[0] if dates else None


def metin_temizle(html_text):
    return re.sub(r"<[^>]+>", "", html_text or "").strip()


def rapor_verisi_cikar(tarih):
    rapor_yolu = os.path.join(REPORTS_DIR, tarih, "index.html")
    if not os.path.exists(rapor_yolu):
        raise FileNotFoundError(f"Rapor bulunamadı: {rapor_yolu}")

    with open(rapor_yolu, "r", encoding="utf-8") as f:
        html = f.read()

    # Başlık & Tarih
    baslik_m = re.search(r'<h1 class="rep-title">(.*?)</h1>', html)
    baslik = metin_temizle(baslik_m.group(1)) if baslik_m else tarih

    # Editöryel özet
    editorial_m = re.search(r'<p class="rep-editorial">(.*?)</p>', html)
    editorial = metin_temizle(editorial_m.group(1)) if editorial_m else ""

    # Öne çıkan araçlar
    araclar = []
    for m in re.finditer(r'<a class="rep-link-item" href="/discover/([^/]+)/">([^<]+)</a>', html):
        slug = m.group(1)
        ad = m.group(2).replace("→", "").strip()
        araclar.append({"slug": slug, "name": ad})

    # Öne çıkan terimler
    terimler = []
    for m in re.finditer(r'<a class="rep-link-item" href="/dictionary/([^/]+)/">([^<]+)</a>', html):
        slug = m.group(1)
        ad = m.group(2).replace("→", "").strip()
        terimler.append({"slug": slug, "name": ad})

    return {
        "tarih": tarih,
        "baslik": baslik,
        "editorial": editorial,
        "araclar": araclar[:4],  # İlk 3-4 araç
        "terimler": terimler[:3]
    }


def bulten_metni_uret(veri):
    """
    Doğal konuşma ritminde, ~150-180 kelimelik 1 dakikalık ses metni oluşturur.
    """
    baslik = veri["baslik"]
    editorial = veri["editorial"]
    araclar = veri["araclar"]

    # Giriş
    paragraflar = [
        f"Merhaba! TreScout ile bir dakikada günün teknoloji özetine hoş geldiniz.",
        f"Bugün {baslik}.",
        editorial
    ]

    # Araç vurguları
    if araclar:
        arac_adlari = [a["name"] for a in araclar[:3]]
        if len(arac_adlari) == 1:
            vurgu = f"Günün öne çıkan açık kaynak projesinde {arac_adlari[0]} dikkat çekiyor."
        elif len(arac_adlari) == 2:
            vurgu = f"Açık kaynak dünyasında bugün öne çıkan projeler: {arac_adlari[0]} ve {arac_adlari[1]}."
        else:
            vurgu = f"Bugün açık kaynak trendlerinde öne çıkan üç proje: {arac_adlari[0]}, {arac_adlari[1]} ve {arac_adlari[2]}."
        paragraflar.append(vurgu)

    # Kapanış
    paragraflar.append(
        "Tüm projelerin kurulum komutları ve tam PDF rapor trescout.com arşivinde. Yarın sabah görüşmek üzere!"
    )

    return "\n\n".join(paragraflar)


def ses_uret(metin, cikti_mp3, ses_kodu="tr-TR-AhmetNeural"):
    """
    TTS motoru ile mp3 üretimi (önce edge-tts, yoksa macOS say komutu).
    """
    # 1. edge-tts dene
    try:
        cmd = ["edge-tts", "--voice", ses_kodu, "--text", metin, "--write-media", cikti_mp3]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if res.returncode == 0 and os.path.exists(cikti_mp3):
            return True, "edge-tts"
    except Exception:
        pass

    # 2. macOS 'say' komutu dene (AIFF -> MP3 veya doğrudan ses)
    if sys.platform == "darwin":
        try:
            aiff_path = cikti_mp3.replace(".mp3", ".aiff")
            cmd = ["say", "-v", "Yelda", metin, "-o", aiff_path]
            res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if res.returncode == 0 and os.path.exists(aiff_path):
                # ffmpeg varsa aiff -> mp3 çevir
                try:
                    subprocess.run(["ffmpeg", "-y", "-i", aiff_path, cikti_mp3],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    if os.path.exists(cikti_mp3):
                        os.remove(aiff_path)
                        return True, "macOS say + ffmpeg"
                except Exception:
                    pass
                return True, "macOS say (aiff)"
        except Exception:
            pass

    return False, "TTS motoru bulunamadı (metin başarıyla kaydedildi)"


def main():
    parser = argparse.ArgumentParser(description="TreScout 1-Dakikalık Sesli Günlük Özet Üreticisi")
    parser.add_argument("--date", help="Rapor tarihi (YYYY-MM-DD formatında, varsayılan: en son rapor)")
    parser.add_argument("--voice", default="tr-TR-AhmetNeural", help="TTS ses kodu (varsayılan: tr-TR-AhmetNeural)")
    args = parser.parse_args()

    tarih = args.date or en_son_rapor_tarihi()
    if not tarih:
        print("Hata: İşlenecek rapor bulunamadı.")
        sys.exit(1)

    print(f"🎙️ TreScout Sesli Özet Hazırlanıyor: {tarih}")
    veri = rapor_verisi_cikar(tarih)
    script_text = bulten_metni_uret(veri)

    hedef_klasor = os.path.join(REPORTS_DIR, tarih)
    metin_dosyasi = os.path.join(hedef_klasor, "audio-digest.txt")
    mp3_dosyasi = os.path.join(hedef_klasor, "audio-digest.mp3")

    with open(metin_dosyasi, "w", encoding="utf-8") as f:
        f.write(script_text)

    print(f"  📝 Bülten metni yazıldı: {metin_dosyasi} ({len(script_text.split())} kelime)")

    ok, motor = ses_uret(script_text, mp3_dosyasi, args.voice)
    if ok:
        print(f"  🔊 Ses dosyası üretildi ({motor}): {mp3_dosyasi}")
    else:
        print(f"  ℹ️ {motor}. Metin dosyası hazır.")

    print("✅ 1-Dakikalık sesli özet işlemi tamamlandı.")


if __name__ == "__main__":
    main()
