# yapay zekâ ile uzun ses kayıtlarını çözümleme

Microsoft tarafından yayınlanan VibeVoice, açık kaynaklı bir sesli yapay zekâ (voice AI) çerçevesi olarak geliştirildi. Sistem, Python tabanlı yapısıyla kullanıcıların kendi ses modellerini eğitmelerine ve uygulamalarına entegre etmelerine olanak tanıyor.

- ★ 51.860
- GitHub Trending · 2026-06-07

TreScout notu: Depo yayımlandıktan sonra değişti: Sesi yazıya çeviren kısım duruyor, yazıyı sese çeviren kısım geri çekildi. Uzun kayıtları tek seferde işleyebilmesi ayırt edici yanı. Hızlı değişen bir proje, işinize katmadan önce deponun bugünkü hâline bakın.

## Güncelleme
- 2 Ağustos 2026: Yıldız 48.569 → 51.860.

## Ne kazandırır?
- Tek seferde 60 dakikaya kadar ses kaydını metne dönüştürür.
- Konuşmacı kimliği, zaman damgası ve içerik detaylarını yapılandırılmış şekilde sunar.
- Özel terimler ve isimler için kullanıcı tanımlı anahtar kelime desteği sağlar.

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
VibeVoice modelini kullanarak elimdeki 60 dakikalık ses kaydını çözümlemek istiyorum. Konuşmacıların kim olduğunu, ne zaman konuştuklarını ve söyledikleri içeriği yapılandırılmış bir metin dosyası olarak almam gerekiyor. Ayrıca modelin teknik terimleri daha doğru tanıması için özel anahtar kelimeler eklemek istiyorum, bu süreci nasıl yapılandırabilirim?

- **Kimin için:** Uzun süreli ses kayıtlarını, toplantı özetlerini veya podcast içeriklerini hızlı ve yapılandırılmış şekilde metne dönüştürmek isteyen kullanıcılar için uygundur. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/microsoft/VibeVoice)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-07 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/vibevoice/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
