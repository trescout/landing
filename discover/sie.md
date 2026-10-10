# Yapay zekâ ajanları için çıkarım sunucusu

Superlinked tarafından geliştirilen SIE, yapay zekâ ajanlarının ihtiyaç duyduğu modelleri çalıştırmak için kullanılan açık kaynaklı bir çıkarım sunucusu (inference server) ve üretim kümesidir. Python tabanlı bu yapı, karmaşık model dağıtımlarını yönetmeyi ve ölçeklenebilir bir altyapı sunmayı hedefler.

- ★ 3.372
- Python
- GitHub Trending · 2026-09-03

## Güncelleme

- **10 Ekim 2026:** Yıldız 3.350 → 3.372, son sürüm v0.10.0 (9 Ekim 2026).
- **30 Eylül 2026:** Yıldız 3.325 → 3.350, son sürüm v0.9.0 (30 Eylül 2026).
- **27 Eylül 2026:** Yıldız 3.198 → 3.325, son sürüm v0.8.3 (26 Eylül 2026).
- **4 Eylül 2026:** Yıldız 3.157 → 3.198, son sürüm v0.7.3 (3 Eylül 2026).

## Ne kazandırır?

- Açık kaynaklı modelleri tek bir küme üzerinden yönetir
- OpenAI uyumlu arayüzü sayesinde kolay entegrasyon sağlar
- Arama, veri çıkarma ve metin üretimi gibi görevleri destekler

## Kurulum

**SDK kurulumu**

```
pip install sie-sdk                # Python
npm install @superlinked/sie-sdk   # TypeScript (pnpm and yarn work too)
```

## Çalıştırma

**İlk yerleştirme denemesi**

```
curl http://localhost:8080/v1/embeddings \
  -H 'Content-Type: application/json' \
  -d '{"model": "sentence-transformers/all-MiniLM-L6-v2", "input": "Hello world"}'
# {"object": "list", "data": [{"object": "embedding", "embedding": [-0.0344, 0.0310, ...
```

## Kod bilmiyorsanız

🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

SIE sunucusu üzerinden bir yapay zekâ ajanı için model çalıştırmak istiyorum. Ajanımın ihtiyaç duyduğu arama, veri çıkarma ve metin üretimi gibi görevleri tek bir API üzerinden nasıl yönetebilirim? SIE'nin sunduğu OpenAI uyumlu uç noktaları kullanarak embedding oluşturma ve metin üretme süreçlerini nasıl yapılandırabilirim?

- **Kimin için:** Kendi altyapısında çok sayıda yapay zekâ modelini ölçeklenebilir şekilde çalıştırmak isteyen geliştiriciler içindir.
- **Lisans:** Apache-2.0

## Bağlantılar

- [GitHub deposu →](https://github.com/superlinked/sie)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-09-03 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Embedding](https://trescout.com/dictionary/embedding/)
- [Inference Server](https://trescout.com/dictionary/inference-server/)
- [Inference](https://trescout.com/dictionary/inference/)
- [SDK](https://trescout.com/dictionary/sdk/)
- [API](https://trescout.com/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/sie/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
