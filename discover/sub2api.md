# Yapay zekâ aboneliklerini tek merkezden yönetin

Sub2API é um serviço de migração de código aberto que combina diferentes assinaturas de IA, como Claude, OpenAI, Gemini e Grok, em uma única interface. Embora permita aos utilizadores partilhar os custos de subscrição, oferece a oportunidade de utilizar estes serviços de forma integrada com as ferramentas existentes.

- ★ 38.841
- Go
- GitHub Trending · 2026-08-23

## Güncelleme
- 23 Ağustos 2026: Yıldız 38.838 → 38.841, son sürüm v0.1.179 (20 Ağustos 2026).

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
