# Thread-safety nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-07-27

Bir programın aynı anda birden fazla işlem yaparken verilerin bozulmasını engelleyen güvenlik özelliği.

## Tanım
Bilgisayarlar aynı anda birçok iş yapar. Eğer iki farklı işlem aynı veriyi aynı anda değiştirmeye çalışırsa kaos çıkar. Bu özellik, işlemlerin birbirini beklemesini veya sırayla çalışmasını sağlar.

## Bir benzetmeyle
Tek bir tuvaletin olduğu bir evde, kapıya kilit takmak gibidir; biri içerideyken diğeri beklemek zorundadır.

## Nasıl çalışır?
Program yazılırken veriye erişim kuralları belirlenir. Bir işlem veriyi kullanırken diğerleri ona 'kilitli' statüsünde görünür.

## Nerede kullanılır?
Bankacılık uygulamaları, web sunucuları ve çoklu işlem yapan tüm yazılımlarda zorunludur.

## Sık karıştırılanlar
Sadece güvenlik (hacklenme) ile ilgili değildir, veri tutarlılığı ile ilgilidir.

## Sıkça sorulanlar

**Thread-safe olmazsa ne olur?**  
Verileriniz karışır, uygulamalar çöker veya yanlış hesaplamalar oluşur.

## İlgili terimler
- [Concurrency](/dictionary/concurrency/)
- [System Programming Language](/dictionary/system-programming-language/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/thread-safety/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
