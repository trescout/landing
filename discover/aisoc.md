# Yapay zekâ destekli güvenlik operasyon merkezi

AiSOC, güvenlik operasyonlarını otomatize etmek için geliştirilmiş açık kaynaklı bir yapay zekâ güvenlik merkezi. Büyük dil modelleri (LLM) ile uyarıları sınıflandıran ve MITRE ATT&CK çerçevesiyle incelemeler yapan araç, API anahtarı gerektirmeden kendi sunucunuzda çalışabiliyor.

- ★ 7.383
- Python
- GitHub Trending · 2026-11-02

## Güncelleme

- **12 Kasım 2026:** Yıldız 7.105 → 7.383, son sürüm v23.2.0 (12 Kasım 2026).
- **10 Kasım 2026:** Yıldız 7.296 → 7.105, son sürüm v23.1.0 (10 Kasım 2026).
- **6 Kasım 2026:** Yıldız 7.313 → 7.296, son sürüm v22.2.0 (6 Kasım 2026).
- **5 Kasım 2026:** Yıldız 7.279 → 7.313, son sürüm v22.1.0 (5 Kasım 2026).

## Ne kazandırır?

- Güvenlik araçlarından gelen verileri otomatik sınıflandırarak tehditleri tespit eder
- Yapay zekâ ajanları ile olayları inceleyip onay için somut aksiyon önerileri sunar
- Tüm süreçleri dışarıya bağımlı olmadan kendi sunucunuz üzerinde güvenle çalıştırır

## Kurulum

**Depoyu indirin ve sistemi başlatın**

```
git clone https://github.com/beenuar/AiSOC && cd AiSOC
make up
```

## Çalıştırma

**Test verisiyle doğrulayın**

```
make smoke
[PASS] raw telemetry accepted by ingest
[PASS] event traversed the spine and became an alert
PASS: 10/10 stages
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Kendi sunucumda çalışacak AiSOC adlı açık kaynaklı yapay zekâ güvenlik merkezini kurup ayağa kaldırmak istiyorum. İlgili GitHub deposunu klonlayıp sistemi başlatmak için sırasıyla 'git clone https://github.com/beenuar/AiSOC && cd AiSOC
make up' komutunu çalıştırmamda bana yardımcı ol.

Depo: https://github.com/beenuar/AiSOC. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Güvenlik uyarılarını ve operasyonlarını kendi altyapısında yerel yapay zekâ desteğiyle yönetmek isteyen sistem ve güvenlik uzmanları içindir.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/beenuar/AiSOC)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-11-02 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Clone](https://trescout.com/dictionary/clone/)
- [LLM](https://trescout.com/dictionary/llm/)
- [API](https://trescout.com/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/aisoc/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
