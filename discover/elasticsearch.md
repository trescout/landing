# Büyük verilerde hızlı arama yapın

Java ile geliştirilen Elasticsearch, büyük veri kümeleri üzerinde hızlı arama ve analiz yapılmasına olanak tanıyan dağıtık (distributed) ve açık kaynaklı bir arama motorudur. RESTful mimarisi sayesinde verilerin gerçek zamanlı olarak indekslenmesini ve sorgulanmasını destekler.

- ★ 77.837
- Java
- GitHub Trending · 2026-07-04

## Güncelleme
- 12 Ağustos 2026: Yıldız 77.787 → 77.837, son sürüm v9.5.1 (11 Ağustos 2026).
- 6 Ağustos 2026: Yıldız 77.640 → 77.787, son sürüm v9.5.0 (4 Ağustos 2026).
- 2 Ağustos 2026: Yıldız 77.374 → 77.640, son sürüm v9.4.4 (21 Temmuz 2026).

## Ne kazandırır?
- Büyük veri kümelerinde hızlı arama ve analiz
- Vektör arama ve yapay zekâ uygulamalarıyla entegrasyon
- Gerçek zamanlı veri indeksleme ve sorgulama

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

## Nasıl başlanır?

Elasticsearch'ü kullanmaya başlamak için en basit yöntem, Elastic Cloud üzerinden yönetilen bir dağıtım oluşturmaktır. Alternatif olarak, kendi kurulumunuzu yönetmek isterseniz resmî web sitesindeki indirme sayfasını ziyaret edebilir veya yerel geliştirme ortamları için sunulan Docker tabanlı başlangıç betiklerini inceleyebilirsiniz.
- [Resmî kaynak →](https://www.elastic.co/products/elasticsearch)

- **Kimin için:** Büyük ölçekli veriler üzerinde hızlı arama, log analizi ve vektör tabanlı arama çözümleri geliştirmek isteyen yazılımcılar ve veri mühendisleri içindir. 

## Bağlantılar
- [GitHub deposu →](https://github.com/elastic/elasticsearch)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-07-04 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Distributed Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/elasticsearch/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
