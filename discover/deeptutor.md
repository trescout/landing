# Yapay zekâ destekli kişiselleştirilmiş eğitim

DeepTutor, öğrenci verilerini kullanarak kişiselleştirilmiş eğitim süreçleri sunan yaşam boyu öğrenme (lifelong learning) tabanlı bir özel ders sistemidir. Proje, yapay zekâ destekli bireyselleştirilmiş öğretim (personalized tutoring) yöntemleriyle öğrenme deneyimini optimize etmeyi amaçlamaktadır.

- ★ 35.981
- Python
- GitHub Trending · 2026-07-16

## Güncelleme
- 17 Ağustos 2026: Yıldız 35.776 → 35.981, son sürüm v1.5.13 (17 Ağustos 2026).
- 15 Ağustos 2026: Yıldız 33.415 → 35.776, son sürüm v1.5.12 (13 Ağustos 2026).
- 10 Ağustos 2026: Yıldız 32.944 → 33.415, son sürüm v1.5.11 (9 Ağustos 2026).
- 7 Ağustos 2026: Yıldız 32.640 → 32.944, son sürüm v1.5.10 (7 Ağustos 2026).

## Ne kazandırır?
- Yaşam boyu öğrenme odaklı özel ders sistemi
- Kişiselleştirilmiş yapay zekâ ajanları ile etkileşim
- Gelişmiş bilgi tabanı ve RAG desteği

## Kurulum

**Hızlı kurulum**

```
mkdir -p my-deeptutor && cd my-deeptutor
pip install -U deeptutor
deeptutor init # prompts for ports + LLM provider + optional embedding
deeptutor start # starts backend + frontend; keep the terminal open
```

**Docker ile çalıştırma**

```
docker run --rm --name deeptutor \
-p 127.0.0.1:3782:3782 \
-v deeptutor-data:/app/data \
ghcr.io/hkuds/deeptutor:latest
```

## Çalıştırma

**Sistemi başlatma**

```
deeptutor start # starts backend + frontend; keep the terminal open
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
DeepTutor sistemini kullanarak öğrenme sürecimi nasıl kişiselleştirebilirim? Kendi yapay zekâ partnerlerimi oluşturmak ve özel eğitim materyallerimi bu sisteme entegre ederek yaşam boyu öğrenme deneyimimi optimize etmek için izlemem gereken temel adımları açıkla.

- **Kimin için:** Kendi özel eğitim asistanını oluşturmak ve kişiselleştirilmiş bir öğrenme ortamı kurmak isteyen öğrenciler ve eğitmenler için uygundur. 
- **Lisans:** Apache-2.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/HKUDS/DeepTutor)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-07-16 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Lifelong Learning Personalized Tutoring Tutoring RAG Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/deeptutor/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
