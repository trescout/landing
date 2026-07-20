# CPU üzerinde çalışan hafif yapay zekâ ses sentezleyici

Kyutai Labs tarafından geliştirilen Pocket-TTS, grafik işlem birimine ihtiyaç duymadan sadece merkezi işlem birimi (CPU) üzerinde çalışan hafif bir metinden sese dönüştürme (text-to-speech) modelidir. Düşük kaynak tüketimi sayesinde donanım kısıtlaması olan cihazlarda hızlı ve verimli ses sentezleme imkânı sunar.

- ★ 6.350
- Python
- GitHub Trending · 2026-07-08

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

## İlgili sözlük terimleri
Text-to-Speech CPU Artificial Intelligence 

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Yıldız ve sayılar keşif tarihindeki değerlerdir.

---
Kaynak: TreScout Keşif · https://trescout.com/discover/pocket-tts/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
