# Açık kaynaklı yerel sesli ajanlar

Hugging Face tarafından geliştirilen speech-to-speech kütüphanesi, açık kaynaklı modeller kullanarak yerel sesli ajanlar (voice agents) oluşturulmasına olanak tanıyor. Python tabanlı bu araç, geliştiricilerin cihaz üzerinde çalışan gerçek zamanlı sesli etkileşim sistemleri kurmasını sağlıyor.

- ★ 7.443
- Python
- GitHub Trending · 2026-07-29

## Ne kazandırır?
- Düşük gecikmeli modüler ses hattı
- OpenAI Realtime uyumlu WebSocket desteği
- Farklı donanımlarda yerel çalışma imkânı

## Kurulum

**Temel kurulum**

```
pip install speech-to-speech
```

**Kaynak koddan kurulum**

```
git clone https://github.com/huggingface/speech-to-speech.git
cd speech-to-speech
uv sync
```

## Çalıştırma

**Sunucuyu başlatma**

```
pip install speech-to-speech
export OPENAI_API_KEY=...
speech-to-speech
```

**İstemci ile bağlanma**

```
python scripts/listen_and_play_realtime.py --host 127.0.0.1 --port 8765
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Bu aracı kullanarak kendi yerel sesli ajanımı kurmak istiyorum. VAD, STT, LLM ve TTS bileşenlerini kullanarak düşük gecikmeli bir ses hattı oluşturmak için izlemem gereken temel adımlar nelerdir? Hangi komutla sunucuyu ayağa kaldırabilirim ve OpenAI Realtime uyumlu bir istemci ile nasıl bağlantı kurabilirim?

- **Kimin için:** Kendi donanımı üzerinde yerel ve özelleştirilebilir sesli etkileşim sistemleri geliştirmek isteyen yazılımcılar içindir. 
- **Lisans:** Apache-2.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/huggingface/speech-to-speech)

## İlgili sözlük terimleri
Voice Agents Agents LLM Artificial Intelligence 

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Yıldız ve sayılar keşif tarihindeki değerlerdir.

---
Kaynak: TreScout Keşif · https://trescout.com/discover/speech-to-speech/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
