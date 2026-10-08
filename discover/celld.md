# Dağıtık sistemlerde kalıcı veri yönetimi

Deno tarafından geliştirilen Celld, dağıtık sistemler için kendi sunucunuzda barındırabileceğiniz (self-hosted) kalıcı nesneler (durable objects) altyapısı sunuyor. Rust diliyle yazılan bu teknoloji, durum yönetimini (state management) farklı düğümler arasında ölçeklenebilir şekilde dağıtmayı sağlıyor.

- ★ 5.067
- Rust
- GitHub Trending · 2026-08-08

## Güncelleme

- **8 Ekim 2026:** Yıldız 4.937 → 5.067, son sürüm v0.6.2 (7 Ekim 2026).
- **2 Ekim 2026:** Yıldız 4.817 → 4.937, son sürüm v0.6.1 (1 Ekim 2026).
- **27 Eylül 2026:** Yıldız 4.630 → 4.817, son sürüm v0.6.0 (26 Eylül 2026).
- **15 Eylül 2026:** Yıldız 4.521 → 4.630, son sürüm v0.5.0 (15 Eylül 2026).

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

- [State Management](https://trescout.com/dictionary/state-management/)
- [Durable Objects](https://trescout.com/dictionary/durable-objects/)
- [Self-hosted](https://trescout.com/dictionary/self-hosted/)
- [Rust](https://trescout.com/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/celld/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
