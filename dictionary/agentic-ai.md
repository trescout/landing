# Agentic AI nedir, ne demek?

*Sözlük · Yapay Zekâ · Son güncelleme: 20 Eylül 2026*

> Ajanik Yapay Zekâ

Agentic AI (ajanik yapay zekâ), önceden belirlenmiş hedeflere ulaşmak için bağımsız kararlar alabilen, çok adımlı eylemleri planlayan, harici araçları (API) kullanan ve hatalarını düzeltebilen otonom sistemler bütünüdür.

## Etimoloji ve Faillik Paradigması

Agentic AI kavramı, yapay zekâ teknolojisinin pasif bir bilgi verme arayüzünden (Chatbot) aktif bir eylem ve karar alma öznesine (Autonomous Agent) evrilmesini ifade eder. İngilizce 'agency' (faillik, eylemlilik, irade koyma) kelimesinden türeyen bu kavram, kullanıcının yalnızca nihai hedefi belirttiği ve geriye kalan tüm stratejik alt adımları sistemin kendi inisiyatifiyle planlayıp yürüttüğü sistemleri tanımlar.

Geleneksel üretken yapay zekâ sistemleri 'prompt-response' (soru-cevap) döngüsüne hapsolmuştur; bir soru sorulduğunda tek bir metin bloğu üretir ve pasif şekilde bir sonraki komutu bekler. Agentic AI sistemleri ise bir çevre (environment) içinde konumlanır; sensörleri veya veri girişleri aracılığıyla durumu gözlemler, hedefe giden adımları tasarlar, gerek duyduğunda internette arama yapar, kod yazar, veritabanına bağlanır ve karşılaştığı hatalarda rotasını revize ederek sonuca ulaşır.

*Şöyle düşünün: Danışma masasındaki memur ile operasyon direktörü arasındaki farkı hayal edin. Memura (geleneksel LLM) 'Paris biletini nasıl alırım?' derseniz adımları anlatır ve susar; eyleme geçmez. Operasyon direktörüne (Agentic AI) ise 'Bana yarın için en uygun bileti al' dersiniz. Direktör uçuş sitelerine API ile bağlanır, fiyatları karşılaştırır, rezervasyonu yapar ve bileti telefonunuza indirir. Agentic AI, tavsiye veren danışmandan işi bizzat bitiren icracı bir asistana dönüşümdür.*

## Teknik Derinlik ve Bilişsel Mimari

- **Bilişsel Döngü (Reasoning & ReAct):** Ajan Düşün -> Eylem Planla -> Araç Çağır -> Gözlemle döngüsünü hedefe ulaşana kadar dinamik olarak yürütür.

- **Araç Entegrasyonu (Tool Use):** REST API'ler, SQL veritabanları, izole Python çalıştırma ortamları ve tarayıcı otomasyonlarıyla dış dünyada işlem yapar.

- **Bellek Mimarisi:** Anlık düşünce adımları bağlam penceresinde, kalıcı deneyimler ise vektör veritabanlarında epizodik hafıza olarak saklanır.

- **Çoklu Ajan Kümeleri (Multi-Agent Swarms):** Farklı uzmanlıktaki ajanlar (araştırmacı, kod yazıcı, denetçi) birbirini kontrol ederek karmaşık işleri tamamlar.

- **Model Context Protocol (MCP) Standardı:** Ajanların harici servislerle evrensel ve güvenli bir arayüzle konuşması sağlanır.

## Sosyolojik Boyut: İş Gücünün Geleceği ve HITL Sorumluluğu

Agentic AI, yazılım mühendisliği ve iş gücü piyasasında köklü bir paradigma değişimini temsil eder. İnsanların bilgisayarlara komut satırıyla veya fareyle tek tek ne yapacağını söylediği mikro-yönetim çağı kapanmakta; insanların yalnızca hedefleri ve etik sınırları belirlediği orkestra şefliği dönemi başlamaktadır.

Ancak bu otonomi devasa güvenlik ve etik sorumluluklar getirir. Kendi kendine finansal işlem yapabilen, sunucularda kod çalıştıran veya sözleşme onaylayan ajanların halüsinasyon görmesi veya yetki sınırlarını aşması felaketlere yol açabilir. Bu nedenle modern mimariler, kritik onay noktalarında insan denetimini şart koşan 'Human-in-the-Loop' (HITL) mekanizmalarını ve katı güvenlik sınırlarını (guardrails) zorunlu kılar.

## Sık Yapılan Hatalar ve Yanılgılar

- **Sonsuz Döngüleri Önlememek:** Ajanın hata anında kendini durmaksızın tekrar etmesini engellemek için maksimum adım sayısı belirlenmelidir.

- **Aşırı Yetki Vermek:** Veritabanı silme veya finansal transfer gibi eylemlere kontrolsüz yetki vermek güvenlik zaafıdır; salt okunur kısıtlar getirilmelidir.

- **Basit İşlerde Ajan Kullanmak:** Tek bir prompt ile halledilecek görevlerde gereksiz ajan kümeleri kurmak maliyeti ve gecikmeyi artırır.

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

- [AI Agent](https://trescout.com/dictionary/ai-agent/)
- [LLM](https://trescout.com/dictionary/llm/)
- [RAG](https://trescout.com/dictionary/rag/)
- [Tools](https://trescout.com/dictionary/tools/)
- [MCP](https://trescout.com/dictionary/mcp/)
- [Subagents](https://trescout.com/dictionary/subagents/)

## İlgili araçlar

- [Personal_AI_Infrastructure](https://trescout.com/discover/personal-ai-infrastructure/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/agentic-ai/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
