# Vector Database nedir?

**Kategori:** Veri & Altyapı  
**Son güncelleme:** 2026-06-03

Yapay zekanın verileri anlamlarına göre hızlıca bulabilmesi için saklandığı özel bir veritabanı türüdür.

## Tanım
Vektör veritabanı, verileri geleneksel satır ve sütunlar yerine anlamlarını temsil eden sayısal vektörler olarak saklayan özel bir depolama sistemidir. Bu yapı, yapay zekanın milyonlarca veri arasından en alakalı olanı milisaniyeler içinde bulmasını sağlar.

## Bir benzetmeyle
Şöyle düşünün: Geleneksel veritabanı bir kütüphanedeki alfabetik katalog gibidir. Vektör veritabanı ise bir insanın zihnindeki kavram haritası gibidir; bir fikri düşündüğünüzde onunla ilişkili tüm anılarınızın aynı anda aklınıza gelmesi gibi çalışır.

## Nasıl çalışır?
Önce veriler embedding yöntemiyle sayısal vektörlere dönüştürülür. Sorgu yapıldığında veritabanı, sorgunun vektörü ile verilerin vektörleri arasındaki mesafeyi ölçer. En kısa mesafeye sahip olanlar, yani anlamca en yakın olanlar sonuç olarak getirilir.

## Nerede kullanılır?
Akıllı arama sistemlerinde, öneri motorlarında ve yapay zekanın uzun süreli hafızasını oluşturduğu RAG sistemlerinde kullanılır.

## Sık karıştırılanlar
SQL gibi klasik veritabanları ile karıştırılır, ancak klasik veritabanları tam eşleşme ararken vektör veritabanları benzerlik arar.

## Sıkça sorulanlar

**Klasik veritabanlarından daha mı yavaştır?**  
Hayır, çok büyük veri setlerinde benzerlik araması yapmak için klasik yöntemlerden çok daha hızlıdır.

**Hangi veriler saklanabilir?**  
Metin, görsel, ses veya video gibi anlamı vektöre dönüştürülebilen her türlü veri saklanabilir.

## İlgili terimler
- [Embedding](/dictionary/embedding/)
- [RAG](/dictionary/rag/)
- [Knowledge Graph](/dictionary/knowledge-graph/)
- [Memory Engine](/dictionary/memory-engine/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/vector-database/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
