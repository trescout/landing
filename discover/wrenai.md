# Yapay zekâ ile otomatik iş zekâsı

Canner tarafından geliştirilen WrenAI, doğal dili veritabanı sorgularına (text-to-SQL) dönüştürerek verileri otomatik olarak panellere ve grafiklere aktaran açık kaynaklı bir üretken iş zekası (generative BI) aracıdır. Platform, yirmiden fazla veri kaynağını destekleyen yönetilebilir bir bağlam katmanı üzerinden yapay zekâ ajanları için güvenilir veri analitiği süreçleri sunar.

- ★ 17.901
- Python
- GitHub Trending · 2026-07-20

## Güncelleme

- **19 Ekim 2026:** Yıldız 17.879 → 17.901, son sürüm wren-langchain-v0.2.3 (19 Ekim 2026).
- **16 Ekim 2026:** Yıldız 17.874 → 17.879, son sürüm wren-v0.16.0 (16 Ekim 2026).
- **15 Ekim 2026:** Yıldız 17.871 → 17.874, son sürüm wren-core-wasm-v0.5.0 (15 Ekim 2026).
- **14 Ekim 2026:** Yıldız 17.870 → 17.871, son sürüm wren-core-py-v0.8.1 (14 Ekim 2026).

## Ne kazandırır?

- Doğal dilden güvenilir SQL sorguları oluşturur
- Verileri otomatik olarak panellere dönüştürür
- 22'den fazla veri kaynağını destekler

## Kurulum

**CLI kurulumu**

```
pip install wrenai                      # core (DuckDB included)
pip install "wrenai[postgres,memory]"   # add per-datasource and memory extras as needed
```

**Yapay zekâ istemcisi için stub kurulumu**

```
npx skills add Canner/WrenAI            # auto-detects Claude Code, Cursor, Cline, Codex, …
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

WrenAI kullanarak veritabanı bağlantımı yapılandır, proje iskeletini oluştur ve ilk sorgumu çalıştır. Ardından raw klasöründeki iş mantığı verilerini projeme dahil ederek bağlamı zenginleştir.

Depo: https://github.com/Canner/WrenAI. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Veri analitiği süreçlerini yapay zekâ ajanları aracılığıyla otomatize etmek ve güvenilir, paylaşılabilir paneller oluşturmak isteyen profesyoneller içindir.

## Bağlantılar

- [GitHub deposu →](https://github.com/Canner/WrenAI)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-07-20 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [BI](https://trescout.com/dictionary/bi/)
- [CLI](https://trescout.com/dictionary/cli/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/wrenai/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
