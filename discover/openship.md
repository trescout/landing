# Kendi sunucunuzda uygulama dağıtımı

OpenShip, kullanıcıların kendi sunucularında barındırabildiği bir uygulama dağıtım platformu (deployment platform) sunuyor. TypeScript diliyle geliştirilen bu araç, bulut tabanlı altyapı hizmetlerine alternatif olarak kendi kendine barındırma (self-hosted) süreçlerini kolaylaştırıyor.

- ★ 11.887
- TypeScript
- GitHub Trending · 2026-07-21

## Güncelleme
- 31 Ağustos 2026: Yıldız 11.739 → 11.887, son sürüm v0.6.9 (30 Ağustos 2026).
- 27 Ağustos 2026: Yıldız 11.135 → 11.739, son sürüm v0.6.8 (25 Ağustos 2026).
- 20 Ağustos 2026: Yıldız 10.864 → 11.135, son sürüm v0.6.7 (20 Ağustos 2026).
- 17 Ağustos 2026: Yıldız 10.565 → 10.864, son sürüm v0.6.6 (17 Ağustos 2026).

## Ne kazandırır?
- Otomatik CI/CD süreçleri
- Koddan konteynere hızlı geçiş
- Veritabanı ve SSL yönetimi

## Kurulum

**CLI ile hızlı kurulum**

```
npm i -g openship # or: curl -fsSL https://get.openship.io | sh
openship up # installs Openship as a background service (starts on boot, auto-restarts)
```

**Docker ile kurulum**

```
git clone https://github.com/oblien/openship.git && cd openship
cp .env.example .env
docker compose up -d
```

## Çalıştırma

**Proje dağıtımı başlatma**

```
cd your-project
openship init # link this directory to a project
openship deploy
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Openship kullanarak bir projeyi yayına almak istiyorum. Proje dizinindeyken openship init komutu ile dizini projeye bağlamam ve ardından openship deploy komutunu çalıştırmam yeterli mi? Bu süreçte veritabanı ve SSL yapılandırması otomatik olarak nasıl yönetiliyor, adım adım açıklar mısın?

- **Kimin için:** Kendi sunucusunda uygulama barındırmak isteyen, karmaşık yapılandırma dosyalarıyla uğraşmadan hızlıca dağıtım yapmak isteyen yazılımcılar içindir. 
- **Lisans:** Apache-2.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/oblien/openship)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-07-21 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Deployment CI/CD Self-hosted CLI Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/openship/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
