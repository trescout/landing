#!/usr/bin/env python3
"""Keşif sayfası "Kod bilmiyorsanız" ajan istemine sabit satırlar.

Gemini'nin README'den yazdığı istem gövdesi (amaç + gerçek komutlar) olduğu gibi
kalır; altına, okurun yapay zekâ kodlama ajanına (Claude Code · Codex ·
Antigravity) yapıştıracağı sabit satırlar eklenir ve Kopyala hepsini kopyalar.
Kaynak: DeepLearning.AI dersleri (2026-10-16 ders iş listesi):
  - depo + README'deki resmî talimatı esas al (J3: istemdeki komut doğrulanmıyordu;
    2026-10-16 ölçümü ~53 komut anışından 6'sı sayfanın komut bloklarında yoktu)
  - işletim sistemi ve ön koşul kontrolü (A1, Y1: 448 istemin 0'ında vardı)
  - yeni boş klasör, dosya silme yok, her komuttan önce açıklama (J4)
  - API anahtarı sohbete yazılmaz, .env ve git dışı (Y2: yalnız anahtar geçen istem)
  - her adımda ne görülmeli + hata mesajını yapıştırma (A1, A2)
Satırlar okurun ajana sesi olduğu için ajana "sen" diye hitap eder (gövdeyle aynı).
Diğer diller: scripts/diller.py "ajan_ek_*" (discover-en.py basar).

Kullanım (mevcut Türkçe sayfalar):
  python3 scripts/ajan_istemi.py             # sıkı: her istem satırları taşımalı
  python3 scripts/ajan_istemi.py --gecis     # CI: her istem satırlı ya da --uygula ile eklenebilir
  python3 scripts/ajan_istemi.py --uygula    # eksik satırları ekler
"""
import glob
import html
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TR = {
    "ajan_ek_depo": "Depo: {url}. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.",
    "ajan_ek_sistem": ("Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, "
                       "Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre "
                       "adım adım kur."),
    "ajan_ek_klasor": ("Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, "
                       "hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle."),
    "ajan_ek_anahtar": ("Bir API anahtarı gerekirse onu sohbete yazmamı isteme. .env dosyasına nasıl ekleyeceğimi "
                        "göster ve bu dosyanın Git'e gönderilmediğinden emin ol."),
    "ajan_ek_hata": ("Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana "
                     "olduğu gibi yapıştıracağım, birlikte düzeltelim."),
}
SIRA = ("ajan_ek_depo", "ajan_ek_sistem", "ajan_ek_klasor", "ajan_ek_anahtar", "ajan_ek_hata")
# İstem gövdesinde API anahtarı / token geçiyorsa anahtar satırı eklenir
ANAHTAR = re.compile(r"(?i)api\s*(anahtar|key)|\banahtar(ı|ını|ınızı|ımı|lar)\b|\btoken\b|\.env\b")
EK = re.compile(r'<p class="disc-ai-ek">(.*?)</p>', re.S)
# "Kod bilmiyorsanız" istem kutusu: başlığı "… ajanınıza (Claude Code · …) yapıştırın" (436 sayfa;
# 45'i "Yapay zekâ ile nasıl kullanılır?" bölümünde). Editöryel "İlk adım için hazır istem" hariç.
BLOK = re.compile(r'<div class="disc-ai"><div class="disc-ai-head"><span>[^<]*ajanınıza[^<]*</span>.*?</div>'
                  r'(<p class="disc-ai-text">(.*?)</p>)((?:<p class="disc-ai-ek">.*?</p>)*)</div>', re.S)


def satirlar(metinler, url, govde):
    """Sabit satırlar (sırayla). metinler: TR ya da diller.py sözlüğü."""
    out = []
    for k in SIRA:
        if k == "ajan_ek_depo" and not url:
            continue
        if k == "ajan_ek_anahtar" and not ANAHTAR.search(govde or ""):
            continue
        out.append(metinler[k].replace("{url}", url or ""))
    return out


def ek_html(satir_listesi, esc=html.escape):
    return "".join(f'<p class="disc-ai-ek">{esc(s)}</p>' for s in satir_listesi)


def _depo(h):
    m = re.search(r'"codeRepository":\s*"([^"]+)"', h)
    return m.group(1) if m else ""


def main():
    uygula = "--uygula" in sys.argv
    gecis = "--gecis" in sys.argv
    tamam = eklenen = 0
    eksik = []
    for yol in sorted(glob.glob(os.path.join(ROOT, "discover", "*", "index.html"))):
        h = open(yol, encoding="utf-8").read()
        m = BLOK.search(h)
        if not m:
            continue
        govde_p, govde_metni, mevcut = m.group(1), html.unescape(m.group(2)), m.group(3)
        beklenen = satirlar(TR, _depo(h), govde_metni)
        if [html.unescape(x) for x in EK.findall(mevcut)] == beklenen:
            tamam += 1
            continue
        if not mevcut and uygula:
            yeni = m.group(0).replace(govde_p, govde_p + ek_html(beklenen), 1)
            open(yol, "w", encoding="utf-8").write(h.replace(m.group(0), yeni, 1))
            eklenen += 1
        elif not mevcut and gecis:
            tamam += 1
        else:
            eksik.append(os.path.relpath(yol, ROOT))
    if uygula:
        print(f"→ Ajan istemi satırları: {eklenen} sayfaya eklendi, {tamam} sayfa zaten güncel")
    if eksik:
        print(f"❌ Ajan istemi: {len(eksik)} sayfada satırlar eksik ya da güncel değil (otomatik eklenemiyor)")
        for yol in eksik[:20]:
            print(f"   {yol}")
        sys.exit(1)
    if not uygula:
        print(f"✓ Ajan istemi satırları · {tamam} keşif sayfası{' (geçiş)' if gecis else ''}")


if __name__ == "__main__":
    main()
