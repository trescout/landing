# Control Plane nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-08-31

Bir sistemin nasıl çalışacağını yöneten, trafiği ve ayarları kontrol eden merkezi yönetim katmanıdır.

## Tanım
Büyük sistemlerde işin yapıldığı yer (data plane) ile bu işin nasıl yapılacağına karar veren yer (control plane) ayrılır. Control plane, sistemin beyni gibidir; hangi verinin nereye gideceğini, kimin yetkili olduğunu ve sistemin genel durumunu yönetir.

## Bir benzetmeyle
Bir havaalanında uçakların uçtuğu pistler data plane ise, uçuş rotalarını belirleyen ve iniş kalkış trafiğini yöneten kule control plane'dir.

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
- [API Gateway](/dictionary/api-gateway/)
- [Networking Stack](/dictionary/networking-stack/)
- [Cloud Native](/dictionary/cloud-native/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/control-plane/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
