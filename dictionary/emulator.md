# Emulator (Emülatör) nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Emülatör (emulator), bir bilgisayarın, telefonun veya oyun konsolunun fiziksel donanım mimarisini yazılımsal olarak taklit ederek, başka platformlara ait programları ve oyunları kendi cihazınızda çalıştırmanızı sağlayan bir öykünme aracıdır.

## Tanım
Emülatör, hedef cihazın işlemcisini (CPU), grafik yongasını (GPU), bellek adreslemesini ve giriş/çıkış (I/O) birimlerini yazılım katmanında birebir kopyalar. Bu sayede fiziksel cihaz elinizde olmadan, o sisteme özel derlenmiş ikili kodları (binary) bilgisayarınızda sanki orijinal donanımdaymış gibi yürütebilirsiniz.

## Emülatör ne demek?
İngilizce "emulate" (öykünmek, taklit etmek) fiilinden türeyen terim, Türkçede teknik olarak **"öykünücü"** veya **"donanım taklitçisi"** olarak tanımlanır. Bilişimde iki temel alanda sıkça aranır:
1. **Mobil ve Yazılım Geliştirme:** Android Studio veya iOS simülatörleri gibi, geliştiricilerin kodlarını gerçek telefon satın almadan farklı ekran boyutlarında ve işletim sistemi sürümlerinde test etmesi.
2. **Oyun ve Nostalji:** PlayStation, Nintendo veya Arcade konsol oyunlarını modern PC veya telefonlarda oynamak.

## Emülatör ile Simülatör arasındaki fark nedir?
- **Simülatör:** Sistemin sadece yüzeysel davranışını ve mantığını taklit eder; donanım seviyesine inmez (ör. bir uçuş simülatörü uçağın fizik motorunu taklit eder ancak kokpitteki çipleri simüle etmez).
- **Emülatör:** Hedef cihazın donanımını (register'lar, bellek veri yolu, saat döngüleri) talimat seviyesinde (instruction-level) birebir taklit eder. Bu nedenle emülatörler simülatörlere göre çok daha yüksek işlemci gücü gerektirir.

## Bir benzetmeyle
Farklı bir ülkenin dilini ve kültürünü sadece ezberleyen bir turist simülatör gibidir; o ülkenin vatandaşının beynini, reflekslerini ve düşünme yapısını birebir kopyalayan bir yapay zekâ ise emülatördür.

## Sıkça sorulanlar

**Emülatör kullanmak yasal mı?**  
Emülatör yazılımlarının kendisi tamamen yasaldır ve tersine mühendislik hakkı kapsamındadır. Ancak konsolun telif hakkı korumalı BIOS dosyalarını veya oyunların ROM/ISO kopyalarını izinsiz internetten indirmek telif ihlali oluşturabilir.

**Neden emülatörler çok fazla bilgisayar gücü tüketir?**  
Çünkü ana bilgisayarınız kendi işletim sistemini çalıştırırken, aynı anda tamamen yabancı bir işlemci mimarisinin komut setini anlık olarak kendi komut setine (JIT/çeviri) dönüştürmek zorundadır.

## İlgili terimler
- [ROM](/dictionary/rom/)
- [Sandbox](/dictionary/sandbox/)
- [Virtual Machines](/dictionary/virtual-machines/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/emulator/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
