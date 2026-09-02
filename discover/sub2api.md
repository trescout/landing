# Yapay zekâ aboneliklerini tek merkezden yönetin

Sub2API, Claude, OpenAI, Gemini ve Grok aboneliklerine tek noktadan erişim ve maliyet paylaşımı sağlayan açık kaynaklı bir aracı hizmettir.

- ★ 40.163
- Go
- GitHub Trending · 2026-08-23

## Güncelleme
- 2 Eylül 2026: Yıldız 40.067 → 40.163, son sürüm v0.2.0 (2 Eylül 2026).
- 1 Eylül 2026: Yıldız 39.987 → 40.067, son sürüm v0.1.185 (1 Eylül 2026).
- 31 Ağustos 2026: Yıldız 39.608 → 39.987, son sürüm v0.1.184 (31 Ağustos 2026).
- 27 Ağustos 2026: Yıldız 38.841 → 39.608, son sürüm v0.1.183 (25 Ağustos 2026).

## Ne kazandırır?
- Farklı yapay zekâ aboneliklerini tek arayüzde birleştirir
- Abonelik maliyetlerini verimli şekilde dağıtmanıza yardımcı olur
- Mevcut araçlarla entegre çalışma imkânı sunar

## Kurulum

**Otomatik kurulum**

```
curl -sSL https://raw.githubusercontent.com/Wei-Shaw/sub2api/main/deploy/install.sh | sudo bash
```

**Docker ile kurulum**

```
curl -sSL https://raw.githubusercontent.com/Wei-Shaw/sub2api/main/deploy/docker-deploy.sh | bash
```

## Çalıştırma

**Servisi başlatma**

```
docker compose up -d
```

**Yönetici şifresini görüntüleme**

```
docker compose -f docker-compose.local.yml logs sub2api | grep "admin password"
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Sub2API platformunu kullanarak Claude, OpenAI, Gemini ve Grok gibi farklı yapay zekâ servislerini tek bir API ağ geçidi üzerinden nasıl yapılandırabilirim? Abonelik kotalarımı verimli dağıtmak ve mevcut yazılım araçlarımla entegre etmek için izlemem gereken temel adımları açıkla. Ayrıca, bu platformu kullanırken Anthropic gibi sağlayıcıların hizmet şartlarına uyum sağlamak adına dikkat etmem gereken yasal ve teknik hususları özetle.

- **Kimin için:** Birden fazla yapay zekâ aboneliğini tek bir platform üzerinden yönetmek ve maliyetlerini optimize etmek isteyen geliştiriciler içindir. 
- **Lisans:** LGPL-3.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/Wei-Shaw/sub2api)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-23 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
API Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/sub2api/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
