# Yapay zekâ için hızlı matris hesaplama

DeepSeek tarafından geliştirilen DeepGEMM, grafik işlem birimleri (GPU) üzerinde matris çarpımı işlemlerini hızlandıran açık kaynaklı bir temel doğrusal cebir alt programları (BLAS) kütüphanesidir. Yazılım, yüksek performanslı hesaplama gerektiren yapay zekâ modelleri için optimize edilmiş çekirdekler (kernels) sunar.

- ★ 8.528
- Cuda
- GitHub Trending · 2026-10-06

## Güncelleme
- 6 Ekim 2026: Yıldız 8.522 → 8.528, son sürüm v2.1.1.post3 (15 Ekim 2025).

## Ne kazandırır?
- Matris çarpımlarını hızlandırarak büyük dil modellerinin çalışma sürelerini kısaltır.
- Kurulum anında CUDA derlemesi beklemeden çekirdekleri çalışma anında otomatik derler.
- Farklı uzman modellerini tek işlemde birleştirerek grafik kartı iletişim kayıplarını azaltır.

## Kurulum

**Depoyu klonlama ve geliştirme ortamını h**

```
# Submodule must be cloned
git clone --recursive git@github.com:deepseek-ai/DeepGEMM.git
cd DeepGEMM

# Link some essential includes and build the C++ extension
cat develop.sh
./develop.sh
```

**Kütüphaneyi kurma**

```
cat install.sh
./install.sh
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
NVIDIA SM90 veya SM100 mimarili donanımımda DeepGEMM kütüphanesini kurmak istiyorum. İlk olarak depoyu alt modülleriyle klonlayıp geliştirme ortamını hazırlamak için '# Submodule must be cloned\ngit clone --recursive git@github.com:deepseek-ai/DeepGEMM.git\ncd DeepGEMM\n\n# Link some essential includes and build the C++ extension\ncat develop.sh\n./develop.sh' komutlarını çalıştırın. Ardından kurulumu tamamlamak için 'cat install.sh\n./install.sh' komutunu uygulayın ve Python ortamında 'import deep_gemm' komutuyla kütüphaneyi kullanıma hazır hâle getirin.

- **Kimin için:** Büyük yapay zekâ modellerini modern NVIDIA grafik işlem birimlerinde en yüksek performansla çalıştırmak isteyen geliştiriciler ve araştırmacılar içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/deepseek-ai/DeepGEMM)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-10-06 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
BLAS Kernels Clone GPU Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/deepgemm/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
