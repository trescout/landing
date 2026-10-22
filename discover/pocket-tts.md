# CPU üzerinde çalışan hafif yapay zekâ ses sentezleyici

Kyutai Labs tarafından geliştirilen Pocket-TTS, grafik işlem birimine ihtiyaç duymadan sadece merkezi işlem birimi (CPU) üzerinde çalışan hafif bir metinden sese dönüştürme (text-to-speech) modelidir. Düşük kaynak tüketimi sayesinde donanım kısıtlaması olan cihazlarda hızlı ve verimli ses sentezleme imkânı sunar.

- ★ 10.002
- Python
- GitHub Trending · 2026-07-08

## Güncelleme

- **22 Ekim 2026:** Yıldız 9.972 → 10.002, son sürüm v4.0.1 (21 Ekim 2026).
- **21 Ekim 2026:** Yıldız 9.663 → 9.972, son sürüm v4.0.0 (20 Ekim 2026).
- **27 Eylül 2026:** Yıldız 9.348 → 9.663, son sürüm v3.3.0 (24 Eylül 2026).
- **4 Eylül 2026:** Yıldız 9.151 → 9.348, son sürüm v3.1.0 (3 Eylül 2026).

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

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Pocket TTS aracını kullanarak metinden sese dönüştürme işlemi yapmak istiyorum. Bilgisayarımda sadece işlemci gücünü kullanarak hızlı bir şekilde ses dosyası üretmek için gerekli komutları ve ses modelini nasıl yapılandıracağımı açıkla. Özellikle varsayılan ses ayarlarını nasıl değiştirebileceğimi ve kendi ses dosyamı kullanarak nasıl ses klonlaması yapabileceğimi adım adım anlat.

Depo: https://github.com/kyutai-labs/pocket-tts. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Donanım kısıtlaması olan cihazlarda hızlı ve verimli bir şekilde metinleri sese dönüştürmek isteyen kullanıcılar içindir.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/kyutai-labs/pocket-tts)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-07-08 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Text-to-Speech](https://trescout.com/dictionary/text-to-speech/)
- [CPU](https://trescout.com/dictionary/cpu/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/pocket-tts/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
