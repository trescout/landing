# Terminal için yapay zekâ kodlama ajanı

DeepSeek-Reasonix, terminal üzerinde çalışan ve DeepSeek modellerini temel alan bir yapay zekâ kodlama ajanıdır. Önek önbelleği (prefix-cache) kararlılığına odaklanan bu araç, geliştiricilerin uzun süreli oturumlarda kesintisiz kodlama desteği almasını sağlar.

- ★ 35.946
- Go
- GitHub Trending · 2026-08-03

## Güncelleme

- **24 Ekim 2026:** Yıldız 35.939 → 35.946, son sürüm studio-v2.50.0 (23 Ekim 2026).
- **23 Ekim 2026:** Yıldız 35.906 → 35.939, son sürüm studio-v2.49.0 (22 Ekim 2026).
- **22 Ekim 2026:** Yıldız 35.898 → 35.906, son sürüm studio-v2.48.0 (22 Ekim 2026).
- **21 Ekim 2026:** Yıldız 35.879 → 35.898, son sürüm studio-v2.47.1 (21 Ekim 2026).

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

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Terminal üzerinde çalışan bu yapay zekâ kodlama ajanı ile çalışırken, projemin mevcut yapısını ve hedeflerini göz önünde bulundurarak kod önerileri geliştir. Önek önbelleği kararlılığını kullanarak uzun süreli oturumlarımızda tutarlı ve düşük maliyetli yanıtlar üretmeye odaklan. Kod yazarken veya hata ayıklarken, projenin gereksinimlerine uygun, modüler ve temiz çözümler sun.

Depo: https://github.com/esengine/DeepSeek-Reasonix. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Terminal ortamında çalışan, kodlama süreçlerini otomatize etmek ve uzun süreli projelerde yapay zekâ desteği almak isteyen yazılım geliştiriciler içindir.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/esengine/DeepSeek-Reasonix)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-08-03 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Terminal](https://trescout.com/dictionary/terminal/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/deepseek-reasonix/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
