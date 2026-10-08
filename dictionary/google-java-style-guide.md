# Google Java Style Guide nedir, ne demek?

*Sözlük · Geliştirme · Son güncelleme: 20 Eylül 2026*

Google Java Style Guide, Google tarafından açık kaynak ve kurumsal Java projelerinde kod okunabilirliğini, tutarlılığını ve bakım kolaylığını sağlamak amacıyla belirlenmiş resmi kodlama standartları bütünüdür.

## Etimoloji ve Kurumsal Kod Standartları

Google Java Style Guide, dünyanın en büyük teknoloji şirketlerinden biri olan Google'ın on binlerce mühendisinin aynı kod tabanında sorunsuz çalışabilmesi için geliştirdiği kurallar bütünüdür. İlk yayınlandığı günden bu yana yalnızca Google içinde değil, küresel açık kaynak ekosisteminde ve kurumsal yazılım dünyasında da de facto bir standart haline gelmiştir.

Kılavuz; kaynak dosya yapısından paket bildirimlerine, girintileme kurallarından sınıf ve değişken adlandırma konvansiyonlarına, Javadoc biçimlendirmesinden hata yönetimine kadar bir Java dosyasının sahip olması gereken tüm biçimsel ve yapısal sınırları çizer. Bir yazılım projesinde herkesin kendi kişisel zevkine göre boşluk bırakması veya parantez açması, kod incelemelerinde (code review) gereksiz tartışmalara ve zaman kaybına yol açar. Google Java Style Guide, bu sübjektif tartışmaları ortadan kaldırarak geliştiricilerin yalnızca iş mantığına (business logic) odaklanmasını sağlar.

*Şöyle düşünün: Trafik kurallarının bulunmadığı, her sürücünün kafasına göre şerit değiştirdiği bir otoyol hayal edin; böyle bir yolda kaza kaçınılmazdır. Standart bir stil kılavuzu ise otoyolun şerit çizgileri ve trafik ışıkları gibidir. Binlerce mühendis aynı kod tabanında çalışırken, kurallara uyulduğu sürece kimse kimseye çarpmaz. Yeni bir projeye dahil olan geliştirici yabancılık çekmez; çünkü kodun ritmi ve yapısı evrensel kurallarla dokunmuştur.*

## Teknik Derinlik ve Temel Kurallar

- **Kaynak Dosya Yapısı ve Girinti:** Dosyalar her zaman UTF-8 kodlanır. Girintileme için sekme (tab) yerine tam iki (2) boşluk kullanılır. Satır uzunluğu 100 karakterle sınırlıdır; parantezler K&R stiline göre satır sonunda yer alır.

- **İçe Aktarma (Imports) Standartları:** Jokerli içe aktarmalar (`import java.util.*;`) yasaktır. Her sınıf tek tek açıkça içe aktarılır ve alfabetik olarak sıralanır.

- **İsimlendirme Konvansiyonları:** Sınıflar `UpperCamelCase`, metot ve değişkenler `lowerCamelCase`, sabitler `CONSTANT_CASE` ile adlandırılır. Kısaltmalarda yalnızca ilk harf büyük tutulur (`XmlHttpRequest`).

- **Savunmacı Programlama ve Otomasyon:** Geçersiz kılınan metotlarda `@Override` zorunludur. Boş bırakılan catch blokları yasaktır. Kurallar `google-java-format`, Checkstyle ve Spotless eklentileriyle CI/CD hattında otomatik denetlenir.

- **Javadoc ve Yorum Standartları:** Genel sınıflar için Javadoc açıklaması yazılması şarttır; `@param`, `@return` ve `@throws` etiketleri eksiksiz doldurulur.

## Sosyolojik Boyut: Okunabilirlik ve Ekip Verimliliği

Yazılım mühendisliğinde yapılan araştırmalar, bir geliştiricinin zamanının yüzde 80'inden fazlasını yeni kod yazmakla değil, mevcut kodu okumakla geçirdiğini göstermektedir. Dolayısıyla okunabilirlik, yazma kolaylığından çok daha değerlidir.

Google Java Style Guide, geliştiricilerin kod üzerindeki kişisel ego ve estetik kaygılarını geride bırakıp ekibin ortak üretkenliğini öncelemesini sağlar. Açık kaynak dünyasında dışarıdan katkı (pull request) kabul eden projeler için bu kılavuz, katkıcıların projeye zahmetsizce uyum sağlamasını güvence altına alan evrensel bir anlaşma metnidir.

## Sık Yapılan Hatalar ve Yanılgılar

- **Biçimlendirmeyi Elle Yapmaya Çalışmak:** Boşlukları tek tek saymak yerine IDE'ye `google-java-format` eklentisi kurulmalı ve otomatik kaydetme formatı açılmalıdır.

- **Checkstyle Kurallarını Kapatmak:** Süreç sıkıştığında stil kontrollerini CI/CD'de devre dışı bırakmak teknik borcu büyütür.

- **Yorum Satırlarında Aşırıya Kaçmak:** Kodun kendini açıklaması hedeflenmeli, aşikar getter/setter metotlarına anlamsız yorumlar yazılmamalıdır.

## Sıkça Sorulanlar

**Google Java Style Guide neden 4 boşluk yerine 2 boşluklu girintileme kullanır?**

İki boşluk kuralı, özellikle iç içe geçmiş lambda ifadeleri, anonim sınıflar ve builder desenlerinde kodun yatayda 100 karakter sınırını aşmasını engeller ve ekran alanını daha verimli kullanır.

**Google Java stil kuralları projelerde otomatik olarak nasıl uygulanır?**

Google tarafından sağlanan 'google-java-format' aracı IDE'lere (IntelliJ, Eclipse, VS Code) entegre edilir ya da Spotless/Maven/Gradle eklentileriyle kod kaydetme ve CI derleme aşamasında otomatik formatlanır.

**Google Java Style Guide ile Oracle (Sun) kodlama kuralları arasındaki fark nedir?**

Sun kuralları 4 boşluklu girinti ve 80 karakter sınırı kullanırken, Google stili 2 boşluk girinti, 100 karakter sınırı, katı import kuralları ve modern araç otomasyonunu merkeze alır.

**Checkstyle ile Google Java Style Guide aynı şey midir?**

Hayır; Google Java Style Guide kurallar dokümanıdır, Checkstyle ise bu kuralları XML formatında yapılandırıp kod tabanında kural ihlallerini denetleyen statik analiz aracıdır.

## İlgili terimler

- [Sun Code Conventions](https://trescout.com/dictionary/sun-code-conventions/)
- [Code Snippets](https://trescout.com/dictionary/code-snippets/)
- [Refactoring](https://trescout.com/dictionary/refactoring/)
- [QA](https://trescout.com/dictionary/qa/)
- [Production Pipeline](https://trescout.com/dictionary/production-pipeline/)
- [TDD](https://trescout.com/dictionary/tdd/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/google-java-style-guide/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
