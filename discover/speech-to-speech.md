# Açık kaynaklı yerel sesli ajanlar

Hugging Face tarafından geliştirilen speech-to-speech kütüphanesi, açık kaynaklı modeller kullanarak yerel sesli ajanlar (voice agents) oluşturulmasına olanak tanıyor. Python tabanlı bu araç, geliştiricilerin cihaz üzerinde çalışan gerçek zamanlı sesli etkileşim sistemleri kurmasını sağlıyor.

- ★ 13.072
- Python
- GitHub Trending · 2026-07-29

## Güncelleme

- **7 Eylül 2026:** Yıldız 12.310 → 13.072, son sürüm v1.0.0 (6 Eylül 2026).
- **12 Ağustos 2026:** Yıldız 11.283 → 12.310, son sürüm v0.2.12 (5 Ağustos 2026).
- **6 Ağustos 2026:** Yıldız 10.774 → 11.283, son sürüm v0.2.12 (5 Ağustos 2026).
- **4 Ağustos 2026:** Yıldız 10.402 → 10.774, son sürüm v0.2.11 (3 Ağustos 2026).

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

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Bu aracı kullanarak kendi yerel sesli ajanımı kurmak istiyorum. VAD, STT, LLM ve TTS bileşenlerini kullanarak düşük gecikmeli bir ses hattı oluşturmak için izlemem gereken temel adımlar nelerdir? Hangi komutla sunucuyu ayağa kaldırabilirim ve OpenAI Realtime uyumlu bir istemci ile nasıl bağlantı kurabilirim?

Depo: https://github.com/huggingface/speech-to-speech. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Kendi donanımı üzerinde yerel ve özelleştirilebilir sesli etkileşim sistemleri geliştirmek isteyen yazılımcılar içindir.
- **Lisans:** Apache-2.0

## Bağlantılar

- [GitHub deposu →](https://github.com/huggingface/speech-to-speech)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-07-29 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Voice Agents](https://trescout.com/dictionary/voice-agents/)
- [Speech-to-Speech](https://trescout.com/dictionary/speech-to-speech/)
- [LLM](https://trescout.com/dictionary/llm/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/speech-to-speech/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
