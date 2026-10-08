# Modern ve Açık Kaynaklı CRM

**Twenty**, teknik ekiplere iş süreçlerine göre özelleştirilebilir modern bir CRM kurma imkânı veren açık kaynaklı bir **Salesforce alternatifidir**. Yapay zekâ destekli iş akışlarına odaklanan bu sistemi kendi sunucunuzda barındırabilirsiniz.

- ★ 57.935
- TypeScript
- Lisans: özel
- GitHub Trending · 26 May 2026

## Güncelleme

- **5 Ekim 2026:** Yıldız 57.768 → 57.935, son sürüm twenty/v2.45.0 (5 Ekim 2026).
- **1 Ekim 2026:** Yıldız 57.699 → 57.768, son sürüm twenty/v2.44.0 (1 Ekim 2026).
- **29 Eylül 2026:** Yıldız 57.541 → 57.699, son sürüm twenty/v2.43.0 (28 Eylül 2026).
- **27 Eylül 2026:** Yıldız 56.924 → 57.541, son sürüm sdk/v2.41.0 (23 Eylül 2026).

- **Kimin için:** Kendi CRM'ini kurmak isteyen teknik ekipler
- **Zorluk:** İleri · self-host (geliştirici gerekir)
- **Ne sunar:** Özelleştirilebilir, AI destekli CRM
- **Ücret:** Açık kaynak · self-host ücretsiz
- **Lisans:** Standart-dışı (NOASSERTION) · ayrıntı aşağıda

## Ne kazandırır?

- Salesforce'a **ücretsiz ve açık kaynaklı** bir alternatif.
- Self-host seçeneğiyle verileriniz üzerinde **tam kontrol**.
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

**Kaynak:** Resmî kaynak: https://docs.twenty.com/developers/self-host/capabilities/docker-compose

## Nasıl kurulur?

Genellikle Docker ile kendi sunucunuza kurulur; kurulum adımları dokümantasyonda. Yönetmek için biraz teknik bilgi gerekir.

## Nasıl kurulur, nasıl kullanılır?

🤖 Kod bilmiyorsanız · yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Twenty adlı açık kaynaklı CRM'i kurmak istiyorum; terminalde 'npx create-twenty-app my-app' komutuyla yeni bir uygulama oluştur, ardından 'npx twenty app:publish --private' ile çalışma alanıma yayınla. Self-hosting için Docker Compose ile nasıl çalıştıracağımı da anlat.

**Lisans:** ⚠️ Lisansı standart değil (GitHub 'NOASSERTION'). 'Açık kaynak' olarak anılır ama kendi başına/self-host kullanım ile ticari/SaaS olarak yeniden sunum farklı şartlara tabi olabilir. **Ticari kullanımdan önce repo'daki LICENSE dosyasını mutlaka okuyun.**

## Bağlantılar

- [GitHub deposu →](https://github.com/twentyhq/twenty)
- [Ana sayfa →](https://twenty.com)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun keşif tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [CRM](https://trescout.com/dictionary/crm/)
- [SaaS](https://trescout.com/dictionary/saas/)
- [Self-hosting](https://trescout.com/dictionary/self-hosting/)
- [Open Source](https://trescout.com/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/twenty/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
