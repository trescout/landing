# Logging nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-08-06

Bir programın çalışırken yaptığı işlemleri veya karşılaştığı hataları takip etmek için kronolojik olarak kayıt altına almasıdır.

## Tanım
Programlar bazen sessizce hata verir. Logging sayesinde, bir hata oluştuğunda programın o ana kadar ne yaptığını, hangi veriyi işlediğini adım adım görebilirsiniz. Bu, bir nevi programın 'kara kutusu'dur.

## Bir benzetmeyle
Bir uçağın uçuş sırasında tüm verilerini kaydeden kara kutusu gibi, programın da tüm hareketlerini günlüğüne işlemesidir.

## Nasıl çalışır?
Kodun içine 'buraya gelindi', 'şu veri işlendi' gibi komutlar eklersiniz. Program çalıştıkça bu bilgiler bir dosyaya veya izleme sistemine yazılır.

## Nerede kullanılır?
Sunucu uygulamalarında, büyük yazılım sistemlerinde ve hata ayıklama süreçlerinde kullanılır.

## Sık karıştırılanlar
Observability ile karıştırılabilir; logging bu gözlemlenebilirliğin temel yapı taşlarından biridir.

## Sıkça sorulanlar

**Her şeyi kaydetmek iyi midir?**  
Hayır, çok fazla kayıt sistemi yavaşlatabilir ve önemli hataları bulmayı zorlaştırabilir; dengeli kayıt tutulmalıdır.

## İlgili terimler
- [Observability](/dictionary/observability/)
- [Traces](/dictionary/traces/)
- [Logs](/dictionary/logs/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/logging/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
