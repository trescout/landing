# Gerçek zamanlı sesli yapay zekâ ajanları

LiveKit Agents, gerçek zamanlı sesli ve görüntülü yapay zekâ ajanları geliştirmek için kullanılan bir Python çerçevesidir (framework). Geliştiricilerin düşük gecikmeli sesli etkileşimler kurmasını sağlayarak, insan benzeri tepkiler veren yapay zekâ sistemlerinin oluşturulmasını kolaylaştırır.

- ★ 15.001
- Python
- GitHub Trending · 2026-08-04

## Güncelleme

- **30 Ekim 2026:** Yıldız 14.912 → 15.001, son sürüm livekit-agents@1.8.10 (29 Ekim 2026).
- **24 Ekim 2026:** Yıldız 14.749 → 14.912, son sürüm livekit-agents@1.8.9 (24 Ekim 2026).
- **15 Ekim 2026:** Yıldız 14.735 → 14.749, son sürüm livekit-agents@1.8.8 (15 Ekim 2026).
- **14 Ekim 2026:** Yıldız 14.677 → 14.735, son sürüm livekit-agents@1.8.7 (14 Ekim 2026).

## Ne kazandırır?

- İnsan benzeri tepkiler veren sesli etkileşimler kurar.
- WebRTC medya sunucusu LiveKit ile tam uyumlu çalışır.
- Telefon görüşmeleri ve çok modlu veri alışverişini destekler.

## Kurulum

**Temel kütüphaneyi yükleme**

```
pip install "livekit-agents[openai,deepgram,cartesia]"
```

**Yapay zekâ asistanı için beceri ekleme**

```
npx skills add livekit/agent-skills --skill livekit-agents
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

LiveKit Agents kullanarak gerçek zamanlı sesli etkileşim kurabilen bir yapay zekâ ajanı geliştirmek istiyorum. Ajanın kullanıcıyı dinlemesi, konuşma sonlarını anlaması ve belirlenen araçları kullanarak yanıt vermesi için gerekli olan Agent, AgentSession ve JobContext yapısını kullanarak bir başlangıç şablonu oluştur. Sesli yanıtlar için gerekli olan STT, LLM ve TTS yapılandırmalarını nasıl yapacağımı ve bu ajan üzerinde nasıl fonksiyonel araçlar tanımlayabileceğimi açıkla.

Depo: https://github.com/livekit/agents. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Gerçek zamanlı sesli ve görüntülü etkileşimli uygulamalar geliştirmek isteyen Python yazılımcıları içindir.
- **Lisans:** Apache-2.0

## Bağlantılar

- [GitHub deposu →](https://github.com/livekit/agents)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-08-04 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Framework](https://trescout.com/dictionary/framework/)
- [LLM](https://trescout.com/dictionary/llm/)
- [Agent](https://trescout.com/dictionary/agent/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/agents/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
