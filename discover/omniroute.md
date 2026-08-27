# Tüm yapay zekâ sağlayıcılarını birleştirin

OmniRoute, 231'den fazla yapay zekâ sağlayıcısını tek bir uç noktada (endpoint) birleştirerek ücretsiz erişim imkânı sunan bir ağ geçididir (gateway). Gelişmiş sıkıştırma teknikleriyle jeton (token) kullanımını azaltırken, akıllı yedekleme ve çok modlu arayüz desteğiyle geliştirici araçlarını optimize eder.

- ★ 56.571
- TypeScript
- GitHub Trending · 2026-07-01

## Güncelleme
- 27 Ağustos 2026: Yıldız 53.963 → 56.571, son sürüm v3.8.50 (26 Ağustos 2026).
- 24 Ağustos 2026: Yıldız 51.059 → 53.963, son sürüm v3.8.49 (30 Temmuz 2026).
- 19 Ağustos 2026: Yıldız 48.542 → 51.059, son sürüm v3.8.49 (30 Temmuz 2026).
- 15 Ağustos 2026: Yıldız 46.052 → 48.542, son sürüm v3.8.49 (30 Temmuz 2026).

## Ne kazandırır?
- 231 farklı yapay zekâ sağlayıcısına tek noktadan erişim
- Gelişmiş sıkıştırma ile %95'e varan jeton tasarrufu
- 50'den fazla ücretsiz katman desteği

## Kurulum

**NPM ile kurulum**

```
npm install -g omniroute
omniroute
```

**Docker ile kurulum**

```
docker run -d --name omniroute --restart unless-stopped --stop-timeout 40 \
-p 20128:20128 -v omniroute-data:/app/data diegosouzapw/omniroute:latest
```

## Çalıştırma

**Bağlantı testi**

```
curl http://localhost:20128/v1/models -H "Authorization: Bearer YOUR_KEY"
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
OmniRoute kullanarak 231 farklı yapay zekâ sağlayıcısını tek bir uç noktada birleştirmek istiyorum. Jeton kullanımımı optimize etmek ve ücretsiz katmanlardan faydalanmak için bu aracı nasıl yapılandırabilirim? Claude Code, Cursor veya Copilot gibi araçlarımı bu ağ geçidine bağlayarak maliyetlerimi düşürmek ve kesintisiz erişim sağlamak için izlemem gereken adımları açıkla.

- **Kimin için:** Yapay zekâ modellerini sık kullanan ve jeton maliyetlerini optimize etmek isteyen geliştiriciler için uygundur. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/diegosouzapw/OmniRoute)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-07-01 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Endpoint Gateway Token Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/omniroute/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
