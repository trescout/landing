# Instances nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-06

Bir yazılımın veya sistemin aynı anda çalışan her bir bağımsız kopyasıdır.

## Tanım
Bilgisayar dünyasında bir programı başlattığınızda, o programın bellekte bir 'örneği' oluşur. Aynı programdan üç farklı pencere açarsanız, o programın üç farklı kopyasını (instance) çalıştırmış olursunuz. Her biri birbirinden bağımsızdır ve kendi verilerini tutar.

## Bir benzetmeyle
Bir Word dosyasını iki farklı pencerede açmak gibidir; her pencere aynı programı kullanır ama üzerinde çalıştığınız metinler birbirinden bağımsızdır.

## Nasıl çalışır?
Sistem kaynakları, her kopya için ayrı bir yer ayırır. Böylece bir kopyada hata oluşursa veya program çökerse, diğer kopyalar bundan etkilenmeden çalışmaya devam edebilir.

## Nerede kullanılır?
Bulut bilişimde, sunucu yönetiminde ve oyun sunucularında çok sık kullanılır.

## Sık karıştırılanlar
Programın kendisi (kaynak kod) ile karıştırılmamalıdır; kaynak kod bir tane, çalışan kopyalar ise sınırsız olabilir.

## Sıkça sorulanlar

**Neden birden fazla kopya çalıştırırız?**  
Yükü dağıtmak, güvenliği artırmak veya aynı anda farklı kullanıcıların işlerini yönetebilmek için kullanılır.

## İlgili terimler
- [Containers](/dictionary/containers/)
- [Virtual Machines](/dictionary/virtual-machines/)
- [Runtime](/dictionary/runtime/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/instances/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
