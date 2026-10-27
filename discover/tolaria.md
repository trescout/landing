# Markdown bilgi tabanı masaüstü uygulaması

Tolaria, Markdown tabanlı bilgi tabanlarını yönetmek için geliştirilen bir masaüstü uygulamasıdır. TypeScript ile yazılan bu araç, kişisel dokümantasyon ve not sistemlerini düzenli bir yapıda tutmayı kolaylaştırır.

- ★ 20.359
- TypeScript
- GitHub Trending · 2026-06-08

## Güncelleme

- **27 Ekim 2026:** Yıldız 20.061 → 20.359, son sürüm v2026-10-26 (26 Ekim 2026).
- **13 Ekim 2026:** Yıldız 19.906 → 20.061, son sürüm v2026-10-13 (13 Ekim 2026).
- **27 Eylül 2026:** Yıldız 19.727 → 19.906, son sürüm v2026-09-24 (24 Eylül 2026).
- **8 Eylül 2026:** Yıldız 19.643 → 19.727, son sürüm v2026-09-08 (8 Eylül 2026).

## Ne kazandırır?

- Markdown dosyalarıyla taşınabilir not yönetimi sağlar.
- Git entegrasyonu ile tam sürüm kontrolü sunar.
- Çevrimdışı çalışma desteğiyle veri sahipliğini korur.

## Kurulum

**Arch/Manjaro için bağımlılıklar**

```
sudo pacman -S --needed webkit2gtk-4.1 base-devel curl wget file openssl \
    appmenu-gtk-module libappindicator-gtk3 librsvg
```

**Debian/Ubuntu için bağımlılıklar**

```
sudo apt install libwebkit2gtk-4.1-dev build-essential curl wget file \
    libxdo-dev libssl-dev libayatana-appindicator3-dev librsvg2-dev \
    libsoup-3.0-dev patchelf
```

## Çalıştırma

**Geliştirme ortamını başlatma**

```
pnpm install
pnpm dev
```

**Masaüstü uygulamasını çalıştırma**

```
pnpm tauri dev
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Tolaria masaüstü uygulamasını kullanarak Markdown tabanlı bilgi tabanımı nasıl yapılandırabilirim? Uygulamanın Git tabanlı yapısını, çevrimdışı çalışma prensibini ve yapay zekâ ajanlarıyla uyumlu çalışma özelliklerini kullanarak notlarımı nasıl organize edeceğimi, standart Markdown dosyalarımı nasıl yöneteceğimi ve klavye odaklı komut paletinden nasıl verim alacağımı adım adım açıkla.

Depo: https://github.com/refactoringhq/tolaria. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Kişisel bilgi yönetimini Markdown dosyaları ve Git sürüm kontrolü ile yerel, çevrimdışı ve özgür bir sistemde tutmak isteyen kullanıcılar içindir.
- **Lisans:** AGPL-3.0

## Bağlantılar

- [GitHub deposu →](https://github.com/refactoringhq/tolaria)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-06-08 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Markdown](https://trescout.com/dictionary/markdown/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/tolaria/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
