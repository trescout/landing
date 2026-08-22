# Otonom yapay zekâ ile derinlemesine araştırma

LangChain tarafından geliştirilen open-deep-research, karmaşık soruları yanıtlamak için internet üzerinde çok adımlı araştırmalar yapan otonom bir sistemdir. Araştırma sürecini planlama, veri toplama ve sentezleme aşamalarıyla otomatize ederek derinlemesine analiz (deep research) süreçlerini kolaylaştırır.

- ★ 12.655
- Python
- GitHub Trending · 2026-07-22

## Güncelleme
- 22 Ağustos 2026: Yıldız 12.307 → 12.655, depo arşivlendi, geliştirme durdu.

## Ne kazandırır?
- Karmaşık sorular için çok adımlı otonom araştırma
- Farklı model sağlayıcıları ve arama araçlarıyla uyumluluk
- LangGraph üzerinden görselleştirilmiş araştırma süreçleri

## Kurulum

**Depoyu klonlama ve ortam hazırlığı**

```
git clone https://github.com/langchain-ai/open_deep_research.git
cd open_deep_research
uv venv
source .venv/bin/activate # On Windows: .venv\Scripts\activate
```

**Bağımlılıkları yükleme**

```
uv sync
# or
uv pip install -r pyproject.toml
```

## Çalıştırma

**Sunucuyu başlatma**

```
# Install dependencies and start the LangGraph server
uvx --refresh --from "langgraph-cli[inmem]" --with-editable . --python 3.11 langgraph dev --allow-blocking
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Open Deep Research aracını kullanarak [ARAŞTIRMA KONUNUZU BURAYA YAZIN] hakkında derinlemesine bir analiz yap. Araştırma sürecini planla, internet üzerinden verileri topla ve bulgularını sentezleyerek kapsamlı bir rapor oluştur.

- **Kimin için:** Karmaşık konularda otonom araştırma süreçlerini otomatize etmek isteyen geliştiriciler ve araştırmacılar içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/langchain-ai/open_deep_research)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-07-22 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/open-deep-research/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
