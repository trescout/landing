# TDD nedir?

*Sözlük · Geliştirme · Son güncelleme: 11 Temmuz 2026*

> Test-Driven Development

Önce yazılacak kodun testini hazırlayıp, ardından bu testi geçecek kadar kod yazmayı esas alan geliştirme yöntemidir.

## Tanım

TDD, 'önce test, sonra kod' felsefesine dayanır. Önce kodun ne yapması gerektiğini tanımlayan bir test yazarsınız; doğal olarak bu test başarısız olur çünkü henüz kod yoktur. Ardından testi geçecek en basit kodu yazarsınız. Bu döngü, yazılımın her adımda hatasız olmasını sağlar.

*Bir sınavı hazırlayan öğretmenin, önce cevap anahtarını oluşturması ve ardından öğrencilerin bu anahtara göre başarılı olmasını beklemesi gibidir.*

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

- [Unit Testing](https://trescout.com/dictionary/unit-testing/)
- [Testing Framework](https://trescout.com/dictionary/testing-framework/)
- [Clean Code](https://trescout.com/dictionary/clean-code/)

## İlgili araçlar

- [Catch2](https://trescout.com/discover/catch2/)
- [Everything Claude Code](https://trescout.com/discover/everything-claude-code/)
- [Babysitter](https://trescout.com/discover/babysitter/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/tdd/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
