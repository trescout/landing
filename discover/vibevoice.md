# Uzun ses kayıtları için yapay zekâ

Microsoft tarafından yayınlanan VibeVoice, açık kaynaklı bir sesli yapay zekâ (voice AI) çerçevesi olarak geliştirildi. Sistem, Python tabanlı yapısıyla kullanıcıların kendi ses modellerini eğitmelerine ve uygulamalarına entegre etmelerine olanak tanıyor.

- ★ 48.569
- GitHub Trending · 2026-06-07

## Ne kazandırır?
- 60 dakikaya kadar kesintisiz ses dökümü
- Konuşmacı, zaman damgası ve içerik takibi
- Özel terimler ile yüksek doğrulukta tanıma

## Kurulum

**GitHub'dan kur**

```
git clone https://github.com/microsoft/VibeVoice.git
cd VibeVoice
pip install -e .
```

## Çalıştırma

**Gradio demo**

```
python demo/vibevoice_asr_gradio_demo.py --model_path microsoft/VibeVoice-ASR --share
```

**Dosyadan transkripsiyon**

```
python demo/vibevoice_asr_inference_from_file.py --model_path microsoft/VibeVoice-ASR --audio_files [ses-dosyasi]
```

Kaynak: Resmî depo · docs/vibevoice-asr.md (microsoft/VibeVoice). Kurulabilir model VibeVoice-ASR; TTS kodu depodan çıkarıldı.

- **Kimin için:** Uzun süreli ses kayıtlarını, podcastleri veya çok konuşmacılı toplantıları metne dökmek isteyen araştırmacılar ve geliştiriciler içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/microsoft/VibeVoice)

## İlgili sözlük terimleri
Artificial Intelligence 

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Yıldız ve sayılar keşif tarihindeki değerlerdir.

---
Kaynak: TreScout Keşif · https://trescout.com/discover/vibevoice/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
