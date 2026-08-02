# Karmaşık görevler için yapay zekâ ajanı

ByteDance tarafından geliştirilen Deer-Flow, uzun süreli görevleri yerine getirmek için tasarlanmış açık kaynaklı bir süper ajan (SuperAgent) çerçevesidir. Sistem; kum havuzu (sandbox), hafıza yönetimi ve alt ajanlar kullanarak karmaşık iş akışlarını otonom şekilde araştırıp kodlayabilmektedir.

- ★ 78.818
- Python
- GitHub Trending · 2026-06-22

## Güncelleme
- 2 Ağustos 2026: Yıldız 72.905 → 78.818, son sürüm v2.0.0 (25 Haziran 2026).

## Ne kazandırır?
- Otonom araştırma ve kodlama yeteneği
- Güvenli kum havuzu ortamında çalışma
- Uzun süreli hafıza ve alt ajan yönetimi

## Kurulum

**Depoyu klonlama**

```
git clone https://github.com/bytedance/deer-flow.git
cd deer-flow
```

**Kurulum sihirbazını başlatma**

```
make setup
```

## Çalıştırma

**Docker ile başlatma**

```
make docker-init # Pull sandbox image (only once or when image updates)
make docker-start # Start services (auto-detects sandbox mode from config.yaml)
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
DeerFlow deposunu bilgisayarıma klonla ve ardından make setup komutunu çalıştırarak yerel geliştirme ortamı için gerekli yapılandırmayı tamamla. Kurulum sihirbazı sırasında LLM sağlayıcısı, web arama tercihleri ve güvenlik ayarları gibi seçenekleri yapılandırmama yardımcı ol.

- **Kimin için:** Karmaşık iş akışlarını otonom şekilde yönetmek ve kodlamak isteyen yazılımcılar ile geliştiriciler için uygundur. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/bytedance/deer-flow)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-22 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
SuperAgent Sandbox LLM Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/deer-flow/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
