# Açık kaynaklı yerel sesli ajanlar

Hugging Face tarafından geliştirilen speech-to-speech kütüphanesi, açık kaynaklı modeller kullanarak yerel sesli ajanlar (voice agents) oluşturulmasına olanak tanıyor. Python tabanlı bu araç, geliştiricilerin cihaz üzerinde çalışan gerçek zamanlı sesli etkileşim sistemleri kurmasını sağlıyor.

- ★ 12.310
- Python
- GitHub Trending · 2026-07-29

## Güncelleme
- 12 Ağustos 2026: Yıldız 11.283 → 12.310, son sürüm v0.2.12 (5 Ağustos 2026).
- 6 Ağustos 2026: Yıldız 10.774 → 11.283, son sürüm v0.2.12 (5 Ağustos 2026).
- 4 Ağustos 2026: Yıldız 10.402 → 10.774, son sürüm v0.2.11 (3 Ağustos 2026).
- 2 Ağustos 2026: Yıldız 7.443 → 10.402, son sürüm v0.2.10 (11 Haziran 2026).

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

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-07-29 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Voice Agents Speech-to-Speech LLM Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/speech-to-speech/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
