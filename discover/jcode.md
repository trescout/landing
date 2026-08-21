# Kodlama ajanları için yüksek performanslı çerçeve

Rust diliyle geliştirilen jcode, kodlama odaklı yapay zekâ ajanlarını test etmek ve değerlendirmek için bir çerçeve (harness) sunuyor. Yazılım geliştirme süreçlerinde kullanılan ajanların performansını ölçmek amacıyla standart bir altyapı sağlıyor.

- ★ 18.120
- Rust
- GitHub Trending · 2026-06-21

## Güncelleme
- 21 Ağustos 2026: Yıldız 17.976 → 18.120, son sürüm v0.79.1 (21 Ağustos 2026).
- 19 Ağustos 2026: Yıldız 17.904 → 17.976, son sürüm v0.78.1 (19 Ağustos 2026).
- 18 Ağustos 2026: Yıldız 17.767 → 17.904, son sürüm v0.78.0 (18 Ağustos 2026).
- 17 Ağustos 2026: Yıldız 17.637 → 17.767, son sürüm v0.77.1 (17 Ağustos 2026).

## Ne kazandırır?
- Çoklu oturum iş akışlarında yüksek kaynak verimliliği
- Düşük bellek kullanımı ve hızlı başlatma süresi
- Kodlama odaklı yapay zekâ ajanları için test altyapısı

## Kurulum

**macOS ve Linux kurulumu**

```
curl -fsSL https://raw.githubusercontent.com/1jehuang/jcode/master/scripts/install.sh | bash
```

**Homebrew ile kurulum**

```
brew tap 1jehuang/jcode
brew install jcode
```

## Çalıştırma

**Ollama ile ilk çalıştırma**

```
ollama pull llama3.2
jcode login --provider ollama
jcode --provider ollama --model llama3.2 run 'hello'
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Kodlama odaklı yapay zekâ ajanımın performansını ve çoklu oturum yönetimi becerisini test etmek istiyorum. jcode çerçevesini kullanarak ajanımın kaynak kullanımını optimize etmemi ve standart bir test ortamı kurmamı sağla.

- **Kimin için:** Yazılım geliştirme süreçlerinde kullanılan yapay zekâ ajanlarını test etmek ve performanslarını ölçmek isteyen geliştiriciler içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/1jehuang/jcode)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-21 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Harness Rust Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/jcode/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
