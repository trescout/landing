# Agentic AI nedir, ne demek?

> Ajanik Yapay Zekâ

**Kategori:** Yapay Zekâ  
**Son güncelleme:** 2026-09-20

Agentic AI (ajanik yapay zekâ), önceden belirlenmiş hedeflere ulaşmak için bağımsız kararlar alabilen, çok adımlı eylemleri planlayan, harici araçları (API) kullanan ve hatalarını düzeltebilen otonom sistemler bütünüdür.

## Etimoloji ve Faillik Paradigması
Agentic AI kavramı, yapay zekâ teknolojisinin pasif bir bilgi verme arayüzünden (Chatbot) aktif bir eylem ve karar alma öznesine (Autonomous Agent) evrilmesini ifade eder. İngilizce 'agency' (faillik, eylemlilik, irade koyma) kelimesinden türeyen bu kavram, kullanıcının yalnızca nihai hedefi belirttiği ve geriye kalan tüm stratejik alt adımları sistemin kendi inisiyatifiyle planlayıp yürüttüğü sistemleri tanımlar.

Geleneksel üretken yapay zekâ sistemleri 'prompt-response' (soru-cevap) döngüsüne hapsolmuştur; bir soru sorulduğunda tek bir metin bloğu üretir ve pasif şekilde bir sonraki komutu bekler. Agentic AI sistemleri ise bir çevre (environment) içinde konumlanır; sensörleri veya veri girişleri aracılığıyla durumu gözlemler, hedefe giden adımları tasarlar, gerek duyduğunda internette arama yapar, kod yazar, veritabanına bağlanır ve karşılaştığı hatalarda rotasını revize ederek sonuca ulaşır.

## Bir Benzetmeyle: Danışmandan Operasyon Direktörüne
Şöyle düşünün: Danışma masasındaki memur ile operasyon direktörü arasındaki farkı hayal edin. Memura (geleneksel LLM) 'Paris biletini nasıl alırım?' derseniz adımları anlatır ve susar; eyleme geçmez. Operasyon direktörüne (Agentic AI) ise 'Bana yarın için en uygun bileti al' dersiniz. Direktör uçuş sitelerine API ile bağlanır, fiyatları karşılaştırır, rezervasyonu yapar ve bileti telefonunuza indirir. Agentic AI, tavsiye veren danışmandan işi bizzat bitiren icracı bir asistana dönüşümdür.

## Teknik Derinlik ve Bilişsel Mimari
Bir Agentic AI mimarisi, bilişsel psikolojiden esinlenen dört temel mühendislik katmanından meydana gelir:

1. Bilişsel Döngü ve Akıl Yürütme (Reasoning & ReAct): Ajanlar hedefe ulaşmak için ReAct (Reasoning + Acting) ve Reflexion döngülerini kullanır. Sistem sırasıyla: Düşünür (Thought) -> Eylem Planlar (Action) -> Eylemi Yürütür -> Sonucu Gözlemler (Observation) -> Gerekirse stratejisini yenileyerek hedefe kadar bu döngüyü sürdürür.

2. Araç Entegrasyonu ve Eylem Katmanı (Tool Use & Function Calling): Ajanların dış dünyayla temas kurabilmesi için REST API'ler, SQL veritabanları, Python kod çalıştırma ortamları (sandboxed REPL) ve web gezintisi yapabilen tarayıcı motorları (Playwright/Puppeteer) tanımlanır. Model Context Protocol (MCP) standardı bu entegrasyonu güvenli hale getirir.

3. Bellek Mimarisi (Memory Systems): Ajanlar iki tür bellek taşır:
- Kısa Vadeli Çalışma Belleği: Devam eden görevin ara adımlarını ve anlık düşünce zincirlerini (scratchpad) context window üzerinde tutar.
- Uzun Vadeli Hafıza: Geçmiş oturumlardan öğrenilen tecrübeleri ve kullanıcı tercihlerini vektör veritabanlarında saklayarak gelecekteki görevlere aktarır.

4. Çoklu Ajan Orkestrasyonu (Multi-Agent Swarms): Karmaşık projelerde tek bir ajan yerine uzmanlaşmış ajan kümeleri (CrewAI, AutoGen, LangGraph) çalışır. Örneğin bir ajan gereksinimleri analiz eder, ikincisi kodu yazar, üçüncüsü güvenlik açığı denetimi (code review) yapar.

