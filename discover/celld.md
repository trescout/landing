# Dağıtık sistemlerde kalıcı veri yönetimi

Deno tarafından geliştirilen Celld, dağıtık sistemler için kendi sunucunuzda barındırabileceğiniz (self-hosted) kalıcı nesneler (durable objects) altyapısı sunuyor. Rust diliyle yazılan bu teknoloji, durum yönetimini (state management) farklı düğümler arasında ölçeklenebilir şekilde dağıtmayı sağlıyor.

- ★ 3.656
- Rust
- GitHub Trending · 2026-08-08

## Güncelleme
- 15 Ağustos 2026: Yıldız 2.266 → 3.656, son sürüm v0.2.1 (14 Ağustos 2026).
- 8 Ağustos 2026: Yıldız 2.264 → 2.266, son sürüm v0.1.0 (5 Ağustos 2026).

## Ne kazandırır?
- Kendi altyapınızda ölçeklenebilir durum yönetimi sağlar.
- Her nesneyi bağımsız bir SQLite veritabanı olarak saklar.
- S3 uyumlu depolama ile düğümler arası koordinasyon kurar.

## Kurulum

**Aracı bilgisayarınıza indirme**

```
curl -fsSL https://celld.dev/install.sh | sh
```

## Çalıştırma

**Kaynak kullanımı sınırlandırılmış düğüm**

```
CELLD_MAX_RESIDENT_CELLS=1000 \
CELLD_RESIDENT_LOW_WATER=800 \
celld --bucket s3://my-cells-bucket --listen 0.0.0.0:8080 \
--advertise node-a.internal:8080
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Celld kullanarak dağıtık bir sistem kurmak istiyorum. S3 uyumlu bir depolama alanı oluşturduktan sonra, düğümlerin bu alanı nasıl kullanacağını ve Wrangler paketlerini nasıl dağıtacağımı adım adım açıkla. Özellikle düğümlerin birbirini nasıl keşfettiği ve veri tutarlılığını S3 üzerinden nasıl sağladığı konusunda teknik detayları basit bir dille özetle.

- **Kimin için:** Dağıtık sistemler üzerinde çalışan ve kendi sunucularında ölçeklenebilir durum yönetimi kurmak isteyen geliştiriciler için uygundur. 
- **Lisans:** Apache-2.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/denoland/celld)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-08 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
State Management Durable Objects Self-hosted Rust Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/celld/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
