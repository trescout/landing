# Resolver Load Balancing nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-06-11

İnternet adres sorgularını birden fazla sunucuya dağıtarak sistemin aşırı yüklenmesini önleme işlemidir.

## Tanım
İnternet trafiği çok yoğun olduğunda, tek bir sunucu tüm sorgulara yetişemez. Bu yöntem, sorguları bir trafik polisi gibi farklı sunuculara yönlendirerek sistemin çökmesini engeller. Böylece her zaman hızlı ve kesintisiz bir bağlantı sağlanır.

## Bir benzetmeyle
Bir süpermarketteki tüm müşterilerin tek bir kasaya gitmesi yerine, 10 farklı kasaya yönlendirilerek kuyruğun eritilmesi gibidir.

## Nasıl çalışır?
Bir yük dengeleyici yazılımı kurun, gelen DNS sorgularını tanımladığınız sunucular arasında eşit şekilde paylaştırın.

## Nerede kullanılır?
Büyük web sitelerinde ve yüksek trafikli ağ altyapılarında kullanılır.

## Sık karıştırılanlar
Sadece sunucu kümeleme ile karıştırılabilir, ancak bu yöntem özellikle sorgu trafiğini yönetmeye odaklanır.

## Sıkça sorulanlar

**Bu sistem sayesinde site hızlanır mı?**  
Evet, sunucu üzerindeki yük azaldığı için yanıt süreleri kısalır.

**Tek bir sunucu bozulursa ne olur?**  
Yük dengeleyici diğer sunuculara yönlendirme yaparak sitenin çalışmaya devam etmesini sağlar.

## İlgili terimler
- [Proxy](/dictionary/proxy/)
- [Reverse Proxy](/dictionary/reverse-proxy/)
- [Runtime](/dictionary/runtime/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/resolver-load-balancing/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
