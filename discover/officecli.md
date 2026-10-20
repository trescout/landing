# Yapay zekâ ile ofis dosyalarını yönetin

OfficeCLI, yapay zekâ ajanlarının Word, Excel ve PowerPoint dosyalarını doğrudan okumasına, düzenlemesine ve otomatize etmesine olanak tanıyan açık kaynaklı bir ofis paketi sunuyor. C# ile geliştirilen bu araç, herhangi bir ofis yazılımı kurulumuna ihtiyaç duymadan tek bir ikili dosya (binary) üzerinden işlem yapılmasına imkân veriyor.

- ★ 32.214
- C#
- GitHub Trending · 2026-07-08

## Güncelleme

- **20 Ekim 2026:** Yıldız 31.905 → 32.214, son sürüm v1.0.158 (20 Ekim 2026).
- **12 Ekim 2026:** Yıldız 31.762 → 31.905, son sürüm v1.0.157 (12 Ekim 2026).
- **9 Ekim 2026:** Yıldız 31.612 → 31.762, son sürüm v1.0.156 (9 Ekim 2026).
- **6 Ekim 2026:** Yıldız 31.577 → 31.612, son sürüm v1.0.155 (6 Ekim 2026).

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

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Senin için hazırlanan OfficeCLI aracı ile Word, Excel ve PowerPoint dosyalarını yönetebilirsin. Bu aracı kullanabilmen için şu komutu çalıştırarak gerekli beceri dosyasını yükle: curl -fsSL https://officecli.ai/SKILL.md. Bu işlemden sonra ofis belgeleri üzerinde okuma, düzenleme ve oluşturma işlemlerini komut satırı üzerinden gerçekleştirebilirsin.

Depo: https://github.com/iOfficeAI/OfficeCLI. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Ofis belgelerini otomatize etmek isteyen geliştiriciler ve yapay zekâ ajanlarını ofis süreçlerine entegre etmek isteyen kullanıcılar içindir.
- **Lisans:** Apache-2.0

## Bağlantılar

- [GitHub deposu →](https://github.com/iOfficeAI/OfficeCLI)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-07-08 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [PowerPoint](https://trescout.com/dictionary/powerpoint/)
- [Binary](https://trescout.com/dictionary/binary/)
- [Skill](https://trescout.com/dictionary/skill/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/officecli/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
