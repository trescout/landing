# Sun Code Conventions nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-20

Sun Code Conventions for the Java Programming Language, 1997 yılında Java'nın yaratıcısı Sun Microsystems tarafından yayınlanan ve yazılım mühendisliği tarihindeki ilk kurumsal kodlama standartları belgesidir.

## Etimoloji ve Yazılım Mühendisliği Mirası
Sun Code Conventions, yazılım geliştirme tarihinde bir programlama dilinin yaratıcısı tarafından yayınlanmış en etkili stil ve mimari kılavuzlarından biridir. 1995 yılında Sun Microsystems tarafından tanıtılan Java dili, "Write Once, Run Anywhere" (Bir Kere Yaz, Her Yerde Çalıştır) mottosuyla platform bağımsızlığını hedeflerken, bu hedefin insan faktöründeki karşılığı da Sun Code Conventions ile formüle edilmiştir: "Herkes Aynı Standartta Okusun ve Anlasın."

1997 yılında taslağı hazırlanan ve 1999 yılında nihai sürümüne ulaşan bu belge, C ve C++ ekosistemindeki parantez savaşları ve kontrolsüz gösterici (pointer) karmaşasından sonra kurumsal yazılım dünyasına tertemiz bir disiplin getirmiştir. Sun Microsystems'ın bu belgede vurguladığı "Bir yazılımın yaşam döngüsü maliyetinin yüzde 80'i bakım aşamasında harcanır ve neredeyse hiçbir yazılım tüm ömrü boyunca ilk yazarı tarafından korunmaz" tespiti, modern temiz kod (Clean Code) hareketinin de temel aforizması haline gelmiştir.

## Bir Benzetmeyle: Java Dünyasının Ortak Metrik Sistemi
Şöyle düşünün: Farklı ülkelerden gelen ve ortak bir mimari şaheser inşa etmek isteyen yüzlerce inşaat mühendisi hayal edin. Eğer her mühendis kendi ülkesinin ölçü birimini (inç, santimetre, arşın) kullanır ve kendi çizim sembollerini tercih ederse, kolonlar birbirini tutmaz ve bina çöker. Sun Code Conventions, Java dünyasının ortak metrik sistemi ve mimari alfabe standardıdır. Hangi ülkeden veya şirketten olursa olsun, bir Java mühendisinin yazdığı sınıf dosyasını açan bir başka mühendis, kolonların ve kirişlerin (sınıfların ve metotların) nereye yerleştirildiğini bir bakışta anlar.

## Teknik Standartlar ve Belgenin Anatomisi
Sun Code Conventions belgesinin getirdiği ve bugün hâlâ Java ekosisteminin genetiğini oluşturan temel teknik standartlar şunlardır:

1. Kaynak Dosya Düzeni ve 80 Karakter Kuralı:
- Her Java kaynak dosyası tek bir public sınıf veya arayüz barındırır.
- Dosya bölümleri kesin bir hiyerarşiyi takip eder: Başlangıç lisans yorumları, paket bildirimi (`package`), içe aktarmalar (`import`), sınıf Javadoc'u ve sınıf gövdesi.
- Satır uzunluğu kesinlikle 80 karakteri aşamaz; bu kural dönemin CRT monitörleri, terminal pencereleri ve kod çıktısı alan nokta vuruşlu yazıcıların sınırları nedeniyle getirilmiştir.

2. Dört Boşluk (4-Space) ve Sekme Kuralı:
- Girintileme birimi tam olarak dört (4) boşluktur. Sekme (tab) genişliği de 8 boşluk olarak kabul edilmiş; kodun farklı editörlerde kaymasını önlemek için standart boşluklar önerilmiştir.
- Blok parantezleri (curly braces) Kernighan and Ritchie (K&R) kuralına göre satır sonuna yerleştirilir; tek satırlık `if` veya `while` gövdelerinde dahi parantez kullanımı zorunlu tutulmuştur.

