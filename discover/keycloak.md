# Uygulamalarınız için merkezi kimlik yönetimi

Keycloak, modern uygulamalar ve hizmetler için açık kaynaklı kimlik ve erişim yönetimi (identity and access management) çözümleri sunuyor. Java tabanlı bu platform, merkezi kimlik doğrulama ve yetkilendirme süreçlerini standartlaştırmak için kullanılıyor.

- ★ 36.028
- Java
- GitHub Trending · 2026-06-28

## Güncelleme
- 6 Ağustos 2026: Yıldız 35.953 → 36.028, son sürüm 26.7.1 (5 Ağustos 2026).
- 2 Ağustos 2026: Yıldız 35.354 → 35.953, son sürüm 26.7.0 (9 Temmuz 2026).

## Ne kazandırır?
- Kullanıcı kimlik doğrulama süreçlerini standartlaştırır.
- Güçlü kimlik yönetimi ve yetkilendirme sağlar.
- Uygulama güvenliğini zahmetsizce artırır.

## Kurulum

**Resmî imajı çek**

```
docker pull quay.io/keycloak/keycloak
```

## Çalıştırma

**Geliştirme kipinde başlat**

```
docker run -p 8080:8080 -e KC_BOOTSTRAP_ADMIN_USERNAME=admin -e KC_BOOTSTRAP_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak start-dev
```

Kaynak: Keycloak resmî imaj deposu · quay.io/keycloak/keycloak

## Nasıl başlanır?

Keycloak'ı kullanmaya başlamak için resmî web sitesi üzerinden dağıtım paketini indirip bilgisayarınıza çıkartmanız gerekmektedir. Alternatif olarak, Docker kullanarak hızlıca çalıştırabilirsiniz. Detaylı kurulum ve yapılandırma adımları için resmî dokümantasyon sayfasını ziyaret edebilirsiniz.
- [Resmî kaynak →](https://www.keycloak.org)

- **Kimin için:** Uygulamalarında kullanıcı kimlik doğrulama ve erişim yönetimi süreçlerini merkezi ve güvenli bir şekilde yönetmek isteyen yazılım geliştiriciler ve sistem yöneticileri içindir. 
- **Lisans:** Apache-2.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/keycloak/keycloak)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-28 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

---
Kaynak: TreScout Keşif · https://trescout.com/discover/keycloak/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
