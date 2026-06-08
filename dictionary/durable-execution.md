# Durable Execution nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-06-08

Bir işlemin, hata veya kesinti olsa bile kaldığı yerden güvenle devam etmesini sağlayan sistemdir.

## Tanım
Normalde bir bilgisayar programı çalışırken elektrik kesilirse veya hata verirse, her şey silinir ve baştan başlamanız gerekir. Durable execution, programın her adımını kaydederek, kesinti anında kaldığı noktayı hatırlar. Bu sayede saatler süren işlemler güvenle tamamlanabilir.

## Bir benzetmeyle
Bir kitap okurken sayfayı unutmamak için ayraç koymak gibidir; kaldığınız yerden devam edebilirsiniz.

## Nasıl çalışır?
Sistem, programın durumunu (state) sürekli bir veritabanına yedekler. Bir hata oluştuğunda sistem, son yedeklenen noktadan itibaren işlemi yeniden başlatır.

## Nerede kullanılır?
Banka transferleri, uzun süren veri işleme süreçleri ve karmaşık yapay zekâ iş akışlarında kullanılır.

## Sık karıştırılanlar
Otomatik kaydetme ile karıştırılabilir, ancak bu sadece dosya değil, programın çalışma mantığının tamamını korur.

## Sıkça sorulanlar

**Her program durable olmalı mı?**  
Kısa işlemler için gerek yoktur, ancak saatler süren kritik işlemler için şarttır.

**Neden bu kadar önemli?**  
Hatalı bir durumda tüm süreci baştan başlatmak hem zaman hem de para kaybıdır.

## İlgili terimler
- [State Management](/dictionary/state-management/)
- [Runtime](/dictionary/runtime/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/durable-execution/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
