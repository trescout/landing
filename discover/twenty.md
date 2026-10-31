# Modern ve açık kaynaklı CRM

**Twenty**, teknik ekiplere iş süreçlerine göre özelleştirilebilir modern bir CRM kurma imkânı veren açık kaynaklı bir **Salesforce alternatifidir**. Yapay zekâ destekli iş akışlarına odaklanan bu sistemi kendi sunucunuzda barındırabilirsiniz.

- ★ 60.189
- TypeScript
- Lisans: özel
- GitHub Trending · 26 May 2026

## Güncelleme

- **31 Ekim 2026:** Yıldız 59.917 → 60.189, son sürüm twenty/v2.54.0 (30 Ekim 2026).
- **27 Ekim 2026:** Yıldız 59.751 → 59.917, son sürüm twenty/v2.52.0 (27 Ekim 2026).
- **26 Ekim 2026:** Yıldız 58.824 → 59.751, son sürüm twenty/v2.51.0 (25 Ekim 2026).
- **21 Ekim 2026:** Yıldız 58.665 → 58.824, son sürüm twenty/v2.50.0 (21 Ekim 2026).

- **Kimin için:** Kendi CRM'ini kurmak isteyen teknik ekipler
- **Zorluk:** İleri · self-host (geliştirici gerekir)
- **Ne sunar:** Özelleştirilebilir, yapay zekâ destekli CRM
- **Ücret:** Açık kaynak · self-host ücretsiz
- **Lisans:** Standart-dışı (NOASSERTION) · ayrıntı aşağıda

## Ne kazandırır?

- Salesforce'a **ücretsiz ve açık kaynaklı** bir alternatif.
- Self-host seçeneğiyle verileriniz üzerinde **tam kontrol**.
- Yapay zekâ destekli modern iş akışları.
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

Kod bilmiyorsanız · yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Twenty adlı açık kaynaklı CRM'i kurmak istiyorum; terminalde 'npx create-twenty-app my-app' komutuyla yeni bir uygulama oluştur, ardından 'npx twenty app:publish --private' ile çalışma alanıma yayınla. Self-hosting için Docker Compose ile nasıl çalıştıracağımı da anlat.

Depo: https://github.com/twentyhq/twenty. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

**Lisans:** ⚠️ Lisansı standart değil (GitHub 'NOASSERTION'). 'Açık kaynak' olarak anılır ama kendi başına/self-host kullanım ile ticari/SaaS olarak yeniden sunum farklı şartlara tabi olabilir. **Ticari kullanımdan önce repo'daki LICENSE dosyasını mutlaka okuyun.**

## Bağlantılar

- [GitHub deposu →](https://github.com/twentyhq/twenty)
- [Ana sayfa →](https://twenty.com)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun keşif tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [CRM](https://trescout.com/dictionary/crm/)
- [SaaS](https://trescout.com/dictionary/saas/)
- [Self-hosting](https://trescout.com/dictionary/self-hosting/)
- [Open Source](https://trescout.com/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/twenty/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
