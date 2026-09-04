# Konum geçmişinizi hareketli videoya dönüştürün

Google Timeline Visualizer, Google Konum Geçmişi verilerinizle bir yıllık seyahatlerinizi görselleştirir.

- ★ 2.962
- Kotlin
- GitHub Trending · 2026-08-20

## Güncelleme
- 4 Eylül 2026: Yıldız 2.946 → 2.962, son sürüm v3.0.12 (4 Eylül 2026).
- 1 Eylül 2026: Yıldız 2.943 → 2.946, son sürüm v3.0.11 (1 Eylül 2026).
- 31 Ağustos 2026: Yıldız 2.879 → 2.943, son sürüm v3.0.10 (31 Ağustos 2026).
- 27 Ağustos 2026: Yıldız 2.871 → 2.879, son sürüm v3.0.4 (27 Ağustos 2026).

## Ne kazandırır?
- Google Haritalar geçmiş verisini MP4 videoya çevirir
- Seyahat rotalarını harita üzerinde animasyonla gösterir
- Kişisel verileri cihazda işleyerek gizliliği korur

## Kurulum

**Gerekli bağımlılıkları yükleme ve çalışt**

```
python -m pip install -r requirements.txt
python visualizer.py --input Timeline.json --year 2025 --camera-movement steady \
--long-trip-compression balanced --output my_trip_2025.mp4
```

**Geliştirme araçlarını yapılandırma**

```
./gradlew test lint assembleGithubDebug assemblePlayDebug
python -m pip install -r requirements-dev.txt
python -m pytest
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Elimdeki Timeline.json dosyasını kullanarak seyahatlerimi gösteren bir video oluşturmak istiyorum. Python ortamında gerekli bağımlılıkları yükledikten sonra, 2025 yılı verilerimi 'steady' kamera hareketi ve 'balanced' sıkıştırma ayarlarıyla 'my_trip_2025.mp4' adında bir dosyaya dönüştürmek için hangi komutu kullanmalıyım?

- **Kimin için:** Google Haritalar'daki konum geçmişini görselleştirmek ve seyahat anılarını video formatında saklamak isteyen herkes için uygundur. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/mahlernim/google-timeline-visualizer)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-20 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/google-timeline-visualizer/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
