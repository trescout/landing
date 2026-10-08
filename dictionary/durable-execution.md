# Durable Execution nedir?

*Sözlük · Geliştirme · Son güncelleme: 8 Haziran 2026*

Bir işlemin, hata veya kesinti olsa bile kaldığı yerden güvenle devam etmesini sağlayan sistemdir.

## Tanım

Normalde bir bilgisayar programı çalışırken elektrik kesilirse veya hata verirse, her şey silinir ve baştan başlamanız gerekir. Durable execution, programın her adımını kaydederek, kesinti anında kaldığı noktayı hatırlar. Bu sayede saatler süren işlemler güvenle tamamlanabilir.

*Bir kitap okurken sayfayı unutmamak için ayraç koymak gibidir; kaldığınız yerden devam edebilirsiniz.*

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

- [State Management](https://trescout.com/dictionary/state-management/)
- [Runtime](https://trescout.com/dictionary/runtime/)

## İlgili araçlar

- [Pg Durable](https://trescout.com/discover/pg-durable/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/durable-execution/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
