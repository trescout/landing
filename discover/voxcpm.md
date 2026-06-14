# Metni doğal sese çevir.

VoxCPM ; çok dilli konuşma üretimi, yaratıcı ses tasarımı ve gerçekçi ses kopyalama (voice cloning) işlemleri için geliştirilmiş, belirteçsiz (tokenizer-free) açık kaynak bir TTS modelidir.

- ★ 22.648
- Python
- Apache-2.0
- GitHub Trending · 30 May 2026

- **Kimin için:** Ses/TTS geliştiren geliştiriciler, araştırmacılar 
- **Zorluk:** İleri · ML/model bilgisi 
- **Ne sunar:** Çok dilli TTS + ses tasarımı + klonlama 
- **Ücret:** Ücretsiz · açık kaynak (Apache-2.0) 
- **Lisans:** Apache-2.0 · ayrıntı aşağıda 

## Ne sunar?
- Çok dilli ve doğal konuşma üretimi.
- Yaratıcı ve özgün ses tasarımı.
- Yüksek doğrulukta ses kopyalama (voice cloning).

## Sorumluluk notu

## Nasıl kurulur, nasıl kullanılır?
🤖 Kod bilmiyorsanız · yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
VoxCPM metinden konuşma aracını kurmak için 'pip install voxcpm' komutunu çalıştır, sonra 'voxcpm design --text "Merhaba dünya" --output out.wav' komutuyla bir ses dosyası üret; istersem referans bir ses dosyasıyla 'voxcpm clone' kullanarak o sesi klonla.

**pip ile kurulum**

```
pip install voxcpm
```

**Sesli tasarım (referans gerektirmez)**

```
voxcpm design --text "VoxCPM2 brings studio-quality multilingual speech synthesis." --output out.wav
```

**Ses klonlama (referans sesle)**

```
voxcpm clone --text "This is a voice cloning demo." --reference-audio path/to/voice.wav --output out.wav
```

Ses kopyalama (voice cloning) içerir. Bir kişinin sesini izni olmadan taklit etmek yasal ve etik sorun yaratır; sorumluluk kullanıcıya aittir. 
Lisans: Apache-2.0 · kod özgürce kullanılabilir/ticari. Model çıktısı ve ses kopyalama için yasal/etik sorumluluk size aittir. 

## Bağlantılar
- [GitHub deposu →](https://github.com/OpenBMB/VoxCPM)

## İlgili sözlük terimleri
Voice Cloning Tokenizer-free Text-to-Speech Clone Open Source Artificial Intelligence 

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Yıldız ve sayılar keşif tarihindeki değerlerdir.

---
Kaynak: TreScout Keşif · https://trescout.com/discover/voxcpm/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
