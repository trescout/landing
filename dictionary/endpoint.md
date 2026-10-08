# Endpoint nedir, ne demek?

*Sözlük · Geliştirme · Son güncelleme: 22 Eylül 2026*

Endpoint (Türkçe karşılığıyla **uç nokta**), ağın kullanıcı ucundaki cihaz veya API ucudur.

## Tanım ve Kelime Kökeni

"End point" **bitiş noktası** demektir. İki anlamı vardır: Fiziksel uçtaki cihaz ve yazılımdaki API ucu. Bilgi cihazda biter veya API ucunda alınır. Güvenlikte dış savunma hattıdır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?

**Kurumsal:** Dizüstü ve telefon filosu.
**Ev:** Akıllı cihazlar.
**API:** Uygulama istek uçları.

## Teknik Derinlik ve Mimari

İki yüz:

**Cihaz:** EDR ile izlenir, yama ve şifreleme uygulanır.
**API:** Adres ve metotla çağrılır (`GET /api/siparis/4521`).

Örnek istek:

```
GET /api/siparis/4521
```

Saldırıların çoğu zayıf uçtan girer. Yama disiplini ve en az yetki kuraldır.

## Sık Karıştırılanlar

Sunucu sanılır. Sunucu merkezdir, uç nokta kullanıcıdadır. API ucuyla da karışır: O adrestir, bu cihazdır.

## Farklı Disiplinlerde Kullanımı

**Adres:** Paketin vardığı kapı.
**Durak:** Hattın son noktası.
**Kapı numarası:** Dairenin adresi.

*Kargo ağında paketin vardığı ev adresi gibidir.*

## Sıkça Sorulanlar

**Neden güvenlik önemli?**

Saldırı zayıf uçtan girer. Yama ve izleme ilk savunmadır.

**API ucu nedir?**

Çağrılabilir adrestir. Metot ve yolla istek karşılanır.

**Nasıl korunur?**

Yama, şifreleme ve en az yetkiyle. EDR izlemesi eklenir.

**Sunucu farkı nedir?**

Sunucu merkezde hizmet verir, uç nokta kenarda tüketir.

## İlgili terimler

- [Network Stack](https://trescout.com/dictionary/network-stack/)
- [VPN](https://trescout.com/dictionary/vpn/)
- [Security Scanner](https://trescout.com/dictionary/security-scanner/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/endpoint/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
