# Açık kaynaklı kurumsal kaynak planlama

Odoo, işletmelerin tüm operasyonel süreçlerini tek bir çatı altında yönetmelerini sağlayan açık kaynaklı bir kurumsal kaynak planlama (enterprise resource planning) platformudur. Python diliyle geliştirilen bu sistem, satıştan muhasebeye kadar geniş bir yelpazede modüler iş uygulamaları sunar.

- ★ 52.082
- GitHub Trending · 2026-06-04

## Ne kazandırır?
- Satış, muhasebe ve depo gibi iş süreçlerini tek merkezden yönetir.
- Birbiriyle uyumlu modüler iş uygulamaları sunar.
- İhtiyaca göre özelleştirilebilir açık kaynaklı bir altyapı sağlar.

## Kurulum

**PostgreSQL veritabanını başlat**

```
docker run -d --name odoo-db -e POSTGRES_DB=postgres -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=change_me postgres:15
```

**Odoo’yu veritabanına bağlayarak başlat**

```
docker run -d --name odoo --link odoo-db:db -p 127.0.0.1:8069:8069 odoo:latest
```

## Çalıştırma

**Yerel arayüze eriş**

```
http://localhost:8069
```

Kaynak: Resmî kaynak: https://hub.docker.com/_/odoo

## Nasıl başlanır?

Odoo kurulumuna başlamak için resmî Odoo dokümantasyon sayfasında yer alan kurulum talimatlarını takip etmeniz gerekmektedir. Yazılımı öğrenmek için Odoo eLearning platformunu veya Scale-up iş oyununu inceleyebilirsiniz.
- [Resmî kaynak →](https://www.odoo.com)

- **Kimin için:** Tüm operasyonel süreçlerini tek bir platform üzerinden yönetmek isteyen işletmeler için uygundur. 

## Bağlantılar
- [GitHub deposu →](https://github.com/odoo/odoo)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-04 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Enterprise Resource Planning

---
Kaynak: TreScout Keşif · https://trescout.com/discover/odoo/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
