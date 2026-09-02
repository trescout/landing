# Güvenli ve özelleştirilebilir ekip iletişimi

Rocket.Chat, görev kritik operasyonlar için tasarlanmış güvenli bir iletişim işletim sistemi (communications operating system) sunuyor. TypeScript diliyle geliştirilen platform, kurum içi mesajlaşma ve iş birliği süreçlerini merkezileştirmeyi hedefliyor.

- ★ 46.064
- TypeScript
- GitHub Trending · 2026-06-18

## Güncelleme
- 2 Eylül 2026: Yıldız 46.005 → 46.064, son sürüm 8.8.0 (1 Eylül 2026).
- 19 Ağustos 2026: Yıldız 45.941 → 46.005, son sürüm 8.7.1 (19 Ağustos 2026).
- 7 Ağustos 2026: Yıldız 45.919 → 45.941, son sürüm 8.7.0 (7 Ağustos 2026).
- 2 Ağustos 2026: Yıldız 45.649 → 45.919, son sürüm 8.6.1 (10 Temmuz 2026).

## Ne kazandırır?
- Uçtan uca şifreleme ile veri güvenliği
- Kendi sunucunuzda barındırma imkânı
- Geniş entegrasyon ve uygulama desteği

## Kurulum

**Resmî compose deposunu klonla**

```
git clone --depth 1 https://github.com/RocketChat/rocketchat-compose.git
```

**Ortam dosyasını oluştur**

```
cd rocketchat-compose
cp .env.example .env
```

**MongoDB ve Rocket.Chat servislerini başlat**

```
docker compose -f compose.database.yml -f compose.yml -f compose.nats.yml up -d
```

## Çalıştırma

**Yerel arayüze eriş**

```
http://localhost:3000
```

Kaynak: Resmî kaynak: https://docs.rocket.chat/docs/deploy-with-docker-docker-compose

## Nasıl başlanır?

Rocket.Chat kurulumuna başlamak için resmî dokümantasyon sayfasındaki Dağıtım Kılavuzunu (Deployment Guide) inceleyebilirsiniz. Kendi sunucunuzda barındırmak için Docker, Podman veya Kubernetes yöntemlerinden birini seçebilir ya da daha hızlı bir başlangıç için Launchpad seçeneğini değerlendirebilirsiniz. Tüm teknik gereksinimler ve detaylı kurulum adımları için Rocket.Chat'in resmî dokümantasyon sitesini ziyaret edin.
- [Resmî kaynak →](https://rocket.chat/)

- **Kimin için:** Veri gizliliğine önem veren ve kendi altyapısı üzerinde tam kontrol sahibi olmak isteyen organizasyonlar için geliştirilmiştir. 

## Bağlantılar
- [GitHub deposu →](https://github.com/RocketChat/Rocket.Chat)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-18 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Communications Operating System Deployment

---
Kaynak: TreScout Keşif · https://trescout.com/discover/rocket-chat/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
