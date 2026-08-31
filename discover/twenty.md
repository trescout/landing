# Modern ve Açık Kaynaklı CRM

Twenty , teknik ekiplere iş süreçlerine göre özelleştirilebilir modern bir CRM kurma imkânı veren açık kaynaklı bir Salesforce alternatifidir . Yapay zekâ destekli iş akışlarına odaklanan bu sistemi kendi sunucunuzda barındırabilirsiniz.

- ★ 55.953
- TypeScript
- Lisans: özel
- GitHub Trending · 26 May 2026

## Güncelleme
- 31 Ağustos 2026: Yıldız 55.660 → 55.953, son sürüm sdk/v2.37.0 (28 Ağustos 2026).
- 27 Ağustos 2026: Yıldız 55.436 → 55.660, son sürüm twenty/v2.35.0 (26 Ağustos 2026).
- 24 Ağustos 2026: Yıldız 54.772 → 55.436, son sürüm twenty/v2.34.0 (24 Ağustos 2026).
- 12 Ağustos 2026: Yıldız 54.367 → 54.772, son sürüm sdk/v2.30.0 (11 Ağustos 2026).

- **Kimin için:** Kendi CRM'ini kurmak isteyen teknik ekipler 
- **Zorluk:** İleri · self-host (geliştirici gerekir) 
- **Ne sunar:** Özelleştirilebilir, AI destekli CRM 
- **Ücret:** Açık kaynak · self-host ücretsiz 
- **Lisans:** Standart-dışı (NOASSERTION) · ayrıntı aşağıda 

## Ne kazandırır?
- Salesforce'a ücretsiz ve açık kaynaklı bir alternatif.
- Self-host seçeneğiyle verileriniz üzerinde tam kontrol .
- AI destekli modern iş akışları.
- İş ihtiyaçlarınıza göre uyarlanabilir esnek yapı taşları.

## Kurulum

**Ortam şablonunu indir**

```
curl -o .env https://raw.githubusercontent.com/twentyhq/twenty/refs/heads/main/packages/twenty-docker/.env.example
```

**Compose dosyasını indir**

```
curl -o docker-compose.yml https://raw.githubusercontent.com/twentyhq/twenty/refs/heads/main/packages/twenty-docker/docker-compose.yml
```

**Şifreleme anahtarı üret**

```
openssl rand -base64 32
```

**Servisleri başlat**

```
docker compose up -d
```

## Çalıştırma

**Yerel arayüze eriş**

```
http://localhost:3000
```

Kaynak: Resmî kaynak: https://docs.twenty.com/developers/self-host/capabilities/docker-compose

## Nasıl kurulur?

Genellikle Docker ile kendi sunucunuza kurulur; kurulum adımları dokümantasyonda. Yönetmek için biraz teknik bilgi gerekir.

## Nasıl kurulur, nasıl kullanılır?
🤖 Kod bilmiyorsanız · yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Twenty adlı açık kaynaklı CRM'i kurmak istiyorum; terminalde 'npx create-twenty-app my-app' komutuyla yeni bir uygulama oluştur, ardından 'npx twenty app:publish --private' ile çalışma alanıma yayınla. Self-hosting için Docker Compose ile nasıl çalıştıracağımı da anlat.

Lisans: ⚠️ Lisansı standart değil (GitHub 'NOASSERTION'). 'Açık kaynak' olarak anılır ama kendi başına/self-host kullanım ile ticari/SaaS olarak yeniden sunum farklı şartlara tabi olabilir. Ticari kullanımdan önce repo'daki LICENSE dosyasını mutlaka okuyun.

## Bağlantılar
- [GitHub deposu →](https://github.com/twentyhq/twenty)
- [Ana sayfa →](https://twenty.com)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun keşif tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
CRM SaaS Self-hosting Open Source Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/twenty/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
