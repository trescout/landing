# ApacheBench (ab) nedir?

> Apache HTTP Server Benchmarking Tool

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-29

Web sunucularının aynı anda gelen yoğun istek trafiği altındaki performansını ve sınırlarını ölçen komut satırı aracıdır.

## Tanım
ApacheBench (ab), web sunucularının belirli bir süre içinde kaç istek karşılayabildiğini test etmek için kullanılan hafif ve popüler bir performans ölçüm aracıdır. Komut satırından tek bir komutla yüzlerce eş zamanlı bağlantı başlatarak sistemin yanıt hızını raporlar. Geliştiricilerin sunucu yapılandırmalarını ve kod optimizasyonlarını doğrulamalarına yardımcı olur.

## Bir benzetmeyle
Bir mağazanın kapısına aynı anda 500 müşteri gönderip kasiyerlerin dakikada kaç kişiye fiş kesebildiğini ve kuyruğun ne kadar uzadığını kronometreyle ölçmeye benzer.

## Nasıl çalışır?
Kullanıcı terminal üzerinden test edilecek hedef adresi, toplam istek sayısını ve aynı anda açılacak bağlantı (eş zamanlılık) miktarını belirler. Araç belirlenen istekleri sunucuya hızla iletir, yanıt sürelerini toplar ve saniye başına düşen istek sayısı (RPS) gibi temel metrikleri tablo olarak sunar.

## Nerede kullanılır?
Web sitesi yayına alınmadan önce yapılan yük testlerinde, sunucu donanımı karşılaştırmalarında ve önbellek (cache) optimizasyonlarının başarısını ölçmede kullanılır.

## Sık karıştırılanlar
Karmaşık kullanıcı senaryolarını simüle eden gelişmiş yük testi araçlarından farklı olarak, yalnızca belirli bir HTTP bağlantısına ardışık veya eş zamanlı yük bindirmeye odaklanır.

## Sıkça sorulanlar

**ApacheBench kullanmak için Apache web sunucusu şart mıdır?**  
Hayır. Nginx, Node.js veya herhangi bir HTTP sunucusunu test etmek için bağımsız olarak çalıştırılabilir.

**Test sonuçlarında en çok hangi değere bakılır?**  
Saniyede tamamlanan istek sayısı (Requests per second) ve yanıtların milisaniye cinsinden gecikme süreleri en kritik göstergelerdir.

## İlgili terimler
- [Benchmark](/dictionary/benchmark/)
- [CLI](/dictionary/cli/)
- [Concurrency](/dictionary/concurrency/)
- [Deployment](/dictionary/deployment/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/apache-bench/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
