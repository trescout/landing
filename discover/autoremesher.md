# Üç boyutlu modeller için otomatik dörtgenleştirme

Autoremesher, üç boyutlu modellerdeki düzensiz yüzey yapılarını otomatik olarak dörtgen ağlara (quad remeshing) dönüştüren bir araçtır. C++ diliyle geliştirilen bu yazılım, karmaşık geometrileri animasyon ve modelleme süreçlerine uygun hale getirmek için optimize edilmiştir.

- ★ 3.322
- C++
- GitHub Trending · 2026-07-09

## Güncelleme

- **24 Ağustos 2026:** Yıldız 3.225 → 3.322, son sürüm 1.2.0 (23 Ağustos 2026).
- **17 Ağustos 2026:** Yıldız 3.087 → 3.225, son sürüm 1.1.0 (16 Ağustos 2026).
- **2 Ağustos 2026:** Yıldız 2.123 → 3.087, son sürüm 1.0.0 (6 Temmuz 2026).

## Ne kazandırır?

- Karmaşık modelleri temiz dörtgen ağlara dönüştürür
- Animasyon süreçleri için optimize edilmiş topoloji sağlar
- Komut satırı üzerinden toplu işlem desteği sunar

## Kurulum

**Linux üzerinde derleme**

```
# Install Qt and build tools
sudo apt install build-essential qt5-qmake qtbase5-dev qttools5-dev-tools libqt5svg5-dev libqt5multimedia5-dev

# Install TBB and OpenGL
sudo apt install libtbb-dev libgl1-mesa-dev

# Clone and build
git clone https://github.com/huxingyi/autoremesher.git
cd autoremesher
qmake
make -j$(nproc)
```

**macOS üzerinde derleme**

```
# Install Xcode Command Line Tools
xcode-select --install

# Install dependencies via Homebrew
brew install qt@5 tbb cmake

# Build
export PATH="/usr/local/opt/qt@5/bin:$PATH"
git clone https://github.com/huxingyi/autoremesher.git
cd autoremesher
qmake CONFIG+=sdk_no_version_check
make -j$(sysctl -n hw.logicalcpu)
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Elimdeki 3D model dosyasını dörtgen ağ yapısına dönüştürmek istiyorum. Autoremesher aracını kullanarak giriş dosyamı belirtilen hedef dörtgen sayısı, kenar ölçeklendirme ve keskin kenar ayarlarıyla nasıl işleyebilirim? Lütfen komut satırı üzerinden kullanabileceğim örnek bir yapılandırma oluştur.

Depo: https://github.com/huxingyi/autoremesher. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Üç boyutlu modelleme ve animasyon süreçlerinde topoloji düzenleme ihtiyacı duyan sanatçılar ve geliştiriciler içindir.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/huxingyi/autoremesher)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-07-09 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Quad Remeshing](https://trescout.com/dictionary/quad-remeshing/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/autoremesher/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
