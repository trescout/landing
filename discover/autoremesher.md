# Üç boyutlu modeller için otomatik dörtgenleştirme

Autoremesher, üç boyutlu modellerdeki düzensiz yüzey yapılarını otomatik olarak dörtgen ağlara (quad remeshing) dönüştüren bir araçtır. C++ diliyle geliştirilen bu yazılım, karmaşık geometrileri animasyon ve modelleme süreçlerine uygun hale getirmek için optimize edilmiştir.

- ★ 2.123
- C++
- GitHub Trending · 2026-07-09

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
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Elimdeki 3D model dosyasını dörtgen ağ yapısına dönüştürmek istiyorum. Autoremesher aracını kullanarak giriş dosyamı belirtilen hedef dörtgen sayısı, kenar ölçeklendirme ve keskin kenar ayarlarıyla nasıl işleyebilirim? Lütfen komut satırı üzerinden kullanabileceğim örnek bir yapılandırma oluştur.

- **Kimin için:** Üç boyutlu modelleme ve animasyon süreçlerinde topoloji düzenleme ihtiyacı duyan sanatçılar ve geliştiriciler içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/huxingyi/autoremesher)

## İlgili sözlük terimleri
Artificial Intelligence 

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Yıldız ve sayılar keşif tarihindeki değerlerdir.

---
Kaynak: TreScout Keşif · https://trescout.com/discover/autoremesher/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
