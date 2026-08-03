# yapay zekâ ile kişisel alım satım

Vibe-Trading, finansal piyasalarda işlem yapmak amacıyla geliştirilmiş kişisel bir alım satım ajanı (trading agent) sunuyor. Proje, Python tabanlı yapısıyla kullanıcıların otomatik ticaret stratejilerini yönetmelerine olanak tanıyor.

- ★ 29.309
- Python
- GitHub Trending · 2026-06-04

## Güncelleme
- 2 Ağustos 2026: Yıldız 10.343 → 29.309, son sürüm v0.1.12 (22 Temmuz 2026).

## Ne kazandırır?
- Kişisel alım satım ajanı ile otomatik strateji yönetimi.
- Çoklu aracı kurum desteği ile piyasa verilerine erişim.
- Güvenlik odaklı işlem yetkisi ve denetim defteri.

## Kurulum

**Doğrudan Kurulum**

```
pip install vibe-trading-ai
```

**Geliştirici Ortamı Kurulumu**

```
git clone https://github.com/HKUDS/Vibe-Trading.git
cd Vibe-Trading
python -m venv .venv

# Activate
source .venv/bin/activate # Linux / macOS
# .venv\Scripts\Activate.ps1 # Windows PowerShell

pip install -e .
cp agent/.env.example agent/.env # Edit — set your LLM provider API key
vibe-trading # Launch interactive TUI
```

## Çalıştırma

**Doğal Dil ile Araştırma**

```
vibe-trading run -p "Backtest a BTC-USDT 20/50 moving-average strategy for 2024, summarize return and drawdown, then export the report"
```

**Strateji Testi**

```
vibe-trading alpha bench --zoo gtja191 --universe csi300 --period 2018-2025 --top 20
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Vibe-Trading ajanı ile finansal piyasalarda işlem yapmak istiyorum. Lütfen bana güncel piyasa verilerini analiz etmemde, belirlediğim stratejileri geriye dönük test etmemde ve aracı kurum bağlantılarımı güvenli bir şekilde yönetmemde yardımcı ol. Özellikle işlem mandalarımı ve risk limitlerimi belirleyerek otomatik alım satım süreçlerini nasıl yapılandırabileceğimi adım adım açıkla.

- **Kimin için:** Finansal piyasalarda otomatik ticaret stratejileri geliştirmek ve yönetmek isteyen kullanıcılar için tasarlanmıştır. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/HKUDS/Vibe-Trading)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-04 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Trading Agent Agent Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/vibe-trading/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
