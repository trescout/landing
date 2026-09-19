# Google Java Style Guide nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-20

Google Java Style Guide, Google tarafından açık kaynak ve kurumsal Java projelerinde kod okunabilirliğini, tutarlılığını ve bakım kolaylığını sağlamak amacıyla belirlenmiş resmi kodlama standartları bütünüdür.

## Etimoloji ve Kurumsal Kod Standartları
Google Java Style Guide, dünyanın en büyük teknoloji şirketlerinden biri olan Google'ın on binlerce mühendisinin aynı kod tabanında sorunsuz çalışabilmesi için geliştirdiği kurallar bütünüdür. İlk yayınlandığı günden bu yana yalnızca Google içinde değil, küresel açık kaynak ekosisteminde ve kurumsal yazılım dünyasında da de facto bir standart haline gelmiştir.

Kılavuz; kaynak dosya yapısından paket bildirimlerine, girintileme kurallarından sınıf ve değişken adlandırma konvansiyonlarına, Javadoc biçimlendirmesinden hata yönetimine kadar bir Java dosyasının sahip olması gereken tüm biçimsel ve yapısal sınırları çizer. Bir yazılım projesinde herkesin kendi kişisel zevkine göre boşluk bırakması veya parantez açması, kod incelemelerinde (code review) gereksiz tartışmalara ve zaman kaybına yol açar. Google Java Style Guide, bu sübjektif tartışmaları ortadan kaldırarak geliştiricilerin yalnızca iş mantığına (business logic) odaklanmasını sağlar.

## Bir Benzetmeyle: Otoyol Trafik Kuralları
Şöyle düşünün: Trafik kurallarının bulunmadığı, her sürücünün kafasına göre şerit değiştirdiği bir otoyol hayal edin; böyle bir yolda kaza kaçınılmazdır. Standart bir stil kılavuzu ise otoyolun şerit çizgileri ve trafik ışıkları gibidir. Binlerce mühendis aynı kod tabanında çalışırken, kurallara uyulduğu sürece kimse kimseye çarpmaz. Yeni bir projeye dahil olan geliştirici yabancılık çekmez; çünkü kodun ritmi ve yapısı evrensel kurallarla dokunmuştur.

## Teknik Derinlik ve Temel Kurallar
Google Java Style Guide'ın temel teknik sütunları ve getirdiği kesin kurallar şunlardır:

1. Kaynak Dosya Yapısı ve Girintileme (Indentation):
- Kaynak dosyalar her zaman UTF-8 olarak kodlanır.
- Girintileme için kesinlikle sekme (tab) karakteri kullanılmaz; her blok seviyesinde tam olarak iki (2) boşluk (spaces) kullanılır.
- Satır uzunluğu kural olarak 100 karakteri aşamaz (URL'ler veya Javadoc bağlantıları gibi bölünemeyen yapılar hariç).
- Parantez yerleşimi K&R (Kernighan & Ritchie) stiline uygundur; açılış süslü parantezi `{` satırın sonunda yer alır, yeni satıra geçmez.

2. İçe Aktarma (Imports) Kuralları:
- Joker karakterli içe aktarmalar (`import java.util.*;`) kesinlikle yasaktır; her sınıf açıkça tek tek içe aktarılmalıdır.
- İçe aktarmalar alfabetik sırayla sıralanır; statik içe aktarmalar (static imports) tek bir blok halinde en üstte yer alır.

3. İsimlendirme Konvansiyonları (Naming Conventions):
- Sınıf isimleri `UpperCamelCase` (örneğin `CustomerService`), metot ve değişken isimleri `lowerCamelCase` (örneğin `calculateTotalAmount`) kuralına uyar.
- Sabitler (constants) büyük harf ve alt çizgiyle (`CONSTANT_CASE`) yazılır.
- Kısaltmalarda yalnızca ilk harf büyük tutulur; örneğin `XMLHTTPRequest` yerine `XmlHttpRequest` yazılır.

4. Savunmacı Kodlama ve Biçimlendirme Otomasyonu:
- Geçersiz kılınan tüm metotlarda `@Override` notasyonu zorunludur.
- Yakalanan istisnalar (exceptions) asla boş bırakılamaz; bilinçli olarak yoksayılacaksa yorum satırıyla (`// expected`) gerekçelendirilmelidir.
- Bu kurallar `google-java-format` CLI aracı, Checkstyle ve Spotless gibi eklentilerle derleme aşamasında (CI/CD) otomatik olarak denetlenir.

5. Javadoc ve Yorum Standartları:
Her genel (public) sınıf, arayüz veya enum için Javadoc açıklaması yazılması zorunludur. Javadoc bloklarında HTML biçimlendirmesi (`<p>`, `<code>`, `<ul>`) temiz tutulur; `@param`, `@return` ve `@throws` etiketleri sırasıyla yazılır ve asla boş açıklamalarla bırakılmaz. Kod bloklarında ise geçici yorumlar yerine temiz metot ayrıştırmaları tercih edilir.

## Sosyolojik Boyut: Okunabilirlik ve Ekip Verimliliği
Yazılım mühendisliğinde yapılan araştırmalar, bir geliştiricinin zamanının yüzde 80'inden fazlasını yeni kod yazmakla değil, mevcut kodu okumakla geçirdiğini göstermektedir. Dolayısıyla okunabilirlik, yazma kolaylığından çok daha değerlidir. 

Google Java Style Guide, geliştiricilerin kod üzerindeki kişisel ego ve estetik kaygılarını geride bırakıp ekibin ortak üretkenliğini öncelemesini sağlar. Açık kaynak dünyasında dışarıdan katkı (pull request) kabul eden projeler için bu kılavuz, katkıcıların projeye zahmetsizce uyum sağlamasını güvence altına alan evrensel bir anlaşma metnidir.

## Sık Yapılan Hatalar ve Yanılgılar
Google Java stilini uygularken en sık yapılan hatalar şunlardır:
- Biçimlendirmeyi Elle Yapmaya Çalışmak: Geliştiricilerin boşlukları tek tek sayarak vakit kaybetmesi büyük bir hatadır; IDE'ye `google-java-format` eklentisi kurulmalı ve kaydetme anında otomatik formatlama devreye alınmalıdır.
- Checkstyle Uyarılarını CI/CD'de Devre Dışı Bırakmak: Süreç sıkıştığında stil kontrollerini atlamak, zamanla kod tabanında stil kirliliğine ve teknik borca yol açar.
- Yorum Satırlarında Aşırıya Kaçmak: Kılavuz, kodun kendisini açıklaması gerektiğini savunur; apaçık görünen getter/setter metotlarına formalite icabı anlamsız Javadoc yazmak gereksizdir.

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
- [Sun Code Conventions](/dictionary/sun-code-conventions/)
- [Code Snippets](/dictionary/code-snippets/)
- [Refactoring](/dictionary/refactoring/)
- [QA](/dictionary/qa/)
- [Production Pipeline](/dictionary/production-pipeline/)
- [TDD](/dictionary/tdd/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/google-java-style-guide/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
