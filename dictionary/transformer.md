# Transformer nedir, ne demek?

**Kategori:** Yapay Zekâ Modelleri  
**Son güncelleme:** 2026-09-20

Transformer, dikkat mekanizmasını (Self-Attention) temel alarak sıralı verileri paralel olarak işleyen, günümüz büyük dil modellerinin ve üretken yapay zekânın temelini oluşturan derin öğrenme mimarisidir.

## Etimoloji ve Ardışık Kısıtların Yıkılışı
Transformer mimarisi, 2017 yılında Google araştırmacılarının yayınladığı 'Attention Is All You Need' makalesiyle duyurulmuştur. Bu makaleden önce doğal dil işleme (NLP), verileri kelime kelime sırayla okuyan Yinelemeli Sinir Ağları (RNN) ve LSTM modellerine bağımlıydı. 

Ancak RNN'lerin doğası gereği ardışık çalışması iki devasa kısıt yaratıyordu: Cümle uzadıkça baştaki bilgilerin unutulması (kaybolan gradyan problemi) ve donanım seviyesinde modern grafik işlemcilerin (GPU) sunduğu devasa paralel hesaplama gücünün kullanılamaması. Transformer mimarisi, yineleme (recurrence) mekanizmasını tamamen çöpe atarak tüm kelimeleri aynı anda paralel olarak işleyen ve aralarındaki anlamsal bağları 'Öz-Dikkat' (Self-Attention) ile kuran devrimsel bir paradigma getirmiştir.

## Bir Benzetmeyle: Kokteyl Partisinde Odaklanan İnsan Zihni
Şöyle düşünün: Gürültülü bir kokteyl partisinde konuştuğunuz kişiyi dinlediğinizi hayal edin. Eski RNN mimarisi tüm sesleri eşit düzeyde ve sırayla kaydeder; konuşma uzadıkça sesler birbirine karışır ve ana tema kaybolur. İnsan beyni ve Transformer ise odadaki uğultuyu aynı anda duyar ancak yalnızca konuştuğu kişinin sesine ve kritik kelimelere dikkat kesilir. Transformer, cümledeki tüm kelimeleri aynı anda masaya yatırır ve kelimeler arasındaki anlam bağını saniyeler içinde hesaplar.

## Teknik Derinlik ve Matematiksel Blok Mimarisi
Transformer mimarisinin iç mekanizması, matematiksel ve donanımsal açıdan beş temel blok üzerine kuruludur:

1. Ölçeklenmiş Nokta Çarpım Dikkati (Scaled Dot-Product Attention): Her girdi kelimesi üç temel vektöre dönüştürülür: Sorgu (Query - Q), Anahtar (Key - K) ve Değer (Value - V). Sistem, Sorgu ile Anahtar arasındaki benzerliği hesaplayarak bir dikkat matrisi çıkarır ve Değer vektörlerini bu ağırlıklarla çarpar. Formül: Attention(Q, K, V) = softmax((Q * K^T) / sqrt(d_k)) * V.

2. Çok Başlı Dikkat (Multi-Head Attention): Tek bir dikkat mekanizması yerine, model aynı anda farklı anlamsal uzaylarda dikkat kesilen birden fazla 'baş' (head) kullanır. Örneğin bir baş cümlenin dilbilgisel özne-yüklem uyumuna odaklanırken, başka bir baş zamirlerin hangi isme işaret ettiğini (coreference) yakalar.

3. Konumsal Kodlama (Positional Encoding): Kelimeler paralel olarak bir kerede modele beslendiğinden, model sıranın ne olduğunu doğal olarak bilemez. Cümlenin sırasını ve ritmini kaybetmemek için her kelime vektörüne sinüzoidal dalgalar veya modern Döner Konumsal Gömmeler (RoPE) eklenir.

4. İleri Besleme ve Katman Normalizasyonu: Dikkat bloklarından çıkan veriler İleri Beslemeli Ağlar (Feed-Forward Networks - FFN), artık bağlantılar (residual connections) ve RMSNorm katmanlarıyla stabilize edilerek gradyan akışı güvenceye alınır.

5. Mimari Çeşitleri: Transformer ailesi üç ana dala ayrılır: Yalnızca Encoder (BERT benzeri anlama modelleri), Yalnızca Decoder (GPT, Llama benzeri nedensel metin üretim modelleri) ve Encoder-Decoder (T5 benzeri çeviri modelleri).

