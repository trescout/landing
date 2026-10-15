"""Gemini çıktısındaki marka yazım hatalarını yayından ÖNCE düzeltir (2026-10-15).

İstemdeki kural ("AI değil yapay zekâ", "Hugging Face") garanti değil; model zaman
zaman uymuyor ve hata sayfaya, oradan çeviri önbelleğine yerleşiyor. 15 Ekim'de
binlerce sayfada elle temizlendi (landing#327, #329). Buradaki düzeltme deterministik:

- "HuggingFace" → "Hugging Face" (model kimliği HuggingFaceTB/..., sınıf adı
  HuggingFaceEmbeddings ve URL'ler korunur)
- "yapay zeka/zekanın" → "yapay zekâ/zekânın"
- Türkçe "AI ajan/asistan/destekli/..." → "yapay zekâ ..." ("Agentic AI" gibi terim
  adları ve İngilizce "AI models" korunur)

Ayna: app/lib/ai/marka-metin.ts (rapor özetleri). Denetim: check-brand-typography.py.
"""
import re

HF = re.compile(r"(?<![\w/.@-])HuggingFace(?![\w/-])")
YZ = re.compile(r"\b([Yy])apay [Zz]eka(?=[a-zçğıöşü]|\b)")
AI = re.compile(r"(?<![\w-])(Agentic |Generative |Physical |Open Source )?AI "
                r"(ajan|asistan|destekli|dostu|karakter|tabanlı|model|araç|ile)([a-zçğıöşüâ]*)")


def _ai(s):
    def r(m):
        if m.group(1) or (m.group(2) == "model" and m.group(3).startswith("s")):
            return m.group(0)
        bas = s[:m.start()]
        buyuk = not bas.strip() or re.search(r"[.!?]\s+$", bas)
        return ("Yapay" if buyuk else "yapay") + " zekâ " + m.group(2) + m.group(3)
    return AI.sub(r, s)


def duzelt(s):
    """Türkçe metin için tüm kurallar."""
    if not isinstance(s, str):
        return s
    return _ai(YZ.sub(lambda m: m.group(1) + "apay zekâ", HF.sub("Hugging Face", s)))


def duzelt_hf(s):
    """Türkçe dışı metin için yalnız "Hugging Face" · Türkçe kalıplar ("AI model" →
    "yapay zekâ model") İngilizce cümleyi bozardı."""
    return HF.sub("Hugging Face", s) if isinstance(s, str) else s


def json_duzelt(o, atla=()):
    """Gemini'nin JSON yanıtında her metin alanını düzeltir; `atla`daki anahtarlar
    (kurulum komutu, İngilizce terim adı) olduğu gibi kalır."""
    if isinstance(o, str):
        return duzelt(o)
    if isinstance(o, list):
        return [json_duzelt(x, atla) for x in o]
    if isinstance(o, dict):
        return {k: (v if k in atla else json_duzelt(v, atla)) for k, v in o.items()}
    return o
