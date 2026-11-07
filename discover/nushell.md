# Yapılandırılmış nesneler sunan komut satırı arayüzü

Rust diliyle geliştirilen nushell, verileri yapılandırılmış nesneler olarak işleyen yeni bir komut satırı arayüzü (shell) sunuyor. Minimum uygulanabilir ürün (minimum-viable-product) seviyesine ulaşan bu proje, bazı komutlarda kararsızlık gösterebilse de günlük kullanım için tercih ediliyor.

- ★ 41.012
- Rust
- GitHub Trending · 2026-11-07

## Güncelleme

- **7 Kasım 2026:** Yıldız 41.011 → 41.012, son sürüm 0.116.1 (4 Ekim 2026).

## Ne kazandırır?

- Verileri yapılandırılmış nesneler olarak işler.
- Komutlar arasında boru hattı akışı sağlar.
- Dosya içeriklerini yapılandırılmış veri olarak yükler.

## Kurulum

**Kurulum**

```
# Linux and macOS
brew install nushell
# Windows
winget install nushell
```

## Çalıştırma

**Klasörleri Listeleme**

```
ls | where type == "dir" | table
# => ╭────┬──────────┬──────┬─────────┬───────────────╮
# => │ #  │   name   │ type │  size   │   modified    │
# => ├────┼──────────┼──────┼─────────┼───────────────┤
# => │  0 │ .cargo   │ dir  │     0 B │ 9 minutes ago │
# => │  1 │ assets   │ dir  │     0 B │ 2 weeks ago   │
# => │  2 │ crates   │ dir  │ 4.0 KiB │ 2 weeks ago   │
# => │  3 │ docker   │ dir  │     0 B │ 2 weeks ago   │
# => │  4 │ docs     │ dir  │     0 B │ 2 weeks ago   │
# => │  5 │ images   │ dir  │     0 B │ 2 weeks ago   │
# => │  6 │ pkg_mgrs │ dir  │     0 B │ 2 weeks ago   │
# => │  7 │ samples  │ dir  │     0 B │ 2 weeks ago   │
# => │  8 │ src      │ dir  │ 4.0 KiB │ 2 weeks ago   │
# => │  9 │ target   │ dir  │     0 B │ a day ago     │
# => │ 10 │ tests    │ dir  │ 4.0 KiB │ 2 weeks ago   │
# => │ 11 │ wix      │ dir  │     0 B │ 2 weeks ago   │
# => ╰────┴──────────┴──────┴─────────┴───────────────╯
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Nushell isimli yeni komut satırı arayüzünü kurmak ve kullanmak istiyorum. Kurulumu tamamladıktan sonra ls | where type == "dir" | table komutunu çalıştırmama yardımcı ol.

Depo: https://github.com/nushell/nushell. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Komut satırında verileri yapılandırılmış nesneler olarak yönetmek isteyen geliştiriciler için uygundur.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/nushell/nushell)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-11-07 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Shell](https://trescout.com/dictionary/shell/)
- [Rust](https://trescout.com/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/nushell/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
