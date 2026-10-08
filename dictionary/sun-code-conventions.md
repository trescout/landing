# Sun Code Conventions nedir, ne demek?

*Sözlük · Geliştirme · Son güncelleme: 20 Eylül 2026*

Sun Code Conventions for the Java Programming Language, 1997 yılında Java'nın yaratıcısı Sun Microsystems tarafından yayınlanan ve yazılım mühendisliği tarihindeki ilk kurumsal kodlama standartları belgesidir.

## Etimoloji ve Yazılım Mühendisliği Mirası

Sun Code Conventions, yazılım geliştirme tarihinde bir programlama dilinin yaratıcısı tarafından yayınlanmış en etkili stil ve mimari kılavuzlarından biridir. 1995 yılında Sun Microsystems tarafından tanıtılan Java dili, "Write Once, Run Anywhere" (Bir Kere Yaz, Her Yerde Çalıştır) mottosuyla platform bağımsızlığını hedeflerken, bu hedefin insan faktöründeki karşılığı da Sun Code Conventions ile formüle edilmiştir: "Herkes Aynı Standartta Okusun ve Anlasın."

1997 yılında taslağı hazırlanan ve 1999 yılında nihai sürümüne ulaşan bu belge, C ve C++ ekosistemindeki parantez savaşları ve kontrolsüz gösterici (pointer) karmaşasından sonra kurumsal yazılım dünyasına tertemiz bir disiplin getirmiştir. Sun Microsystems'ın bu belgede vurguladığı "Bir yazılımın yaşam döngüsü maliyetinin yüzde 80'i bakım aşamasında harcanır ve neredeyse hiçbir yazılım tüm ömrü boyunca ilk yazarı tarafından korunmaz" tespiti, modern temiz kod (Clean Code) hareketinin de temel aforizması haline gelmiştir.

*Şöyle düşünün: Farklı ülkelerden gelen ve ortak bir mimari şaheser inşa etmek isteyen yüzlerce inşaat mühendisi hayal edin. Eğer her mühendis kendi ülkesinin ölçü birimini (inç, santimetre, arşın) kullanır ve kendi çizim sembollerini tercih ederse, kolonlar birbirini tutmaz ve bina çöker. Sun Code Conventions, Java dünyasının ortak metrik sistemi ve mimari alfabe standardıdır. Hangi ülkeden veya şirketten olursa olsun, bir Java mühendisinin yazdığı sınıf dosyasını açan bir başka mühendis, kolonların ve kirişlerin (sınıfların ve metotların) nereye yerleştirildiğini bir bakışta anlar.*

## Teknik Standartlar ve Belgenin Anatomisi

- **Kaynak Dosya Düzeni ve 80 Karakter:** Her dosya tek bir public sınıf içerir. 80 karakter sınırı dönemin terminal ve çıktı yazıcıları için konulmuştur.

- **Dört Boşluk (4-Space) Girintileme:** Standart girinti 4 boşluktur. Parantezler K&R stiline göre satır sonuna konulur; tek satırlık koşullarda bile parantez zorunludur.

- **İsimlendirme Konvansiyonlarının Doğuşu (CamelCase):** Sınıflar `UpperCamelCase`, metotlar `lowerCamelCase` ile yazılır. Ters alan adı (`com.sun.*`) paket isimlendirmesi ilk bu belgeyle kurala bağlanmıştır.

- **Tarihsel Dondurulma ve Miras:** Belge 1999'da dondurulmuş; modern dönemde bayrağı Google Java Style Guide ve modern linter araçlarına devretmiştir.

## Sosyolojik Boyut: Kolektif Disiplin ve Bakım Kültürü

Sun Code Conventions, yazılımın salt bir deha ürünü değil, kolektif bir endüstriyel mühendislik disiplini olduğunu tescilleyen tarihi bir dönüm noktasıdır. Bireysel programcının "benim tarzım böyle" inadını kırarak, yazılımı okunabilirlik ve sürdürülebilirlik eksenine oturtmuştur.

Bugün finans, bankacılık ve kamu altyapılarında çalışan milyonlarca satırlık miras (legacy) Java projesi, hâlâ Sun Microsystems'ın 1997'de koyduğu bu kurallar sayesinde ayakta durmaktadır. Modern araçlar değişse de Sun'ın kurduğu mantıksal iskelet, yazılım mühendisliğinin kültürel mirasıdır.

## Sık Yapılan Hatalar ve Tarihsel Yanılgılar

- **80 Karakter Sınırında İnat Etmek:** Geniş ekranlarda 80 karakter kuralını katı uygulamak kodu gereksiz dikeyde böler; modern 100-120 karakter standartları benimsenmelidir.

- **Dondurulmuş Belgeyi Güncel Sanmak:** 1999'dan beri güncellenmeyen Sun kılavuzunu modern projelerde tek kaynak almak teknik borç yaratır.

- **Koşullarda Parantezi Unutmak:** Tek satırlık gövdelerde parantez koymamak ileride güvenlik açıklarına yol açabilir.

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

- [Google Java Style Guide](https://trescout.com/dictionary/google-java-style-guide/)
- [Code Snippets](https://trescout.com/dictionary/code-snippets/)
- [Refactoring](https://trescout.com/dictionary/refactoring/)
- [QA](https://trescout.com/dictionary/qa/)
- [Syntax](https://trescout.com/dictionary/syntax/)

## İlgili araçlar

- [Checkstyle](https://trescout.com/discover/checkstyle/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/sun-code-conventions/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
