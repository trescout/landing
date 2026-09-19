# Plugin nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Plugin (eklenti), bir yazılımın çekirdek koduna dokunmadan ona yeni işlevler, araçlar ve yetenekler kazandıran bağımsız yazılım modülüdür.

## Tanım ve mimarisi
Plugin (Türkçe adıyla eklenti), ana bir yazılım uygulamasının yeteneklerini dinamik olarak genişletmek için tasarlanmış bağımsız yazılım bileşenidir. Uygulamaların monolitik ve hantal bir yapıya dönüşmesini engeller; çekirdek sistemi hafif ve yalın tutarken kullanıcının ihtiyacına göre eklentilerle kişiselleştirilmesine olanak tanır. Tarayıcılardan kod editörlerine (VS Code eklentileri), içerik yönetim sistemlerinden (WordPress eklentileri) yapay zekâ araçlarına kadar modern yazılım mimarilerinin merkezindedir.

## Bir benzetmeyle
Bir akıllı telefonu düşünün: Telefonun işletim sistemi ana programdır; uygulama mağazasından indirdiğiniz her bir bağımsız uygulama ise telefonunuza yeni yetenekler kazandıran birer eklenti gibidir. Cihazın fabrika donanımını sökmeden istediğiniz özelliği takıp çıkarabilirsiniz.

## Nasıl çalışır?
1. **API ve Kanca (Hook) Arayüzleri:** Ana yazılım, dış modüllerin entegre olabilmesi için standart uygulama geliştirme arayüzleri (API) ve olay kancaları sunar.
2. **Yalıtım ve İzinler:** Modern platformlar, güvenlik amacıyla eklentileri sandbox (yalıtılmış alan) içinde çalıştırarak sistem kaynaklarına kontrollü erişim verir.
3. **Dinamik Yükleme:** Ana program yeniden derlenmeye veya baştan kurulmaya gerek kalmadan eklentiyi çalışır duruma getirebilir.

## Nerede kullanılır?
Web tarayıcılarında (Chrome, Firefox eklentileri), modern IDE ve kod editörlerinde (VS Code, Neovim), tasarım araçlarında (Figma) ve büyük dil modellerinin internete bağlanmasını sağlayan yapay zekâ platformlarında kullanılır.

## Sıkça sorulanlar

**Plugin ne demek ve Türkçe karşılığı nedir?**  
İngilizce 'plug in' (fişe takmak, bağlamak) deyiminden türemiştir; Türkçede 'eklenti' olarak adlandırılır. Bir sisteme tak-çıkar mantığıyla özellik eklemeyi ifade eder.

**Plugin ile Extension arasındaki fark nedir?**  
Günlük kullanımda sıklıkla birbirinin yerine geçer. Ancak teknik olarak 'plugin' genellikle ana uygulamanın alt motorunu ve veri işleme yeteneklerini genişleten derin kütüphaneleri ifade ederken; 'extension' kullanıcı arayüzünü (UI) ve deneyimini özelleştiren eklentiler için kullanılır.

**Eklentiler sistem güvenliğini ve hızını nasıl etkiler?**  
Kaynağı doğrulanmamış eklentiler güvenlik açığı yaratabilir veya aşırı bellek tüketerek ana uygulamayı yavaşlatabilir. Bu yüzden yalnızca güvenilir pazar yerlerinden (marketplace) yüklenmeli ve gereksiz eklentiler kaldırılmalıdır.

## İlgili terimler
- [SDK](/dictionary/sdk/)
- [API](/dictionary/api/)
- [LSP](/dictionary/lsp/)
- [AI Code Editor](/dictionary/ai-code-editor/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/plugin/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
