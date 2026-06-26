# WhatsApp için açık kaynaklı ağ geçidi

OpenWA, WhatsApp mesajlaşma protokolü için ücretsiz ve açık kaynaklı bir ağ geçidi (API gateway) çözümü sunuyor. TypeScript diliyle geliştirilen bu araç, kullanıcıların kendi sunucularında (self-hosted) WhatsApp entegrasyonlarını yönetmelerine olanak tanıyor.

- ★ 9.223
- TypeScript
- GitHub Trending · 2026-06-17

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
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
OpenWA aracını kullanarak WhatsApp üzerinden mesajlaşma süreçlerimi otomatize etmek istiyorum. REST API uç noktalarını kullanarak yeni bir oturum oluşturmak, mesaj göndermek ve gelen mesajları webhook üzerinden dinlemek için gerekli temel yapılandırma adımlarını bana açıkla. Özellikle çoklu oturum yönetimi ve API anahtarı güvenliği konularında dikkat etmem gerekenleri belirt.

- **Kimin için:** Kendi WhatsApp entegrasyonlarını geliştirmek isteyen ve mesajlaşma altyapısı üzerinde tam kontrol sahibi olmayı hedefleyen yazılımcılar içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/rmyndharis/OpenWA)

## İlgili sözlük terimleri
API Gateway Self-hosted API Artificial Intelligence 

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Yıldız ve sayılar keşif tarihindeki değerlerdir.

---
Kaynak: TreScout Keşif · https://trescout.com/discover/openwa/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
