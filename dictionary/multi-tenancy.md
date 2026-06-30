# Multi-tenancy nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-06-30

Tek bir yazılımın, aynı anda birçok farklı kullanıcıya veya şirkete birbirinden bağımsız hizmet vermesidir.

## Tanım
Bir apartman binası düşünün; herkes aynı binayı kullanır ama herkesin kendi dairesi vardır. Multi-tenancy, yazılım dünyasında aynı sunucuyu ve aynı programı paylaşan farklı müşterilerin, birbirlerinin verilerini görmeden kendi alanlarında çalışmasıdır.

## Bir benzetmeyle
Bir otelde herkesin aynı binayı ve aynı havuzu kullanması ama herkesin kendi özel odasının olması gibidir.

## Nasıl çalışır?
Yazılım, veritabanında her kullanıcıya özel bir 'etiket' atar. Sistem, bir kullanıcıdan gelen isteği sadece o etikete sahip verilerle eşleştirir, böylece karışıklık olmaz.

## Nerede kullanılır?
SaaS (yazılım hizmeti) platformlarında, bulut tabanlı uygulamalarda ve kurumsal yönetim yazılımlarında kullanılır.

## Sık karıştırılanlar
Paylaşımlı sunucu ile karıştırılabilir; ancak burada paylaşılan sadece donanım değil, yazılımın mantıksal yapısıdır.

## Sıkça sorulanlar

**Neden tek bir program kullanılıyor?**  
Çünkü her kullanıcı için ayrı bir program kurmak çok maliyetli ve yönetimi zordur; tek bir merkezden güncelleme yapmak çok daha kolaydır.

## İlgili terimler
- [SaaS](/dictionary/saas/)
- [PaaS](/dictionary/paas/)
- [Cloud Native](/dictionary/cloud-native/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/multi-tenancy/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
