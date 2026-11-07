# Model-View-Controller nedir?

*Geliştirme · Son güncelleme: 7 Kasım 2026*

> Model-View-Controller

Bir yazılımın verisini, arayüzünü ve mantığını ayıran mimari yapı.

## Tanım

Model-View-Controller, yazılım geliştirirken kodun birbirine girmesini önleyen popüler bir tasarım desenidir. Model kısmı veritabanını ve verinin işlenme kurallarını yönetir, View kısmı ise kullanıcının ekranda gördüğü tasarımı sunar. Controller ise bu ikisi arasında köprü kurarak kullanıcının yaptığı hamleleri modele iletir ve sonucu ekrana yansıtır.

*Bir restorandaki işleyiş gibidir. Model mutfaktaki malzemeler ve tariflerdir, View müşterinin oturduğu masa ve tabaktır, garson ise mutfakla müşteri arasında gidip gelen Controller görevini üstlenir.*

## Nasıl çalışır?

Uygulama geliştirirken veritabanı işlemlerini, tasarım kodlarını ve iş kurallarını ayrı dosyalarda yazarsınız. Controller kullanıcının isteğini yakalar ve gerekirse Model'den veri çekip View'a gönderir. Bu sayede bir yerde hata çıktığında diğer kısımları bozmadan kolayca düzeltebilirsiniz.

## Nerede kullanılır?

Web siteleri, mobil uygulamalar ve büyük kurumsal yazılımlar tasarlanırken yaygın olarak kullanılır.

## Sık karıştırılanlar

Doğrudan bir veritabanı veya arayüz kütüphanesi değildir, tüm sistemin nasıl organize edileceğini belirleyen üst düzey bir mimari düzendir.

## Sorular ve yanıtlar

**Neden her şeyi tek bir dosyada yazmak yerine bu yapıyı kullanalım?**

Çünkü proje büyüdüğünde kodun içinde kaybolursunuz; tasarımı değiştirmek istediğinizde veritabanı kodları patlayabilir. Bu yapı düzen sağlar.

**Küçük projelerde de kullanmak şart mı?**

Şart değildir ama küçük projeler de zamanla büyüyebilir, bu yüzden temelden bu mantıkla başlamak işinizi sonradan kolaylaştırır.

## İlgili terimler

- [Frontend](https://trescout.com/dictionary/frontend/)
- [Backend](https://trescout.com/dictionary/backend/)
- [Database](https://trescout.com/dictionary/database/)
- [Architecture Diagrams](https://trescout.com/dictionary/architecture-diagrams/)

## İlgili araçlar

- [Rails](https://trescout.com/discover/rails/)

Bu açıklama TreScout için yapay zekâ ile sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/model-view-controller/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
