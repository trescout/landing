# Context nedir ve ne demek?

**Kategori:** Yapay Zekâ  
**Son güncelleme:** 2026-09-19

**Context** (Türkçe karşılığıyla **bağlam**), bir verinin, komutun veya sürecin doğru şekilde yorumlanabilmesi ve yürütülebilmesi için ihtiyaç duyduğu çevresel ve anlamsal bilgilerin bütünüdür.

Bilgisayar bilimlerinde "context" iki ana alanda hayati bir role sahiptir:
1. **Yapay Zekâ ve Büyük Dil Modellerinde (LLM):** Modelin girdi dizilerini doğru anlamlandırabilmesi için dikkat (attention) mekanizmasına beslenen belirteçler (token), geçmiş mesajlar, sistem yönergeleri ve dış belgeler.
2. **İşletim Sistemleri ve Yazılım Geliştirmede:** Bir işlemcinin veya çalışma zamanının (runtime) bir iş parçacığını durdurup başka birine geçmesi için saklanan donanım/yazılım durumu (Context Switching) ve asenkron operasyonlarda yaşam döngüsü yönetimi (Go `context.Context`, React Context vb.).

---

## 1. Yapay Zekâ ve LLM'lerde Context (Bağlam)

Büyük dil modelleri (LLM) insan gibi kalıcı bir belleğe veya deneyim hafızasına sahip değildir; her sorguda yalnızca o an bağlam penceresine (context window) dahil edilen verileri "hatırlar".

### Transformer ve Dikkat (Self-Attention) Mekanizması
Transformer mimarisinde bağlam, cümlenin başındaki bir kelimenin sonundaki bir kelimeyle ilişkisini ağırlıklandırarak (Sorgu/Query, Anahtar/Key, Değer/Value vektörleri) kurulur. Model, "banka" kelimesinin finansal bir kuruluş mu yoksa nehir kıyısı mı olduğunu yalnızca içinde geçtiği cümlenin bağlamına bakarak çözer.

### Context Window (Bağlam Penceresi) ve Sınırları
- **Token Kapasitesi:** Bir modelin tek seferde okuyabildiği ve yanıt üretebildiği maksimum uzunluktur (örn. 8K, 32K, 128K veya 1M+ token).
- **Bellek Maliyeti (KV Cache):** Bağlam uzadıkça dikkat matrisinin bellek gereksinimi karesel ($O(N^2)$) olarak artar. Bu yükü hafifletmek için FlashAttention ve KV-Cache optimizasyonları kullanılır.
- **Kayıp Ortanca Problemi (Lost in the Middle):** Araştırmalar, LLM'lerin uzun metinlerin başında ve sonunda yer alan bilgilere ortadaki bilgilere kıyasla daha iyi odaklandığını göstermektedir.
- **RAG (Retrieval-Augmented Generation):** Milyonlarca sayfalık kurumsal veriyi context window içine sığdırmak yerine, arama motoru veya vektör veritabanıyla sadece sorguyla en alakalı paragraflar filtrelenerek bağlam olarak modele aktarılır.

---

## 2. İşletim Sistemleri ve Programlamada Context

Sistem programlamada "context", bir programın yürütülmesi esnasında o anki durumunu eksiksiz yansıtan tüm değişken ve kayıtçı (register) değerlerini ifade eder.

### Context Switching (Bağlam Değiştirme)
Çoklu görev (multitasking) çalıştıran bir işletim sistemi, CPU çekirdeğini farklı süreçler (process) ve iş parçacıkları (thread) arasında paylaştırır:
1. Çalışan işlemin CPU kayıtçıları (RAX, RSP, RIP vb.), yığın işaretçisi ve bellek sayfaları İşlem Kontrol Bloğuna (PCB - Process Control Block) kaydedilir.
2. Sıradaki işlemin kayıtçıları CPU'ya geri yüklenir.
3. **Maliyet:** Bağlam değiştirme donanım düzeyinde çok maliyetlidir; çünkü CPU L1/L2 önbelleklerinin ve TLB (Translation Lookaside Buffer) adres haritalarının geçersiz kalmasına (cache pollution) neden olur.

