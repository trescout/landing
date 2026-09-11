# Devasa yapay zekâ modellerini yerel çalıştırın

Colibri, büyük ölçekli uzmanlar karışımı (Mixture of Experts) modellerini düşük donanım gereksinimleriyle yerel bilgisayarlarda çalıştırmayı sağlayan C dili tabanlı bir motor. Uzman katmanlarını disk üzerinden akış yöntemiyle işleyerek, yüksek kapasiteli yapay zekâ modellerini kısıtlı donanımlarda çalıştırmayı mümkün kılıyor.

- ★ 27.610
- C
- GitHub Trending · 2026-09-11

## Güncelleme
- 11 Eylül 2026: Yıldız 27.608 → 27.610, son sürüm v1.10.2 (6 Eylül 2026).

## Ne kazandırır?
- Yüksek kapasiteli modelleri kısıtlı donanımlarda çalıştırır
- VRAM, RAM ve disk belleğini tek katman gibi yönetir
- Uzman katmanlarını akış yöntemiyle işleyerek verimlilik sağlar

## Kurulum

**Kaynak koddan derleme**

```
git clone https://github.com/JustVugg/colibri && cd colibri/c
./setup.sh # checks gcc/OpenMP, builds, self-tests
```

## Çalıştırma

**Sohbet arayüzünü başlatma**

```
cd c
make deepseek-v4
python ./coli chat --model /path/to/DeepSeek-V4-Flash --ram 32
# also: coli run / coli serve / coli web
# Windows CUDA tier: make cuda-dsv4-dll CUDA_ARCH=portable (+ make cuda-dsv4-dg-dll on RTX 50)
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Colibri motorunu kullanarak yerel bilgisayarımda büyük ölçekli yapay zekâ modellerini çalıştırmak istiyorum. Donanım kaynaklarımı (VRAM, RAM ve NVMe disk) en verimli şekilde kullanacak şekilde yapılandırmamı sağla. Özellikle GLM veya DeepSeek gibi modelleri, sistemimin bellek kapasitesine göre nasıl optimize edip çalıştırabileceğimi adım adım açıkla.

- **Kimin için:** Büyük dil modellerini kısıtlı donanım kaynaklarıyla kendi bilgisayarında çalıştırmak isteyen araştırmacılar ve yazılımcılar içindir. 
- **Lisans:** Apache-2.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/JustVugg/colibri)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-09-11 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Mixture of Experts VRAM RAM Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/colibri/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
