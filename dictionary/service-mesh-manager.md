# Service Mesh Manager nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

Service mesh manager, servis trafiğini izleyip yöneten konsol ve araç setidir.

## Tanım ve Kelime Kökeni
"Manager" **yönetici** demektir. Mesh trafiği taşır, manager izler ve yönetir: Kuralları dağıtır, sağlığı gösterir, sertifikaları döndürür. Kuledeki radar ekranı gibidir.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Bulut:** Büyük mikro hizmet ağları.
- **Güvenlik:** Trafik denetimi.
- **Operasyon:** Arıza ayıklama.

## Teknik Derinlik ve Mimari
İşlevler:
- **Görünürlük:** Servis haritası ve akış grafiği (Kiali benzeri).
- **Politika:** Trafik ve güvenlik kuralı dağıtımı.
- **Sertifika:** Kimlik yenileme otomasyonu.

Durum denetimi:

```
istioctl proxy-status
```

Manuel yönetim yüzlerce serviste imkansızdır, araç hata payını küçültür. Sıfırlar iddiası verilmez, azaltır.

## Sık Karıştırılanlar
Ağ geçidi sanılır. Geçit kapıda durur, manager tüm iç trafiği yönetir. Biri kapı, diğeri kontrol merkezidir.

## Farklı Disiplinlerde Kullanımı
- **Kule:** Radar ekranlı yönetim.
- **Trafik merkezi:** Sinyal ve kamera ağı.
- **Orkestra şefi:** Bölüm düzeni.

## Bir benzetmeyle
Uçak trafiğini yöneten kulenin radar ekranı gibidir; hangi uçağın nerede olduğu buradan izlenir.

## Sıkça sorulanlar

**Neden manuel yönetilmiyor?**  
Servis çokluğu izlemeyi imkansız kılar. Araç hatayı ve gecikmeyi kısaltır.

**Mesh olmadan çalışır mı?**  
Hayır. Manager mesh üstünde koşar, altyapı şarttır.

**Hangisi seçilmeli?**  
Mesh ile uyumlu olanı. Istio kuruluysa onun konsolu seçilir.

**Maliyeti nedir?**  
Kaynak ve öğrenme bedeli vardır. Karmaşa büyüyünce karşılığını verir.

## İlgili terimler
- [Service Mesh](/dictionary/service-mesh/)
- [Cloud Native](/dictionary/cloud-native/)
- [Observability](/dictionary/observability/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/service-mesh-manager/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
