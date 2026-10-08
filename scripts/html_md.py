#!/usr/bin/env python3
"""
Sayfa HTML'i → Markdown · sözlük ve keşif .md uç noktalarının ortak dönüştürücüsü.

Neden gerekti (2026-10-08): .md'ler (llms.txt ve <link rel=alternate> bunları
gösteriyor) her üreticide ayrı, regex ile ve eksik çıkarılıyordu:
- dictionary-en.py bölümden yalnız ilk <p>'yi alıyordu · liste, tablo, kod,
  "karıştırılır" kutusu düşüyordu (assembly.md'de 2 bölüm boştu).
- discover-en.py ilgili terimleri ve bağlantı adreslerini atıyordu (çeviri
  keşif .md'lerinin yarısı HTML içeriğinin %60'ından azını taşıyordu).
- discover-md.py ilgili terimleri bağlantısız tek satıra yapıştırıyordu.
Tek, HTML ağacını gezen bir dönüştürücü: sayfada ne varsa .md'de de o var.

Kullanım: from html_md import md_dosyasi; md_dosyasi(sayfa_html, "Source: … · <url>")
Statik, ağ yok. Guard: scripts/check-md-paritesi.py
"""
import re
from html.parser import HTMLParser

# Sayfa gövdesinde .md'ye girmeyen parçalar: geri linki, üst şerit (sözlükte
# kategori + tarih H1 altına taşınır), abonelik formu, kaydet şeridi, kopyala düğmeleri.
GURULTU = [r'<a class="disc-back".*?</a>', r'<div class="disc-top">.*?</div>',
           r'<aside class="disc-cta">.*?</aside>', r'<aside class="disc-save">.*?</aside>',
           r'<form\b.*?</form>', r'<button\b.*?</button>', r'<script\b.*?</script>']

BLOK = {"p", "div", "section", "article", "aside", "figure", "figcaption", "blockquote",
        "h1", "h2", "h3", "h4", "ul", "ol", "li", "pre", "table", "tr"}
BOS = {"br", "img", "input", "hr", "meta", "link", "source", "wbr"}


def _sinif(attrs):
    return (dict(attrs).get("class") or "").split()


