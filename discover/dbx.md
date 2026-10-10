# Hafif veritabanı istemcisi

Rust diliyle geliştirilen dbx, 100'den fazla veritabanı türünü destekleyen 25 MB boyutunda hafif bir veritabanı istemcisi (database client) sunuyor. Masaüstü uygulaması, komut satırı arayüzü (CLI) ve Docker desteğinin yanı sıra yerleşik yapay zekâ asistanı ve Model Bağlantı Protokolü (MCP) gibi özellikler içeriyor.

- ★ 25.555
- Rust
- GitHub Trending · 2026-09-29

## Güncelleme

- **10 Ekim 2026:** Yıldız 25.380 → 25.555, son sürüm v0.6.39 (10 Ekim 2026).
- **9 Ekim 2026:** Yıldız 25.357 → 25.380, son sürüm v0.6.38 (9 Ekim 2026).
- **9 Ekim 2026:** Yıldız 25.183 → 25.357, son sürüm v0.6.37 (8 Ekim 2026).
- **8 Ekim 2026:** Yıldız 24.988 → 25.183, son sürüm v0.6.36 (8 Ekim 2026).

## Ne kazandırır?

- Yüzden fazla veritabanı türünü destekler.
- Masaüstü, Docker ve komut satırı ile çalışır.
- Yapay zekâ asistanı ve Model Bağlantı Protokolü içerir.

## Kurulum

**Masaüstü Uygulaması Kurulumu**

```
brew install --cask dbx
```

**Komut Satırı Aracı Kurulumu**

```
npm install -g @dbx-app/cli
# or via Homebrew
brew tap t8y2/tap && brew install dbx-cli
dbx agent setup
dbx connections list --json
dbx query local "select 1" --json
```

## Çalıştırma

**Docker ile Çalıştırma**

```
# The default keeps the key in the persistent /app/data volume.
docker run -d --pull=always --name dbx -p 4224:4224 \
  -v dbx-data:/app/data \
  t8y2/dbx:latest
```

## Kod bilmiyorsanız

🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

dbx uygulamasını kurmak ve çalıştırmak için gerekli adımları uygula. Masaüstü uygulaması için brew install --cask dbx komutunu, komut satırı aracı için ise npm install -g @dbx-app/cli
# or via Homebrew
brew tap t8y2/tap && brew install dbx-cli
dbx agent setup
dbx connections list --json
dbx query local "select 1" --json komutlarını kullan. Docker ile çalıştırmak istersen # The default keeps the key in the persistent /app/data volume.
docker run -d --pull=always --name dbx -p 4224:4224 \
-v dbx-data:/app/data \
t8y2/dbx:latest komutunu çalıştır.

- **Kimin için:** Farklı veritabanı türlerini hafif bir arayüz ve yapay zekâ desteğiyle yönetmek isteyen geliştiriciler içindir.
- **Lisans:** Apache-2.0

## Bağlantılar

- [GitHub deposu →](https://github.com/t8y2/dbx)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-09-29 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Database Client](https://trescout.com/dictionary/database-client/)
- [Local](https://trescout.com/dictionary/local/)
- [Database](https://trescout.com/dictionary/database/)
- [MCP](https://trescout.com/dictionary/mcp/)
- [Agent](https://trescout.com/dictionary/agent/)
- [CLI](https://trescout.com/dictionary/cli/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/dbx/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
