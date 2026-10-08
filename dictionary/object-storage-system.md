# Object Storage System nedir?

*Sözlük · Veri & Altyapı · Son güncelleme: 19 Eylül 2026*

Verileri dosya klasörleri yerine benzersiz kimliklerle saklayan, büyük ölçekli depolama yöntemidir.

## Tanım

Geleneksel bilgisayarınızdaki dosya sistemi bir ağaç yapısı gibidir; klasör içinde klasör şeklinde ilerler. Nesne depolama ise veriyi bir nesne olarak ele alır ve ona özel bir kimlik verir. Bu sayede veriye ulaşmak için klasör yollarını takip etmek yerine, doğrudan o kimliği kullanarak veriye hızla erişebilirsiniz.

*Bir kütüphanede kitabı raflar ve numaralarla bulmak yerine, kitabın üzerine yapıştırılmış sihirli bir barkodu okutup kitabın anında elinize ışınlanması gibidir.*

## Nasıl çalışır?

Veri sisteme yüklendiğinde bir nesne haline gelir ve yanına bazı açıklamalar (metadata) eklenir. İhtiyaç duyduğunuzda bu nesneyi kimliği üzerinden çağırırsınız.

## Nerede kullanılır?

Bulut depolama hizmetlerinde, büyük veri yedeklemelerinde ve medya içeriklerinin sunulmasında kullanılır.

## Sık karıştırılanlar

Normal sabit disk dosya sistemleri ile karıştırılabilir; ancak bu sistem çok daha büyük veriler için tasarlanmıştır.

## Sıkça sorulanlar

**Neden klasör kullanmıyor?**

Çünkü milyarlarca veriyi klasör yapısında yönetmek çok yavaştır, nesne sistemi ise çok daha hızlıdır.

## İlgili terimler

- [Database](https://trescout.com/dictionary/database/)
- [Cloud Computing](https://trescout.com/dictionary/cloud-computing/)
- [Data Layer](https://trescout.com/dictionary/data-layer/)

## İlgili araçlar

- [Rustfs](https://trescout.com/discover/rustfs/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/object-storage-system/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
