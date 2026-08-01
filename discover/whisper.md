# Sesleri yapay zekâ ile yazıya dökün

OpenAI tarafından geliştirilen Whisper, geniş ölçekli zayıf denetimli öğrenme (weak supervision) yöntemiyle eğitilmiş bir konuşma tanıma (speech recognition) modelidir. Çok dilli ses verilerini metne dönüştürme ve çeviri yapma süreçlerinde yüksek doğruluk oranları sunar.

- ★ 101.952
- Python
- GitHub Trending · 2026-06-07

## Ne kazandırır?
- Ses dosyalarını yüksek doğrulukla metne dönüştürme.
- Farklı dillerdeki konuşmaları İngilizceye çevirme.
- Sesli içeriklerde dil tanımlama ve konuşma etkinliği tespiti.

## Kurulum

**Sistem bağımlılıkları**

```
sudo apt update && sudo apt install ffmpeg
```

**Ek kurulum gereksinimi**

```
pip install setuptools-rust
```

## Çalıştırma

**Ses dosyasını metne dönüştürme**

```
whisper audio.flac audio.mp3 audio.wav --model turbo
```

**Belirli bir dilde transkripsiyon**

```
whisper japanese.wav --language Japanese
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Whisper aracını kullanarak elimdeki ses dosyasını metne dönüştürmek istiyorum. Sistemimde gerekli kurulumları yaptım. Ses dosyamın içeriğini metne çevirmek için terminale yazmam gereken temel komut yapısı nedir ve farklı dillerdeki ses dosyaları için dil belirtme parametresini nasıl kullanmalıyım?

- **Kimin için:** Ses verilerini metne dönüştürme, çeviri yapma veya dil tanımlama süreçlerini otomatize etmek isteyen geliştiriciler ve araştırmacılar içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/openai/whisper)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-07 tarihindeki hâlini anlatır: yıldız, sayılar ve metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Whisper Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/whisper/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
