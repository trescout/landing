# Web siteleri için betik dili

PHP, özellikle web geliştirme süreçleri için tasarlanmış genel amaçlı bir betik dili (scripting language) olarak kullanılıyor. C diliyle yazılan bu yorumlayıcı, dünya genelindeki birçok internet sitesinin altyapısını oluşturuyor.

- ★ 41.410
- C
- GitHub Trending · 2026-10-23

## Güncelleme

- **23 Ekim 2026:** Yıldız 41.391 → 41.410, son sürüm php-8.5.12 (21 Ekim 2026).

## Ne kazandırır?

- Dinamik internet siteleri ve web uygulamaları çalıştırmanızı sağlar.
- Kaynak kodundan doğrudan derleyerek en güncel sürümü test etme imkânı sunar.
- Kapsamlı yerleşik test araçlarıyla sistem kararlılığını ölçmenize yardımcı olur.

## Kurulum

**Ubuntu için derleme araçlarını kurun**

```
sudo apt install -y pkg-config build-essential autoconf bison re2c libxml2-dev libsqlite3-dev
```

**Fedora için derleme araçlarını kurun**

```
sudo dnf install re2c bison autoconf make ccache libxml2-devel sqlite-devel
```

## Çalıştırma

**Kaynak kodunu derleyin**

```
make -j4
```

**Testleri çalıştırın**

```
make TEST_PHP_ARGS=-j4 test
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

PHP yorumlayıcısını kaynak kodundan derleyip test etmek istiyorum. Ubuntu kullanıyorsam paket yönetim aracı üzerinden gerekli derleme araçlarını kurmak için sudo apt install -y pkg-config build-essential autoconf bison re2c libxml2-dev libsqlite3-dev komutunu çalıştır. Fedora kullanıyorsam sudo dnf install re2c bison autoconf make ccache libxml2-devel sqlite-devel komutunu, macOS kullanıyorsam paket yöneticisi Homebrew ile brew install autoconf bison re2c libiconv libxml2 sqlite komutunu kullan. Ardından projeyi derlemek için make -j4 komutunu yürüt. Derleme tamamlandıktan sonra testleri eşzamanlı olarak koşturmak için make TEST_PHP_ARGS=-j4 test komutunu veya dil testlerini çalıştırmak için make TESTS=tests/lang/ test komutunu uygula.

Depo: https://github.com/php/php-src. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Web uygulamaları geliştirenler ve PHP çekirdek kodunu inceleyip doğrudan kaynaktan derlemek isteyen geliştiriciler içindir.
- **Lisans:** BSD-3-Clause

## Bağlantılar

- [GitHub deposu →](https://github.com/php/php-src)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-10-23 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Scripting Language](https://trescout.com/dictionary/scripting-language/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/php-src/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
