# Yapay zekâ modelleri eğitme aracı

karpathy/nanochat, büyük dil modelleri (LLM) eğitmek için geliştirilmiş, tek bir grafik işlem birimi (GPU) üzerinde çalışabilen deneysel bir yazılım çatısıdır. Tokenlaştırma, ön eğitim, ince ayar (fine-tuning), değerlendirme ve çıkarım süreçlerini kapsayan bu proje, geliştiricilere minimal ve üzerinde değişiklik yapılabilir bir yapı sunar.

- ★ 59.998
- Python
- GitHub Trending · 2026-11-03

## Ne kazandırır?

- Tek bir grafik işlem birimi üzerinde yapay zekâ modeli eğitmenizi sağlar.
- Metin oluşturma adımlarını komut satırı üzerinden yönetmenize imkân tanır.
- Farklı donanım türleri için esnek kurulum seçenekleri sunar.

## Kurulum

**Bağımlılıkları yükleme**

```
uv sync --extra gpu    # Use for CUDA (A100/H100/etc.)
uv sync --extra cpu    # (or) Use for CPU-only / MPS
source .venv/bin/activate
```

## Çalıştırma

**Eğitim sürecini başlatma**

```
bash runs/speedrun.sh
```

**Model ile sohbet etme**

```
python -m scripts.chat_cli
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

nanochat isimli yapay zekâ aracını kurmak ve çalıştırmak istiyorum. Öncelikle uv sync --extra gpu # Use for CUDA (A100/H100/etc.)
uv sync --extra cpu # (or) Use for CPU-only / MPS
source .venv/bin/activate komutunu kullanarak bağımlılıkları kur ve sanal ortamı aktif et. Ardından bash runs/speedrun.sh komutuyla süreci başlat ve tamamlandığında python -m scripts.chat_cli komutunu çalıştırarak model ile iletişime geç.

Depo: https://github.com/karpathy/nanochat. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Büyük dil modellerini sıfırdan eğitmek ve test etmek isteyen geliştiriciler içindir.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/karpathy/nanochat)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-11-03 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Fine-tuning](https://trescout.com/dictionary/fine-tuning/)
- [GPU](https://trescout.com/dictionary/gpu/)
- [LLM](https://trescout.com/dictionary/llm/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/nanochat/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
