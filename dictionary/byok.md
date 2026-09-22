# BYOK nedir, ne demek?

> Bring Your Own Key

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

BYOK (**Bring Your Own Key**, kendi anahtarını getir), şifre anahtarının sizde durduğu düzendir.

## Tanım ve Kelime Kökeni
Verinin durduğu yerle anahtarın durduğu yer ayrılır. Sağlayıcı veriyi görür, açamaz. Kontrol sizdedir, sorumluluk da sizdedir.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Bulut:** Şifreli disk ve yedek.
- **Kurumsal:** Regülasyonlu veri.
- **YZ:** Kendi API anahtarı.

## Teknik Derinlik ve Mimari
Düzen:
- **Üretim:** Güçlü rastgele anahtar.
- **Saklama:** Donanım kasası (HSM) veya yönetici.
- **Rotasyon:** Periyodik yenileme.

Üretim örneği:

```
openssl rand -base64 32
```

Kayıp kuralı: Anahtar giderse veri gider. Yedek ve vasiyet planı şarttır.

## Sık Karıştırılanlar
Şifreleme sanılır. Şifreleme kilittir, BYOK anahtarın kimde durduğudur. Biri kapı, diğeri anahtarlık düzenidir.

## Farklı Disiplinlerde Kullanımı
- **Kasa:** Kendi anahtarınızla açma.
- **Emanet:** Mühürlü zarf teslimi.
- **Kiralık kasa:** Banka bilmez içerik.

## Bir benzetmeyle
Kasaya kendi getirdiğiniz anahtarla kilit vurmaya benzer.

## Sıkça sorulanlar

**Kaybedersem ne olur?**  
Erişim kalıcı gider. Yedek ve vasiyet planı şarttır.

**Neden kullanılır?**  
Sağlayıcı erişimini kapatmak için. Gizlilik ve uyum gerektirir.

**YZ araçlarında nedir?**  
Kendi API anahtarıyla çalışmadır. Kota ve fatura sizdedir.

**Maliyeti nedir?**  
Kasa ve yönetim bedeli vardır. Kritik veride karşılığını verir.

## İlgili terimler
- [Cybersecurity Skills](/dictionary/cybersecurity-skills/)
- [End-to-End Encryption](/dictionary/end-to-end-encryption/)
- [Secrets](/dictionary/secrets/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/byok/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
