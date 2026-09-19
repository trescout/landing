# LLM nedir, ne demek?

> Large Language Model

**Kategori:** Yapay Zekâ Modelleri  
**Son güncelleme:** 2026-09-20

LLM (Large Language Model - Büyük Dil Modeli), devasa metin külliyatları üzerinde milyarlarca parametreyle eğitilmiş, insan dilini anlama, yorumlama, akıl yürütme ve metin üretme kapasitesine sahip derin öğrenme modelidir.

## Etimoloji ve Ölçeklenme Yasaları
Büyük Dil Modelleri (LLM), yapay zekâ ve doğal dil işleme (NLP) tarihindeki en büyük teknolojik sıçramayı temsil eder. Kökleri 1950'lerin kural tabanlı sistemlerine ve 1990'ların istatistiksel n-gram modellerine dayansa da, günümüz LLM devrimi 2017 yılında Google araştırmacılarının yayınladığı 'Attention Is All You Need' makalesi ve Transformer mimarisinin doğuşuyla başlamıştır.

Bir dil modelini 'Büyük' (Large) kılan unsur yalnızca disk üzerindeki boyutu değil; milyarlarca (hatta trilyonlarca) ağırlık parametresine sahip olması ve internet ölçeğindeki devasa veri kümeleri üzerinde eğitilmesidir. Chinchilla ölçekleme yasalarının (scaling laws) kanıtladığı üzere, model parametreleri ve eğitim verisi belirli matematiksel oranlarla büyütüldüğünde modellerde daha önce açıkça programlanmamış beklenmedik yetenekler (emergent abilities) ortaya çıkar: Kod yazma, mantık yürütme, çok dilli çeviri ve metaforik anlama gibi beceriler bu ölçeklenmenin doğal bir sonucudur.

## Bir Benzetmeyle: İnsanlığın Dil Bestecisi
Şöyle düşünün: Milyonlarca klasik müzik bestesini ve caz kaydını dinlemiş yetenekli bir piyanist hayal edin. Klavyede üç nota çaldığınızda, seslerin devamında hangi harmoninin gelmesi gerektiğini anında hisseder ve melodiyi zarafetle tamamlar. LLM tam olarak bu dil bestecisidir. Kafasında soyut anlamları değil; hangi kelimeden sonra hangi ifadenin gelme olasılığının en yüksek olduğunu hesaplayan matematiksel bir harmoni taşır. Siz cümleyi başlattığınızda o, kolektif insanlık kütüphanesinden süzülen olasılıklarla devam eder.

## Teknik Derinlik ve Eğitim Aşamaları
Modern bir LLM'in geliştirilmesi ve çalıştırılması üç kritik aşamalı bir mühendislik sürecidir:

1. Ön Eğitim (Pre-Training): Milyarlarca web sayfası, kitap, kod deposu ve ansiklopedi taranarak modeller yüzlerce terabaytlık metin üzerinde gözetimsiz (unsupervised) olarak eğitilir. Modelin tek görevi 'bir sonraki tokenı tahmin etmektir' (Next Token Prediction / Causal Language Modeling). Binlerce GPU kümesinde aylarca süren ve milyonlarca dolara mal olan bu aşamada model dünyanın temel dil kalıplarını, gramerini ve genel kültürünü öğrenir.

2. İnce Ayar ve Hizalama (Post-Training & Alignment): Ham bir temel model (Base Model) yalnızca metin tamamlar, soruya cevap vermeyi bilmez. Modelin güvenli, faydalı ve yardımsever bir asistana dönüşmesi için iki aşama uygulanır:
- Gözetimli İnce Ayar (Supervised Fine-Tuning - SFT): Uzmanlar tarafından hazırlanmış kaliteli soru-cevap veri setleriyle model talimat takip etmeye (instruction following) alıştırılır.
- İnsan Geri Bildirimiyle Pekiştirmeli Öğrenme (RLHF & DPO): İnsan tercihlerine dayalı ödül modelleriyle modelin zararlı içerik üretmesi engellenir ve yanıt kalitesi optimize edilir.

3. Çıkarım Mimarisi (Inference Optimization): Kullanıcı modeli çalıştırdığında tokenlar tek tek üretilir (autoregressive generation). Çıkarım hızını artırmak için KV Cache, PagedAttention mimarisi (vLLM) ve ağırlık sıkıştırma (Kuantizasyon - AWQ/GGUF) teknikleri kullanılır.

