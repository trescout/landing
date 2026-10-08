# Service Mesh Manager nedir, ne demek?

*Sözlük · Geliştirme · Son güncelleme: 22 Eylül 2026*

Service mesh manager, servis trafiğini izleyip yöneten konsol ve araç setidir.

## Tanım ve Kelime Kökeni

"Manager" **yönetici** demektir. Mesh trafiği taşır, manager izler ve yönetir: Kuralları dağıtır, sağlığı gösterir, sertifikaları döndürür. Kuledeki radar ekranı gibidir.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?

**Bulut:** Büyük mikro hizmet ağları.
**Güvenlik:** Trafik denetimi.
**Operasyon:** Arıza ayıklama.

## Teknik Derinlik ve Mimari

İşlevler:

**Görünürlük:** Servis haritası ve akış grafiği (Kiali benzeri).
**Politika:** Trafik ve güvenlik kuralı dağıtımı.
**Sertifika:** Kimlik yenileme otomasyonu.

Durum denetimi:

```
istioctl proxy-status
```

Manuel yönetim yüzlerce serviste imkansızdır, araç hata payını küçültür. Sıfırlar iddiası verilmez, azaltır.

## Sık Karıştırılanlar

Ağ geçidi sanılır. Geçit kapıda durur, manager tüm iç trafiği yönetir. Biri kapı, diğeri kontrol merkezidir.

## Farklı Disiplinlerde Kullanımı

**Kule:** Radar ekranlı yönetim.
**Trafik merkezi:** Sinyal ve kamera ağı.
**Orkestra şefi:** Bölüm düzeni.

*Uçak trafiğini yöneten kulenin radar ekranı gibidir; hangi uçağın nerede olduğu buradan izlenir.*

## Sıkça Sorulanlar

**Neden manuel yönetilmiyor?**

Servis çokluğu izlemeyi imkansız kılar. Araç hatayı ve gecikmeyi kısaltır.

**Mesh olmadan çalışır mı?**

Hayır. Manager mesh üstünde koşar, altyapı şarttır.

**Hangisi seçilmeli?**

Mesh ile uyumlu olanı. Istio kuruluysa onun konsolu seçilir.

**Maliyeti nedir?**

Kaynak ve öğrenme bedeli vardır. Karmaşa büyüyünce karşılığını verir.

## İlgili terimler

- [Service Mesh](https://trescout.com/dictionary/service-mesh/)
- [Cloud Native](https://trescout.com/dictionary/cloud-native/)
- [Observability](https://trescout.com/dictionary/observability/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/service-mesh-manager/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
