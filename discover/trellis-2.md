# Görsellerden yüksek kaliteli 3D modeller üretin

Microsoft tarafından geliştirilen TRELLIS, metin veya görsel girdilerini üç boyutlu (3D) modellere dönüştüren bir yapısal gizli temsil (structured latent) mimarisi. Bu teknoloji, yüksek kaliteli 3D varlıkları hızlı ve kompakt bir şekilde oluşturmak için üretken yapay zekâ (generative AI) yöntemlerini kullanıyor.

- ★ 12.009
- Python
- GitHub Trending · 2026-08-02

## Güncelleme

- **15 Ekim 2026:** Yıldız 11.002 → 12.009.
- **3 Eylül 2026:** Yıldız 9.992 → 11.002.

## Ne kazandırır?

- Tek bir görselden detaylı ve dokulu 3D varlıklar oluşturur.
- Karmaşık yapıları ve açık yüzeyleri başarıyla işler.
- PBR yani fizik tabanlı görselleştirme materyalleriyle gerçekçi sonuçlar verir.

## Kurulum

**Depoyu klonlayın**

```
git clone -b main https://github.com/microsoft/TRELLIS.2.git --recursive
    cd TRELLIS.2
```

**Bağımlılıkları yükleyin**

```
. ./setup.sh --new-env --basic --flash-attn --nvdiffrast --nvdiffrec --cumesh --o-voxel --flexgemm
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Elimdeki 2D görseli 3D bir modele dönüştürmek istiyorum. TRELLIS.2 modelini kullanarak, yüksek kaliteli dokulara ve fizik tabanlı materyal özelliklerine sahip, karmaşık topolojileri koruyan bir 3D varlık oluşturmam için gerekli olan temel işlem adımlarını ve örnek Python kod yapısını açıkla.

Depo: https://github.com/microsoft/TRELLIS.2. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Yüksek çözünürlüklü ve detaylı 3D varlıklar üretmek isteyen, Linux tabanlı bir sistem ve güçlü bir NVIDIA ekran kartına sahip kullanıcılar içindir.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/microsoft/TRELLIS.2)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-08-02 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Structured Latent](https://trescout.com/dictionary/structured-latent/)
- [Generative AI](https://trescout.com/dictionary/generative-ai/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/trellis-2/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
