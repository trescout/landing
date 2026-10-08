# Caching nedir, ne demek?

*Sözlük · Veri & Altyapı · Son güncelleme: 22 Eylül 2026*

Caching (Türkçe karşılığıyla **önbellekleme**), sık veriyi hızlı kata kopyalamadır.

## Tanım ve Kelime Kökeni

"Cache" **saklı stok** demektir. Sistem aynı veriyi tekrar hesaplamak yerine kopyasından verir. Yanıt süresi düşer, yük hafifler. Tarayıcıdan veri merkezine her katta çalışır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?

**Tarayıcı:** Sayfa ve resim saklama.
**Uygulama:** Çevrimdışı kopya.
**Sunucu:** Sorgu sonucu saklama.

## Teknik Derinlik ve Mimari

Stratejiler:

**LRU:** En eski kullanılmayan çıkar.
**TTL:** Süresi dolan düşer.
**Cache-aside:** Uygulama yönetir.

Tarayıcı yönergesi:

```
Cache-Control: public, max-age=3600
```

Bu satır kopyanın bir saat geçerli olduğunu söyler. Tutarlılık bedeli vardır: Kaynak değişince kopya eskir, kritik veride süre kısa tutulur.

## Sık Karıştırılanlar

Veritabanı sanılır. Veritabanı kalıcı ve geniştir, önbellek geçici ve hızlıdır. Biri kasa, diğeri cep cüzdanıdır.

## Farklı Disiplinlerde Kullanımı

**Çanta:** Sık kitap el altında.
**Buzdolabı:** Günlük yemek önde.
**Kiler:** Toplu stok arkada.

*Sık kullanılan kitabı çantada taşımak gibidir; her seferinde kütüphaneye gidilmez.*

## Sıkça Sorulanlar

**Önbellek dolarsa ne olur?**

Eski ve az kullanılan düşer, yenisi yazılır. Politika bunu yönetir.

**Ne zaman temizlenir?**

Süre dolunca, kapasite taşınca veya elle. Kritik veri kısa süreli tutulur.

**Tutarsızlık olur mu?**

Olabilir. Kaynak değişince kopya eskir, sürüm ve süre disiplini gerekir.

**Nerede tutulur?**

Bellek, disk veya CDN ucunda. Hız ve kapasite dengesine göre seçilir.

## İlgili terimler

- [KV Cache](https://trescout.com/dictionary/kv-cache/)
- [Prefix Cache](https://trescout.com/dictionary/prefix-cache/)
- [Database](https://trescout.com/dictionary/database/)

## İlgili araçlar

- [Free for Dev](https://trescout.com/discover/free-for-dev/)
- [OmniRoute](https://trescout.com/discover/omniroute/)
- [Guava](https://trescout.com/discover/guava/)
- [Omlx](https://trescout.com/discover/omlx/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/caching/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
