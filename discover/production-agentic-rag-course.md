# Yapay zekâ ile akıllı veri getirme

Production-agentic-rag-course, karmaşık veri kaynaklarından bilgi getirme süreçlerini otomatize eden ajan tabanlı getirme destekli üretim (agentic RAG) sistemlerinin geliştirilmesine yönelik uygulamalı bir eğitim sunuyor. Python dilini temel alan bu kaynak, ölçeklenebilir ve üretim seviyesinde yapay zekâ uygulamaları oluşturmak için gerekli teknik mimariyi öğretiyor.

- ★ 9.265
- GitHub Trending · 2026-06-03

## Güncelleme

- **3 Ekim 2026:** Yıldız 8.216 → 9.265, son sürüm week7.0 (26 Kasım 2025).
- **2 Ağustos 2026:** Yıldız 6.536 → 8.216, son sürüm week7.0 (26 Kasım 2025).

## Ne kazandırır?

- Üretim seviyesinde RAG sistemleri için gerekli altyapıyı kurma.
- Hibrit arama ve akıllı veri işleme yöntemlerini uygulama.
- LangGraph ile ajan tabanlı karar mekanizmaları geliştirme.

## Kurulum

**Depoyu klonlama ve kurulum**

```
git clone <repository-url>
cd arxiv-paper-curator

# 2. Configure environment (IMPORTANT!)
cp .env.example .env
# The .env file contains all necessary configuration for OpenSearch, 
# arXiv API, and service connections. Defaults work out of the box.
# You need to add Jina embeddings free api key and langfuse keys (check the blogs)

# 3. Install dependencies
uv sync

# 4. Start all services
docker compose up --build -d

# 5. Verify everything works
curl http://localhost:8000/api/v1/health
```

## Çalıştırma

**Belirli bir haftanın içeriğini çalıştırm**

```
git clone --branch <WEEK_TAG> https://github.com/jamwithai/arxiv-paper-curator
cd arxiv-paper-curator
uv sync
docker compose down -v
docker compose up --build -d

# Replace <WEEK_TAG> with: week1.0, week2.0, etc.
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Production-agentic-rag-course projesini kullanarak bir akademik araştırma asistanı geliştirmek istiyorum. Projenin temel kurulumu için git clone komutu ile depoyu indirdikten sonra .env dosyasını yapılandırıp uv sync ile bağımlılıkları yüklemem gerekiyor. Ardından docker compose up --build -d komutu ile tüm servisleri başlatarak http://localhost:8000/api/v1/health adresi üzerinden sistemin çalıştığını doğrulamak istiyorum. Bu süreçte dikkat etmem gereken API anahtarları ve servis yapılandırmaları hakkında bana rehberlik eder misin?

Depo: https://github.com/jamwithai/production-agentic-rag-course. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Bir API anahtarı gerekirse onu sohbete yazmamı isteme. .env dosyasına nasıl ekleyeceğimi göster ve bu dosyanın Git'e gönderilmediğinden emin ol.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Üretim seviyesinde, ölçeklenebilir ve ajan tabanlı RAG sistemleri geliştirmek isteyen yapay zekâ mühendisleri ve geliştiriciler içindir.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/jamwithai/production-agentic-rag-course)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-06-03 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Agentic](https://trescout.com/dictionary/agentic/)
- [Localhost](https://trescout.com/dictionary/localhost/)
- [Clone](https://trescout.com/dictionary/clone/)
- [RAG](https://trescout.com/dictionary/rag/)
- [API](https://trescout.com/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/production-agentic-rag-course/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
