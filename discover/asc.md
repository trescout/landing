# Android uygulamalarını hızlıca analiz edin

ASC, mobil uygulama araştırmacıları ve yapay zekâ ajanları için geliştirilmiş oldukça hızlı bir Android kaynak koda dönüştürücü (decompiler) arayüzüdür. Python ile yazılan bu araç, karmaşık uygulama dosyalarını analiz etme sürecini hızlandırmayı hedefler.

- ★ 2.498
- Python
- GitHub Trending · 2026-09-16

## Güncelleme

- **21 Ekim 2026:** Yıldız 2.399 → 2.498, son sürüm dev-0.1.2-post3 (21 Ekim 2026).
- **15 Ekim 2026:** Yıldız 2.236 → 2.399, son sürüm dev-0.1.2-post2 (14 Ekim 2026).
- **10 Ekim 2026:** Yıldız 1.980 → 2.236, son sürüm dev-0.1.1-post4 (10 Ekim 2026).
- **27 Eylül 2026:** Yıldız 1.336 → 1.980, son sürüm dev-0.1.1-post2 (21 Eylül 2026).

## Ne kazandırır?

- Büyük uygulama dosyalarını saniyeler içinde tarar
- Belleği yormadan doğrudan kod üzerinde sorgu yapar
- Gereksiz ön işlem yapmadan hızlı sonuç üretir

## Kurulum

**Paket yöneticisi ile kurulum**

```
pip install droidasc
```

**Kaynak koddan kurulum**

```
pip install .
```

## Çalıştırma

**Uygulama dosyasını görsel arayüzle açma**

```
droidasc app.apk --gui
```

**Belirli bir sınıfı dışa aktarma**

```
droidasc getclass app.apk Lcom/poc/Main; -o Main.java
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Bir Android uygulama araştırmacısı gibi davran. Droid ASC aracını kullanarak bir APK dosyasındaki belirli bir sınıfı bulmak, AndroidManifest.xml dosyasını çözümlemek veya kod içindeki referansları aramak için bana yardımcı ol. Komutları oluştururken aracın getclass, getmanifest ve findrefs komutlarını doğru parametrelerle kullan ve çıktıları nasıl yorumlamam gerektiğini açıkla.

Depo: https://github.com/MG1937/ASC. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Mobil uygulama güvenliği araştırmacıları ve Android yazılım geliştiricileri için uygundur.
- **Lisans:** Apache-2.0

## Bağlantılar

- [GitHub deposu →](https://github.com/MG1937/ASC)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-09-16 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Decompiler](https://trescout.com/dictionary/decompiler/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/asc/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
