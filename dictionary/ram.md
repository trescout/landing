# RAM nedir, ne demek?

> Random Access Memory

**Kategori:** Veri & Altyapı  
**Son güncelleme:** 2026-09-22

RAM (**Random Access Memory**, rastgele erişimli bellek), işlemcinin aktif veriyi tuttuğu geçici bellektir.

## Tanım ve Kelime Kökeni
Bilgisayar kapanınca içeriği silinir, ama işlemciye yakın olduğu için çok yüksek hızda çalışır. İşlemci iş yaparken dosyaları buraya çeker. Programlar açıldığında diskten RAM içine kopyalanır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Bilgisayar:** Sekmeler ve uygulamalar.
- **Telefon:** Arka plandaki uygulamalar.
- **Sunucu:** Eşzamanlı istekler.

## Teknik Derinlik ve Mimari
Türler:
- **DRAM:** Ana bellek, yoğun ve ucuz.
- **SRAM:** Önbellek, hızlı ve pahalı.
- **Swap:** Diskten ayrılan yedek alan, yavaşlatır.

Durum denetimi:

```
free -h
```

Kural: Dolunca sistem yavaşlar veya uygulama kapanır. 8 GB temel, 16 GB rahat, 32 GB iş istasyonudur. İhtiyaç üstü kapasite boşta bekler.

## Sık Karıştırılanlar
Depolama sanılır. RAM geçici çalışma alanıdır, disk kalıcı kütüphanedir. Kapanınca RAM boşalır, disk kalır.

## Farklı Disiplinlerde Kullanımı
- **Masa:** Genişlik arttıkça açık dosya sayısı.
- **Tezgah:** Malzemenin el altında durması.
- **Beyaz tahta:** Geçici not alanı.

## Bir benzetmeyle
Bilgisayarın masası gibidir; masa genişledikçe aynı anda açık dosya sayısı artar.

## Sıkça sorulanlar

**RAM dolarsa ne olur?**  
Sistem yavaşlar veya uygulamalar kapanır. Gereksiz sekmeler kapatılır, gerekirse kapasite artırılır.

**Fazlası hızlandırır mı?**  
İhtiyaç kadar evet, üstü boşta bekler. Darboğaz diskse RAM artışı fark etmez.

**SSD farkı nedir?**  
SSD kalıcı depodur, RAM geçici alandır. İkisi birlikte çalışır, biri diğerinin yerini tutmaz.

**Ne kadar yeterli?**  
Günlük işte 8, geliştirmede 16, ağır işte 32 GB pratik karşılıklardır.

## İlgili terimler
- [VRAM](/dictionary/vram/)
- [Runtime](/dictionary/runtime/)
- [CPU](/dictionary/cpu/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/ram/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
