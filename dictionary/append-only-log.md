# Append-only log nedir, ne demek?

**Kategori:** Veri & Altyapı  
**Son güncelleme:** 2026-09-20

Append-only log (yalnızca ekleme yapılabilen kütük), verilerin asla yerinde değiştirilmediği veya silinmediği, her yeni işlemin dosyanın sonuna kronolojik sırayla eklendiği değişmez (immutable) bir veri yapısı mimarisidir.

## Etimoloji ve Değişmezlik Paradigması
Append-only log kavramı, geleneksel veritabanlarının "yerinde güncelleme" (update-in-place) paradigmasına köklü bir alternatif olarak geliştirilmiştir. Klasik veritabanlarında bir bakiye veya profil güncellendiğinde diskteki eski veri silinerek üzerine yeni değer yazılır. Bu yaklaşım, sistem çökmesinde yarım kalan yazmaların veriyi bozması, kilitlenme darboğazları ve rastgele disk erişimi (random I/O) nedeniyle ciddi güvenilirlik sorunları yaratır.

Append-only log mimarisinde ise geçmiş kutsaldır ve tahrif edilemez. Bir banka hesabı bakiyesini doğrudan değiştirmek yerine, her para yatırma ve çekme hareketi günlüğün sonuna yeni bir kayıt olarak eklenir. Sistemin geçerli durumu (state), geçmişten bugüne eklenen tüm bu olayların kronolojik olarak sırayla yürütülmesinin (fold/reduce) doğal bir sonucudur. Bu prensip, modern dağıtık sistemlerin, yüksek performanslı depolama motorlarının ve blokzincir ağlarının omurgasını oluşturur.

## Bir Benzetmeyle: Muhasebecinin Yevmiye Defteri
Şöyle düşünün: Bir muhasebecinin tuttuğu resmi yevmiye defterini hayal edin. Muhasebeci bir satırda hata yaptığında önceki sayfaları açıp daksille eski sayıyı silemez. Bunun yerine defterin en son boş satırına hatayı düzelten yeni bir ters kayıt satırı ekler. Defter yalnızca ileriye doğru büyür, geçmiş asla değiştirilmez; paranın ne zaman ve nasıl hareket ettiği geriye dönük denetlenebilir. Append-only log tam olarak bu dijital defterdir; veriyi anlık fotoğraf değil, yaşayan bir tarihçe olarak kaydeder.

## Teknik Derinlik ve Sistem Mimarisi
Teknik düzeyde append-only log mimarisi, donanım optimizasyonları ve veri tutarlılığı açısından üç ana temel üzerine kuruludur:

1. **Sıralı Disk Erişimi (Sequential I/O) ve WAL:** Manyetik diskler (HDD) ve hatta modern katı hal sürücüleri (SSD/NVMe), rastgele adreslere yazmaktan ziyade ardışık bloklara yazarken katbekat daha yüksek verimle çalışır. PostgreSQL, MySQL ve SQLite gibi veritabanları bu nedenle Write-Ahead Logging (WAL) kullanır. Bir işlem (transaction) geldiğinde önce diske ardışık olarak bir append-only log satırı yazılır ve fsync edilir. Bu sayede sunucunun elektriği aniden kesilse bile, yeniden başlatmada log baştan okunarak veri tabanı tam tutarlı haline saniyeler içinde döndürülür.

2. **LSM-Tree ve Veri Birleştirme (Compaction):** RocksDB, Apache Cassandra ve Bigtable gibi yüksek yazma yoğunluklu NoSQL motorları Log-Structured Merge-Tree (LSM-Tree) mimarisini kullanır. Gelen tüm veriler önce bellekteki sıralı bir yapıya (MemTable) ve eşzamanlı bir append-only günlüğe eklenir. MemTable dolduğunda diske değişmez SSTable dosyaları olarak dökülür. Zamanla biriken eski veya geçersiz veriler arkaplanda çalışan birleştirme (compaction) işlemleriyle temizlenir.

3. **Olay Kaynakları (Event Sourcing) ve Dağıtık Akış (Kafka):** Mikroservis mimarilerinde Apache Kafka ve Redpanda gibi dağıtık mesajlaşma platformları devasa birer dağıtık append-only log gibi çalışır. Uygulama durumları veritabanında saklanmak yerine, üretilen olaylar (events) değişmez kütüklere yazılır. Farklı servisler bu kütüğü kendi hızlarında tüketerek kendi yerel durumlarını oluşturur.

