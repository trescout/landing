# Service Mesh nedir, ne demek?

*Sözlük · Geliştirme · Son güncelleme: 22 Eylül 2026*

Service mesh, mikro hizmetlerin trafiğini yöneten görünmez altyapı katmanıdır.

## Tanım ve Kelime Kökeni

Yüzlerce parçalı sistemde parçaların birbirini bulması ve güvenli konuşması zordur. Service mesh iletişimi yönetir, trafiği düzenler, güvenliği sağlar. Koda dokunmadan ağ politikası uygular.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?

**Bulut:** Mikro hizmetli büyük uygulamalar.
**Banka:** Sıkı güvenlikli servis trafiği.
**E-ticaret:** Kampanya yükü altında sipariş hattı.

## Teknik Derinlik ve Mimari

Parçalar:

**Sidecar:** Her servisin yanındaki küçük vekil, trafik buradan akar.
**Control plane:** Kuralları dağıtan beyin.
**Data plane:** İşi yapan vekiller.
**mTLS:** Servisler arası şifreli kimlik.
**Dayanıklılık:** Yeniden deneme ve devre kesici.

Yeniden deneme kuralı:

```
retries:
  attempts: 3
  perTryTimeout: 2s
```

Istio ve Linkerd bilinen uygulamalarıdır. Küçük sistemde maliyeti faydasını aşar.

## Farklı Disiplinlerde Kullanımı

**Havaalanı:** Uçakları çarpıştırmayan kule.
**Trafik:** Akışı düzenleyen sinyal ağı.
**Posta:** Gönderiyi ayıran dağıtım merkezi.

*Büyük bir havaalanındaki uçuş trafiğini yöneten kule gibidir; servislerin birbirine çarpmadan güvenli hareket etmesini sağlar.*

## Sıkça Sorulanlar

**Her projeye gerekli mi?**

Hayır. Az servisli sistemde yük getirir. Karmaşa büyüyünce anlam kazanır.

**Maliyeti nedir?**

Vekil başına bellek ve gecikme ekler. Gözlemlenebilirlik kazancı karşılığında ödenir.

**Kubernetes şart mı?**

Hayır, ama çoğunlukla birlikte kullanılır. Sanal makinelerde de koşan sürümler vardır.

**API gateway yerine geçer mi?**

Hayır. Gateway dış kapıdır, mesh iç trafiktir. İkisi birlikte çalışır.

## İlgili terimler

- [Cloud Native](https://trescout.com/dictionary/cloud-native/)
- [API](https://trescout.com/dictionary/api/)
- [Proxy](https://trescout.com/dictionary/proxy/)

## İlgili araçlar

- [Meshery](https://trescout.com/discover/meshery/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/service-mesh/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
