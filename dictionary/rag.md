# RAG nedir, ne demek?

> Retrieval-Augmented Generation

**Kategori:** Yapay Zekâ Modelleri  
**Son güncelleme:** 2026-09-20

RAG (Retrieval-Augmented Generation - Geri Getirmeyle Zenginleştirilmiş Üretim), büyük dil modellerinin (LLM) harici ve dinamik bir bilgi tabanından alakalı verileri çekerek yanıt üretmesini sağlayan hibrit bir yapay zekâ mimarisidir.

## Etimoloji ve Parametrik Olmayan Bellek
Retrieval-Augmented Generation (RAG) kavramı, ilk olarak 2020 yılında Patrick Lewis ve Meta AI araştırmacıları tarafından yayınlanan makaleyle yapay zekâ literatürüne kazandırılmıştır. Büyük dil modelleri (LLM), eğitimlerinin tamamlandığı an dondurulan parametrik bir belleğe (ağırlıklara) sahiptir. Bu durum iki devasa problem doğurur: Model eğitim tarihinden sonraki güncel olayları bilemez ve eğitim verisinde bulunmayan kurumsal iç belgelere veya özel verilere erişemez. Bu sınırları zorlayan kullanıcılar ise modelin gerçeğe aykırı bilgiler uydurmasıyla, yani halüsinasyon (hallucination) problemiyle karşılaşır.

