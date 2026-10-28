# WhatsApp için açık kaynaklı ağ geçidi

OpenWA, WhatsApp mesajlaşma protokolü için ücretsiz ve açık kaynaklı bir ağ geçidi (API gateway) çözümü sunuyor. TypeScript diliyle geliştirilen bu araç, kullanıcıların kendi sunucularında (self-hosted) WhatsApp entegrasyonlarını yönetmelerine olanak tanıyor.

- ★ 16.328
- TypeScript
- GitHub Trending · 2026-06-17

## Güncelleme

- **28 Ekim 2026:** Yıldız 15.471 → 16.328, son sürüm v0.26.0 (28 Ekim 2026).
- **15 Ekim 2026:** Yıldız 14.976 → 15.471, son sürüm v0.25.0 (15 Ekim 2026).
- **3 Ekim 2026:** Yıldız 14.622 → 14.976, son sürüm v0.24.0 (3 Ekim 2026).
- **27 Eylül 2026:** Yıldız 14.197 → 14.622, son sürüm v0.23.7 (25 Eylül 2026).

## Ne kazandırır?

- WhatsApp mesajlaşma altyapısı üzerinde tam kontrol
- Modern arayüz ile oturum ve webhook yönetimi
- Docker desteği ile hızlı ve kolay kurulum

## Kurulum

**Docker ile hızlı kurulum**

```
# Clone and start
git clone https://github.com/rmyndharis/OpenWA.git
cd OpenWA
docker compose -f docker-compose.dev.yml up -d

# Access
# Dashboard: http://localhost:2886
# API: http://localhost:2785/api
# Swagger: http://localhost:2785/api/docs
```

**Yerel geliştirme ortamı**

```
# Clone repository
git clone https://github.com/rmyndharis/OpenWA.git
cd OpenWA

# Install dependencies (includes dashboard)
npm install

# Start API + Dashboard (config is auto-generated on first run)
npm run dev

# Access
# Dashboard: http://localhost:2886
# API: http://localhost:2785/api
# Swagger: http://localhost:2785/api/docs
```

## Çalıştırma

**Üretim ortamında başlatma**

```
# Basic production (SQLite, local storage)
docker compose up -d

# With PostgreSQL database
docker compose --profile postgres up -d

# Full stack (PostgreSQL, Redis, Dashboard, Traefik)
docker compose --profile full up -d
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

OpenWA aracını kullanarak WhatsApp üzerinden mesajlaşma süreçlerimi otomatize etmek istiyorum. REST API uç noktalarını kullanarak yeni bir oturum oluşturmak, mesaj göndermek ve gelen mesajları webhook üzerinden dinlemek için gerekli temel yapılandırma adımlarını bana açıkla. Özellikle çoklu oturum yönetimi ve API anahtarı güvenliği konularında dikkat etmem gerekenleri belirt.

Depo: https://github.com/rmyndharis/OpenWA. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Bir API anahtarı gerekirse onu sohbete yazmamı isteme. .env dosyasına nasıl ekleyeceğimi göster ve bu dosyanın Git'e gönderilmediğinden emin ol.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Kendi WhatsApp entegrasyonlarını geliştirmek isteyen ve mesajlaşma altyapısı üzerinde tam kontrol sahibi olmayı hedefleyen yazılımcılar içindir.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/rmyndharis/OpenWA)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-06-17 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [API Gateway](https://trescout.com/dictionary/api-gateway/)
- [Gateway](https://trescout.com/dictionary/gateway/)
- [Self-hosted](https://trescout.com/dictionary/self-hosted/)
- [API](https://trescout.com/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/openwa/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
