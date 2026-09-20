# Plugin nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Plugin (eklenti), bir yazılımın çekirdek kodunu değiştirmeden veya yeniden derlemeye gerek kalmadan sisteme yeni yetenekler, araçlar ve işlevler kazandıran bağımsız modüler yazılım bileşenidir.

## Kavramsal köken ve mimari felsefe
"Plugin" terimi İngilizce "plug in" (fişe takmak, prize bağlamak) eyleminden türemiştir. Tıpkı bir ses amfisine bağlanan efekt pedalı ya da bilgisayara USB ile takılan bir donanım gibi, yazılıma da ihtiyaç duyulduğunda takılıp çıkarılabilen modülleri ifade eder.

Yazılım mimarisinde plugin felsefesi, nesne yönelimli programlamanın temel yapı taşlarından biri olan **Açık/Kapalı Prensibi'ne (Open-Closed Principle - OCP)** dayanır: *"Bir yazılım varlığı (sınıf, modül, fonksiyon) genişletilmeye açık, ancak değiştirilmeye kapalı olmalıdır."* 

Bu yaklaşım sayesinde ana platform (çekirdek), binlerce farklı özelliğin ağırlığı altında hantallaşmak (bloatware) yerine hafif ve kararlı kalır; kullanıcılar ve üçüncü taraf geliştiriciler ise sistemi kendi ihtiyaçlarına göre özelleştirebilir.

## Mikroçekirdek (Microkernel) mimarisi ve çalışma prensibi
Plugin tabanlı sistemler genellikle **Mikroçekirdek Mimarisi (Microkernel Pattern)** ile inşa edilir. Bu mimaride sistem iki ana parçadan oluşur:

1. **Çekirdek Sistem (Core System):** Uygulamanın çalışması için gereken asgari mantığı, yaşam döngüsü yönetimini ve eklenti kayıt defterini (plugin registry) barındırır.
2. **Eklenti Modülleri (Plug-in Modules):** Çekirdeğin sunduğu kancalar (hooks) ve uygulama arayüzleri (API) üzerinden sisteme bağlanan, bağımsız geliştirilen bileşenlerdir.

### İletişim mekanizmaları:
- **Kancalar (Hooks):** Olay tabanlı sistemlerde eklentiler, sistemin belirli anlarına kanca atar (örneğin WordPress'teki Action ve Filter hook'ları).
- **Servis Sağlayıcı Arayüzü (SPI):** Java ve kurumsal sistemlerde eklentiler standart arayüzleri (`interface`) uygulayarak sisteme entegre olur.
- **Yalıtım ve Güvenlik (Sandboxing):** Modern eklenti sistemleri (örneğin Figma veya modern tarayıcılar), eklentilerin ana bellek alanına doğrudan erişmesini engellemek için WebAssembly (WASM), Web Workers veya izole süreçler (process isolation) kullanır.

## Benzer kavramlar: Plugin, Extension, Add-on ve Mod
Yazılım ekosisteminde bu terimler sıklıkla birbirinin yerine kullanılsa da nüansları vardır:
- **Plugin:** Genellikle ana uygulamanın hesaplama, format dönüştürme veya veri işleme yeteneklerini derinlemesine artıran modüllerdir (ör. Photoshop filtreleri, ses prodüksiyonunda VST ses efektleri).
- **Extension:** Kullanıcı arayüzünü (UI) ve kullanıcı deneyimini özelleştiren, mevcut özellikleri zenginleştiren eklentilerdir (ör. Chrome Uzantıları, VS Code Extensions).
- **Add-on:** Çoğunlukla açık kaynaklı veya topluluk yazılımlarında ek paketleri tanımlamak için kullanılan genel bir şemsiye terimdir (ör. Blender Add-ons).
- **Mod:** Oyun dünyasında (özellikle Minecraft gibi) oyun mekaniklerini, grafiklerini ve mantığını değiştiren kullanıcı yapımı eklentilerdir.

## Yapay zeka çağında eklentiler ve Model Context Protocol (MCP)
Yapay zeka devrimiyle birlikte eklenti mimarisi yepyeni bir boyut kazanmıştır. Büyük dil modelleri (LLM) kapalı birer bilgi deposu olmaktan çıkıp, eklentiler ve "Araç Çağırma" (Tool/Function Calling) mekanizmaları sayesinde web'de arama yapabilen, veritabanı sorgulayabilen ve API'ler üzerinden eyleme geçebilen otonom ajanlara dönüşmüştür. Anthropic'in geliştirdiği **Model Context Protocol (MCP)**, LLM'lerin farklı veri kaynaklarına ve araçlara standart bir eklenti protokolüyle bağlanmasını sağlayarak modern eklenti mimarisinin en güncel örneğini oluşturmaktadır.

## Bir benzetmeyle
Bir müzisyenin elektro gitar amfisini düşünün: Amfinin kendisi temel ses yükseltme görevini üstlenir (çekirdek). Müzisyen amfi ile gitar arasına distortion, chorus veya delay pedalları takarak (plugin) amfinin devrelerine hiç dokunmadan sınırsız sayıda yeni ses tonu elde edebilir.

## Sıkça sorulanlar

**Plugin ne demek ve Türkçe karşılığı nedir?**  
İngilizce "plug in" (takmak) kökünden gelir ve Türkçede "eklenti" olarak adlandırılır. Bir ana yazılıma ek işlevler kazandıran bağımsız yazılım parçasıdır.

**Eklentiler performans düşüşüne veya güvenlik açığına yol açar mı?**  
Evet. Kötü optimize edilmiş eklentiler aşırı bellek ve CPU tüketebilir. Ayrıca üçüncü taraf eklentiler tedarik zinciri saldırılarına (supply chain attacks) açık kapı bırakabileceğinden yalnızca güvenilir kaynaklardan yüklenmelidir.

**Plugin ile Extension arasındaki fark nedir?**  
Plugin terimi daha çok uygulamanın çekirdek yeteneklerini ve veri motorunu genişleten modülleri (ör. ses/görüntü filtreleri) ifade ederken; Extension çoğunlukla arayüzü ve kullanıcı etkileşimini geliştiren eklentiler için tercih edilir.

**Model Context Protocol (MCP) eklenti midir?**  
MCP, yapay zeka modellerinin harici araçlar, veritabanları ve servislerle konuşmasını standartlaştıran açık bir eklenti protokolüdür.

## İlgili terimler
- [SDK](/dictionary/sdk/)
- [API](/dictionary/api/)
- [LSP](/dictionary/lsp/)
- [MCP](/dictionary/mcp/)
- [Bundler](/dictionary/bundler/)
- [Runtime](/dictionary/runtime/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/plugin/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
