# Endpoint nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

Endpoint (Türkçe karşılığıyla **uç nokta**), ağın kullanıcı ucundaki cihaz veya API ucudur.

## Tanım ve Kelime Kökeni
"End point" **bitiş noktası** demektir. İki anlamı vardır: Fiziksel uçtaki cihaz ve yazılımdaki API ucu. Bilgi cihazda biter veya API ucunda alınır. Güvenlikte dış savunma hattıdır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Kurumsal:** Dizüstü ve telefon filosu.
- **Ev:** Akıllı cihazlar.
- **API:** Uygulama istek uçları.

## Teknik Derinlik ve Mimari
İki yüz:
- **Cihaz:** EDR ile izlenir, yama ve şifreleme uygulanır.
- **API:** Adres ve metotla çağrılır (`GET /api/siparis/4521`).

Örnek istek:

```
GET /api/siparis/4521
```

Saldırıların çoğu zayıf uçtan girer. Yama disiplini ve en az yetki kuraldır.

## Sık Karıştırılanlar
Sunucu sanılır. Sunucu merkezdir, uç nokta kullanıcıdadır. API ucuyla da karışır: O adrestir, bu cihazdır.

## Farklı Disiplinlerde Kullanımı
- **Adres:** Paketin vardığı kapı.
- **Durak:** Hattın son noktası.
- **Kapı numarası:** Dairenin adresi.

## Bir benzetmeyle
Kargo ağında paketin vardığı ev adresi gibidir.

## Sıkça sorulanlar

**Neden güvenlik önemli?**  
Saldırı zayıf uçtan girer. Yama ve izleme ilk savunmadır.

**API ucu nedir?**  
Çağrılabilir adrestir. Metot ve yolla istek karşılanır.

**Nasıl korunur?**  
Yama, şifreleme ve en az yetkiyle. EDR izlemesi eklenir.

**Sunucu farkı nedir?**  
Sunucu merkezde hizmet verir, uç nokta kenarda tüketir.

## İlgili terimler
- [Network Stack](/dictionary/network-stack/)
- [VPN](/dictionary/vpn/)
- [Security Scanner](/dictionary/security-scanner/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/endpoint/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
