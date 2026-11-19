# Virtual DOM nedir?

*Geliştirme · Son güncelleme: 19 Kasım 2026*

Gerçek web sayfası yapısının bellekte tutulan hafif bir kopyası üzerinden güncellemeleri yöneten teknik.

## Tanım

Sanal DOM, bir web sayfasında değişiklik olduğunda tüm sayfayı baştan yüklemek yerine sadece değişen kısmı tespit edip gerçeğe yansıtmak için kullanılan bir performans optimizasyonudur. Bellek üzerinde çalışan bu hafif kopya sayesinde tarayıcı yorulmaz ve sayfalar çok daha akıcı çalışır.

*Bir kitabı kaleme almadan önce karalama defterine kurşun kalemle taslak çizmek gibidir. Hataları ve değişiklikleri taslak üzerinde yapıp temizledikten sonra asıl kitaba tek seferde geçirirsiniz.*

## Nasıl çalışır?

Uygulama içinde bir veri değiştiğinde sistem önce sanal DOM üzerinde yeni bir ağaç oluşturur. Eski ağaç ile yeni ağacı karşılaştırarak aradaki farkı bulur ve sadece o küçük farkı gerçek DOM üzerine aktararak tarayıcının iş yükünü hafifletir.

## Nerede kullanılır?

Modern arayüz kütüphanelerinde ve tek sayfalık web uygulamalarının performans yönetiminde temel araç olarak görev yapar.

## Sık karıştırılanlar

Tarayıcının kendi ana DOM yapısıyla karıştırılabilir. Sanal DOM tamamen bellekte yaşayan ve geçici olan bir optimizasyon katmanıdır.

## Sorular ve yanıtlar

**Her web sitesinde sanal DOM var mıdır?**

Hayır, genellikle React gibi modern ve gelişmiş arayüz kütüphaneleri kullanan projelerde bulunur.

**Gerçek DOM'dan daha mı hızlıdır?**

Doğrudan DOM değiştirmek maliyetli olduğu için sanal karşılaştırma yapmak genellikle web sitesini hızlandırır.

## İlgili terimler

- [DOM](https://trescout.com/dictionary/dom/)
- [Frontend](https://trescout.com/dictionary/frontend/)
- [Framework](https://trescout.com/dictionary/framework/)

## İlgili araçlar

- [Solid](https://trescout.com/discover/solid/)

Bu açıklama TreScout için yapay zekâ ile sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/virtual-dom/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
