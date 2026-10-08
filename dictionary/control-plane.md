# Control Plane nedir?

*Sözlük · Geliştirme · Son güncelleme: 31 Ağustos 2026*

Bir sistemin nasıl çalışacağını yöneten, trafiği ve ayarları kontrol eden merkezi yönetim katmanıdır.

## Tanım

Büyük sistemlerde işin yapıldığı yer (data plane) ile bu işin nasıl yapılacağına karar veren yer (control plane) ayrılır. Control plane, sistemin beyni gibidir; hangi verinin nereye gideceğini, kimin yetkili olduğunu ve sistemin genel durumunu yönetir.

*Bir havaalanında uçakların uçtuğu pistler data plane ise, uçuş rotalarını belirleyen ve iniş kalkış trafiğini yöneten kule control plane'dir.*

## Nasıl çalışır?

Merkezi bir yazılım veya arayüz üzerinden kurallar belirlenir. Bu kurallar sistemin diğer parçalarına iletilerek operasyonel süreklilik sağlanır.

## Nerede kullanılır?

Bulut bilişim mimarilerinde, ağ yönetim sistemlerinde ve büyük ölçekli veri merkezlerinde bulunur.

## Sık karıştırılanlar

Data plane ile karıştırılabilir; biri yönetir, diğeri işi yapar.

## Sıkça sorulanlar

**Çökerse ne olur?**

Sistem yeni komut alamaz veya trafiği yönetemez hale gelir, bu nedenle genellikle çok yüksek erişilebilirlikle korunur.

## İlgili terimler

- [API Gateway](https://trescout.com/dictionary/api-gateway/)
- [Network Stack](https://trescout.com/dictionary/network-stack/)
- [Cloud Native](https://trescout.com/dictionary/cloud-native/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/control-plane/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
