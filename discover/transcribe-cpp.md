# Yerel sistemlerde hızlı konuşma dönüştürme

Transcribe.cpp, 16'dan fazla model ailesini destekleyen ve C++ diliyle geliştirilen bir konuşmayı metne dönüştürme (speech-to-text) çıkarım (inference) kütüphanesidir. Ggml altyapısını kullanan bu araç, farklı ses işleme modellerinin yerel sistemlerde verimli bir şekilde çalıştırılmasını sağlar.

- ★ 1.865
- C++
- GitHub Trending · 2026-07-21

## Güncelleme
- 31 Ağustos 2026: Yıldız 1.825 → 1.865, son sürüm v0.2.3 (30 Ağustos 2026).
- 24 Ağustos 2026: Yıldız 1.816 → 1.825, son sürüm v0.2.2 (24 Ağustos 2026).
- 20 Ağustos 2026: Yıldız 1.802 → 1.816, son sürüm v0.2.1 (20 Ağustos 2026).
- 18 Ağustos 2026: Yıldız 1.673 → 1.802, son sürüm v0.2.0 (17 Ağustos 2026).

## Ne kazandırır?
- 16 farklı model ailesi desteği
- GPU ve CPU üzerinde yüksek performans
- GGUF formatı ile verimli çıkarım

## Kurulum

**Vulkan destekli Linux kurulumu**

```
# Ubuntu/Debian
sudo apt install build-essential cmake libvulkan-dev glslc libopenblas-dev

cmake -B build -DTRANSCRIBE_VULKAN=ON
cmake --build build
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Transcribe.cpp aracını kullanarak yerel bir ses dosyasını metne dönüştürmek istiyorum. Sistemimde derlenmiş olan transcribe-cli aracını ve indirdiğim GGUF formatındaki model dosyasını kullanarak, 16 kHz mono WAV formatındaki ses dosyamı nasıl işleyebilirim? Lütfen bu işlem için gerekli olan komut yapısını ve dikkat etmem gereken dosya yollarını açıkla.

- **Kimin için:** Kendi donanımı üzerinde gizlilik odaklı ve hızlı konuşma tanıma sistemleri çalıştırmak isteyen geliştiriciler içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/handy-computer/transcribe.cpp)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-07-21 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Speech-to-Text GGUF STT CPU Inference GPU

---
Kaynak: TreScout Keşif · https://trescout.com/discover/transcribe-cpp/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
