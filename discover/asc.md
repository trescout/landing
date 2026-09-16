# Android uygulamalarını hızlıca analiz edin

ASC, mobil uygulama araştırmacıları ve yapay zekâ ajanları için geliştirilmiş oldukça hızlı bir Android kaynak koda dönüştürücü (decompiler) arayüzüdür. Python ile yazılan bu araç, karmaşık uygulama dosyalarını analiz etme sürecini hızlandırmayı hedefler.

- ★ 1.336
- Python
- GitHub Trending · 2026-09-16

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
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Bir Android uygulama araştırmacısı gibi davran. Droid ASC aracını kullanarak bir APK dosyasındaki belirli bir sınıfı bulmak, AndroidManifest.xml dosyasını çözümlemek veya kod içindeki referansları aramak için bana yardımcı ol. Komutları oluştururken aracın getclass, getmanifest ve findrefs komutlarını doğru parametrelerle kullan ve çıktıları nasıl yorumlamam gerektiğini açıkla.

- **Kimin için:** Mobil uygulama güvenliği araştırmacıları ve Android yazılım geliştiricileri için uygundur. 
- **Lisans:** Apache-2.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/MG1937/ASC)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-09-16 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Decompiler Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/asc/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