4. Dikkat Mekanizması ve Bağlam Ölçekleme:
Transformer mimarisinin kalbindeki Çok Başlı Öz-Dikkat (Multi-Head Self-Attention), her tokenın cümledeki diğer tüm tokenlarla olan ilişkisini aynı anda hesaplar. Modern modellerde bağlam penceresini yüz binlerce token seviyesine çıkarmak için Döner Konumsal Gömme (Rotary Position Embedding - RoPE), bellek erişimini optimize eden FlashAttention-2 ve gruplanmış sorgu dikkati (Grouped-Query Attention - GQA) mimarileri kullanılır.

## Sosyolojik Boyut: Zekâ Tanımı ve İnsan Makine Etkileşimi
LLM'ler, bilginin üretimi, işlenmesi ve tüketimi ekseninde matbaanın veya internetin icadına denk bir dönüşüm yaratmıştır. Yazılı dili ve programlama kodunu makineler için doğrudan işlenebilir bir arayüze dönüştürerek insan-bilgisayar etkileşimini kökten değiştirmiştir.

Ancak bu devrim derin sosyolojik ve felsefi tartışmaları da beraberinde getirmiştir: Veri mülkiyeti ve telif hakları, önyargı ve kültürel hegemonya, dezenformasyon ve yapay zekâ güvenlik riskleri (AI Safety/Alignment). Noam Chomsky ve Emily Bender gibi dilbilimcilerin 'stokastik papağan' (stochastic parrot) eleştirisinde vurguladığı gibi, modellerin dili mükemmel taklit etmesi gerçek anlamda bir bilince veya anlama yetisine sahip olduklarını göstermez; bu sistemler insan aklının dijital aynalarıdır.

## Sık Yapılan Hatalar ve Yanılgılar
LLM kullanılırken en sık düşülen yanılgılar şunlardır:
- Arama Motoru veya Doğruluk Mercii Sanmak: LLM'ler olgusal bir veritabanı değil, olasılıksal metin üreteçleridir; kritik konularda söyledikleri mutlaka teyit edilmelidir.
- Yanıtlara Körlemesine Güvenmek: Halüsinasyon modelin doğasında vardır; RAG veya harici doğrulama araçları olmadan çıktıları doğrudan üretim ortamına basmak risklidir.
- Küçük Görevler İçin Devasa Modeller Seçmek: Basit bir sınıflandırma veya özetleme için yüz milyarlarca parametreli modeller çalıştırmak enerji ve maliyet israfıdır; SLM'ler (küçük dil modelleri) tercih edilmelidir.

## Sıkça Sorulanlar

**Büyük Dil Modelleri (LLM) gerçek anlamda düşünür veya anlar mı?**  
Hayır; LLM'lerin bilinci, duygusu veya insan benzeri bir anlama yetisi yoktur; matematiksel istatistikler ve dikkat mekanizmalarıyla hangi kelimenin gelme olasılığının yüksek olduğunu hesaplayarak çıktı üretirler.

**LLM bağlam penceresi (context window) ne anlama gelir?**  
Modelin tek bir konuşma veya işlem anında aynı anda hafızasında tutabileceği ve dikkat (attention) mekanizmasıyla işleyebileceği maksimum token (kelime/karakter parçası) sınırıdır.

**Açık kaynak (Open Weights) modeller kapalı modeller kadar güçlü müdür?**  
Llama, DeepSeek ve Mistral gibi modern açık ağırlıklı modeller, optimize edilmiş mimarileriyle tescilli kapalı modellere (GPT-4 vb.) pek çok benchmark testinde yetişmiş ve yerel çalıştırma avantajı sağlamıştır.

**LLM'lerin donanım gereksinimi neden bu kadar yüksektir?**  
Milyarlarca parametrenin her bir token üretiminde GPU/NPU video belleğinde (VRAM) tutulması ve yüksek bellek bant genişliğiyle taranması gerektiği için yüksek donanım kaynağı talep ederler.

## İlgili terimler
- [Transformer](/dictionary/transformer/)
- [Token](/dictionary/token/)
- [Context Window](/dictionary/context-window/)
- [Inference](/dictionary/inference/)
- [Fine-Tuning](/dictionary/fine-tuning/)
- [SLM](/dictionary/slm/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/llm/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
