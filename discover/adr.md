# Kurumsal yapay zekâ ajanları için güvenlik

Uber tarafından geliştirilen ADR, kurumsal yapay zekâ ajanlarını gözlemlenebilirlik, güvenlik kıyaslaması ve tehdit algılama yöntemleriyle koruma altına alıyor. Yazılım, yapay zekâ sistemlerinin güvenliğini artırmak için geliştirilmiş bir güvenlik çerçevesi (framework) sunuyor.

- ★ 1.123
- Python
- GitHub Trending · 2026-08-05

## Güncelleme
- 6 Ağustos 2026: Yıldız 782 → 1.123, son sürüm sensor-v1.0.0 (31 Temmuz 2026).

## Ne kazandırır?
- Yapay zekâ ajanlarının gerçekleştirdiği işlemleri izleyerek ne yaptıklarını ve neden yaptıklarını anlamanızı sağlar.
- 17 farklı saldırı tekniğine karşı 300'den fazla görevle ajan güvenliğini test eder.
- Şüpheli oturumları tespit etmek için iki aşamalı bir mimari kullanır.

## Kurulum

**Tespit sistemini hazırlama**

```
git clone https://github.com/uber/ADR
cd ADR/Detection
uv sync
export ANTHROPIC_API_KEY="..." OPENAI_API_KEY="..."
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Kurumsal yapay zekâ ajanlarımı güvenlik açıklarına karşı nasıl koruyabilirim? ADR sistemini kullanarak ajan faaliyetlerini nasıl izleyebilir, tehditleri nasıl tespit edebilir ve güvenlik kıyaslaması yaparak sistemimin savunma gücünü nasıl değerlendirebilirim? Lütfen bu süreçte izlemem gereken adımları ve ADR'nin sunduğu gözlemlenebilirlik özelliklerini nasıl yapılandıracağımı açıkla.

- **Kimin için:** Kurumsal düzeyde yapay zekâ ajanları çalıştıran ve bu sistemlerin güvenliğini sağlamak isteyen güvenlik uzmanları ile yazılım geliştiriciler için uygundur. 
- **Lisans:** Apache-2.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/uber/ADR)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-05 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Framework Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/adr/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
