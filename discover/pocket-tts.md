# CPU üzerinde çalışan hafif yapay zekâ ses sentezleyici

Kyutai Labs tarafından geliştirilen Pocket-TTS, grafik işlem birimine ihtiyaç duymadan sadece merkezi işlem birimi (CPU) üzerinde çalışan hafif bir metinden sese dönüştürme (text-to-speech) modelidir. Düşük kaynak tüketimi sayesinde donanım kısıtlaması olan cihazlarda hızlı ve verimli ses sentezleme imkânı sunar.

- ★ 9.348
- Python
- GitHub Trending · 2026-07-08

## Güncelleme
- 4 Eylül 2026: Yıldız 9.151 → 9.348, son sürüm v3.1.0 (3 Eylül 2026).
- 27 Ağustos 2026: Yıldız 7.994 → 9.151, son sürüm v3.0.2 (25 Ağustos 2026).
- 2 Ağustos 2026: Yıldız 6.350 → 7.994, son sürüm v2.1.0 (4 Mayıs 2026).

## Ne kazandırır?
- Ekran kartı gerektirmeden sadece işlemci ile çalışır
- Düşük kaynak tüketimiyle hızlı ses üretimi sağlar
- Ses klonlama ve çoklu dil desteği sunar

## Kurulum

**Paket kurulumu**

```
pip install pocket-tts
# or
uv add pocket-tts
```

## Çalıştırma

**Ses dosyası oluşturma**

```
uvx pocket-tts generate
# or if you installed it manually with pip:
pocket-tts generate
```

**Yerel sunucu başlatma**

```
uvx pocket-tts serve
# or if you installed it manually with pip:
pocket-tts serve
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Pocket TTS aracını kullanarak metinden sese dönüştürme işlemi yapmak istiyorum. Bilgisayarımda sadece işlemci gücünü kullanarak hızlı bir şekilde ses dosyası üretmek için gerekli komutları ve ses modelini nasıl yapılandıracağımı açıkla. Özellikle varsayılan ses ayarlarını nasıl değiştirebileceğimi ve kendi ses dosyamı kullanarak nasıl ses klonlaması yapabileceğimi adım adım anlat.

- **Kimin için:** Donanım kısıtlaması olan cihazlarda hızlı ve verimli bir şekilde metinleri sese dönüştürmek isteyen kullanıcılar içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/kyutai-labs/pocket-tts)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-07-08 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Text-to-Speech CPU Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/pocket-tts/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
