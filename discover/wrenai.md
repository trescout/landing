# Yapay zekâ ile otomatik iş zekâsı

Canner tarafından geliştirilen WrenAI, doğal dili veritabanı sorgularına (text-to-SQL) dönüştürerek verileri otomatik olarak panellere ve grafiklere aktaran açık kaynaklı bir üretken iş zekası (generative BI) aracıdır. Platform, yirmiden fazla veri kaynağını destekleyen yönetilebilir bir bağlam katmanı üzerinden yapay zekâ ajanları için güvenilir veri analitiği süreçleri sunar.

- ★ 17.219
- Python
- GitHub Trending · 2026-07-20

## Güncelleme
- 11 Ağustos 2026: Yıldız 17.046 → 17.219, son sürüm wren-semantic-core-v0.3.1 (11 Ağustos 2026).
- 6 Ağustos 2026: Yıldız 16.780 → 17.046, son sürüm 0.29.2 (5 Ağustos 2026).
- 2 Ağustos 2026: Yıldız 16.314 → 16.780, son sürüm wren-pydantic-v0.2.1 (29 Temmuz 2026).

## Ne kazandırır?
- Doğal dilden güvenilir SQL sorguları oluşturur
- Verileri otomatik olarak panellere dönüştürür
- 22'den fazla veri kaynağını destekler

## Kurulum

**CLI kurulumu**

```
pip install wrenai # core (DuckDB included)
pip install "wrenai[postgres,memory]" # add per-datasource and memory extras as needed
```

**Yapay zekâ istemcisi için stub kurulumu**

```
npx skills add Canner/WrenAI # auto-detects Claude Code, Cursor, Cline, Codex, …
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
WrenAI kullanarak veritabanı bağlantımı yapılandır, proje iskeletini oluştur ve ilk sorgumu çalıştır. Ardından raw klasöründeki iş mantığı verilerini projeme dahil ederek bağlamı zenginleştir.

- **Kimin için:** Veri analitiği süreçlerini yapay zekâ ajanları aracılığıyla otomatize etmek ve güvenilir, paylaşılabilir paneller oluşturmak isteyen profesyoneller içindir. 

## Bağlantılar
- [GitHub deposu →](https://github.com/Canner/WrenAI)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-07-20 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
BI CLI Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/wrenai/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
