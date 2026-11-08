# Nvidia ekran kartları için kubernetes yönetimi

NVIDIA Kubernetes Engine (NVKE), çıplak metal (bare metal) sunucular üzerinde GPU destekli Kubernetes kümeleri yönetimi sağlayan bir kontrol düzlemi (management plane) sunuyor. Go diliyle geliştirilen bu araç, Docker altyapısı üzerinde sanal TPM desteğiyle çalışarak küme kurulumu ve iş yükü oluşturma süreçlerini kolaylaştırıyor.

- ★ 603
- Go
- GitHub Trending · 2026-11-08

## Güncelleme

- **8 Kasım 2026:** Yıldız 600 → 603, son sürüm v0.23.1 (3 Kasım 2026).

## Ne kazandırır?

- Kendi donanımınızda yönetilen kümeler kurun.
- Bağımsız iş yükü kümeleri oluşturun.
- Kaynak koddan ikili dosyalar derleyin.

## Kurulum

**Kaynak koddan derleme**

```
git clone https://github.com/dsx-ai-factory/nvke.git
cd nvke
make build
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

NVIDIA Kubernetes Engine aracını kaynak koddan derlemek için projeyi klonlayıp dizine girmemi ve ardından git clone https://github.com/dsx-ai-factory/nvke.git
cd nvke
make build komutunu çalıştırmamı istiyorum.

Depo: https://github.com/dsx-ai-factory/nvke. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Kendi GPU altyapısında Kubernetes kümeleri yönetmek isteyen platform ekipleri içindir.
- **Lisans:** Apache-2.0

## Bağlantılar

- [GitHub deposu →](https://github.com/dsx-ai-factory/nvke)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-11-08 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Bare Metal](https://trescout.com/dictionary/bare-metal/)
- [Clone](https://trescout.com/dictionary/clone/)
- [GPU](https://trescout.com/dictionary/gpu/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/nvke/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
