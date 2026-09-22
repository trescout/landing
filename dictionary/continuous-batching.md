# Continuous Batching nedir, ne demek?

**Kategori:** Yapay Zekâ  
**Son güncelleme:** 2026-09-22

Continuous batching (Türkçe karşılığıyla **sürekli gruplama**), istekleri bekletmeden motora alan tekniktir.

## Tanım ve Kelime Kökeni
Klasik grup bitmeden yeni istek girer. Donanım boş kalmaz, cevap hızlı döner. Sohbet botu ve yoğun servislerin motor odasıdır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Sohbet:** Anlık yanıt hattı.
- **API:** Yoğun uçlar.
- **Bulut:** Maliyetli GPU kuyruğu.

## Teknik Derinlik ve Mimari
Akış:

```
gelen → boş çekirdeğe yerleş → biten çıkar → yeni girer
```

Kazanç: Verim ve gecikme düşer. Sınır: Adil kuyruk gerekir, aç istek takılır. vLLM bilinen uygulayıcısıdır.

## Sık Karıştırılanlar
Hız sanılır. Oysa konu verimdir: Aynı donanımla çok iş yapılır. Hız yan üründür.

## Farklı Disiplinlerde Kullanımı
- **Şef:** Masaları bekletmeden pişirme.
- **Otobüs:** Doldukça kalkmayan ring.
- **Asansör:** Ara kat yolcusu alma.

## Bir benzetmeyle
Tek masayı bitirmeden her masaya servis veren şef gibidir.

## Sıkça sorulanlar

**Neden önemli?**  
Bekleme düşer, maliyet düşer. Yoğun hatta fark açılır.

**Her modelde var mı?**  
Hayır. Gelişmiş motorların özelliğidir.

**Gecikme ne olur?**  
Ortalama düşer, kuyruk adaleti gözetilir.

**Ne zaman gerekir?**  
Eşzamanlı istek artınca. Düşük yükte fark edilmez.

## İlgili terimler
- [Inference Engine](/dictionary/inference-engine/)
- [LLM](/dictionary/llm/)
- [Inference](/dictionary/inference/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/continuous-batching/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
