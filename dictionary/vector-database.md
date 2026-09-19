# Vector Database nedir, ne demek?

> Vektör Veritabanı

**Kategori:** Veri & Altyapı  
**Son güncelleme:** 2026-09-20

Vector Database (vektör veritabanı), yüksek boyutlu sayısal vektörleri (embeddings) depolamak, indekslemek ve aralarındaki anlamsal benzerlik mesafelerini milisaniyeler içinde sorgulamak için tasarlanmış özel veritabanı mimarisidir.

## Etimoloji ve Çok Boyutlu Anlamsal Uzay
Vektör Veritabanı (Vector Database), modern yapay zekâ ve derin öğrenme ekosisteminin veri depolama katmanındaki en kritik bileşenidir. Geleneksel ilişkisel veritabanları (RDBMS) ve NoSQL sistemleri, verileri tam eşleşme (örneğin `WHERE id = 5` veya `name LIKE '%Ali%'`) ve katı hiyerarşiler üzerinden sorgulamak için optimize edilmiştir. Ancak yapay zekâ çağında karşılaşılan verilerin büyük çoğunluğu (metinler, fotoğraflar, sesler, videolar) yapılandırılmamış (unstructured) niteliktedir.

Derin öğrenme modelleri bu yapılandırılmamış verileri anlamlandırabilmek için 'embedding' adı verilen yüzlerce veya binlerce boyuttan oluşan sayısal vektör dizilerine dönüştürür. Vektör veritabanları, bu devasa çok boyutlu uzayda milyonlarca hatta milyarlarca veri noktası arasındaki geometrik mesafeleri hesaplar. Bu sayede 'anlamca birbirine en yakın olan' verileri (Nearest Neighbor Search) geleneksel arama yöntemlerinin imkânsız gördüğü hızlarda bulup çıkarır.

## Bir Benzetmeyle: Anlam Galaksisindeki Yıldız Haritası
Şöyle düşünün: Milyonlarca kitabın yalnızca alfabetik yazar adına göre dizildiği bir kütüphane klasik SQL veritabanıdır. 'Bana yalnızlık hissini anlatan, sonbahar hüznü taşıyan ve Dostoyevski tarzı romanları getir' derseniz, klasik katalog kilitlenir çünkü kapaklarda bu kelimeler geçmeyebilir. Vektör veritabanı ise kitapları devasa bir galakside konumlandırmak gibidir. Hüzünlü kitaplar belirli bir yıldız kümesinde toplanır, bilimkurgu maceraları başka bir kolda yer alır. Bir duyguyla geldiğinizde sistem galaksideki en yakın komşu yıldızları milisaniyelerde bulur.

## Teknik Derinlik ve İndeksleme Mimarisi
Teknik düzeyde bir vektör veritabanının yüksek performans sağlaması üç temel mimari sütuna dayanır:

1. Mesafe Metrikleri (Distance Metrics): İki vektör arasındaki anlamsal benzerliği ölçmek için geometrik formüller kullanılır:
- Kosinüs Benzerliği (Cosine Similarity): İki vektör arasındaki açıyı ölçer; uzunluktan bağımsız olarak yön benzerliğine odaklandığı için metin ve dil modellerinde standarttır.
- Öklid Mesafesi (Euclidean / L2): İki nokta arasındaki doğrudan fiziksel uzaklığı hesaplar; görüntü işleme ve yüz tanıma sistemlerinde yaygındır.
- Nokta Çarpım (Dot Product): Vektörlerin hem yönünü hem büyüklüğünü dikkate alır; normalize edilmiş modellerde çok hızlıdır.

2. Yaklaşık En Yakın Komşu (ANN) ve İndeksleme: Milyonlarca vektör arasında kaba kuvvetle (brute-force) tüm mesafeleri hesaplamak sorgu sürelerini felç eder. Bu nedenle Yaklaşık En Yakın Komşu (Approximate Nearest Neighbor - ANN) algoritmaları kullanılır:
- HNSW (Hierarchical Navigable Small World): Vektörleri çok katmanlı bir grafik ağı üzerinde bağlar; sorgu anında üst katmanlardan hızlı sıçramalarla en yakın düğüme milisaniyelerde iner.
- IVF (Inverted File Index): Vektör uzayını Voronoi hücrelerine böler ve aramayı yalnızca ilgili hücrelerle sınırlandırır.

