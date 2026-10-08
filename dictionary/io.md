# I/O nedir, ne demek?

*Sözlük · Geliştirme · Son güncelleme: 22 Eylül 2026*

> Input/Output

I/O (**Input/Output**, girdi-çıktı), sistemin dış dünyayla veri alışverişidir.

## Tanım ve Kelime Kökeni

Klavye yazısı, indirilen dosya, ekrana basılan sonuç: Hepsi I/O işlemidir. Sistem dış dünyayla bu kanal üzerinden konuşur. Bilgisayarın duyuları ve elleri gibidir.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?

**Klavye:** Yazı girişi.
**Ağ:** Dosya indirme.
**Ekran:** Sonuç gösterme.

## Teknik Derinlik ve Mimari

Kavramlar:

**Blocking:** İşlem bitene kadar bekleme.
**Non-blocking:** Beklemeden devam, sonuç gelince haber.
**Buffer:** Hız farkını dengeleyen ara depo.
**Darboğaz:** En yavaş halka tüm hattı yavaşlatır, genellikle disk veya ağdır.

Dosya okuma örneği:

```
const veri = await fs.readFile("not.txt", "utf8");
```

Bu satır dosya gelene kadar beklemez, diğer işler sürer. Sonuç hazır olunca devam edilir.

## Farklı Disiplinlerde Kullanımı

**İnsan:** Göz kulak girişi, konuşma çıkışı.
**Restoran:** Sipariş girişi, servis çıkışı.
**Fabrika:** Hammadde girişi, ürün çıkışı.

*Bir insanın dış dünyadan bilgi alması ve dış dünyaya tepki vermesi gibidir; gözler giriş, konuşma çıkıştır.*

## Sıkça Sorulanlar

**I/O neden darboğaz olur?**

İşlemci hızlıdır, disk ve ağ yavaştır. Veri yetişmeyince sistem bekler, darboğaz burada oluşur.

**Blocking nedir?**

Sonuç gelene kadar bekleyen çağrıdır. Arayüzü kilitler, sunucuda iş israf eder.

**Nasıl hızlandırılır?**

Önbellek, toplu okuma ve eşzamansız çağrıyla. Önce ölçülür, sonra en yavaş halka düzeltilir.

**Async ne alaka?**

Bekleme sırasında başka iş yapma düzenidir. Tek iş parçacığıyla çok iş çevrilir.

## İlgili terimler

- [API](https://trescout.com/dictionary/api/)
- [Data Pipeline](https://trescout.com/dictionary/data-pipeline/)
- [Streaming Applications](https://trescout.com/dictionary/streaming-applications/)

## İlgili araçlar

- [Asio](https://trescout.com/discover/asio/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/io/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
