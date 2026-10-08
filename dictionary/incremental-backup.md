# Incremental Backup nedir?

*Sözlük · Veri & Altyapı · Son güncelleme: 12 Haziran 2026*

Sadece en son yedeklemeden sonra değişen dosyaları kaydederek zamandan ve alandan tasarruf eden yedekleme yöntemidir.

## Tanım

Artımlı yedekleme, her seferinde tüm veriyi kopyalamak yerine sadece son değişiklikleri tespit eder ve bunları ekler. Bu yöntem, yedekleme süresini ciddi oranda kısaltır ve depolama alanını verimli kullanmanızı sağlar. Büyük veri setleri için vazgeçilmez bir stratejidir.

*Bir kitabın tamamını her gün yeniden yazmak yerine, sadece o gün eklenen sayfaları not defterine yazıp eklemek gibidir.*

## Nasıl çalışır?

Sistem, dosyaların son değiştirilme tarihlerini kontrol eder. Sadece değişen veya yeni eklenen parçaları yedekleme dosyasına ekler.

## Nerede kullanılır?

Kurumsal veritabanlarında, büyük dosya sunucularında ve profesyonel yedekleme sistemlerinde kullanılır.

## Sık karıştırılanlar

Tam yedekleme (full backup) ile karıştırılmamalıdır; tam yedekleme her seferinde her şeyi kopyalar.

## Sıkça sorulanlar

**Geri yükleme yaparken zor mu?**

Evet, tüm parçaların birleştirilmesi gerektiği için tam yedeklemeye göre biraz daha karmaşıktır.

**Ne sıklıkla yapılmalı?**

Veri değişim hızınıza bağlı olarak günlük veya saatlik yapılabilir.

## İlgili terimler

- [Backup Program](https://trescout.com/dictionary/backup-program/)
- [Data Pipeline](https://trescout.com/dictionary/data-pipeline/)

## İlgili araçlar

- [Restic](https://trescout.com/discover/restic/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/incremental-backup/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
