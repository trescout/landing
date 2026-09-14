# Experts Streamed from Disk nedir?

**Kategori:** Yapay Zekâ  
**Son güncelleme:** 2026-09-14

Devasa yapay zekâ modellerinin parçalarının, belleğe sığmadığında diskten anlık olarak yüklenmesi yöntemidir.

## Tanım
Yapay zekâ modelleri bazen o kadar büyüktür ki bilgisayarın RAM kapasitesine sığmazlar. Bu teknikte, modelin sadece o an ihtiyaç duyulan kısımları (uzmanları) diskten hızlıca okunarak belleğe getirilir. Böylece çok büyük modeller, sınırlı donanımlarda bile çalışabilir hale gelir.

## Bir benzetmeyle
Dev bir kütüphanedeki tüm kitapları masanızın üzerine sığdıramazsınız; bu yüzden sadece o an okuyacağınız sayfayı raftan alıp okur, işiniz bitince geri koyarsınız.

## Nasıl çalışır?
Sistem, modelin ağırlıklarını küçük parçalara böler ve bunları diskte saklar. Kullanıcı bir soru sorduğunda, modelin ilgili parçaları çok hızlı bir şekilde diskten belleğe aktarılır, işlem yapılır ve ardından bellek boşaltılır.

## Nerede kullanılır?
Özellikle ev tipi bilgisayarlarda çok büyük dil modellerini çalıştırmak isteyen geliştiriciler ve donanım kısıtı olan sunucularda kullanılır.

## Sık karıştırılanlar
Modelin tamamının belleğe yüklenmesiyle karıştırılabilir; burada sadece ihtiyaç anında yükleme söz konusudur.

## Sıkça sorulanlar

**Bu yöntem hızı düşürür mü?**  
Evet, diskten okuma işlemi RAM'e göre daha yavaş olduğu için modelin yanıt verme süresinde bir miktar gecikme yaşanabilir.

**Her model bu şekilde çalışabilir mi?**  
Modelin bu mimariyle tasarlanmış olması gerekir; yani parçalı (Mixture of Experts) bir yapıda olması şarttır.

## İlgili terimler
- [Mixture of Experts](/dictionary/mixture-of-experts/)
- [RAM](/dictionary/ram/)
- [Inference Engine](/dictionary/inference-engine/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/experts-streamed-from-disk/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
