# Farklı karakter iskeletlerini tek modelle canlandırın

UniMate, farklı iskelet yapılarını tek bir model üzerinden hareketlendirmeye yarayan bir animasyon teknolojisi. SIGGRAPH Asia 2026 kapsamında sunulan bu çalışma, karakter animasyonu süreçlerini standartlaştırmayı amaçlıyor.

- ★ 1.166
- Python
- GitHub Trending · 2026-10-02

## Ne kazandırır?
- İnsan, hayvan ve nesne gibi farklı iskelet yapılarını tek bir yapay zekâ modeliyle hareketlendirir.
- Büyük ölçekli UniML3D veri seti ile geniş kapsamlı animasyon desteği sunar.
- Karakter animasyonu süreçlerini standartlaştırarak iş akışını hızlandırır.

## Kurulum

**Ortam hazırlığı**

```
conda create -n unimate python=3.10 -y
conda activate unimate
pip install "setuptools 

## Çalıştırma

**Örnek animasyon oluşturma**

```
python -m unimate.inference.sample \
--exp_dir outputs/uniml3d_60frames_graph_adaln \
--test_cases_json test_cases.json \
--num_repetitions 3
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
UniMate projesini kullanarak elimdeki farklı iskelet yapısına sahip karakter modellerini nasıl standart bir formatta hareketlendirebilirim? Projenin sunduğu UniML3D veri setinden ve önceden eğitilmiş kontrol noktalarından faydalanarak animasyon oluşturma sürecini adım adım açıkla.

- **Kimin için:** Karakter animasyonu süreçlerini otomatize etmek ve farklı iskelet yapıları arasında geçiş yapabilmek isteyen 3D sanatçıları ve geliştiriciler içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/Friedrich-M/UniMate)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-10-02 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/unimate/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
