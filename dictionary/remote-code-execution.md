# Remote Code Execution nedir?

*Sözlük · Geliştirme · Son güncelleme: 6 Eylül 2026*

> RCE

Yetkisiz bir kişinin, internet üzerinden başka bir bilgisayarda kendi komutlarını çalıştırabilmesi durumudur.

## Tanım

Siber güvenlik dünyasındaki en kritik açıklardan biridir. Bir saldırgan, hedef sistemdeki bir zafiyeti kullanarak o bilgisayara uzaktan emir gönderebilir ve sistemin kontrolünü ele geçirebilir. Bu, bilgisayarınızda sizin yerinize bir başkasının oturum açıp program çalıştırması gibidir.

*Evinizin anahtarını bir yabancıya kaptırmak gibidir; o kişi artık evin içindeki her şeyi dilediği gibi yönetebilir, eşyalarınızı kullanabilir veya değiştirebilir.*

## Nasıl çalışır?

Genellikle yazılımların kullanıcıdan gelen verileri yeterince denetlememesinden kaynaklanır. Saldırgan, veri girilmesi gereken bir alana komut satırı kodları yazar ve sistem bu kodları 'gerçek bir komut' sanarak çalıştırır.

## Nerede kullanılır?

Sunucularda, web uygulamalarında ve güncellenmemiş yazılımlarda bir güvenlik riski olarak görülür.

## Sık karıştırılanlar

Sadece veri çalınması ile karıştırılmamalıdır; bu durum verinin ötesinde sistemin tam kontrolünü içerir.

## Sıkça sorulanlar

**Bundan nasıl korunurum?**

En iyi korunma yolu yazılımlarınızı her zaman güncel tutmak ve güvenilmeyen kaynaklardan gelen komutları çalıştırmamaktır.

## İlgili terimler

- [Zero-day Exploit](https://trescout.com/dictionary/zero-day/)
- [Vulnerability Scanning](https://trescout.com/dictionary/vulnerability-scanning/)
- [Cybersecurity Skills](https://trescout.com/dictionary/cybersecurity-skills/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/remote-code-execution/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
