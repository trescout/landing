# Multi-process nedir?

*Sözlük · Geliştirme · Son güncelleme: 7 Ekim 2026*

Bir bilgisayar programının, işlerini birbirinden tamamen bağımsız ve kendi özel bellek alanına sahip birden fazla alt sürece bölerek aynı anda çalıştırma yöntemidir.

## Tanım

Geleneksel programlamada bir uygulama genellikle tek bir hat üzerinden sırayla çalışır. Multi-process yani çoklu süreç yaklaşımında ise işletim sistemi, her bir iş için ayrı birer çalışma alanı oluşturur. TreScout sözlüğünde sıkça karşılaşacağınız bu yöntem sayesinde süreçlerden biri hata alıp çökerse, diğer süreçler bu durumdan etkilenmeden çalışmaya devam eder.

*Bunu aynı mutfakta çalışan ama kendi tezgahları, kendi bıçakları ve kendi malzemeleri olan bağımsız aşçılara benzetebilirsiniz. Aşçılardan biri elini kesip işi bıraksa bile diğer aşçılar kendi tezgahlarında yemek yapmaya güvenle devam eder.*

## Nasıl çalışır?

İşletim sistemi seviyesinde her bir süreç için ayrı bir bellek adresi ayrılır. Program ana bir süreçten yeni alt süreçler türetir ve bu süreçler birbirleriyle özel iletişim kanalları üzerinden haberleşerek görevleri paylaşır.

## Nerede kullanılır?

Özellikle internet tarayıcılarında her sekmenin ayrı bir süreç olarak çalıştırılmasında, büyük veri işleme sistemlerinde ve arka planda ağır hesaplamalar yapan sunucu uygulamalarında sıkça kullanılır.

## Sık karıştırılanlar

Multi-threading kavramı ile karıştırılır. Multi-threading yönteminde işler aynı bellek alanını paylaşan hafif iş parçacıklarıyla yapılırken, multi-process yönteminde her işin kendine ait tamamen yalıtılmış bir bellek alanı vardır.

## Sıkça sorulanlar

**Multi-process kullanmak bilgisayarı yorar mı?**

Evet, her süreç için ayrı bellek ve kaynak ayrıldığından dolayı diğer yöntemlere göre bilgisayarın kaynaklarını daha fazla tüketebilir.

**Hangi durumlarda multi-process tercih edilmelidir?**

Birbirinin çökmesinden etkilenmesini istemediğiniz, güvenlik ve kararlılığın ön planda olduğu ağır işlerde tercih edilmelidir.

## İlgili terimler

- [Concurrency](https://trescout.com/dictionary/concurrency/)
- [Runtime](https://trescout.com/dictionary/runtime/)
- [Thread-safety](https://trescout.com/dictionary/thread-safety/)
- [Distributed](https://trescout.com/dictionary/distributed/)

## İlgili araçlar

- [Raddebugger](https://trescout.com/discover/raddebugger/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/multi-process/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