3. İsimlendirme Konvansiyonlarının Doğuşu (CamelCase):
- Sınıflar ve arayüzler isim olmalı ve `UpperCamelCase` ile yazılmalıdır (`Raster`, `ImageSprite`).
- Metotlar fiil olmalı ve `lowerCamelCase` ile yazılmalıdır (`run()`, `getBackground()`).
- Paket isimleri dünya genelinde çakışmaları önlemek için ters alan adı kuralına (`com.sun.media`, `org.apache.commons`) bağlanmıştır.
- Sabitler tamamen büyük harfle yazılır (`MIN_PRIORITY`).

4. Belgenin Dondurulması ve Mirası:
- Belge 1999 yılından sonra resmi olarak güncellenmemiş (dondurulmuş) ve Oracle'ın Sun Microsystems'ı satın almasından sonra bir miras dokümanı olarak kalmıştır. Bayrak daha sonra Google Java Style Guide ve Spring Framework Conventions gibi modern rehberlere devredilmiştir.

## Sosyolojik Boyut: Kolektif Disiplin ve Bakım Kültürü
Sun Code Conventions, yazılımın salt bir deha ürünü değil, kolektif bir endüstriyel mühendislik disiplini olduğunu tescilleyen tarihi bir dönüm noktasıdır. Bireysel programcının "benim tarzım böyle" inadını kırarak, yazılımı okunabilirlik ve sürdürülebilirlik eksenine oturtmuştur.

Bugün finans, bankacılık ve kamu altyapılarında çalışan milyonlarca satırlık miras (legacy) Java projesi, hâlâ Sun Microsystems'ın 1997'de koyduğu bu kurallar sayesinde ayakta durmaktadır. Modern araçlar değişse de Sun'ın kurduğu mantıksal iskelet, yazılım mühendisliğinin kültürel mirasıdır.

## Sık Yapılan Hatalar ve Tarihsel Yanılgılar
Sun Code Conventions bağlamında yapılan tarihsel ve pratik yanılgılar şunlardır:
- 80 Karakter Sınırında İnat Etmek: Günümüz geniş ekranlarında 80 karakter kuralını katı şekilde uygulamak kodu gereksiz yere dikeyde parçalar; modern projeler 100 veya 120 karakteri benimsemelidir.
- Dondurulmuş Bir Belgeyi Yeni Projelerde Güncel Sanmak: 1999'dan beri güncellenmeyen Sun kılavuzunu yeni projelerde Google Style veya modern statik analiz araçları yerine birincil kaynak almak hatalıdır.
- Tek Satırlık Koşullarda Parantezi Unutmak: Sun kılavuzu `if (condition) doSomething();` yazımını kesinlikle yasaklar; parantez koymamak ileride güvenlik açıklarına (Apple goto fail hatası gibi) yol açar.

## Sıkça Sorulanlar

**Sun Code Conventions neden 1999 yılından sonra güncellenmemiştir?**  
Sun Microsystems temel standartları belirledikten sonra biçimlendirme kurallarının topluluk ve açık kaynak araçları (Checkstyle vb.) tarafından yönetilmesini tercih etmiş ve dokümanı tarihsel referans olarak dondurmuştur.

**Sun Code Conventions'taki 80 karakter sınırı nereden kaynaklanmaktadır?**  
1990'lı yılların UNIX terminal ekranları, 80 sütunluk punch kart mirası ve kod incelemelerinde kullanılan çıktı yazıcılarının standart genişliği nedeniyle bu sınır belirlenmiştir.

**Modern Java projelerinde Sun kuralları yerine ne kullanılmalıdır?**  
Günümüz projelerinde 2 boşluklu Google Java Style Guide veya Spring Framework kodlama standartları ile Spotless ve google-java-format gibi otomatik araçlar tercih edilmektedir.

**Ters alan adı (reverse domain name) paket isimlendirmesini ilk kim zorunlu kılmıştır?**  
Sun Microsystems, Java sınıflarının küresel ölçekte isim çakışması yaşamasını engellemek için 'com.sun' veya 'org.apache' gibi ters alan adı standardını Sun Code Conventions ile getirmiştir.

## İlgili terimler
- [Google Java Style Guide](/dictionary/google-java-style-guide/)
- [Code Snippets](/dictionary/code-snippets/)
- [Refactoring](/dictionary/refactoring/)
- [QA](/dictionary/qa/)
- [Syntax](/dictionary/syntax/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/sun-code-conventions/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
