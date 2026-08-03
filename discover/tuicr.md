# Terminalde Vim ile kod inceleme

Rust diliyle geliştirilen tuicr, Vim klavye kısayollarını destekleyen bir uçbirim kullanıcı arayüzü (terminal user interface) tabanlı kod inceleme (code review) aracıdır. Geliştiricilerin kod gözden geçirme süreçlerini doğrudan terminal üzerinden yönetmelerine olanak tanır.

- ★ 2.291
- Rust
- GitHub Trending · 2026-07-31

## Güncelleme
- 2 Ağustos 2026: Yıldız 1.940 → 2.291, son sürüm v0.20.0 (2 Ağustos 2026).

## Ne kazandırır?
- Vim kısayollarıyla terminalde hızlı kod inceleme
- GitHub ve GitLab'a doğrudan yorum gönderme
- Yapay zekâ araçları için yapılandırılmış çıktı desteği

## Kurulum

**Standart kurulum**

```
curl -fsSL tuicr.dev/install.sh | sh
# or
brew install agavra/tap/tuicr
```

**Alternatif paket yöneticileri**

```
# Cargo
cargo install tuicr

# Mise
mise use github:agavra/tuicr

# Nix
nix run github:agavra/tuicr
```

## Çalıştırma

**Yerel değişiklikleri inceleme**

```
tuicr -w
```

**Belirli bir PR'ı inceleme**

```
tuicr pr 125
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Bu kod incelemesini incele ve bulduğun hataları veya iyileştirme önerilerini, her bir yorumun dosya yolu ve satır numarasıyla belirtildiği yapılandırılmış bir liste halinde hazırla. İncelemeyi yaparken tuicr üzerinden kopyaladığım markdown formatındaki veriyi baz alarak, kodun okunabilirliğini ve performansını artıracak somut öneriler sun.

- **Kimin için:** Kod inceleme süreçlerini terminalden ayrılmadan, Vim kısayollarıyla yönetmek isteyen geliştiriciler içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/agavra/tuicr)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-07-31 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Code Review User Interface Markdown Terminal Rust Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/tuicr/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
