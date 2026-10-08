# ARQ nedir?

*Sözlük · Geliştirme · Son güncelleme: 12 Haziran 2026*

> Automatic Repeat Request

Veri iletimi sırasında hata oluştuğunda bilginin otomatik olarak tekrar gönderilmesini sağlayan hata kontrol mekanizmasıdır.

## Tanım

İnternet üzerinden veri gönderirken bazen paketler kaybolabilir veya bozulabilir. ARQ, alıcı tarafın veriyi alıp almadığını kontrol eder ve hata tespit ederse göndericiye 'bunu alamadım, tekrar gönder' der. Bu sayede verinin eksiksiz ve hatasız ulaşması sağlanır.

*Telefonda konuşurken karşı tarafın 'anlamadım, tekrar söyler misin?' demesi ve sizin o cümleyi tekrar etmeniz gibidir.*

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

- [API](https://trescout.com/dictionary/api/)
- [DNS Tunneling](https://trescout.com/dictionary/dns-tunneling/)
- [Computer Science](https://trescout.com/dictionary/computer-science/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/arq/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
