# Vector Database nedir, ne demek?

*Sözlük · Veri & Altyapı · Son güncelleme: 20 Eylül 2026*

> Vektör Veritabanı

Vector Database (vektör veritabanı), yüksek boyutlu sayısal vektörleri (embeddings) depolamak, indekslemek ve aralarındaki anlamsal benzerlik mesafelerini milisaniyeler içinde sorgulamak için tasarlanmış özel veritabanı mimarisidir.

## Etimoloji ve Çok Boyutlu Anlamsal Uzay

Vektör Veritabanı (Vector Database), modern yapay zekâ ve derin öğrenme ekosisteminin veri depolama katmanındaki en kritik bileşenidir. Geleneksel ilişkisel veritabanları (RDBMS) ve NoSQL sistemleri, verileri tam eşleşme (örneğin `WHERE id = 5` veya `name LIKE '%Ali%'`) ve katı hiyerarşiler üzerinden sorgulamak için optimize edilmiştir. Ancak yapay zekâ çağında karşılaşılan verilerin büyük çoğunluğu (metinler, fotoğraflar, sesler, videolar) yapılandırılmamış (unstructured) niteliktedir.

Derin öğrenme modelleri bu yapılandırılmamış verileri anlamlandırabilmek için 'embedding' adı verilen yüzlerce veya binlerce boyuttan oluşan sayısal vektör dizilerine dönüştürür. Vektör veritabanları, bu devasa çok boyutlu uzayda milyonlarca hatta milyarlarca veri noktası arasındaki geometrik mesafeleri hesaplar. Bu sayede 'anlamca birbirine en yakın olan' verileri (Nearest Neighbor Search) geleneksel arama yöntemlerinin imkânsız gördüğü hızlarda bulup çıkarır.

*Şöyle düşünün: Milyonlarca kitabın yalnızca alfabetik yazar adına göre dizildiği bir kütüphane klasik SQL veritabanıdır. 'Bana yalnızlık hissini anlatan, sonbahar hüznü taşıyan ve Dostoyevski tarzı romanları getir' derseniz, klasik katalog kilitlenir çünkü kapaklarda bu kelimeler geçmeyebilir. Vektör veritabanı ise kitapları devasa bir galakside konumlandırmak gibidir. Hüzünlü kitaplar belirli bir yıldız kümesinde toplanır, bilimkurgu maceraları başka bir kolda yer alır. Bir duyguyla geldiğinizde sistem galaksideki en yakın komşu yıldızları milisaniyelerde bulur.*

## Teknik Derinlik ve İndeksleme Mimarisi

- **Mesafe Metrikleri:** İki embedding arasındaki benzerlik Kosinüs Benzerliği (açı), Öklid Mesafesi (doğrudan uzaklık) veya Nokta Çarpım formülleriyle hesaplanır.

- **Yaklaşık En Yakın Komşu (ANN) ve HNSW:** Milyonlarca vektör arasında brute-force arama yerine hiyerarşik küçük dünya grafikleri (HNSW) ve IVF indeksleriyle milisaniyelerde sonuca ulaşılır.

- **Hibrit Arama ve Metaveri Filtreleme:** Yalnızca vektörler değil; tarih, kullanıcı ve kategori gibi yapılandırılmış metaverilerle birleştirilerek ön filtreleme (pre-filtering) uygulanır.

- **Kuantizasyon ve Çok Modlu Arama:** Skalar ve ürün kuantizasyonuyla RAM tüketimi yüzde 75 düşürülür; CLIP benzeri modellerle görsel ve metin aynı vektör uzayında aranabilir.

## Sosyolojik Boyut: Yapay Zekânın Uzun Vadeli Belleği

Vektör veritabanları, yapay zekâ modellerinin 'hafıza kaybı' (amnezi) sorununu çözen uzun vadeli dijital hafızadır. Büyük dil modelleri tek başlarına statik ve unutkan sistemlerdir; her oturum kapandığında geçmiş deneyimlerini yitirirler.

Vektör veritabanı bu modellere insan zihnine benzer çağrışımsal bir bellek kazandırır. Bir şirketin on yıllık yazışmaları, bir doktorun binlerce hasta geçmişi veya bir araştırmacının tüm arşivi vektör tabanında saklanarak yapay zekânın emrine verilir. Bu teknoloji, veri silolarını anlamsal bir zekâ ağına dönüştürerek insanlığın bilgiye erişim paradigmasını kalıcı olarak değiştirmiştir.

## Sık Yapılan Hatalar ve Yanılgılar

- **Model Uyuşmazlığı:** Farklı embedding modellerinin ürettiği vektörleri aynı koleksiyonda yarıştırmak anlamsız sonuçlar doğurur.

- **Metaveri Filtresini Unutmak:** Saf vektör benzerliği zaman veya kategori bağlamını kaçırabilir; filtrelerle desteklenmelidir.

- **Bellek Maliyetini Öngörmemek:** Yüksek boyutlu vektörleri sıkıştırmasız RAM'de tutmak maliyet patlaması yaratır; kuantizasyon uygulanmalıdır.

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

- [Embedding](https://trescout.com/dictionary/embedding/)
- [RAG](https://trescout.com/dictionary/rag/)
- [LLM](https://trescout.com/dictionary/llm/)
- [Context Window](https://trescout.com/dictionary/context-window/)
- [Knowledge Graph](https://trescout.com/dictionary/knowledge-graph/)
- [Memory Management](https://trescout.com/dictionary/memory-management/)

## İlgili araçlar

- [Turbovec](https://trescout.com/discover/turbovec/)
- [Zvec](https://trescout.com/discover/zvec/)
- [ODS](https://trescout.com/discover/ods/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/vector-database/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
