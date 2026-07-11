# Serialization nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-07-11

Karmaşık veri yapılarını, depolanabilir veya iletilebilir düz bir metin veya bayt dizisine dönüştürme işlemidir.

## Tanım
Bilgisayarın belleğinde karmaşık bir şekilde tutulan nesneleri (örneğin bir kullanıcı profili), internet üzerinden göndermek veya bir dosyaya kaydetmek için düz bir satıra çevirmeniz gerekir. Bu işleme serileştirme denir. Karşı taraf bu veriyi aldığında ise 'deserialization' yaparak tekrar eski karmaşık yapısına kavuşturur.

## Bir benzetmeyle
Bir mobilyayı taşımak için parçalarına ayırıp düz bir kutuya yerleştirmek gibidir; varış noktasında kutuyu açıp mobilyayı tekrar kurarsınız.

## Nasıl çalışır?
Veri genellikle JSON, XML veya daha hızlı olan ikili formatlara (Binary) dönüştürülür. Bu sayede verinin orijinal yapısı korunarak farklı sistemler arasında taşınabilir hale gelir.

## Nerede kullanılır?
API iletişimlerinde, veritabanı kayıtlarında ve oyunlarda kayıt dosyası oluştururken kullanılır.

## Sıkça sorulanlar

**Neden serileştirmeye ihtiyaç duyarız?**  
Bilgisayarın belleğindeki veriler sadece o anki program için anlamlıdır. Başka bir bilgisayara veya diske veri göndermek için onu evrensel bir formata çevirmemiz gerekir.

## İlgili terimler
- [API](/dictionary/api/)
- [Data Pipeline](/dictionary/data-pipeline/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/serialization/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
