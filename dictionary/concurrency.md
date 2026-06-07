# Concurrency nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-06-07

Bir bilgisayarın aynı anda birden fazla işlemi yönetebilme ve parçalar halinde yürütebilme yeteneğidir.

## Tanım
Bilgisayarlar aslında aynı anda tek bir işi çok hızlı yaparlar. Concurrency, bir işi küçük parçalara bölüp, bir iş bitmeden diğerine geçerek hepsini aynı anda yapıyormuş gibi hissettiren bir yönetim biçimidir.

## Bir benzetmeyle
Bir aşçının aynı anda hem çorbayı karıştırıp hem de salata doğraması gibidir; birini yaparken diğerine kısa süreliğine ara verir.

## Nasıl çalışır?
İşlemci, görevleri çok hızlı bir şekilde sırayla işleyerek kullanıcıya hepsinin aynı anda gerçekleştiği izlenimini verir.

## Nerede kullanılır?
Web sunucuları, çok kullanıcılı uygulamalar ve modern işletim sistemlerinde kullanılır.

## Sık karıştırılanlar
Paralellik (parallelism) ile karıştırılır; paralellik aynı anda gerçekten iki farklı işlemcinin iki işi yapmasıdır, concurrency ise işlerin zamanlamasıdır.

## Sıkça sorulanlar

**Neden önemli?**  
Bilgisayarın boş durmamasını ve aynı anda binlerce kullanıcıya hizmet verebilmesini sağlar.

**Kod yazarken zor mu?**  
Evet, aynı anda iki iş birbiriyle çakışırsa hatalar oluşabilir, dikkatli yönetilmelidir.

## İlgili terimler
- [State Management](/dictionary/state-management/)
- [Runtime](/dictionary/runtime/)
- [Computer Science](/dictionary/computer-science/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/concurrency/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
