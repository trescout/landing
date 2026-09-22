# Identity Provider nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

Identity provider (Türkçe karşılığıyla **kimlik sağlayıcı**), girişleri doğrulayan merkezi servistir.

## Tanım ve Kelime Kökeni
Her uygulamaya ayrı şifre yerine tek merkezden giriş yapılır. Uygulama kim olduğunuzu servise sorar, onay alır. Parolanız uygulamalara dağılmaz, merkezde kalır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Şirket:** Tek girişle tüm sistemler.
- **Web:** Sosyal hesapla giriş.
- **Kurumsal:** Çalışan yaşam döngüsü.

## Teknik Derinlik ve Mimari
Akış:

```
giriş → doğrulama → jeton → uygulama
```

Parçalar:
- **Kimlik jetonu:** Kim olduğunuzun belgesi.
- **Erişim jetonu:** Ne yapabileceğinizin izni.
- **MFA:** Parolaya ek ikinci kanıt.
- **Oturum:** Tek girişle çok uygulama (SSO).

Kural: Jeton süresi kısa tutulur, yenileme arka planda döner.

## Sık Karıştırılanlar
Şifre yöneticisi sanılır. O parolayı saklar, bu kimliği onaylar. Biri kasa, diğeri noterdir.

## Farklı Disiplinlerde Kullanımı
- **Resepsiyon:** Pasaporta karşı kart anahtar.
- **Noter:** Kimlik tasdiki.
- **Pasaport kontrolü:** Damga ile geçiş.

## Bir benzetmeyle
Otel resepsiyonunda pasaport gösterip kart anahtar almaya benzer; oda kapısı resepsiyon onayına güvenir.

## Sıkça sorulanlar

**Güvenli midir?**  
Evet. Parola her uygulamaya dağılmadığı için saldırı yüzeyi küçülür.

**Sistem çökerse ne olur?**  
Bağlı uygulamalar etkilenir. Yedeklilik ve acil erişim planı şarttır.

**SSO farkı nedir?**  
SSO tek giriş deneyimidir, sağlayıcı altyapısıdır. Biri yüz, diğeri omurgadır.

**Kendim kurabilir miyim?**  
Evet, açık kaynak seçenekler vardır. Yama ve yedek disiplini size aittir.

## İlgili terimler
- [SSO](/dictionary/sso/)
- [OIDC](/dictionary/oidc/)
- [RBAC](/dictionary/rbac/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/identity-provider/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
