# yapay zekâ ile uzun ses kayıtlarını çözümleyin

Microsoft tarafından yayınlanan VibeVoice, açık kaynaklı bir sesli yapay zekâ (voice AI) çerçevesi olarak geliştirildi. Sistem, Python tabanlı yapısıyla kullanıcıların kendi ses modellerini eğitmelerine ve uygulamalarına entegre etmelerine olanak tanıyor.

- ★ 48.569
- GitHub Trending · 2026-06-07

TreScout notu: Depo yayımlandıktan sonra değişti: metinden konuşma tarafı geri çekildi, bugün kurulabilir olan konuşmadan metne modeli. Uzun kayıtları tek parça işleyebilmesi ayırt edici yanı. Hızlı değişen bir proje, üretim işine koymadan önce deponun güncel durumuna bakın.

## Ne kazandırır?
- 60 dakikaya kadar kesintisiz ses kaydı işleme
- Konuşmacı, zaman damgası ve içerik ayrımı
- Özel terimler ile doğruluk oranını artırma

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

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
VibeVoice-ASR modelini kullanarak elimdeki 60 dakikalık uzun ses kaydını analiz etmeni istiyorum. Ses kaydındaki konuşmacıları, her birinin ne zaman konuştuğunu ve konuşma içeriklerini yapılandırılmış bir metin olarak hazırla. Analiz sırasında teknik terimlerin doğru anlaşılması için verdiğim özel kelime listesini (hotwords) dikkate al.

- **Kimin için:** Uzun süreli ses kayıtlarını, toplantı dökümlerini veya podcast içeriklerini hızlı ve yapılandırılmış şekilde metne dönüştürmek isteyen kullanıcılar içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/microsoft/VibeVoice)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-07 tarihindeki hâlini anlatır: yıldız, sayılar ve metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Text-to-Speech Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/vibevoice/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