class _Cevirici(HTMLParser):
    def __init__(self, taban):
        super().__init__(convert_charrefs=True)
        self.taban = taban
        self.bloklar = []      # (tür, metin) · tür: "p" | "li"
        self.buf = []          # satır içi metin
        self.yigin = []        # açık etiketlerin kapanış eylemleri
        self.listeler = []     # ["ul"|"ol", sayaç]
        self.onek = ""         # sıradaki bloğun öneki ("## ", "- ", "> " …)
        self.tur = "p"
        self.pre = None        # <pre> içi ham metin
        self.tablo = None      # satır listesi
        self.kod = 0           # açık satır içi <code> sayısı
        self.hucre = None      # hücre açıkken dış satır içi tampon (geri yüklenir)

    # · yardımcılar
    def _bosalt(self):
        metin = "".join(self.buf)
        self.buf = []
        metin = "\n".join(re.sub(r"[ \t\r\f\v]+", " ", s).strip() for s in metin.split("\n")).strip()
        if metin:
            self.bloklar.append((self.tur, self.onek + metin))
        self.onek, self.tur = "", "p"

    def _sar(self, idx, sol, sag=None):
        """buf[idx:]'ı işaretle sar · baştaki/sondaki boşluk işaretin dışına."""
        ic = "".join(self.buf[idx:])
        del self.buf[idx:]
        if not ic.strip():
            self.buf.append(ic)
            return
        bas = ic[:len(ic) - len(ic.lstrip())]
        son = ic[len(ic.rstrip()):]
        self.buf.append(bas + sol + ic.strip() + (sol if sag is None else sag) + son)

    def _adres(self, href):
        if href.startswith("/"):
            return self.taban + href
        return href

    def _li_baslat(self):
        self._bosalt()
        derinlik = max(len(self.listeler), 1)
        tur = self.listeler[-1] if self.listeler else ["ul", 0]
        tur[1] += 1
        isaret = f"{tur[1]}. " if tur[0] == "ol" else "- "
        self.onek, self.tur = "  " * (derinlik - 1) + isaret, "li"

    # · ayrıştırıcı olayları
    def handle_starttag(self, tag, attrs):
        if self.pre is not None:
            if tag not in BOS:
                self.yigin.append((tag, None))
            return
        if tag in BOS:
            if tag == "br":
                self.buf.append(" " if self.hucre is not None else "\n")
            return
        sinif = _sinif(attrs)
        eylem = None
        if self.tablo is not None and tag in ("td", "th"):
            self.hucre, self.buf = self.buf, []
            eylem = ("hucre",)
        elif self.tablo is not None and tag == "tr":
            self.tablo.append([])
        elif tag == "table":
            self._bosalt()
            self.tablo = []
            eylem = ("tablo",)
        elif tag == "pre":
            self._bosalt()
            self.pre = []
            eylem = ("pre",)
        elif tag in ("ul", "ol") or (tag == "div" and ({"disc-facts", "dict-related", "disc-related"} & set(sinif))):
            if self.tur == "li" or self.buf:
                self._bosalt()
            self.listeler.append(["ol" if tag == "ol" else "ul", 0])
            eylem = ("liste",)
        elif tag == "li" or (tag == "div" and "disc-fact" in sinif):
            self._li_baslat()
            eylem = ("blok",)
        elif tag == "a" and self.listeler and self.listeler[-1][0] == "ul" and self.yigin and self.yigin[-1][0] == "div" and self.yigin[-1][1] == ("liste",):
            # ilgili terimler/araçlar kutusu: her bağlantı bir madde
            self._li_baslat()
            eylem = ("a-li", len(self.buf), dict(attrs).get("href") or "")
        elif tag in ("h1", "h2", "h3", "h4"):
            self._bosalt()
            self.onek = "#" * int(tag[1]) + " "
            eylem = ("blok",)
        elif tag == "p" and "dict-en" in sinif:
            self._bosalt()
            self.onek = "> "
            eylem = ("blok",)
        elif tag == "p" and "dict-faq-q" in sinif:
            self._bosalt()
            eylem = ("kalin-blok", len(self.buf))
        elif tag == "div" and "disc-cmd-head" in sinif:
            self._bosalt()
            eylem = ("kalin-blok", len(self.buf))
        elif tag == "div" and "dict-analogy" in sinif:
            self._bosalt()
            eylem = ("italik-blok", len(self.buf))
        elif tag == "figcaption":
            self._bosalt()
            eylem = ("italik-blok", len(self.buf))
        elif tag in BLOK:
            self._bosalt()
            eylem = ("blok",)
        elif tag in ("strong", "b") or (tag == "span" and "disc-fact-k" in sinif):
            eylem = ("sar", len(self.buf), "**", ":**" if "disc-fact-k" in sinif else "**")
        elif tag in ("em", "i"):
            eylem = ("sar", len(self.buf), "*", "*")
        elif tag == "code":
            self.kod += 1
            eylem = ("sar-kod", len(self.buf), "`", "`")
        elif tag == "a":
            eylem = ("a", len(self.buf), dict(attrs).get("href") or "")
        elif tag == "span" and "disc-fact-v" in sinif:
            self.buf.append(" ")
        self.yigin.append((tag, eylem))

    def handle_endtag(self, tag):
        if tag in BOS:
            return
        # kapanışı eşleşen açılışa kadar yığını sar (bozuk HTML'e karşı)
        while self.yigin:
            t, eylem = self.yigin.pop()
            self._kapat(eylem)
            if t == tag:
                break

    def _kapat(self, eylem):
        if eylem is None:
            return
        tur = eylem[0]
        if tur == "pre":
            kod = "".join(self.pre).strip("\n")
            self.pre = None
            self.bloklar.append(("p", f"```\n{kod}\n```"))
        elif tur == "hucre":
            hucre = re.sub(r"\s+", " ", "".join(self.buf)).strip().replace("|", "\\|")
            self.buf, self.hucre = self.hucre, None
            if self.tablo:
                self.tablo[-1].append(hucre)
        elif tur == "tablo":
            satirlar = [s for s in self.tablo if s]
            self.tablo = None
            if satirlar:
                gen = max(len(s) for s in satirlar)
                satirlar = [s + [""] * (gen - len(s)) for s in satirlar]
                cizgi = ["| " + " | ".join(satirlar[0]) + " |", "|" + "---|" * gen]
                cizgi += ["| " + " | ".join(s) + " |" for s in satirlar[1:]]
                self.bloklar.append(("p", "\n".join(cizgi)))
        elif tur == "liste":
            self._bosalt()
            self.listeler.pop()
            if not self.listeler:
                self.bloklar.append(("ayrac", ""))  # iki ayrı liste birleşmesin
        elif tur in ("blok",):
            self._bosalt()
        elif tur == "kalin-blok":
            self._sar(eylem[1], "**")
            self._bosalt()
        elif tur == "italik-blok":
            self._sar(eylem[1], "*")
            self._bosalt()
        elif tur in ("sar", "sar-kod"):
            if tur == "sar-kod":
                self.kod -= 1
            self._sar(eylem[1], eylem[2], eylem[3])
        elif tur in ("a", "a-li"):
            idx, href = eylem[1], eylem[2]
            if href and not href.startswith("#"):
                ic = "".join(self.buf[idx:]).strip()
                del self.buf[idx:]
                if ic:
                    self.buf.append(f"[{ic}]({self._adres(href)})")
            if tur == "a-li":
                self._bosalt()

    def handle_data(self, data):
        if self.pre is not None:
            self.pre.append(data)
        elif self.kod:
            self.buf.append(data)
        else:
            # düz metindeki "<branch>" markdown'da etiket sanılıp gizlenmesin
            self.buf.append(data.replace("<", "\\<"))

    def sonuc(self):
        while self.yigin:
            self._kapat(self.yigin.pop()[1])
        self._bosalt()
        out = []
        onceki = None
        for tur, metin in self.bloklar:
            if tur == "ayrac":
                onceki = tur
                continue
            if out:
                out.append("\n" if tur == "li" and onceki == "li" else "\n\n")
            out.append(metin)
            onceki = tur
        return "".join(out).strip() + "\n"