### Dillerde Context Yönetimi
- **Go (`context.Context`):** Ağ istekleri veya asenkron goroutine'ler arasında iptal sinyalleri (cancellation), son teslim tarihleri (deadline) ve istek kapsamındaki meta verileri taşımak için kullanılır.
- **Python (`with` blokları):** Bağlam yöneticileri (Context Managers), dosya okuma veya veritabanı bağlantısı açma/kapama gibi kaynak temizleme işlemlerini güvenli hale getirir.
- **React (Context API):** Bileşen ağacında ara bileşenlere tek tek props geçirmeden (prop drilling olmadan) global state'i derinlemesine iletme yöntemidir.

---

## Karşılaştırma: Farklı Disiplinlerde Context Kavramı

| Alan | Context'in Temsil Ettiği Değer | Tipik Bileşenler | Karşılaşılan Sorunlar |
| :--- | :--- | :--- | :--- |
| **Yapay Zekâ (LLM)** | Giriş istemi + Geçmiş sohbet + Belgeler | Tokenlar, Attention Maskeleri, KV Cache | Token sınırı, Halüsinasyon, Bellek tüketimi |
| **İşletim Sistemleri** | Bir sürecin donanımsal anlık durumu | Register'lar, Program Counter, Sayfa Tabloları | CPU gecikmesi, Cache misses, TLB flush |
| **Yazılım Geliştirme** | İstek yaşam döngüsü ve ortam verisi | Timeout sinyali, Yetkilendirme token'ı | Bellek sızıntısı, İptal edilmeyen asenkron çağrılar |

---

## Sıkça Sorulan Sorular

### Context ne demek, Türkçe karşılığı nedir?
Türkçe karşılığı "bağlam"dır. Herhangi bir ifadenin, verinin ya da işlemin içinde yer aldığı şartlar, arka plan ve onunla ilişkili bütünleyici durumlar bütünü anlamına gelir.

### Prompt ile Context arasındaki fark nedir?
Prompt, yapay zekâya doğrudan verilen girdi, soru veya eylem talimatıdır ("Bu kodu açıkla"). Context ise modelin bu talimatı doğru yerine getirmesi için sağlanan ek bilgi, kodun tamamı, ortam değişkenleri veya geçmiş konuşmalardır.

### Context Window (Bağlam Penceresi) neden sınırlıdır?
Transformer mimarisinde her bir token diğer tüm tokenlarla çapraz ilişkilendirilir. Bu matematiksel hesaplama ve saklanan bellek (KV-Cache), bağlam uzunluğunun karesiyle doğru orantılı arttığı için GPU belleği donanımsal bir sınır oluşturur.

### İşletim sisteminde "Context Switch" neden performans kaybına yol açar?
Bir süreçten diğerine geçerken CPU'nun kayıtçılarını kaydetmesi, yeni sürecin bellek alanını yüklemesi ve işlemci önbelleklerinin (L1/L2/L3 ve TLB) temizlenip yeniden dolması gerekir. Bu durum mikro saniyeler mertebesinde doğrudan işlemci kaybına yol açar.

### Go dilinde context paketi neden her fonksiyona ilk parametre olarak verilir?
Go'da `ctx context.Context` parametresi, bir HTTP isteği iptal edildiğinde veya zaman aşımına uğradığında arkadaki veritabanı sorgularının ve arka plan işlerinin de durdurulmasını sağlayarak sunucu kaynaklarının boş yere tüketilmesini önler.

## İlgili terimler
- [Context Window](/dictionary/context-window/)
- [Prompt](/dictionary/prompt/)
- [RAG](/dictionary/rag/)
- [Runtime](/dictionary/runtime/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/context/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
