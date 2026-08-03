# Akış verisinden üç boyutlu sahneler oluşturun

Lingbot-map, akış halindeki verilerden sahneleri yeniden oluşturmak için tasarlanmış ileri beslemeli bir üç boyutlu temel modeldir (3D foundation model). Proje, Python diliyle geliştirilen mimarisi sayesinde karmaşık çevresel verileri işleyerek görselleştirme süreçlerini optimize eder.

- ★ 16.054
- Python
- GitHub Trending · 2026-06-29

## Güncelleme
- 2 Ağustos 2026: Yıldız 8.439 → 16.054.

## Ne kazandırır?
- Uzun video sekanslarında kararlı 3D yeniden oluşturma
- Düşük gecikmeli akışlı çıkarım desteği
- Karmaşık çevresel verileri işleyebilen yapay zekâ mimarisi

## Kurulum

**Ortam hazırlığı ve temel kurulum**

```
conda create -n lingbot-map python=3.10 -y
conda activate lingbot-map
```

**Gerekli kütüphanelerin yüklenmesi**

```
pip install torch==2.8.0 torchvision==0.23.0 --index-url https://download.pytorch.org/whl/cu128
```

## Çalıştırma

**Örnek sahneyi başlatma**

```
python demo.py --model_path /path/to/lingbot-map-long.pt \
--image_folder example/courthouse --mask_sky
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
LingBot-Map kullanarak akış halindeki verilerden 3D sahne oluşturmak istiyorum. Kurulumu tamamladım ve model dosyam hazır. Courthouse örneğini çalıştırmak için gerekli olan komutu kullanarak, yerel tarayıcımda görselleştirme arayüzünü nasıl başlatabilirim?

- **Kimin için:** 3D bilgisayarlı görü ve akışlı veri işleme süreçleriyle ilgilenen araştırmacılar ve geliştiriciler için uygundur. 
- **Lisans:** Apache-2.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/Robbyant/lingbot-map)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-29 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Foundation Model Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/lingbot-map/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
