# Kendi sunucunuzda uygulama dağıtımı

OpenShip, kullanıcıların kendi sunucularında barındırabildiği bir uygulama dağıtım platformu (deployment platform) sunuyor. TypeScript diliyle geliştirilen bu araç, bulut tabanlı altyapı hizmetlerine alternatif olarak kendi kendine barındırma (self-hosted) süreçlerini kolaylaştırıyor.

- ★ 5.130
- TypeScript
- GitHub Trending · 2026-07-21

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

## İlgili sözlük terimleri
Deployment Self-hosted CLI Artificial Intelligence 

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Yıldız ve sayılar keşif tarihindeki değerlerdir.

---
Kaynak: TreScout Keşif · https://trescout.com/discover/openship/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
