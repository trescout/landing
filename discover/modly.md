# Görsellerden üç boyutlu modeller oluşturun

Modly, görsellerden üç boyutlu modeller (3D models) oluşturan ve tüm işlemleri yerel ekran kartı (GPU) üzerinde gerçekleştiren bir masaüstü uygulamasıdır. İnternet bağlantısına ihtiyaç duymadan çalışan bu araç, yapay zekâ destekli modelleme sürecini kişisel bilgisayarlara taşır.

- ★ 6.115
- TypeScript
- GitHub Trending · 2026-08-14

## Güncelleme
- 15 Ağustos 2026: Yıldız 5.550 → 6.115, son sürüm v0.4.1 (16 Temmuz 2026).

## Ne kazandırır?
- Fotoğrafları yerel bilgisayarda 3D modellere dönüştürür
- İnternet bağlantısı gerektirmeden tamamen çevrimdışı çalışır
- Harici modellerle genişletilebilir esnek bir yapı sunar

## Kurulum

**Bağımlılıkları yükleme**

```
npm install
```

**Python altyapısını hazırlama**

```
cd api
python -m venv .venv
.venv\Scripts\activate # Windows
source .venv/bin/activate # Linux / macOS
pip install -r requirements.txt
```

## Çalıştırma

**Uygulamayı başlatma**

```
# Windows
launch.bat

# Linux / macOS
./launch.sh
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Modly uygulamasını kullanarak bir görseli 3D modele dönüştürmek istiyorum. Uygulama içerisinde 'Workflows' sekmesine giderek 'Image -> Generate Mesh -> Add to Scene' akışını kurmama yardımcı ol. Ardından 'Generate' sekmesinden ilgili iş akışını seçerek 3D model üretimini başlatmamı sağla. Eğer bir hata alırsam 'Settings/Logs/Errors' kısmından sorunu nasıl analiz edebilirim?

- **Kimin için:** Kendi bilgisayarının ekran kartı gücünü kullanarak gizlilikten ödün vermeden üç boyutlu tasarımlar üretmek isteyen dijital sanatçılar ve geliştiriciler içindir. 

## Bağlantılar
- [GitHub deposu →](https://github.com/lightningpixel/modly)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-14 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Logs Workflows Mesh GPU Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/modly/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
