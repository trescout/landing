# Caching nedir?

**Kategori:** Veri & Altyapı  
**Son güncelleme:** 2026-08-07

Sık kullanılan verilerin, hızlı erişim sağlamak amacıyla geçici olarak bellekte saklanmasıdır.

## Tanım
Caching, bir sistemin aynı veriyi tekrar tekrar hesaplamasını veya uzak bir kaynaktan çekmesini engellemek için kullanılan bir hızlandırma yöntemidir. Veri, hızlı erişilebilen bir alana (önbelleğe) kopyalanır ve ihtiyaç duyulduğunda buradan sunulur. Bu, sistemin genel yanıt süresini ciddi oranda düşürür.

## Bir benzetmeyle
Sürekli kullandığınız bir kitabı çantanızda taşımak gibidir; her seferinde kütüphaneye gidip kitabı raftan almanız gerekmez, elinizin altındadır.

## Nasıl çalışır?
Sistem, bir veriyi talep ettiğinde önce önbelleğe bakar; veri oradaysa hemen alır, yoksa ana kaynaktan çeker ve bir kopyasını önbelleğe bırakır.

## Nerede kullanılır?
Web tarayıcılarında, uygulamalarda ve büyük ölçekli veri merkezlerinde performansı artırmak için yaygın olarak kullanılır.

## Sık karıştırılanlar
Veritabanı ile karıştırılabilir ancak cache geçici ve hızlıdır, veritabanı ise kalıcı ve daha geniştir.

## Sıkça sorulanlar

**Önbellek dolarsa ne olur?**  
Eski veya az kullanılan veriler silinir ve yerlerine yeni veriler yazılır.

## İlgili terimler
- [KV Cache](/dictionary/kv-cache/)
- [Prefix Cache](/dictionary/prefix-cache/)
- [Database](/dictionary/database/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/caching/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
