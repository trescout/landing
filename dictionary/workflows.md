# Workflows nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

Workflow (Türkçe karşılığıyla **iş akışı**), işin düzenli adım dizisidir.

## Tanım ve Kelime Kökeni
"Flow" **akış** demektir. Hedefe giden adımlar sıraya dizilir, karmaşık iş küçük parçalara bölünür. Doğru akış hatayı azaltır, hızı artırır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Geliştirme:** Kod inceleme hattı.
- **Destek:** Bilet karşılama düzeni.
- **Ofis:** Onay zinciri.

## Teknik Derinlik ve Mimari
Akış tarifi:
- **Tetikleyici:** Başlatan olay.
- **Adım:** Sıralı işler.
- **Koşul:** Dallanma kuralı.
- **Çıktı:** Sonuç ve kayıt.

Tetikleme örneği:

```
on: [push]
```

Bu satır, koda her gönderimde akışın çalışacağını söyler. Otomasyon kuralı: İkinci kez elle yapılan iş adaya yazılır.

## Sık Karıştırılanlar
Pipeline sanılır. Pipeline teknik veri akışıdır, workflow daha genel iş düzenidir. Her pipeline bir workflow sayılır, tersi şart değildir.

## Farklı Disiplinlerde Kullanımı
- **Tarif:** Hazırlık, pişirme ve servis.
- **Montaj:** Parça sırası.
- **Kontuar:** Kayıt ve yönlendirme.

## Bir benzetmeyle
Yemek tarifi gibidir; malzeme hazırlama, pişirme ve servis adımlarının tamamı iş akışıdır.

## Sıkça sorulanlar

**Neden otomatize edilmeli?**  
Tekrar hata ve zaman üretir. Otomasyon ikisini de kısar.

**İş akışları değişebilir mi?**  
Evet. İhtiyaç değiştikçe güncellenir, sürümü tutulur.

**Nereden başlanır?**  
En sık tekrarlanan işten. Adımlar yazılır, biri otomasyona alınır.

**Araç şart mı?**  
Hayır. Kâğıt liste de akıştır. Hacim büyüyünce araç gerekir.

## İlgili terimler
- [Pipeline](/dictionary/pipeline/)
- [Data Pipeline](/dictionary/data-pipeline/)
- [CI-CD](/dictionary/ci-cd/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/workflows/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
