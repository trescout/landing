# Kendi fotoğraf ve video arşivinizi yönetin

Immich, fotoğraf ve video dosyalarını yönetmek için geliştirilmiş, yüksek performanslı bir öz sunuculu (self-hosted) medya yönetim çözümüdür. TypeScript ile yazılan bu platform, kullanıcılara kendi altyapıları üzerinde merkezi bir medya arşivi oluşturma imkânı tanır.

- ★ 109.538
- TypeScript
- GitHub Trending · 2026-07-05

## Güncelleme
- 2 Ağustos 2026: Yıldız 105.748 → 109.538, son sürüm v3.1.0 (29 Temmuz 2026).

## Ne kazandırır?
- Fotoğraf ve videolar için merkezi depolama
- Yüz tanıma ve nesne tabanlı arama
- Mobil ve web üzerinden yedekleme

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

## Nasıl başlanır?

Kurulum ve kullanım detayları için resmî dokümantasyon sayfasını ziyaret edin. https://immich.app/ adresindeki kurulum rehberlerini takip ederek kendi sunucunuz üzerinde medya yönetiminizi başlatabilirsiniz.
- [Resmî kaynak →](https://immich.app)

- **Kimin için:** Kendi fotoğraf ve video arşivini bulut servislerine bağımlı kalmadan, kendi altyapısı üzerinde yönetmek isteyen kullanıcılar içindir. 
- **Lisans:** AGPL-3.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/immich-app/immich)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-07-05 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Self-hosted

---
Kaynak: TreScout Keşif · https://trescout.com/discover/immich/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
