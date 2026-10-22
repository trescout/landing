# SaaS ve yapay zekâ uygulamaları için kimlik doğrulama

Logto, SaaS ve yapay zekâ uygulamaları için Açık Kimlik Doğrulama (OIDC) ve OAuth 2.1 protokollerini temel alan bir kimlik doğrulama ve yetkilendirme altyapısı sunuyor. Çoklu kiracılık (multi-tenancy), tek oturum açma (SSO) ve rol tabanlı erişim denetimi (RBAC) gibi özellikleri TypeScript ile geliştirilmiş bir yapıda birleştiriyor.

- ★ 14.676
- TypeScript
- GitHub Trending · 2026-06-30

## Güncelleme

- **13 Ekim 2026:** Yıldız 14.646 → 14.676, son sürüm v1.45.0 (13 Ekim 2026).
- **30 Eylül 2026:** Yıldız 14.484 → 14.646, son sürüm v1.44.0 (30 Eylül 2026).
- **31 Ağustos 2026:** Yıldız 14.271 → 14.484, son sürüm v1.43.0 (31 Ağustos 2026).
- **2 Ağustos 2026:** Yıldız 12.903 → 14.271, son sürüm v1.42.0 (30 Temmuz 2026).

## Ne kazandırır?

- OIDC ve OAuth 2.1 protokolleri ile güvenli altyapı
- Çoklu kiracılık ve rol tabanlı erişim denetimi
- 30'dan fazla çerçeve için hazır SDK desteği

## Kurulum

**Docker Compose ile kurulum**

```
curl -fsSL https://raw.githubusercontent.com/logto-io/logto/HEAD/docker-compose.yml | \
  docker compose -p logto -f - up
```

**Node.js ile kurulum**

```
npm init @logto
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Logto kullanarak uygulamam için güvenli bir kimlik doğrulama sistemi kurmak istiyorum. OIDC ve OAuth 2.1 protokollerini temel alan bu yapıda, çoklu kiracılık ve rol tabanlı erişim denetimi özelliklerini nasıl yapılandırabilirim? SaaS projemde kullanıcı giriş akışlarını ve kurumsal SSO entegrasyonunu yönetmek için izlemem gereken temel adımları açıklar mısın?

Depo: https://github.com/logto-io/logto. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** SaaS platformları ve yapay zekâ tabanlı uygulamalar geliştiren, güvenli kimlik doğrulama altyapısına ihtiyaç duyan yazılım ekipleri için uygundur.
- **Lisans:** MPL-2.0

## Bağlantılar

- [GitHub deposu →](https://github.com/logto-io/logto)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-06-30 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [OIDC](https://trescout.com/dictionary/oidc/)
- [Multi-tenancy](https://trescout.com/dictionary/multi-tenancy/)
- [RBAC](https://trescout.com/dictionary/rbac/)
- [SSO](https://trescout.com/dictionary/sso/)
- [SaaS](https://trescout.com/dictionary/saas/)
- [SDK](https://trescout.com/dictionary/sdk/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/logto/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
