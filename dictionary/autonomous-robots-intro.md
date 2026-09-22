# Introduction to Autonomous Robots nedir?

**Kategori:** Yapay Zekâ  
**Son güncelleme:** 2026-09-22

Otonom robotlar, sürekli komut almadan çevresinde hareket eden makinelerdir.

## Tanım ve Kelime Kökeni
"Autonomous" **özerk** demektir. Üçlü düzen: Algı (sensör), işlem (yapay zekâ) ve eylem (motor). Robot yolu ezberlemez, engeli aşıp hedefe gider.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Depo:** Raf arası taşıma.
- **Fabrika:** Montaj hattı.
- **Araç:** Sürücü destek sistemleri.

## Teknik Derinlik ve Mimari
Döngü:

```
algıla → planla → hareket et → denetle
```

Parçalar:
- **Algı:** Kamera, lidar ve radar.
- **Konum:** Harita üstünde yer bulma.
- **Plan:** Engel çevresinden rota.
- **Denetim:** Hata duruşu ve insan devralması.

ROS ortak çatıdır. Güvenlik kuralı: İnsan yakınında hız ve güç sınırlanır.

## Sık Karıştırılanlar
Kumandalı robot sanılır. O tamamen insan elindedir, bu hedefle baş başadır. Biri kukla, diğeri çıraktır.

## Farklı Disiplinlerde Kullanımı
- **Oyuncak araba:** Yolu kendi bulan model.
- **Asansör:** Düğmeye göre kat seçimi.
- **Otopilot:** Rotayı koruyan düzen.

## Bir benzetmeyle
Oyuncak arabayı kumandayla sürmek yerine gideceği yeri söyleyip yolunu bulmasını beklemeye benzer.

## Sıkça sorulanlar

**Nasıl öğrenirler?**  
Veri analizi ve deneme yanılmayla. Simülasyonda prova, sahada ince ayar yapılır.

**Güvenli mi?**  
Tasarlandığı sınırda evet. Hata duruşu ve insan devralması şarttır.

**Nerede kullanılır?**  
Depo, fabrika ve yolda. Tekrarlı ve tehlikeli işlerde öndedir.

**Ne zaman yaygınlaşır?**  
Maliyet ve mevzuat belirler. Kapalı alan önce, açık yol sonra gelir.

## İlgili terimler
- [Physical AI](/dictionary/physical-ai/)
- [Autonomous Agent](/dictionary/autonomous-agent/)
- [Computer Vision](/dictionary/computer-vision/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/autonomous-robots-intro/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
