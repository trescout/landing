# PDF belgelerini yapay zekâ için dönüştürün

AllenAI tarafından geliştirilen olmocr, PDF belgelerini büyük dil modelleri (large language models) için uygun metin formatlarına dönüştüren bir araç takımıdır. Bu yazılım, karmaşık doküman yapılarının doğrusal bir biçimde işlenmesini sağlayarak veri seti hazırlama süreçlerini kolaylaştırır.

- ★ 19.259
- Python
- GitHub Trending · 2026-07-02

## Güncelleme
- 2 Ağustos 2026: Yıldız 18.418 → 19.259, son sürüm v0.4.27 (12 Mart 2026).

## Ne kazandırır?
- PDF ve resim formatlarını temiz Markdown metnine dönüştürür
- Denklem, tablo ve karmaşık düzenleri doğru okuma sırasıyla işler
- Üst ve alt bilgileri otomatik olarak temizler

## Kurulum

**Sistem bağımlılıklarını yükleme**

```
sudo apt-get update
sudo apt-get install poppler-utils ttf-mscorefonts-installer msttcorefonts fonts-crosextra-caladea fonts-crosextra-carlito gsfonts lcdf-typetools
```

**Python ortamı oluşturma**

```
conda create -n olmocr python=3.11
conda activate olmocr
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Elimdeki PDF belgelerini yapay zekâ modellerinin kolayca okuyabileceği temiz bir Markdown formatına dönüştürmek istiyorum. Bu işlem için gerekli olan kurulum adımlarını ve yerel GPU üzerinde çalıştırma yöntemini bana adım adım açıklar mısın?

- **Kimin için:** Karmaşık PDF belgelerini büyük dil modelleri için veri setine dönüştürmek isteyen araştırmacılar ve geliştiriciler içindir. 
- **Lisans:** Apache-2.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/allenai/olmocr)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-07-02 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Markdown GPU PDF Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/olmocr/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
