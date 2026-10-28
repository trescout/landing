# Yapay zekâ destekli kişiselleştirilmiş eğitim

DeepTutor, öğrenci verilerini kullanarak kişiselleştirilmiş eğitim süreçleri sunan yaşam boyu öğrenme (lifelong learning) tabanlı bir özel ders sistemidir. Proje, yapay zekâ destekli bireyselleştirilmiş öğretim (personalized tutoring) yöntemleriyle öğrenme deneyimini optimize etmeyi amaçlamaktadır.

- ★ 46.783
- Python
- GitHub Trending · 2026-07-16

## Güncelleme

- **28 Ekim 2026:** Yıldız 44.479 → 46.783, son sürüm v1.6.15 (18 Ekim 2026).
- **27 Ekim 2026:** Yıldız 41.717 → 44.479, son sürüm v1.6.15 (18 Ekim 2026).
- **19 Ekim 2026:** Yıldız 40.928 → 41.717, son sürüm v1.6.15 (18 Ekim 2026).
- **8 Ekim 2026:** Yıldız 40.808 → 40.928, son sürüm v1.6.14 (8 Ekim 2026).

## Ne kazandırır?

- Yaşam boyu öğrenme odaklı özel ders sistemi
- Kişiselleştirilmiş yapay zekâ ajanları ile etkileşim
- Gelişmiş bilgi tabanı ve RAG desteği

## Kurulum

**Hızlı kurulum**

```
mkdir -p my-deeptutor && cd my-deeptutor
pip install -U deeptutor
deeptutor init     # prompts for ports + LLM provider + optional embedding
deeptutor start    # starts backend + frontend; keep the terminal open
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
deeptutor start    # starts backend + frontend; keep the terminal open
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

DeepTutor sistemini kullanarak öğrenme sürecimi nasıl kişiselleştirebilirim? Kendi yapay zekâ partnerlerimi oluşturmak ve özel eğitim materyallerimi bu sisteme entegre ederek yaşam boyu öğrenme deneyimimi optimize etmek için izlemem gereken temel adımları açıkla.

Depo: https://github.com/HKUDS/DeepTutor. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Kendi özel eğitim asistanını oluşturmak ve kişiselleştirilmiş bir öğrenme ortamı kurmak isteyen öğrenciler ve eğitmenler için uygundur.
- **Lisans:** Apache-2.0

## Bağlantılar

- [GitHub deposu →](https://github.com/HKUDS/DeepTutor)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-07-16 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Lifelong Learning](https://trescout.com/dictionary/lifelong-learning/)
- [Personalized Tutoring](https://trescout.com/dictionary/personalized-tutoring/)
- [Tutoring](https://trescout.com/dictionary/tutoring/)
- [RAG](https://trescout.com/dictionary/rag/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/deeptutor/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
