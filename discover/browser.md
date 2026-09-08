# Hızlı ve hafif yapay zekâ tarayıcısı

Lightpanda, yapay zekâ ve otomasyon süreçleri için özel olarak geliştirilmiş, Zig diliyle yazılmış bir başsız tarayıcı (headless browser). Geleneksel tarayıcılara kıyasla daha az kaynak tüketerek veri kazıma ve web otomasyonu işlemlerini hızlandırmayı amaçlıyor.

- ★ 35.072
- Zig
- GitHub Trending · 2026-09-08

## Güncelleme
- 8 Eylül 2026: Yıldız 35.068 → 35.072, son sürüm nightly (16 Temmuz 2024).

## Ne kazandırır?
- Geleneksel tarayıcılara göre 16 kata kadar daha az bellek tüketimi sağlar.
- Web sayfalarını 9 kata kadar daha hızlı işleyerek veri kazıma süreçlerini hızlandırır.
- Doğrudan tarayıcı içinde çalışan yapay zekâ ajan desteği sunar.

## Kurulum

**Homebrew ile macOS kurulumu**

```
brew install lightpanda-io/browser/lightpanda
```

**Docker ile konteyner kurulumu**

```
docker run -d --name lightpanda -p 127.0.0.1:9222:9222 lightpanda/browser:nightly
```

## Çalıştırma

**Web sayfasını metin olarak alma**

```
./lightpanda fetch --obey-robots --dump html --log-format pretty --log-level info https://demo-browser.lightpanda.io/campfire-commerce/
```

**CDP sunucusunu başlatma**

```
./lightpanda serve --obey-robots --log-format pretty --log-level info --host 127.0.0.1 --port 9222
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Sen bir web otomasyon uzmanısın. Lightpanda başsız tarayıcıyı kullanarak belirtilen web sitesindeki verileri en verimli şekilde çekmeni istiyorum. Bellek kullanımını optimize et, robots.txt kurallarına uy ve elde ettiğin veriyi yapılandırılmış bir formatta sun. İşlemi gerçekleştirirken hata payını düşürmek için gerekli bekleme sürelerini (wait-selector veya wait-ms) dinamik olarak ayarla.

- **Kimin için:** Hızlı veri kazıma ve web otomasyonu süreçlerinde kaynak tasarrufu yapmak isteyen yazılımcılar ve yapay zekâ ajanı geliştirenler için uygundur. 
- **Lisans:** AGPL-3.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/lightpanda-io/browser)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-09-08 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Headless Browser Web Scraping Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/browser/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
