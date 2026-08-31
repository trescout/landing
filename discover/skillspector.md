# Yapay zekâ yeteneklerini güvenli kılın

NVIDIA tarafından geliştirilen SkillSpector, yapay zekâ ajanlarına ait yetenek paketlerindeki (skills) güvenlik açıklarını ve kötü niyetli kalıpları tespit eden bir tarama aracıdır. Python tabanlı bu yazılım, ajan tabanlı sistemlerin geliştirilme sürecinde karşılaşılan güvenlik risklerini analiz etmeyi hedefler.

- ★ 15.415
- Python
- GitHub Trending · 2026-06-12

## Güncelleme
- 31 Ağustos 2026: Yıldız 15.024 → 15.415, son sürüm v2.11.0 (28 Ağustos 2026).
- 27 Ağustos 2026: Yıldız 14.760 → 15.024, son sürüm v2.10.0 (26 Ağustos 2026).
- 19 Ağustos 2026: Yıldız 14.655 → 14.760, son sürüm v2.9.6 (18 Ağustos 2026).
- 15 Ağustos 2026: Yıldız 14.527 → 14.655, son sürüm v2.9.5 (15 Ağustos 2026).

## Ne kazandırır?
- Yapay zekâ ajan yeteneklerindeki güvenlik açıklarını ve kötü niyetli kalıpları tespit eder.
- Statik analiz ve isteğe bağlı yapay zekâ değerlendirmesi ile iki aşamalı güvenlik taraması sunar.
- Risk puanlaması ve detaylı raporlama ile ajanların güvenliğini doğrulamayı sağlar.

## Kurulum

**Depoyu klonlama ve sanal ortam oluşturma**

```
# Clone the repository
git clone https://github.com/NVIDIA/skillspector.git
cd skillspector

# Create and activate virtual environment
uv venv .venv && source .venv/bin/activate
# or: python3 -m venv .venv && source .venv/bin/activate
```

**Kurulumu tamamlama**

```
# Install for production use
make install

# Or install with development dependencies
make install-dev
```

## Çalıştırma

**Yerel dizini tarama**

```
skillspector scan ./my-skill/
```

**Git deposunu tarama**

```
skillspector scan https://github.com/user/my-skill
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
SkillSpector aracını kullanarak bir yapay zekâ ajanı yeteneğini güvenlik taramasından geçirmek istiyorum. Yerel bir dizindeki yeteneği taramak için 'skillspector scan ./my-skill/' komutunu nasıl kullanırım ve tarama sonuçlarını JSON formatında 'report.json' dosyasına kaydetmek için komuta hangi parametreleri eklemeliyim?

- **Kimin için:** Yapay zekâ ajanları geliştiren ve kullandıkları yetenek paketlerinin güvenlik risklerini analiz etmek isteyen yazılım geliştiriciler içindir. 
- **Lisans:** Apache-2.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/NVIDIA/SkillSpector)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-12 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
AI Skills Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/skillspector/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
