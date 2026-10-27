# PDF verilerini yapay zekâya hazırlayın

OpenDataLoader PDF, yapay zekâ modelleri için veriyi hazır hale getiren açık kaynaklı bir PDF ayrıştırıcıdır (PDF parser). Java tabanlı bu proje, PDF belgelerinin erişilebilirliğini otomatikleştirerek veri işleme süreçlerini hızlandırır.

- ★ 30.057
- Java
- GitHub Trending · 2026-06-04

## Güncelleme

- **27 Ekim 2026:** Yıldız 29.817 → 30.057, son sürüm v2.5.16 (27 Ekim 2026).
- **22 Ekim 2026:** Yıldız 29.752 → 29.817, son sürüm v2.5.15 (22 Ekim 2026).
- **21 Ekim 2026:** Yıldız 29.669 → 29.752, son sürüm v2.5.14 (21 Ekim 2026).
- **13 Ekim 2026:** Yıldız 29.447 → 29.669, son sürüm v2.5.13 (13 Ekim 2026).

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

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

OpenDataLoader PDF aracını kullanarak elimdeki PDF dosyalarını analiz etmek ve bunları RAG veya LLM süreçlerinde kullanabileceğim yapılandırılmış veri formatlarına (Markdown veya JSON) dönüştürmek istiyorum. Python SDK'sını kullanarak yerel bilgisayarımda çalışacak şekilde, belgelerimdeki tabloları, başlıkları ve metinleri doğru okuma sırasıyla ayıklayacak bir betik hazırlamama yardımcı olur musun? Ayrıca karmaşık sayfalar için hibrit modun nasıl aktif edileceğini ve çıktıların nasıl özelleştirileceğini adım adım açıkla.

Depo: https://github.com/opendataloader-project/opendataloader-pdf. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** PDF belgelerini yapay zekâ modelleri için yapılandırılmış veriye dönüştürmek isteyen geliştiriciler ve PDF erişilebilirliğini otomatize etmesi gereken kullanıcılar içindir.
- **Lisans:** Apache-2.0

## Bağlantılar

- [GitHub deposu →](https://github.com/opendataloader-project/opendataloader-pdf)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-06-04 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [PDF Parser](https://trescout.com/dictionary/pdf-parser/)
- [Parser](https://trescout.com/dictionary/parser/)
- [Markdown](https://trescout.com/dictionary/markdown/)
- [SDK](https://trescout.com/dictionary/sdk/)
- [RAG](https://trescout.com/dictionary/rag/)
- [PDF](https://trescout.com/dictionary/pdf/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/opendataloader-pdf/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
