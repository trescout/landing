# Yapay zekâ ile otomatik iş zekâsı

Canner tarafından geliştirilen WrenAI, doğal dili veritabanı sorgularına (text-to-SQL) dönüştürerek verileri otomatik olarak panellere ve grafiklere aktaran açık kaynaklı bir üretken iş zekası (generative BI) aracıdır. Platform, yirmiden fazla veri kaynağını destekleyen yönetilebilir bir bağlam katmanı üzerinden yapay zekâ ajanları için güvenilir veri analitiği süreçleri sunar.

- ★ 17.431
- Python
- GitHub Trending · 2026-07-20

## Güncelleme
- 31 Ağustos 2026: Yıldız 17.302 → 17.431, son sürüm wren-core-py-v0.7.6 (31 Ağustos 2026).
- 18 Ağustos 2026: Yıldız 17.239 → 17.302, son sürüm wren-v0.13.3 (18 Ağustos 2026).
- 12 Ağustos 2026: Yıldız 17.219 → 17.239, son sürüm wren-core-py-v0.7.4 (12 Ağustos 2026).
- 11 Ağustos 2026: Yıldız 17.046 → 17.219, son sürüm wren-semantic-core-v0.3.1 (11 Ağustos 2026).

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
