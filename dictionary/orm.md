# ORM nedir?

*Sözlük · Geliştirme · Son güncelleme: 9 Temmuz 2026*

> Object-Relational Mapping

Veritabanı tablolarını kod içindeki nesnelere dönüştüren bir köprüdür.

## Tanım

Yazılım geliştirirken veritabanındaki karmaşık tablolarla uğraşmak yerine, bu verileri programlama dilindeki nesneler gibi kullanmanızı sağlar. Bu sayede SQL gibi karmaşık sorgular yazmadan verileri yönetebilirsiniz. Kodunuzu daha okunabilir ve yönetilebilir kılar.

*Veritabanındaki ham verileri birer kutu olarak düşünün; ORM bu kutuları sizin için açıp içindeki eşyaları doğrudan kullanabileceğiniz birer nesneye dönüştüren bir yardımcı gibidir.*

## Nasıl çalışır?

Veritabanı ile uygulama kodu arasında bir katman olarak çalışır. Siz kodunuzda bir veriyi kaydettiğinizde, o bu işlemi arka planda uygun SQL sorgusuna çevirir. Böylece veritabanı yapısı değişse bile kodunuzu çok az değiştirmeniz yeterli olur.

## Nerede kullanılır?

Web uygulamaları, kurumsal yazılımlar ve veritabanı yoğunluklu projelerde sıkça kullanılır.

## Sık karıştırılanlar

Veritabanı sürücüsü ile karıştırılabilir; sürücü ham bağlantıyı sağlar, ORM ise bu bağlantıyı kolaylaştırır.

## Sıkça sorulanlar

**Neden ORM kullanmalıyım?**

Veritabanı işlemlerini hızlandırır ve kod hatalarını azaltır.

**Performansı düşürür mü?**

Çok karmaşık sorgularda bazen manuel SQL daha hızlı olabilir ancak çoğu durumda sağladığı kolaylık buna değerdir.

## İlgili terimler

- [Database](https://trescout.com/dictionary/database/)
- [Tech Stack](https://trescout.com/dictionary/tech-stack/)

## İlgili araçlar

- [Prisma](https://trescout.com/discover/prisma/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/orm/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