RAG mimarisi, parametrik bellek (LLM'in dil yeteneği) ile parametrik olmayan belleği (vektör veritabanları, arama motorları ve doküman depoları) birleştirerek bu çıkmazı çözer. Kullanıcı bir soru sorduğunda, sistem önce harici bilgi havuzunda anlamsal bir arama yapar (Retrieval). Bulunan en alakalı metin parçacıkları kullanıcının sorusuyla harmanlanarak modelin bağlam penceresine (context window) yerleştirilir ve model yalnızca bu doğrulanmış kaynaklara dayanarak yanıt üretir (Generation). Böylece sıfırdan model eğitme maliyetine girmeden, güncel ve kaynak gösteren akıllı sistemler inşa edilir.

## Bir Benzetmeyle: Açık Kitap Sınavı
Şöyle düşünün: Tıp fakültesindeki iki sınav senaryosunu hayal edin. Kapalı kitap sınavında öğrenci binlerce sayfalık literatürü ezberden yanıtlar; hatırlayamadığı yerde mantıklı görünen ancak ölümcül olabilecek yanlış bir teşhis uydurabilir (LLM halüsinasyonu). Açık kitap sınavında ise öğrenci kütüphanedeki en güncel tıp ansiklopedisini açar, taze araştırmayı okur ve doğrulanmış veriye atıfla yanıt verir. RAG mimarisi, yapay zekâyı ezbercilikten çıkarıp masasında devasa bir kütüphane bulunan açık kitap araştırmacısına dönüştürür.

## Teknik Derinlik ve Boru Hattı (Pipeline) Mimarisi
Modern bir kurumsal RAG boru hattı (pipeline) beş temel mühendislik adımından meydana gelir:

1. Doküman İşleme ve Parçalama (Chunking): Ham dokümanlar (PDF, Word, Markdown, HTML) temizlenir ve mantıksal metin parçalarına (chunks) bölünür. Parçalama aşamasında sabit karakter sınırları yerine, cümle ve paragraf bütünlüğünü koruyan anlamsal parçalama (semantic chunking) uygulanır.

2. Sayısal Dönüşüm (Embedding) ve İndeksleme: Her metin parçası bir embedding modeli (Cohere, OpenAI, BGE vb.) aracılığıyla yüksek boyutlu sayısal vektörlere dönüştürülür ve bir vektör veritabanına (Qdrant, Milvus, pgvector) kaydedilir.

3. Hibrit Arama (Hybrid Search): Kullanıcı sorgusu geldiğinde yalnızca anlamsal vektör araması (Dense Retrieval) değil, aynı zamanda anahtar kelime eşleşmesi yapan BM25 algoritması (Sparse Retrieval) birlikte koşturulur. Bu iki arama sonucu Reciprocal Rank Fusion (RRF) ile birleştirilerek hem anlamsal benzerlik hem de teknik terim tutarlılığı yakalanır.

4. Yeniden Sıralama (Re-ranking): İlk aşamada getirilen yüzlerce parça arasından en kritik olanları seçmek için bir Cross-Encoder Re-ranker modeli çalıştırılır. Parçalar bağlam alaka düzeyine göre milisaniyeler içinde elenerek ilk 3-5 parçaya indirilir.

5. Bağlam Enjeksiyonu ve Doğrulanmış Üretim: Seçilen kaynak parçalar sistem komutuna (prompt) 'Yalnızca verilen metne dayanarak yanıtla ve kaynak belirt' talimatıyla iliştirilir. LLM yanıtını üretirken dipnotlar ve kaynak linkleri ekler.

## Sosyolojik Boyut: Bilginin Demokratikleşmesi ve Şeffaflık
RAG teknolojisi, yapay zekânın kurumsal dünyaya güvenli adaptasyonundaki en büyük eşiktir. Milyonlarca dolarlık bütçeler gerektiren model eğitimi (pre-training) ve ince ayar (fine-tuning) süreçleri yalnızca küresel teknoloji devlerinin tekelindeyken, RAG mimarisi küçük bir işletmenin veya bireysel bir araştırmacının dahi kendi verileriyle güçlü bir yapay zekâ asistanı kurmasını mümkün kılarak teknolojiyi demokratikleştirmiştir.

Bunun da ötesinde RAG, yapay zekâda şeffaflık ve denetlenebilirlik (explainability) sağlar. Kara kutu olarak çalışan modellerin aksine, RAG sistemlerinin ürettiği her iddianın dayandığı orijinal PDF sayfası veya veritabanı kaydı açıkça doğrulanabilir. Bu nitelik, hukuk, sağlık ve finans gibi sıfır hata toleransına sahip sektörlerde yapay zekânın yasal ve etik kabulünü sağlayan temel güvencedir.

## Sık Yapılan Hatalar ve Yanılgılar
RAG mimarilerinde en sık karşılaşılan sistemik hatalar şunlardır:
- Kötü Parçalama (Chunking) Stratejisi: Metinleri cümle ortasından rastgele bölmek bağlam kaybına yol açar ve retrieval kalitesini çözer.
- Yeniden Sıralamayı (Re-ranking) Atlamak: Vektör benzerliği her zaman anlamsal doğruluk demek değildir; cross-encoder olmadan doğrudan ilk gelen parçaları prompta basmak halüsinasyonu tetikler.
- Kayıp Ortada (Lost-in-the-Middle) Fenomenini Unutmak: LLM'ler uzun bağlam pencerelerinin ortasında kalan bilgileri gözden kaçırabilir; en kritik kaynak parçalar promptun en başına veya en sonuna yerleştirilmelidir.

## Sıkça Sorulanlar

**RAG ile Fine-Tuning (İnce Ayar) arasındaki temel fark nedir?**  
Fine-Tuning modele yeni bir üslup, format veya uzmanlık kazandırmak için ağırlıklarını güncellerken; RAG modelin ağırlıklarına dokunmadan harici ve güncel verileri dinamik bağlam olarak sunar.

**RAG mimarisinde halüsinasyon riski tamamen sıfırlanır mı?**  
Tamamen sıfırlanmaz ancak büyük oranda azalır; modelin yalnızca bağlamda verilen kaynaklara dayanarak yanıt vermesi sağlandığında ve sıkı sistem komutları uygulandığında uydurma bilgi riski minimuma iner.

**GraphRAG nedir ve geleneksel vektör tabanlı RAG'den ne farkı vardır?**  
GraphRAG metinleri yalnızca vektör olarak değil, bilgi grafı (Knowledge Graph) şeklinde varlıklar ve ilişkiler ağı olarak modeller; böylece parçalı belgeler arasındaki karmaşık mantıksal bağlantıları çok daha iyi çözer.

**RAG sistemi kurmak için hangi bileşenler gereklidir?**  
Doküman ayrıştırıcılar, metin parçalama araçları, bir embedding modeli, vektör veritabanı, opsiyonel bir yeniden sıralama (re-ranker) modeli ve nihai yanıtı üretecek bir LLM gerekir.

## İlgili terimler
- [LLM](/dictionary/llm/)
- [Vector Database](/dictionary/vector-database/)
- [Embedding](/dictionary/embedding/)
- [Hallucination](/dictionary/hallucination/)
- [Context Window](/dictionary/context-window/)
- [Agentic AI](/dictionary/agentic-ai/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/rag/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
