# Hızlı ve yerel PDF metin işleme

Firecrawl tarafından geliştirilen PDF Inspector, PDF dosyalarını incelemek, sınıflandırmak ve metinlerini ayıklamak için tasarlanmış hızlı bir Rust kütüphanesidir. Taranmış belgeler ile metin tabanlı dosyaları ayırt ederek veri işleme süreçlerinde akıllı yönlendirme kararları alınmasını sağlar.

- ★ 19.394
- Rust
- GitHub Trending · 2026-08-04

## Güncelleme

- **28 Eylül 2026:** Yıldız 19.360 → 19.394, son sürüm v1.25.2 (28 Eylül 2026).
- **27 Eylül 2026:** Yıldız 19.121 → 19.360, son sürüm v1.24.0 (23 Eylül 2026).
- **15 Eylül 2026:** Yıldız 18.994 → 19.121, son sürüm v1.20.0 (15 Eylül 2026).
- **10 Eylül 2026:** Yıldız 18.936 → 18.994, son sürüm v1.19.0 (9 Eylül 2026).

## Ne kazandırır?

- PDF dosyalarını saniyeler içinde sınıflandırır
- Metinleri Markdown formatına hatasız dönüştürür
- Optik Karakter Tanıma (OCR) hizmetlerine gerek duymaz

## Kurulum

**Python ile kurulum**

```
pip install maturin
maturin develop --release
```

**Node.js ile kurulum**

```
npm install @firecrawl/pdf-inspector
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Elimdeki PDF dosyasını analiz etmem gerekiyor. Bu dosyayı metin tabanlı mı yoksa taranmış bir belge mi olduğunu anlamak için sınıflandır. Eğer metin tabanlıysa, içerisindeki metinleri, tabloları ve başlıkları koruyarak temiz bir Markdown formatına dönüştür. İşlemi yaparken OCR kullanmadan, dosyanın kendi yapısını ve yazı tipi bilgilerini kullanarak okuma sırasını doğru bir şekilde belirle.

Depo: https://github.com/firecrawl/pdf-inspector. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Raporlar, finansal belgeler veya araştırma makaleleri gibi yapılandırılmış metin verilerine hızlıca ihtiyaç duyan geliştiriciler için uygundur.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/firecrawl/pdf-inspector)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-08-04 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [PDF Inspector](https://trescout.com/dictionary/pdf-inspector/)
- [Markdown](https://trescout.com/dictionary/markdown/)
- [PDF](https://trescout.com/dictionary/pdf/)
- [Rust](https://trescout.com/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/pdf-inspector/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
