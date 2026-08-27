# Oyun Kütüphanenizi Merkezileştirin

Romm; retro oyun koleksiyonunuzu modern ve şık bir web arayüzü üzerinden düzenlemenizi sağlayan bir oyun kütüphanesi yöneticisidir.

- ★ 12.170
- GitHub Trending · 2026-07-04

## Güncelleme
- 20 Ağustos 2026: Yıldız 11.859 → 12.170, son sürüm 5.2.0 (20 Ağustos 2026).
- 2 Ağustos 2026: Yıldız 9.887 → 11.859, son sürüm 5.1.0 (29 Temmuz 2026).

## Bu araç ne yapar?

Romm; retro oyun koleksiyonunuzu modern ve şık bir web arayüzü üzerinden düzenlemenizi sağlayan, doğrudan kendi sunucunuzda barındırabileceğiniz bir oyun kütüphanesi yöneticisidir. IGDB entegrasyonuyla oyun meta verilerini otomatik olarak çeker.

## Kimin için?

Dağınık durumdaki oyun dosyalarını merkezi, görsel açıdan zengin bir arşive dönüştürmek isteyen retro oyun tutkunları.

## Ne beklememeli?

Dijital oyun satın alımları yapmak isteyenler veya güncel platformları yönetmek için istemci arayanlar.

## Öne çıkanlar
- Tarayıcı üzerinden erişilebilen modern bir kütüphane arayüzü sunar.
- Oyun kapağı, çıkış tarihi ve açıklama gibi bilgileri otomatik olarak indirir.
- Çoklu kullanıcı desteği ve oynatma geçmişi takibi sağlar.

## İlk kullanım akışı
- Romm için gereken Docker ve Docker Compose dosyalarını indirin.
- API erişimi için gerekli anahtarları oluşturup yapılandırma dosyasına ekleyin.
- Oyun dosyalarınızın bulunduğu dizini bağlayarak (mount) servisi başlatın.
- Web arayüzüne giriş yaparak ilk kütüphane taramasını başlatın.

## Güvenli başlangıç

Kütüphanenizi oluştururken kullanacağınız dosyaların yasal mülkiyetinize ait kopyalar olduğundan ve yerel telif hakkı yasalarına uyduğunuzdan emin olmalısınız.

## İlk görev istemi
İlk adım için hazır istem 
Romm kütüphanesine yeni bir platform (örneğin SNES) nasıl eklenir?

## Kurulum

**Örnek compose dosyasını al**

```
curl -o docker-compose.yml https://raw.githubusercontent.com/rommapp/romm/master/examples/docker-compose.example.yml
```

## Çalıştırma

**Başlat**

```
docker compose up -d
```

Kaynak: Depodaki examples/docker-compose.example.yml

## Bağlantılar
- [GitHub deposu →](https://github.com/rommapp/romm)
- [Romm resmî README →](https://github.com/rommapp/romm)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-07-04 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

---
Kaynak: TreScout Keşif · https://trescout.com/discover/romm/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
