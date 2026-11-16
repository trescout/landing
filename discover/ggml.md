# Yapay zekâ modelleri için tensör kütüphanesi

ggml-org/ggml, makine öğrenmesi modelleri için C++ diliyle geliştirilmiş bir tensör kütüphanesidir. Yazılım, temel matris çarpımı gibi işlemler için sade ve açıklayıcı örnekler sunarak yapay zekâ modellerinin çalıştırılmasını kolaylaştırır.

- ★ 15.988
- C++
- GitHub Trending · 2026-11-16

## Güncelleme

- **16 Kasım 2026:** Yıldız 15.982 → 15.988, son sürüm v1.0.0 (13 Kasım 2026).

## Ne kazandırır?

- Haricî bağımlılık olmadan C ve C++ dilleriyle yüksek performanslı tensör işlemleri sunar.
- Merkezî işlem birimi CPU, grafik işlem birimi GPU ve tarayıcı ortamlarında çalışabilir.
- Veri boyutunu küçülten kuantizasyon biçimleriyle bellek kullanımını azaltır.

## Kurulum

**Kaynak koddan derleme**

```
git clone https://github.com/ggml-org/ggml
cd ggml

mkdir build && cd build
cmake ..
cmake --build . --config Release -j 8
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Yapay zekâ modellerini çalıştırmak amacıyla ggml tensör kütüphanesini kaynak koddan derlemek istiyorum. İlgili repoyu klonlayıp derleme klasörü oluşturmak ve yazılımı derlemek için `git clone https://github.com/ggml-org/ggml
cd ggml

mkdir build && cd build
cmake ..
cmake --build . --config Release -j 8` komutunu adım adım çalıştırmamda bana rehberlik et.

Depo: https://github.com/ggml-org/ggml. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Yapay zekâ modellerini farklı donanımlarda minimum kaynak kullanımıyla çalıştırmak isteyen geliştiriciler içindir.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/ggml-org/ggml)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-11-16 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [CPU](https://trescout.com/dictionary/cpu/)
- [Clone](https://trescout.com/dictionary/clone/)
- [GPU](https://trescout.com/dictionary/gpu/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/ggml/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
