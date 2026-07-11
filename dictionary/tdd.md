# TDD nedir?

> Test-Driven Development

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-07-11

Önce yazılacak kodun testini hazırlayıp, ardından bu testi geçecek kadar kod yazmayı esas alan geliştirme yöntemidir.

## Tanım
TDD, 'önce test, sonra kod' felsefesine dayanır. Önce kodun ne yapması gerektiğini tanımlayan bir test yazarsınız; doğal olarak bu test başarısız olur çünkü henüz kod yoktur. Ardından testi geçecek en basit kodu yazarsınız. Bu döngü, yazılımın her adımda hatasız olmasını sağlar.

## Bir benzetmeyle
Bir sınavı hazırlayan öğretmenin, önce cevap anahtarını oluşturması ve ardından öğrencilerin bu anahtara göre başarılı olmasını beklemesi gibidir.

## Nasıl çalışır?
Üç aşamalı döngü: 1. Test yaz (Başarısız olur), 2. Kodu yaz (Testi geçer), 3. Kodu temizle (Refactor). Bu süreç sürekli tekrar eder.

## Nerede kullanılır?
Modern yazılım geliştirme ekiplerinde, özellikle güvenliğin ve kalitenin ön planda olduğu projelerde uygulanır.

## Sık karıştırılanlar
Unit Testing ile karıştırılabilir; TDD bir yöntemdir, Unit Testing ise bu yöntemin kullandığı bir araçtır.

## Sıkça sorulanlar

**TDD zaman kaybettirmez mi?**  
Başlangıçta yavaşlatıyor gibi görünse de, ileride hata ayıklama süresini kısalttığı için toplamda zaman kazandırır.

## İlgili terimler
- [Unit Testing](/dictionary/unit-testing/)
- [Testing Framework](/dictionary/testing-framework/)
- [Clean Code](/dictionary/clean-code/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/tdd/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
