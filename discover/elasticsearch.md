# Dağıtık ve Güçlü Arama Motoru

Elasticsearch; RESTful API tabanlı, dağıtık ve yüksek performanslı bir arama ve analitik motorudur.

- ★ 77.846
- GitHub Trending · 2026-07-04

## Güncelleme
- 20 Ağustos 2026: Yıldız 77.837 → 77.846, son sürüm v9.5.2 (20 Ağustos 2026).
- 12 Ağustos 2026: Yıldız 77.787 → 77.837, son sürüm v9.5.1 (11 Ağustos 2026).
- 6 Ağustos 2026: Yıldız 77.640 → 77.787, son sürüm v9.5.0 (4 Ağustos 2026).
- 2 Ağustos 2026: Yıldız 77.374 → 77.640, son sürüm v9.4.4 (21 Temmuz 2026).

## Bu araç ne yapar?

Elasticsearch; RESTful API tabanlı, dağıtık ve yüksek performanslı bir arama ve analitik motorudur. Büyük hacimli metin, sayısal ve coğrafi veriler üzerinde gerçek zamanlı arama, log analizi ve veri görselleştirme altyapısı sağlar.

## Kimin için?

Milyonlarca satırlık veri üzerinde milisaniyeler içinde karmaşık aramalar ve log analizi yapmak isteyenler.

## Ne beklememeli?

İlişkisel veri modellerine ve karmaşık SQL `JOIN` işlemlerine ihtiyaç duyan geleneksel veritabanı kullanıcıları.

## Öne çıkanlar
- Büyük hacimli verilerde yüksek hızlı tam metin araması sunar.
- Dağıtık mimarisi sayesinde yatay olarak kolayca ölçeklenebilir.
- Log yönetimi ve sistem izleme için zengin bir ekosistem barındırır.

## İlk kullanım akışı
- Resmî dokümantasyondaki Docker veya paket yöneticisi talimatlarıyla Elasticsearch'ü kurun.
- Varsayılan güvenlik ayarlarını (parolalar ve sertifikalar) yapılandırın.
- Bir REST istemcisi ile ana uç noktaya (endpoint) istek göndererek küme durumunu doğrulayın.

## Güvenli başlangıç

Elasticsearch düğümlerini hiçbir zaman genel internete açık bırakmamalı ve yerleşik güvenlik özelliklerini her zaman etkinleştirmelisiniz.

## İlk görev istemi
İlk adım için hazır istem 
Elasticsearch'te yeni bir dizin (index) nasıl oluşturulur?

## Kurulum

**Docker imajını çek**

```
docker pull docker.elastic.co/elasticsearch/elasticsearch:9.5.0
```

**macOS (Homebrew)**

```
brew install elastic/tap/elasticsearch-full
```

## Çalıştırma

**Tek düğüm modunda Docker ile başlat**

```
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:9.5.0
```

Kaynak: Elastic Docker Registry · Homebrew (elastic/tap/elasticsearch-full) · resmî Elastic dokümantasyonu

## İlgili sözlük terimleri
API 

## Bağlantılar
- [GitHub deposu →](https://github.com/elastic/elasticsearch)
- [Elasticsearch resmî README →](https://github.com/elastic/elasticsearch)
- [Elasticsearch resmî sitesi →](https://www.elastic.co/elasticsearch)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-07-04 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

---
Kaynak: TreScout Keşif · https://trescout.com/discover/elasticsearch/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
