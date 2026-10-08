# VPS nedir, ne demek?

*Sözlük · Geliştirme · Son güncelleme: 22 Eylül 2026*

> Virtual Private Server

VPS (**Virtual Private Server**, sanal özel sunucu), fiziksel sunucunun sanallaştırmayla bölünmüş, size ayrılmış bağımsız dilimidir.

## Tanım ve Kelime Kökeni

Devasa bir sunucu, hipervizör yazılımıyla küçük parçalara bölünür. Her parça kendi işletim sistemini çalıştırır ve ayrılmış RAM ile işlemci payına sahiptir. Komşu dilimler ne yaparsa yapsın sizinki etkilenmez. Bu yüzden kendi sunucunuz varmış gibi dilediğiniz yazılımı kurar ve yönetirsiniz.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?

**Web sitesi:** Trafiği büyüyen blog ve mağazalar.
**Kişisel bulut:** Dosya eşitleme ve yedekleme.
**Test ortamı:** Canlıya çıkmadan deneme yapma.
**Oyun ve VPN:** Arkadaş grubu oyun sunucusu, özel tünel.

## Teknik Derinlik ve Mimari

Bilmeniz gerekenler:

**Garanti kaynak:** RAM ve CPU payınız rezerve edilir, komşu yoğunluğu sizi yavaşlatmaz.
**Root erişimi:** İşletim sisteminde tam yetki, istediğiniz paketi kurarsınız.
**Snapshot:** Diske anlık görüntü alınır, hata yaparsanız geri dönersiniz.
**İlk kurulum:** Güncelleme, güvenlik duvarı ve parola yerine anahtar kullanımı.

Bağlantı örneği:

```
ssh kullanici@sunucu-adresi -p 22
```

Yönetilen (managed) VPS hizmetinde bakım sağlayıcıdadır, yönetilmeyende sizdedir. Seçim, teknik bilginize göre yapılır.

## Sık Karıştırılanlar

Paylaşımlı hosting ile karıştırılabilir. Paylaşımlı hostingde kaynakları başkalarıyla ortak kullanırsınız, VPS içinde size ayrılan kaynaklar garantidir. Bir üst basamak ise tüm makinenin sizde olduğu dedicated server olur.

## Farklı Disiplinlerde Kullanımı

**Apartman:** Ortak bina, bağımsız daire ve kilitli kapı.
**Ofis katı:** Ortak resepsiyon, özel çalışma alanı.
**Kiralık kasa:** Banka binasında size özel bölme.

*Büyük bir apartmandaki bağımsız bir daire gibidir; binanın genel altyapısını paylaşırsınız ama kendi kapınız ve özel alanınız vardır.*

## Sıkça Sorulanlar

**VPS yönetmek için teknik bilgi gerekir mi?**

Yönetilmeyen pakette evet: Güncelleme, güvenlik duvarı ve yedekleme sizdedir. Temel Linux bilgisi yeterlidir. Zorlanırsanız yönetilen pakete geçebilirsiniz.

**Paylaşımlı hostingden farkı nedir?**

Paylaşımlıda kaynak ortaktır, komşu yoğunluğu sizi yavaşlatır. VPS içinde payınız garantidir ve root yetkiniz vardır.

**Ne kadar kaynakla başlanmalı?**

Küçük site için 1-2 GB RAM genellikle yeterlidir. İzleme grafiklerine bakıp kademeli büyütmeniz önerilir.

**Yedekleme nasıl yapılır?**

Sağlayıcının snapshot özelliği artı harici yedek kuralı önerilir. Tek kopya yedek sayılmaz.

## İlgili terimler

- [Virtual Machines](https://trescout.com/dictionary/virtual-machines/)
- [Cloud Computing](https://trescout.com/dictionary/cloud-computing/)
- [Self-Hosting](https://trescout.com/dictionary/self-hosting/)

## İlgili araçlar

- [DeskcommCRM](https://trescout.com/discover/deskcommcrm/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/vps/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
