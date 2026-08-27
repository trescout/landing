# Temel Model Araştırması İçin Açık Geliştirme Platformu

Temel modellerin araştırılması ve geliştirilmesi için bir araştırma programı, yazılım platformu ve topluluktur. Veri işlemeden ön eğitim, son eğitim ve değerlendirmeye uzanan kapsamı belgeler.

- ★ 1.967
- Python
- GitHub Trending · 2026-08-25

## Kurulum

**Resmî depoyu klonla**

```
git clone https://github.com/marin-community/marin.git
```

**Python ortamını oluştur**

```
uv venv --python 3.12
```

**Bağımlılıkları kur**

```
uv sync --all-packages
```

## Çalıştırma

**CPU smoke testini çalıştır**

```
wandb offline
uv run python experiments/tutorials/train_tiny_model.py --device cpu --dataset tinystories --version dev --run
```

Kaynak: Resmî README ve dokümantasyon kaynakları: https://marin.readthedocs.io/en/latest/tutorials/installation/, https://marin.readthedocs.io/en/latest/tutorials/first-experiment/, https://github.com/marin-community/marin

## Bu araç ne yapar?

Deneyleri bağımlı adımlar olarak topolojik sırada yürütür. Resmî ilk deney, TinyStories verisini tokenleştirip küçük bir dil modeli eğitmeyi gösterir; açık geliştirme yaklaşımı kodu, veriyi, kararları ve başarısız deneyleri de belgeler.

## Kimin için?

Veri kürasyonu, dönüşümü, filtreleme, tokenleştirme, model eğitimi ve değerlendirme araştırmaları yapan ekipler.

## Ne beklememeli?

Temel model araştırması kapsamına girmeyen basit uygulama geliştirme işleri veya gerekli Python ve geliştirme ortamını kurmak istemeyenler.

## Öne çıkanlar
- Veri işlemeden ön eğitim, son eğitim ve değerlendirmeye uzanan araştırma kapsamı
- Bağımlı adımları topolojik sırada yürüten deney iş akışı
- Başarısız deneyleri ve geliştirme kararlarını da kapsayan açık dokümantasyon

## İlk kullanım akışı
- Resmî depoyu klonlayın ve Python 3.12 veya üzeri bir sanal ortam oluşturun
- uv ile bağımlılıkları senkronize edin
- MARIN_PREFIX ortam değişkenini yapılandırın
- CPU üzerinde çevrimdışı TinyStories smoke testini çalıştırın

## Güvenli başlangıç

CPU smoke testi yalnızca ilk doğrulama içindir. CPU, GPU ve TPU bağımlılıkları ayrı donanım ekleri gerektirebilir. WANDB_API_KEY ve HF_TOKEN yalnızca ilgili izleme veya kapalı model iş akışlarında gerekir.

## İlk görev istemi
İlk adım için hazır istem 
Çevrimdışı TinyStories akışıyla CPU üzerinde küçük bir model eğitimini ilk doğrulama olarak çalıştır.

## Bağlantılar
- [GitHub deposu →](https://github.com/marin-community/marin)
- [Kurulum dokümantasyonu →](https://marin.readthedocs.io/en/latest/tutorials/installation/)
- [İlk deney →](https://marin.readthedocs.io/en/latest/tutorials/first-experiment/)
- [Resmî README →](https://github.com/marin-community/marin)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-25 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
CPU GPU

---
Kaynak: TreScout Keşif · https://trescout.com/discover/marin/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
