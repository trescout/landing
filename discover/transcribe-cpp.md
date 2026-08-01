# yerel sistemlerde hızlı konuşma dönüştürme

Transcribe.cpp, 16'dan fazla model ailesini destekleyen ve C++ diliyle geliştirilen bir konuşmayı metne dönüştürme (speech-to-text) çıkarım (inference) kütüphanesidir. Ggml altyapısını kullanan bu araç, farklı ses işleme modellerinin yerel sistemlerde verimli bir şekilde çalıştırılmasını sağlar.

- ★ 1.357
- C++
- GitHub Trending · 2026-07-21

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
Speech-to-Text Inference CPU GPU Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/transcribe-cpp/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
