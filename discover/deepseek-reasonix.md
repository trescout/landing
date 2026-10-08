# Terminal için yapay zekâ kodlama ajanı

DeepSeek-Reasonix, terminal üzerinde çalışan ve DeepSeek modellerini temel alan bir yapay zekâ kodlama ajanıdır. Önek önbelleği (prefix-cache) kararlılığına odaklanan bu araç, geliştiricilerin uzun süreli oturumlarda kesintisiz kodlama desteği almasını sağlar.

- ★ 35.747
- Go
- GitHub Trending · 2026-08-03

## Güncelleme

- **8 Ekim 2026:** Yıldız 35.747 → 35.747, son sürüm studio-v2.32.0 (8 Ekim 2026).
- **8 Ekim 2026:** Yıldız 35.744 → 35.747, son sürüm studio-v2.31.0 (8 Ekim 2026).
- **7 Ekim 2026:** Yıldız 35.742 → 35.744, son sürüm studio-v2.30.0 (7 Ekim 2026).
- **6 Ekim 2026:** Yıldız 35.735 → 35.742, son sürüm studio-v2.29.0 (6 Ekim 2026).

## Ne kazandırır?

- DeepSeek modelleriyle uzun süreli kesintisiz kodlama desteği sağlar.
- Önek önbelleği özelliğiyle düşük maliyetli oturum yönetimi sunar.
- Yapılandırılabilir eklenti desteğiyle terminal üzerinden esnek kullanım imkânı tanır.

## Kurulum

**NPM veya Homebrew ile kurulum**

```
npm i -g reasonix                  # any OS; pulls the prebuilt native binary
brew install esengine/reasonix/reasonix   # macOS
```

**Kaynak koddan derleme**

```
git clone https://github.com/esengine/DeepSeek-Reasonix.git
cd DeepSeek-Reasonix
make build      # -> bin/reasonix(.exe)
make cross      # -> dist/ (darwin|linux|windows × amd64|arm64)
```

## Çalıştırma

**Yapılandırma ve başlatma**

```
reasonix setup                      # configure a provider and model
reasonix                            # start an interactive session
reasonix run "implement the TODOs in main.go"
```

## Kod bilmiyorsanız

🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Terminal üzerinde çalışan bu yapay zekâ kodlama ajanı ile çalışırken, projemin mevcut yapısını ve hedeflerini göz önünde bulundurarak kod önerileri geliştir. Önek önbelleği kararlılığını kullanarak uzun süreli oturumlarımızda tutarlı ve düşük maliyetli yanıtlar üretmeye odaklan. Kod yazarken veya hata ayıklarken, projenin gereksinimlerine uygun, modüler ve temiz çözümler sun.

- **Kimin için:** Terminal ortamında çalışan, kodlama süreçlerini otomatize etmek ve uzun süreli projelerde yapay zekâ desteği almak isteyen yazılım geliştiriciler içindir.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/esengine/DeepSeek-Reasonix)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-03 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Terminal](https://trescout.com/dictionary/terminal/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/deepseek-reasonix/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