3. Hibrit Depolama ve Metaveri Filtreleme (Metadata Filtering): Modern vektör motorları (Qdrant, Milvus, Pinecone, pgvector) yalnızca vektörleri değil, onlara bağlı metaverileri (yazar, tarih, kategori) de saklar. Ön filtreleme (pre-filtering) teknikleriyle sorgu uzayı daraltılarak yüksek doğruluk elde edilir.

4. Kuantizasyon ve Çok Modlu (Multimodal) Arama:
Milyonlarca yüksek boyutlu vektörü bellekte tutmanın yüksek maliyetini düşürmek için Skalar Kuantizasyon (SQ) ve Ürün Kuantizasyonu (Product Quantization - PQ) uygulanır; bu sayede bellek ayak izi 4 kata kadar küçültülür. Ayrıca CLIP gibi çok modlu modeller sayesinde, bir metin sorgusuyla bir görselin vektörü aynı uzayda eşleştirilerek 'gün batımında sahil' metniyle doğrudan ilgili fotoğraf saniyeler içinde bulunabilir.

## Sosyolojik Boyut: Yapay Zekânın Uzun Vadeli Belleği
Vektör veritabanları, yapay zekâ modellerinin 'hafıza kaybı' (amnezi) sorununu çözen uzun vadeli dijital hafızadır. Büyük dil modelleri tek başlarına statik ve unutkan sistemlerdir; her oturum kapandığında geçmiş deneyimlerini yitirirler. 

Vektör veritabanı bu modellere insan zihnine benzer çağrışımsal bir bellek kazandırır. Bir şirketin on yıllık yazışmaları, bir doktorun binlerce hasta geçmişi veya bir araştırmacının tüm arşivi vektör tabanında saklanarak yapay zekânın emrine verilir. Bu teknoloji, veri silolarını anlamsal bir zekâ ağına dönüştürerek insanlığın bilgiye erişim paradigmasını kalıcı olarak değiştirmiştir.

## Sık Yapılan Hatalar ve Yanılgılar
Vektör veritabanı projelerinde en sık yapılan mimari hatalar şunlardır:
- Model Uyuşmazlığına Dikkat Etmemek: Farklı embedding modellerinin ürettiği vektörleri aynı koleksiyonda karşılaştırmak anlamsız sonuçlar üretir; her koleksiyon tek bir modelle beslenmelidir.
- Metaveri Filtrelemesini İhmal Etmek: Saf vektör araması bazen çok alakasız tarih veya kategorilerden veriler getirebilir; mutlaka yapılandırılmış metaveri filtreleri eklenmelidir.
- Boyut ve Bellek Maliyetini Hesaplamamak: 1536 veya 3072 boyutlu vektörlerin milyarlarcasını RAM'de tutmak devasa maliyetler doğurur; ürün aşamasında disk tabanlı indeksleme veya skalar kuantizasyon (SQ) kullanılmalıdır.

## Sıkça Sorulanlar

**Klasik ilişkisel veritabanları (PostgreSQL vb.) vektör veritabanı olarak kullanılabilir mi?**  
Evet; pgvector gibi açık kaynaklı eklentiler sayesinde PostgreSQL gibi güçlü ilişkisel veritabanları HNSW indeksleri oluşturarak vektör benzerlik aramalarını başarıyla yürütebilir.

**Vektör veritabanı ile geleneksel tam metin (Full-Text) arama arasındaki fark nedir?**  
Tam metin arama (Elasticsearch vb.) kelimelerin birebir eşleşmesine (lexical) odaklanırken; vektör veritabanı eş anlamlıları, kavramsal ilişkileri ve anlamsal benzerliği (semantic) bulur.

**Embedding boyutu (dimensions) ne anlama gelir?**  
Bir verinin kaç adet sayısal koordinatla temsil edildiğini belirtir; örneğin 1536 boyutlu bir embedding, o verinin 1536 eksenli çok boyutlu bir uzaydaki noktasal koordinatıdır.

**Kuantizasyon vektör veritabanlarında nasıl tasarruf sağlar?**  
32-bit kayan noktalı (float32) sayıları 8-bit veya 1-bit tam sayılara dönüştürerek bellek (RAM) tüketimini yüzde 75'e varan oranda düşürür ve arama hızını katlar.

## İlgili terimler
- [Embedding](/dictionary/embedding/)
- [RAG](/dictionary/rag/)
- [LLM](/dictionary/llm/)
- [Context Window](/dictionary/context-window/)
- [Knowledge Graph](/dictionary/knowledge-graph/)
- [Memory Management](/dictionary/memory-management/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/vector-database/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
