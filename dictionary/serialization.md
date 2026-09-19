# Serialization nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Serialization (serileştirme), bir programlama dilinin çalışma belleğinde (RAM) tutulan karmaşık nesneleri ve veri yapılarını, depolanabilir veya ağ üzerinden iletilebilir düz bir bayt dizisi ya da metin formatına dönüştürme işlemidir.

## Tanım
Bilgisayarın belleğinde dinamik ve karmaşık bir şekilde tutulan nesneleri (örneğin bir kullanıcı profili, oturum verisi veya oyun durumu), internet üzerinden göndermek ya da bir dosyaya/veritabanına kaydetmek için düz bir akışa çevirmeniz gerekir. Bu işleme serileştirme (serialization) denir. Karşı taraf bu veriyi aldığında ise **deserialization (ters serileştirme)** yaparak tekrar canlı bellek nesnesine kavuşturur.

## Serialization ne demek ve nasıl çalışır?
Bellekteki nesneler genellikle dağınık bellek adreslerine ve referanslara (pointers) sahiptir. Başka bir sunucu veya program bu yerel bellek adreslerini doğrudan okuyamaz. Serialization işlemi, bu hiyerarşik nesne ağacını doğrusal (linear) bir biçime sokar.

## En yaygın serileştirme formatları
- **JSON (JavaScript Object Notation):** Web API'lerinin, REST servislerinin ve modern web uygulamalarının fiili standardıdır; insanlar tarafından kolayca okunabilir.
- **Protocol Buffers (Protobuf):** Google tarafından geliştirilen, mikroservisler (gRPC) arasında inanılmaz hız ve düşük ağ bant genişliği sunan kompakt ikili (binary) formattır.
- **MessagePack & BSON:** JSON benzeri anahtar-değer yapılarını ikili formatta hızlandıran ve sıkıştıran çözümlerdir.
- **YAML & XML:** İnsan tarafından okunabilir yapılandırma dosyalarında ve eski kurumsal sistem entegrasyonlarında tercih edilir.
- **Dile Özgü Formatlar:** Python'daki `pickle` veya Java nesne serileştirme kütüphaneleri (güvenlik açıklarına dikkat edilmelidir).

## Bir benzetmeyle
Bir mobilyayı taşımak için parçalarına ayırıp düz ve yassı bir kutuya yerleştirmek gibidir; varış noktasında kutuyu açıp kılavuza bakarak mobilyayı tekrar kurarsınız (deserialization).

## Güvenlik boyutu: Deserialization zaafiyetleri
Güvenilmeyen veya dış kaynaklardan gelen serileştirilmiş verilerin kontrolsüzce deserialization işlemine tabi tutulması, uzaktan kod çalıştırma (RCE) açıklarına yol açabilir. Bu nedenle modern yazılımlarda çalıştırılabilir kod içeren serileştirme yerine, sıkı şema doğrulaması (schema validation) sunan JSON veya Protobuf tercih edilir.

## Sıkça sorulanlar

**Neden serileştirmeye ihtiyaç duyarız?**  
Bilgisayarın belleğindeki veriler geçicidir ve sadece o sürece özeldir. Başka bir bilgisayara, mikroservise veya kalıcı diske veri göndermek için onu evrensel bir akışa çevirmek gerekir.

**JSON ile Protocol Buffers arasındaki temel fark nedir?**  
JSON insan tarafından okunabilir ve esnektir; Protobuf ise ikili (binary) formatta sıkıştırılmış olup şema bağımlıdır, çok daha az yer kaplar ve katbekat hızlı serileştirilir.

## İlgili terimler
- [API](/dictionary/api/)
- [Data Pipeline](/dictionary/data-pipeline/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/serialization/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