4. **Kriptografik Değişmezlik ve Blokzincir:** Bitcoin ve Ethereum gibi dağıtık defter teknolojileri (DLT), her bloğun önceki bloğun kriptografik özetini (hash) içerdiği dağıtık birer append-only log kütüğüdür. Ağdaki hiçbir düğüm geçmiş blokları değiştiremez; yalnızca konsensüs kurallarına uygun yeni bloklar kütüğün sonuna eklenebilir.

## Sosyolojik Boyut: Dijital Hafıza ve Denetim İzi
Append-only log, salt bir yazılım deseni olmanın ötesinde, dijital hesap verebilirlik ve şeffaflık felsefesini temsil eder. Kurumsal dünyada ve kamu yönetiminde "kimin, neyi, ne zaman değiştirdiği" sorusunun tahrif edilemez bir kesinlikle yanıtlanabilmesi, güven krizlerinin önüne geçen en kritik emniyet supabıdır.

Geleneksel sistemlerde veritabanı yöneticisinin tek bir SQL komutuyla geçmişi silip yeniden yazabilmesi kurumsal hafızayı kırılganlaştırır. Append-only sistemler ise geçmişin yeniden yazılamayacağını garanti ederek insan hatasına, iç tehditlere ve yetki suistimallerine karşı matematiksel bir dokunulmazlık kalkanı örer.

## Sık Yapılan Hatalar ve Yanılgılar
Append-only log sistemleri tasarlanırken en sık yapılan mimari hatalar şunlardır:
- **Disk Tüketimini Öngörmemek:** Logların yalnızca büyüdüğü unutularak uygun veri saklama (retention) ve sıkıştırma (compaction) stratejileri kurulmazsa disk alanı hızla tükenir.
- **Okuma Performansını İhmal Etmek:** Son durumu hesaplamak için milyonlarca satırlık kütüğü baştan sona taramak (replay) okuma sürelerini felç eder; düzenli durum anlık görüntüleri (snapshots) alınmalıdır.
- **GDPR Unutulma Hakkını Göz Ardı Etmek:** Kişisel verilerin korunması kanunları silme hakkı talep ettiğinde, değişmez loglardan veri silmek mimariyi zorlar; bu sorun şifreleme anahtarının silinmesiyle verinin anlamsızlaştırıldığı kripto-imha (crypto-shredding) yöntemiyle çözülmelidir.

## Sıkça Sorulanlar

**Append-only log mimarisi neden yerinde güncelleme (update-in-place) modeline göre daha hızlıdır?**  
Diskte rastgele blok aramak yerine veriyi her zaman dosyanın sonuna sıralı olarak yazmak (sequential write), disk kafası hareketini ve I/O gecikmesini en aza indirerek çok yüksek yazma hızları sağlar.

**Append-only log sonsuza kadar büyürse disk alanı nasıl yönetilir?**  
Sistemler belirli aralıklarla mevcut durumun anlık görüntüsünü (snapshot) alır ve arkaplanda birleştirme (compaction) ya da segment temizleme süreçleri çalıştırarak eski logları güvenle siler veya arşivler.

**Dağıtık sistemlerde ve Apache Kafka'da append-only log nasıl kullanılır?**  
Kafka konuları (topics), mesajların kronolojik sırayla eklendiği bölünmüş (partitioned) birer append-only logdur; birden fazla tüketici bağımsız ofset değerleriyle kütüğü kayıpsız ve yüksek hızda okur.

**GDPR unutulma hakkı append-only log tutan sistemlerde nasıl uygulanır?**  
Değişmez kütükteki kullanıcı verileri özel bir anahtarla şifrelenir; kullanıcı silinme talep ettiğinde yalnızca o kullanıcının şifreleme anahtarı imha edilerek (crypto-shredding) kütük bozulmadan veriler okunamaz hale getirilir.

## İlgili terimler
- [Distributed](/dictionary/distributed/)
- [Serialization](/dictionary/serialization/)
- [Local](/dictionary/local/)
- [Self-hosted](/dictionary/self-hosted/)
- [Runtime](/dictionary/runtime/)
- [Memory Management](/dictionary/memory-management/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/append-only-log/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
