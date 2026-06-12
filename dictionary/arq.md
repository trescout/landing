# ARQ nedir?

> Automatic Repeat Request

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-06-12

Veri iletimi sırasında hata oluştuğunda bilginin otomatik olarak tekrar gönderilmesini sağlayan hata kontrol mekanizmasıdır.

## Tanım
İnternet üzerinden veri gönderirken bazen paketler kaybolabilir veya bozulabilir. ARQ, alıcı tarafın veriyi alıp almadığını kontrol eder ve hata tespit ederse göndericiye 'bunu alamadım, tekrar gönder' der. Bu sayede verinin eksiksiz ve hatasız ulaşması sağlanır.

## Bir benzetmeyle
Telefonda konuşurken karşı tarafın 'anlamadım, tekrar söyler misin?' demesi ve sizin o cümleyi tekrar etmeniz gibidir.

## Nasıl çalışır?
Gönderici veri paketini yollar ve bir onay bekler. Eğer belirli bir sürede onay gelmezse, paket bozuk veya kayıp kabul edilir ve tekrar gönderilir.

## Nerede kullanılır?
TCP protokolü gibi internetin temel iletişim kurallarında ve ağ protokollerinde kullanılır.

## Sıkça sorulanlar

**Neden bu kadar önemli?**  
İnternet bağlantıları her zaman mükemmel değildir; ARQ verinin güvenilirliğini sağlar.

**Gecikmeye neden olur mu?**  
Evet, hatalı paketlerin tekrar gönderilmesi süreci biraz yavaşlatabilir.

## İlgili terimler
- [API](/dictionary/api/)
- [DNS Tunneling](/dictionary/dns-tunneling/)
- [Computer Science](/dictionary/computer-science/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/arq/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