6. Maskeli Dikkat ve Çıkarım Önbelleği (KV Cache):
Metin üretiminde modelin gelecekteki kelimeleri görmesini engellemek için Maskeli Çok Başlı Dikkat (Masked Multi-Head Attention) kullanılır; her yeni token yalnızca kendisinden önceki tokenlara dikkat kesilebilir. Çıkarım sırasında önceki adımların anahtar ve değer tensörleri KV Cache ile hafızada tutularak tekrarlayan matris çarpımları engellenir.

## Sosyolojik Boyut: GPU Simyası ve Evrensel Zekâ Arayışı
Transformer mimarisi, yalnızca bilgisayar bilimlerinde bir algoritma yeniliği değil; donanım ile yazılımın tarihteki en kusursuz simyasıdır. GPU mimarisinin paralel tensör çarpım yetenekleri ile Transformer'ın paralel dikkat matematiği birbirini besleyerek milyarlarca dolarlık yapay zekâ sanayi devrimini başlatmıştır.

Bunun ötesinde Transformer, metin sınırlarını aşarak evrensel bir yapay zekâ omurgası haline gelmiştir. Görselleri piksel parçaları olarak işleyen Vision Transformer (ViT), ses sinyallerini işleyen Whisper ve biyolojide protein katlanmalarını çözen AlphaFold, gücünü aynı dikkat mekanizmasından alır. İnsanlığın karmaşık sistemleri anlama ve modelleme kapasitesi Transformer ile yeni bir bilişsel çağa girmiştir.

## Sık Yapılan Hatalar ve Yanılgılar
Transformer mimarisiyle ilgili en sık yapılan yanılgılar şunlardır:
- Kuadratik Karmaşıklığı (O(N^2)) Unutmak: Standart dikkat mekanizmasında girdi uzunluğu iki katına çıktığında hesaplama maliyeti dört katına çıkar; bu durum uzun metinlerde bellek patlamasına yol açar (FlashAttention bu darboğazı hafifletir).
- Dikkat Ağırlıklarını Mantıksal Açıklama Sanmak: Yüksek dikkat skoru her zaman insan mantığıyla açıklanabilir bir nedensellik ilişkisi taşımaz; istatistiksel bir korelasyondur.
- Yanlış Göreve Yanlış Model Seçmek: Salt metin sınıflandırması veya arama için devasa Decoder modelleri kullanmak kaynak israfıdır; Encoder modelleri tercih edilmelidir.

## Sıkça Sorulanlar

**Transformer mimarisinin RNN ve LSTM modellerine göre en büyük üstünlüğü nedir?**  
Verileri tek tek sırayla okumak yerine cümlenin tamamını aynı anda paralel işleyebilmesi, böylece uzun mesafeli anlamsal bağları unutmaması ve GPU donanımlarında çok yüksek hızda eğitilebilmesidir.

**Query, Key ve Value (Q, K, V) kavramları ne işe yarar?**  
Arama motoru mantığına benzer: Query aranan sorguyu, Key doküman başlıklarını/etiketlerini, Value ise dokümanın asıl içeriğini temsil eder; Query ile Key eşleştiğinde Value ağırlıklandırılarak çekilir.

**FlashAttention nedir ve Transformer modellerine nasıl hız kazandırır?**  
GPU'nun yavaş genel belleği (HBM) ile hızlı yazmaçları (SRAM) arasındaki bellek transferlerini optimize ederek kuadratik dikkat hesaplamasını donanım seviyesinde hızlandıran ve VRAM tüketimini düşüren bir algoritmadır.

**Transformer modelleri yalnızca metin işlemek için mi kullanılır?**  
Hayır; günümüzde görüntüler (Vision Transformer), ses dosyaları (Whisper), video üretimi (Sora) ve hatta biyolojide protein yapıları (AlphaFold) Transformer mimarisiyle işlenmektedir.

## İlgili terimler
- [LLM](/dictionary/llm/)
- [Token](/dictionary/token/)
- [Context Window](/dictionary/context-window/)
- [Inference](/dictionary/inference/)
- [Fine-Tuning](/dictionary/fine-tuning/)
- [Diffusion Model](/dictionary/diffusion-model/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/transformer/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
