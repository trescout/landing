# Kendi Sunucunuzda Fotoğraf ve Video Yedekleme

Immich; kişisel fotoğraf ve videolarınızı yedeklemeniz için tasarlanmış, doğrudan kendi sunucunuzda barındırabileceğiniz yüksek performanslı bir çözümdür.

- ★ 109.538
- GitHub Trending · 2026-07-05

## Güncelleme
- 2 Ağustos 2026: Yıldız 105.748 → 109.538, son sürüm v3.1.0 (29 Temmuz 2026).

## Bu araç ne yapar?

Immich; kişisel fotoğraf ve videolarınızı yedeklemeniz için tasarlanmış, doğrudan kendi sunucunuzda barındırabileceğiniz yüksek performanslı bir çözümdür. Mobil ve web uygulamaları aracılığıyla medya kütüphanenizi yönetmenizi sağlar.

## Kimin için?

Fotoğraf ve videolarını üçüncü taraf bulut servisleri yerine kendi donanımlarında depolamak ve yönetmek isteyenler.

## Ne beklememeli?

Kendi sunucusunu yönetmek istemeyen veya teknik kurulum süreçleriyle uğraşmak istemeyen kullanıcılar.

## Öne çıkanlar
- Fotoğraf ve videoları orijinal kalitelerinde yedekler.
- Web ve mobil uygulamalarıyla erişim imkânı sunar.
- Kendi donanımınızda barındırılarak veri gizliliği sağlar.
- Çoklu kullanıcı desteği ile aile üyeleri veya ekipler için alanlar oluşturur.

## İlk kullanım akışı
- Resmî dokümantasyonda belirtilen donanım gereksinimlerini karşıladığınızdan emin olun.
- Docker ve Docker Compose kullanarak Immich kapsayıcılarını başlatın.
- Mobil uygulamayı cihazınıza indirin ve sunucu adresinizi girerek bağlanın.
- İlk yönetici hesabını oluşturun ve yedekleme işlemini başlatın.

## Güvenli başlangıç

Immich yoğun şekilde geliştirilmeye devam etmektedir; bu nedenle kurulumunuzu güncellemeden önce mutlaka sürüm notlarını okumalı ve medyanızın harici bir yedeğini almalısınız.

## İlk görev istemi
İlk adım için hazır istem 
Immich kurulumunda yeni bir kullanıcı nasıl eklenir?

## Kurulum

**Docker Compose yapılandırmasını indir**

```
mkdir immich-app && cd immich-app
wget -O docker-compose.yml https://github.com/immich-app/immich/releases/latest/download/docker-compose.yml
wget -O .env https://github.com/immich-app/immich/releases/latest/download/example.env
```

## Çalıştırma

**Docker servislerini başlat**

```
docker compose up -d
```

Kaynak: Resmî Immich dokümantasyonu (immich.app/docs/install/docker-compose)

## Bağlantılar
- [GitHub deposu →](https://github.com/immich-app/immich)
- [Immich resmî README →](https://github.com/immich-app/immich)
- [Immich resmî sitesi →](https://immich.app/)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-07-05 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

---
Kaynak: TreScout Keşif · https://trescout.com/discover/immich/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
