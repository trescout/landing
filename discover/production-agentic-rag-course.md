# Production Agentic RAG Course

Production-agentic-rag-course, karmaşık veri kaynaklarından bilgi getirme süreçlerini otomatize eden ajan tabanlı getirme destekli üretim (agentic RAG) sistemlerinin geliştirilmesine yönelik uygulamalı bir eğitim sunuyor. Python dilini temel alan bu kaynak, ölçeklenebilir ve üretim seviyesinde yapay zekâ uygulamaları oluşturmak için gerekli teknik mimariyi öğretiyor.

- ★ 6.536
- GitHub Trending · 2026-06-03

## Ne kazandırır?
- Üretim seviyesinde RAG sistemleri için gerekli altyapıyı kurma.
- Hibrit arama ve akıllı veri işleme yöntemlerini uygulama.
- LangGraph ile ajan tabanlı karar mekanizmaları geliştirme.

## Kurulum

**Depoyu klonlama ve kurulum**

```
git clone 
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
git clone --branch https://github.com/jamwithai/arxiv-paper-curator
cd arxiv-paper-curator
uv sync
docker compose down -v
docker compose up --build -d

# Replace with: week1.0, week2.0, etc.
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Production-agentic-rag-course projesini kullanarak bir akademik araştırma asistanı geliştirmek istiyorum. Projenin temel kurulumu için git clone komutu ile depoyu indirdikten sonra .env dosyasını yapılandırıp uv sync ile bağımlılıkları yüklemem gerekiyor. Ardından docker compose up --build -d komutu ile tüm servisleri başlatarak http://localhost:8000/api/v1/health adresi üzerinden sistemin çalıştığını doğrulamak istiyorum. Bu süreçte dikkat etmem gereken API anahtarları ve servis yapılandırmaları hakkında bana rehberlik eder misin?

- **Kimin için:** Üretim seviyesinde, ölçeklenebilir ve ajan tabanlı RAG sistemleri geliştirmek isteyen yapay zekâ mühendisleri ve geliştiriciler içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/jamwithai/production-agentic-rag-course)

## İlgili sözlük terimleri
API RAG Artificial Intelligence 

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Yıldız ve sayılar keşif tarihindeki değerlerdir.

---
Kaynak: TreScout Keşif · https://trescout.com/discover/production-agentic-rag-course/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
