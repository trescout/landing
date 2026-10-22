# Yapay zekâ modellerini hızlı çalıştırma ve sunma motoru

vllm-project/vllm, büyük dil modelleri (LLM) için yüksek işlem hacmi ve bellek verimliliği sağlayan bir çıkarım (inference) ve sunum motorudur. Python diliyle geliştirilen bu araç, yapay zekâ modellerinin çalıştırılma süreçlerini hızlandırmayı amaçlar.

- ★ 94.625
- Python
- GitHub Trending · 2026-10-21

## Güncelleme

- **21 Ekim 2026:** Yıldız 94.616 → 94.625, son sürüm v0.32.0 (18 Ekim 2026).

## Ne kazandırır?

- bellek verimliliği sağlayan pagedattention yönetimi sunar
- popüler hugging face modelleriyle uyumlu çalışır
- openai uyumlu api sunucusu desteği barındırır

## Kurulum

**vllm kurulumu**

```
uv pip install vllm
vllm download-kernels  # precompiled kernels for faster startup
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Bilgisayarıma vllm motorunu kurmak istiyorum. Kurulumu gerçekleştirmek için şu komutları kullan:

uv pip install vllm
vllm download-kernels # precompiled kernels for faster startup

Depo: https://github.com/vllm-project/vllm. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Büyük dil modellerini kendi sunucusunda hızlı ve verimli bir şekilde çalıştırmak isteyen geliştiriciler içindir.
- **Lisans:** Apache-2.0

## Bağlantılar

- [GitHub deposu →](https://github.com/vllm-project/vllm)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-10-21 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Kernels](https://trescout.com/dictionary/kernels/)
- [Inference](https://trescout.com/dictionary/inference/)
- [LLM](https://trescout.com/dictionary/llm/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/vllm/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
