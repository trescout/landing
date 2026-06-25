# Packet Fragmentation nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-06-25

İnternet üzerinden gönderilen verilerin, ağın taşıma kapasitesine göre daha küçük parçalara bölünmesi işlemidir.

## Tanım
İnternette veri gönderirken, her ağın taşıyabileceği maksimum bir boyut vardır. Eğer gönderdiğiniz veri bu boyuttan büyükse, sistem onu küçük parçalara ayırır, hedefe ulaştırır ve orada tekrar birleştirir.

## Bir benzetmeyle
Çok büyük bir kargoyu tek bir kamyona sığdıramadığınızda, onu daha küçük kutulara bölüp farklı kamyonlarla gönderip, varış noktasında tekrar birleştirmeniz gibidir.

## Nasıl çalışır?
Veri gönderilirken ağ cihazları paketin boyutunu kontrol eder. Eğer limit aşılmışsa, paket parçalanır ve her parçaya bir 'sıra numarası' verilir. Alıcı cihaz bu numaralara bakarak parçaları doğru sırayla birleştirir.

## Nerede kullanılır?
İnternet protokolleri ve ağ iletişimi süreçlerinde arka planda sürekli gerçekleşir.

## Sık karıştırılanlar
Veri kaybıyla karıştırılabilir, ancak bu kontrollü bir bölme işlemidir.

## Sıkça sorulanlar

**Parçalar kaybolursa ne olur?**  
Alıcı cihaz parçaların eksik olduğunu anlar ve göndericiden o parçayı tekrar göndermesini ister.

## İlgili terimler
- [Networking Stack](/dictionary/networking-stack/)
- [DNS Tunneling](/dictionary/dns-tunneling/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/packet-fragmentation/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
