# Yapay zekâ ile ofis dosyalarını yönetin

OfficeCLI, yapay zekâ ajanlarının Word, Excel ve PowerPoint dosyalarını doğrudan okumasına, düzenlemesine ve otomatize etmesine olanak tanıyan açık kaynaklı bir ofis paketi sunuyor. C# ile geliştirilen bu araç, herhangi bir ofis yazılımı kurulumuna ihtiyaç duymadan tek bir ikili dosya (binary) üzerinden işlem yapılmasına imkân veriyor.

- ★ 29.368
- C#
- GitHub Trending · 2026-07-08

## Güncelleme
- 27 Ağustos 2026: Yıldız 28.422 → 29.368, son sürüm v1.0.145 (25 Ağustos 2026).
- 15 Ağustos 2026: Yıldız 27.506 → 28.422, son sürüm v1.0.144 (13 Ağustos 2026).
- 11 Ağustos 2026: Yıldız 25.967 → 27.506, son sürüm v1.0.143 (28 Temmuz 2026).
- 6 Ağustos 2026: Yıldız 24.245 → 25.967, son sürüm v1.0.143 (28 Temmuz 2026).

## Ne kazandırır?
- Word, Excel ve PowerPoint dosyalarını kodla düzenleyin
- Ofis yazılımı kurmadan doğrudan işlem yapın
- Yapay zekâ ajanlarına belge oluşturma yeteneği kazandırın

## Kurulum

**macOS veya Linux üzerine kurulum**

```
curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash
```

**Windows üzerine kurulum**

```
irm https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.ps1 | iex
```

## Çalıştırma

**Boş bir sunum oluşturma**

```
officecli create deck.pptx
```

**Sunuma slayt ekleme**

```
officecli add deck.pptx / --type slide --prop title="Hello, World!"
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Senin için hazırlanan OfficeCLI aracı ile Word, Excel ve PowerPoint dosyalarını yönetebilirsin. Bu aracı kullanabilmen için şu komutu çalıştırarak gerekli beceri dosyasını yükle: curl -fsSL https://officecli.ai/SKILL.md. Bu işlemden sonra ofis belgeleri üzerinde okuma, düzenleme ve oluşturma işlemlerini komut satırı üzerinden gerçekleştirebilirsin.

- **Kimin için:** Ofis belgelerini otomatize etmek isteyen geliştiriciler ve yapay zekâ ajanlarını ofis süreçlerine entegre etmek isteyen kullanıcılar içindir. 
- **Lisans:** Apache-2.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/iOfficeAI/OfficeCLI)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-07-08 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Binary PowerPoint Skill Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/officecli/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