def sayfa_md(sayfa_html, taban="https://trescout.com"):
    """Sayfanın <article class="disc"> gövdesini Markdown'a çevirir."""
    m = re.search(r'<article class="disc">(.*?)</article>', sayfa_html, re.S)
    if not m:
        return None
    govde = m.group(1)
    # Sözlük üst şeridi (kategori + son güncelleme) H1'in altına tek satır olarak
    # taşınır · keşifteki günlük ivme ("↑ +142 today") her gün değiştiği için alınmaz.
    ust = re.search(r'<div class="disc-top"><span class="disc-eyebrow">(.*?)</span>'
                    r'<time class="dict-time"[^>]*>(.*?)</time></div>', govde, re.S)
    if ust:
        govde = re.sub(r"(</h1>)", lambda h: f"{h.group(1)}<p><em>{ust.group(1)} · {ust.group(2)}</em></p>", govde, count=1)
    for pat in GURULTU:
        govde = re.sub(pat, "", govde, flags=re.S)
    c = _Cevirici(taban)
    c.feed(govde)
    c.close()
    return c.sonuc()


def md_dosyasi(sayfa_html, kaynak, taban="https://trescout.com"):
    """.md dosyasının tamamı · gövde + kaynak satırı. Üreticiler ve md-uret.py aynı biçimi yazar."""
    govde = sayfa_md(sayfa_html, taban)
    return None if govde is None else f"{govde}\n---\n{kaynak}\n"
