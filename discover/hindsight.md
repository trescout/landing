# Yapay zekâ ajanları için akıllı bellek katmanı

Hindsight, yapay zekâ ajanları için öğrenen bir bellek katmanı (memory layer) sunuyor. Geçmiş etkileşimlerden çıkarım yaparak ajanların karar alma süreçlerini iyileştiren bu açık kaynaklı kütüphane, sistemlerin zamanla daha tutarlı sonuçlar üretmesini sağlıyor.

- ★ 39.425
- GitHub Trending · 2026-09-25

## Güncelleme
- 28 Eylül 2026: Yıldız 35.563 → 39.425, son sürüm v0.10.1 (21 Eylül 2026).
- 27 Eylül 2026: Yıldız 30.381 → 35.563, son sürüm v0.10.1 (21 Eylül 2026).
- 26 Eylül 2026: Yıldız 28.397 → 30.381.

## Ne kazandırır?
- Geçmiş etkileşimlerden öğrenen ve zamanla daha tutarlı sonuçlar üreten bellek mimarisi sunar.
- Doğrudan bilgi hatırlamanın ötesine geçerek ajanların karar alma süreçlerini iyileştirir.
- Python, Node.js ve Go gibi farklı diller için istemci kütüphaneleri barındırır.

## Kurulum

**Docker ile sunucu başlatma**

```
export OPENAI_API_KEY=sk-xxx

docker run -it --pull always --name hindsight --restart unless-stopped -p 8888:8888 -p 9999:9999 \
-e HINDSIGHT_API_LLM_API_KEY=$OPENAI_API_KEY \
-v hindsight-data:/home/hindsight/.pg0 \
ghcr.io/vectorize-io/hindsight:latest
```

## Çalıştırma

**Python ile istemci kurma**

```
pip install hindsight-client -U # Python
npm install @vectorize-io/hindsight-client # Node.js / TypeScript
go get github.com/vectorize-io/hindsight/hindsight-clients/go # Go
curl -fsSL https://hindsight.vectorize.io/get-cli | bash # CLI
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Yapay zekâ ajanımın geçmiş etkileşimlerden öğrenmesini, sadece konuşma geçmişini hatırlamakla kalmayıp zamanla daha tutarlı kararlar almasını istiyorum. Projeme bu bellek katmanını entegre etmek için gerekli sunucu kurulumunu ve istemci bağlantılarını yapılandırmama yardım et.

- **Kimin için:** Yapay zekâ ajanlarının zamanla öğrenmesini ve daha tutarlı kararlar almasını isteyen geliştiriciler. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/vectorize-io/hindsight)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-09-25 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Memory Layer Memory Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/hindsight/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
