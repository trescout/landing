# Time Series Database nedir?

*Veri & Altyapı · Son güncelleme: 7 Kasım 2026*

Zaman içindeki değişimleri kronolojik sırayla saklayan özel veritabanı.

## Tanım

Time Series Database, verilerin zaman damgasıyla birlikte kaydedildiği ve saniyeler içindeki değişimlerin analiz edildiği yüksek hızlı bir veritabanı türüdür. Klasik veritabanlarından farklı olarak verileri güncellemek yerine sürekli olarak alta yeni bir zaman kaydı ekler. Milyonlarca sensörün veya sunucunun anlık durumunu izlemek için optimize edilmiştir.

*Bir sporcunun antrenman boyunca her saniye nabzını ve hızını kağıda alt alta kaydettiği kronometreli bir defter tutması gibidir.*

## Nasıl çalışır?

Sistemler belirli aralıklarla durum raporu gönderir ve bu veritabanı bu raporları zamana göre sıralı bir şekilde diskine yazar. Sorgulama yaparken geçmişe dönük trendleri ve anlık değişimleri çok hızlı bir şekilde grafikleştirmenize olanak tanır.

## Nerede kullanılır?

Sunucu performans izleme araçlarında, borsa veri akışlarında ve akıllı ev sensör sistemlerinde kullanılır.

## Sık karıştırılanlar

İlişkisel veritabanlarıyla karıştırılabilir; ilişkisel veritabanları anlık durumları güncellerken bu sistemler zaman içindeki tüm geçmişi biriktirir.

## Sorular ve yanıtlar

**Neden normal bir veritabanı bu iş için kullanılmıyor?**

Normal veritabanları zamanla biriken devasa veri yığınları altında yavaşlar, oysa bu sistemler zaman verisini çok hızlı işlemek üzere tasarlanmıştır.

**Eski veriler siliniyor mu?**

Genellikle belirli bir süreden sonra eski veriler otomatik olarak özetlenir veya diskten temizlenir.

## İlgili terimler

- [Database](https://trescout.com/dictionary/database/)
- [Monitoring Tool](https://trescout.com/dictionary/monitoring-tool/)
- [Data Processing](https://trescout.com/dictionary/data-processing/)

## İlgili araçlar

- [Prometheus](https://trescout.com/discover/prometheus/)

Bu açıklama TreScout için yapay zekâ ile sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/time-series-database/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
