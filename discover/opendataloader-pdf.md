# PDF verilerini yapay zekâya hazırlayın

OpenDataLoader PDF, yapay zekâ modelleri için veriyi hazır hale getiren açık kaynaklı bir PDF ayrıştırıcıdır (PDF parser). Java tabanlı bu proje, PDF belgelerinin erişilebilirliğini otomatikleştirerek veri işleme süreçlerini hızlandırır.

- ★ 28.095
- Java
- GitHub Trending · 2026-06-04

## Güncelleme
- 2 Ağustos 2026: Yıldız 23.530 → 28.095, son sürüm v2.5.0 (14 Temmuz 2026).

## Ne kazandırır?
- PDF dosyalarını yapay zekâ modelleri için Markdown, JSON veya HTML formatına dönüştürür.
- Taranmış belgeler ve karmaşık tablolar için yüksek doğrulukta veri ayıklama sağlar.
- Erişilebilirlik standartlarına uygun olarak PDF dosyalarını otomatik etiketler.

## Kurulum

**Python ile kurulum**

```
pip install -U opendataloader-pdf
```

**Hibrit mod ile kurulum**

```
pip install -U "opendataloader-pdf[hybrid]"
```

## Çalıştırma

**PDF dönüştürme işlemi**

```
import opendataloader_pdf

# Batch all files in one call — each convert() spawns a JVM process, so repeated calls are slow
opendataloader_pdf.convert(
input_path=["file1.pdf", "file2.pdf", "folder/"],
output_dir="output/",
format="markdown,json"
)
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
OpenDataLoader PDF aracını kullanarak elimdeki PDF dosyalarını analiz etmek ve bunları RAG veya LLM süreçlerinde kullanabileceğim yapılandırılmış veri formatlarına (Markdown veya JSON) dönüştürmek istiyorum. Python SDK'sını kullanarak yerel bilgisayarımda çalışacak şekilde, belgelerimdeki tabloları, başlıkları ve metinleri doğru okuma sırasıyla ayıklayacak bir betik hazırlamama yardımcı olur musun? Ayrıca karmaşık sayfalar için hibrit modun nasıl aktif edileceğini ve çıktıların nasıl özelleştirileceğini adım adım açıkla.

- **Kimin için:** PDF belgelerini yapay zekâ modelleri için yapılandırılmış veriye dönüştürmek isteyen geliştiriciler ve PDF erişilebilirliğini otomatize etmesi gereken kullanıcılar içindir. 
- **Lisans:** Apache-2.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/opendataloader-project/opendataloader-pdf)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-04 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
PDF Parser Parser SDK RAG Markdown PDF

---
Kaynak: TreScout Keşif · https://trescout.com/discover/opendataloader-pdf/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
