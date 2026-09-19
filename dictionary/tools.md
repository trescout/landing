# Tools ne demek, nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Tools (araçlar), yapay zekâ modellerinin ve yazılımların harici fonksiyonları, API'leri veya veritabanlarını çağırarak dünyayla etkileşime girmesini sağlayan yeteneklerdir.

## Tanım ve LLM dünyasındaki rolü
Yapay zekâ ve büyük dil modellerinde (LLM) 'Tools' (Araçlar), modelin kendi iç ağırlıklarıyla sınırlı kalmayıp gerçek dünyadaki sistemlerle eyleme geçmesini sağlayan fonksiyonel köprülerdir. Normalde bir dil modeli sadece metin üretebilir; ancak bir 'tool' verildiğinde internette güncel arama yapabilir, Python kodu çalıştırabilir, veritabanına sorgu atabilir veya bir GitHub reposunda issue açabilir. Bu dönüşüm, LLM'leri pasif metin üreteçlerinden otonom ajanlara (AI Agent) dönüştürür.

## Bir benzetmeyle
Bir usta düşünün: Teorik bilgisi ne kadar geniş olursa olsun, çekiç, tornavida veya metre gibi el aletleri (tools) olmadan bir masayı tamir edemez. Yapay zekâ için araçlar da modelin eline verilen bu dijital alet çantasıdır.

## Nasıl çalışır? (Function Calling)
1. **Araç Tanımı:** Geliştirici, modelin kullanabileceği fonksiyonu JSON Schema formatında (adı, açıklaması ve parametreleri) modele tanıtır.
2. **Kullanım Kararı:** Kullanıcının sorusunu analiz eden model, iç mantığıyla bu soruyu doğrudan yanıtlamak yerine bir aracı çağırması gerektiğine karar verir.
3. **Fonksiyon Çağrısı:** Model doğrudan kodu çalıştırmaz; çalıştırılması gereken aracın adını ve argümanlarını JSON olarak geri döner.
4. **Yürütme ve Yanıt:** Sunucu veya istemci kodu çalıştırır, sonucu modele geri iletir ve model nihai yanıtı kullanıcıya sunar.

## Nerede kullanılır?
Ajan mimarilerinde (AI Agent), model bağlam protokollerinde (MCP), kodlama asistanlarında (Cursor, Antigravity) ve RAG (Retrieval-Augmented Generation) sistemlerinde kullanılır.

## Sık karıştırılanlar
- **Tool vs Plugin:** Bir tool genellikle tek bir amaca hizmet eden spesifik bir fonksiyon çağrısıdır (örneğin hava durumu sorgulama); plugin ise birden çok aracı ve kullanıcı arayüzünü içinde barındıran daha geniş bir eklenti paketidir.

## Sıkça sorulanlar

**Tools ne demek ve Türkçe karşılığı nedir?**  
İngilizce 'araçlar / gereçler' anlamına gelir. Yazılımda sistemin işlevini yerine getirmek için kullandığı yardımcı kütüphane ve fonksiyonları temsil eder.

**Yapay zekâ modelleri aracı rastgele mi çağırır?**  
Hayır, modelin sistem yönergesine (system prompt) ve kullanıcının prompt'una göre en uygun aracı seçebilmesi için araç açıklamalarının (tool description) son derece net ve açık yazılması gerekir.

**Model Context Protocol (MCP) araç kullanımını nasıl değiştirdi?**  
Anthropic tarafından geliştirilen MCP, her yapay zekâ modeli için ayrı ayrı araç entegrasyonu yazma zorunluluğunu kaldırarak; araçların ve veri kaynaklarının evrensel bir protokolle tüm yapay zekâ sistemlerine bağlanmasını sağladı.

## İlgili terimler
- [MCP](/dictionary/mcp/)
- [AI Agent](/dictionary/ai-agent/)
- [Plugin](/dictionary/plugin/)
- [SDK](/dictionary/sdk/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/tools/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
