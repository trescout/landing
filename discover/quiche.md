# Rust ile quic ve http3 destegi

Cloudflare tarafından geliştirilen quiche, QUIC taşıma protokolünün ve HTTP/3 ağ standardının Rust diliyle yazılmış bir uygulamasını sunuyor. İnternet trafiğini hızlandırmayı amaçlayan bu kütüphane, ağ performansını optimize etmek isteyen geliştiriciler için düşük seviyeli bir altyapı sağlıyor.

- ★ 12.638
- GitHub Trending · 2026-09-20

## Güncelleme
- 27 Eylül 2026: Yıldız 12.452 → 12.638, son sürüm 0.30.0 (17 Eylül 2026).

## Ne kazandırır?
- QUIC tasiyma protokolunu uygulamak
- HTTP/3 ag standardi uzerinde calismak
- Dusuk seviyeli ag paketlerini islemek

## Kurulum

**Projeyi klonlayin**

```
git clone https://github.com/cloudflare/quiche
```

## Çalıştırma

**Istemciyi calistirin**

```
cargo run --bin quiche-client -- https://cloudflare-quic.com/
```

**Sunucuyu calistirin**

```
cargo run --bin quiche-server -- --cert apps/src/bin/cert.crt --key apps/src/bin/cert.key
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Rust programlama dilinde yazilmis olan bu kutuphaneyi kullanarak QUIC paketlerini islemek ve ag baglanti durumlarini yonetmek istiyorum. Projeyi klonladiktan sonra istemciyi ve sunucuyu calistirmak icin hangi adimlari izlemeliyim?

- **Kimin için:** Ag performansini optimize etmek ve HTTP/3 destegi saglamak isteyen gelistiriciler. 
- **Lisans:** BSD-2-Clause 

## Bağlantılar
- [GitHub deposu →](https://github.com/cloudflare/quiche)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-09-20 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Rust Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/quiche/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
