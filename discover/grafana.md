# Verilerinizi tek arayüzde görselleştirin

Grafana, farklı veri kaynaklarından gelen metrikleri, günlükleri (logs) ve izleme verilerini (traces) tek bir arayüzde birleştiren açık kaynaklı bir gözlemlenebilirlik ve veri görselleştirme platformudur. Prometheus, Elasticsearch ve PostgreSQL gibi birçok sistemle entegre çalışarak karmaşık veri setlerinin analiz edilmesini sağlar.

- ★ 76.114
- TypeScript
- GitHub Trending · 2026-06-27

## Güncelleme
- 6 Ağustos 2026: Yıldız 75.925 → 76.114, son sürüm v13.1.2 (4 Ağustos 2026).
- 2 Ağustos 2026: Yıldız 74.994 → 75.925, son sürüm v13.1.1 (21 Temmuz 2026).

## Ne kazandırır?
- Farklı veri kaynaklarını tek panelde birleştirme
- Esnek ve dinamik kontrol panelleri oluşturma
- Metrikler üzerinden otomatik uyarı sistemleri kurma

## Kurulum

**macOS (Homebrew)**

```
brew install grafana
```

**Docker ile**

```
docker run -d -p 3000:3000 --name=grafana grafana/grafana
```

## Çalıştırma

**Homebrew servisi olarak başlat**

```
brew services start grafana
```

Kaynak: Homebrew (grafana) · Docker Hub (grafana/grafana) · resmî Grafana dokümantasyonu (grafana.com/docs)

## Nasıl başlanır?

Grafana kullanmaya başlamak için resmî web sitesi olan grafana.com/get adresini ziyaret edin. İhtiyacınıza uygun kurulum rehberlerine ulaşmak için grafana.com/docs/grafana/latest/setup-grafana/installation/ sayfasındaki dokümanları inceleyebilirsiniz.
- [Resmî kaynak →](https://grafana.com)

- **Kimin için:** Farklı kaynaklardan gelen verilerini tek bir merkezden izlemek ve görselleştirmek isteyen sistem yöneticileri ve veri analistleri içindir. 
- **Lisans:** AGPL-3.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/grafana/grafana)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-27 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Logs Traces

---
Kaynak: TreScout Keşif · https://trescout.com/discover/grafana/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
