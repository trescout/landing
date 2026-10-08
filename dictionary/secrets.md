# Secrets nedir?

*Sözlük · Geliştirme · Son güncelleme: 4 Haziran 2026*

Yazılım uygulamalarının güvenli bir şekilde çalışması için ihtiyaç duyduğu şifreler, API anahtarları ve erişim kodlarıdır.

## Tanım

Secrets, bir programın başka bir sisteme bağlanırken kimliğini doğrulamak için kullandığı gizli bilgilerdir. Bunlar genellikle veritabanı şifreleri, özel anahtarlar veya servis erişim belirteçleri olabilir. Bu bilgilerin kodun içine gömülmesi güvenlik riski oluşturduğu için genellikle özel kasa sistemlerinde saklanır.

*Evinizin kapısını açmak için kullandığınız anahtar gibidir; eğer bu anahtarı paspasın altına koyarsanız herkes içeri girebilir, bu yüzden onu güvenli bir kasada tutmanız gerekir.*

## Nasıl çalışır?

Geliştiriciler bu gizli bilgileri kod dosyalarına yazmak yerine ortam değişkenleri veya gizli yönetim araçları kullanarak uygulamaya güvenli bir şekilde tanımlarlar.

## Nerede kullanılır?

Bulut servislerinde, veritabanı bağlantılarında ve uygulama kimlik doğrulama süreçlerinde kullanılır.

## Sık karıştırılanlar

Normal kullanıcı şifreleri ile karıştırılabilir ancak bunlar insanlar için değil, makineler için tasarlanmış dijital kimliklerdir.

## Sıkça sorulanlar

**Secrets neden kodun içinde tutulmaz?**

Kodunuzu paylaştığınızda veya yanlışlıkla internete yüklediğinizde herkes bu anahtarları ele geçirip sistemlerinize sızabilir.

**Secrets çalınırsa ne yapmalıyım?**

Hemen o anahtarı iptal edip yeni bir tane oluşturmalı ve sisteminize sızma olup olmadığını kontrol etmelisiniz.

## İlgili terimler

- [API](https://trescout.com/dictionary/api/)
- [Self-hosting](https://trescout.com/dictionary/self-hosting/)
- [Observability](https://trescout.com/dictionary/observability/)

## İlgili araçlar

- [Trivy](https://trescout.com/discover/trivy/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/secrets/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