5. Model Context Protocol (MCP) ve Standartlaşma:
Ajanların harici araçlarla konuşurken her sağlayıcı için ayrı kod yazma zorunluluğu, Anthropic tarafından geliştirilen açık kaynak Model Context Protocol (MCP) ile aşılmıştır. MCP sayesinde ajanlar dosya sistemlerine, GitHub repolarına veya PostgreSQL veritabanlarına tek tip bir güvenli protokol üzerinden bağlanarak evrensel bir uyumluluk kazanır.

## Sosyolojik Boyut: İş Gücünün Geleceği ve HITL Sorumluluğu
Agentic AI, yazılım mühendisliği ve iş gücü piyasasında köklü bir paradigma değişimini temsil eder. İnsanların bilgisayarlara komut satırıyla veya fareyle tek tek ne yapacağını söylediği mikro-yönetim çağı kapanmakta; insanların yalnızca hedefleri ve etik sınırları belirlediği orkestra şefliği dönemi başlamaktadır.

Ancak bu otonomi devasa güvenlik ve etik sorumluluklar getirir. Kendi kendine finansal işlem yapabilen, sunucularda kod çalıştıran veya sözleşme onaylayan ajanların halüsinasyon görmesi veya yetki sınırlarını aşması felaketlere yol açabilir. Bu nedenle modern mimariler, kritik onay noktalarında insan denetimini şart koşan 'Human-in-the-Loop' (HITL) mekanizmalarını ve katı güvenlik sınırlarını (guardrails) zorunlu kılar.

## Sık Yapılan Hatalar ve Yanılgılar
Agentic AI sistemleri kurulurken en sık karşılaşılan hatalar şunlardır:
- Sonsuz Döngüleri (Infinite Loops) Sınırlandırmamak: Ajanın bir API hatasında veya mantık çıkmazında durmaksızın kendini tekrar etmesi maliyetleri patlatır; maksimum adım sınırı konulmalıdır.
- Aşırı Yetki (Over-Permissioning) Tanımak: Ajanlara korumasız veritabanı silme veya doğrudan para transferi yetkisi vermek siber güvenlik felaketidir; 'salt okunur' veya 'onay gerektiren' sınırlar çizilmelidir.
- Basit Görevler İçin Karmaşık Ajan Kümeleri Kurmak: Tek bir prompt ile çözülebilecek işlerde beş farklı ajanı yarıştırmak gecikmeyi ve hata payını artırır.

## Sıkça Sorulanlar

**Agentic AI ile sıradan bir yapay zekâ sohbet botu (Chatbot) arasındaki temel fark nedir?**  
Sohbet botu pasif olarak sorulara yanıt üretir ve bekler; Agentic AI ise hedefi gerçekleştirmek için kendi kendine alt görevler planlar, araçları (API) çalıştırır ve otonom eyleme geçer.

**ReAct çerçevesi ne anlama gelir?**  
Akıl yürütme (Reasoning) ve Eylem (Acting) kelimelerinden oluşan bu mimari, ajanın her eylem öncesinde düşünmesini, eylem sonucunu gözlemlemesini ve döngüsel olarak kendini düzeltmesini sağlar.

**Human-in-the-Loop (HITL) yaklaşımı neden gereklidir?**  
Kritik veri silme, ödeme yapma veya kamuya mesaj paylaşma gibi geri dönüşü olmayan riskli adımlarda son kararın bir insan onayına bırakılmasını sağlayarak yapay zekâ risklerini önler.

**Çoklu ajan (Multi-Agent) sistemleri neden tek bir ajandan daha başarılıdır?**  
Farklı rollerde (araştırmacı, yazar, denetçi) uzmanlaşmış küçük ajanların birbirinin çıktısını denetlemesi halüsinasyonları azaltır ve karmaşık projelerin parçalara bölünerek çözülmesini sağlar.

## İlgili terimler
- [AI Agent](/dictionary/ai-agent/)
- [LLM](/dictionary/llm/)
- [RAG](/dictionary/rag/)
- [Tools](/dictionary/tools/)
- [MCP](/dictionary/mcp/)
- [Subagents](/dictionary/subagents/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/agentic-ai/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
