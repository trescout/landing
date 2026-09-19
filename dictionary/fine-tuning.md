# Fine-tuning nedir, ne demek?

**Kategori:** Yapay Zekâ  
**Son güncelleme:** 2026-09-20

Fine-Tuning (ince ayar), önceden eğitilmiş genel amaçlı bir yapay zekâ temel modelinin belirli bir uzmanlık alanı, görev, üslup veya kurumsal veri kümesi üzerinde ağırlıklarının optimize edilerek özelleştirilmesi sürecidir.

## Etimoloji ve Transfer Öğrenimi Felsefesi
Fine-Tuning kavramı, derin öğrenme ve makine öğrenimi disiplinindeki 'Transfer Öğrenimi' (Transfer Learning) felsefesine dayanır. Milyarlarca parametreye sahip modern bir temel modeli (Foundation Model) sıfırdan eğitmek (pre-training), binlerce gelişmiş GPU kümesinde aylarca süren ve milyonlarca dolarlık devasa bütçeler gerektiren bir süreçtir. Bu maliyet, şirketlerin kendi özel yapay zekâ modellerini geliştirmesini neredeyse imkânsız kılabilirdi.

İnce Ayar mimarisi bu engeli ortadan kaldırır. İnternet ölçeğindeki genel veriyle dünyanın temel dil ve mantık kalıplarını zaten öğrenmiş olan temel model alınır; hedef alana ait (örneğin tıp, hukuk, finans veya şirket içi yazışmalar) çok daha küçük, seçilmiş ve kaliteli bir veri kümesi üzerinde ek bir eğitimden geçirilir. Bu süreçte modelin genel kavrayış yeteneği korunurken, hedef göreve dair özel terminoloji, üslup ve çıktı formatı modelin sinir ağı ağırlıklarına kalıcı olarak işlenir.

## Bir Benzetmeyle: Tıp Hekiminin Uzmanlık İhtisası
Şöyle düşünün: Tıp fakültesini dereceyle bitirmiş genç bir hekim hayal edin. Bu hekim temel biyolojiyi, insan anatomisini, farmakolojiyi ve genel tıp bilgisini eksiksiz bilir; yani ön eğitimini (Pre-Training) başarıyla tamamlamıştır. Ancak bu hekimden doğrudan kalp nakli ameliyatına girmesini bekleyemezsiniz. Hekimin bir cerraha dönüşebilmesi için tıp fakültesini sıfırdan okumasına gerek yoktur; bunun yerine birkaç yıl boyunca yalnızca kalp cerrahisi kliniğinde uzmanlık ihtisası yapar. Fine-Tuning tam olarak bu uzmanlık ihtisasıdır; temel dil bilgisine sahip bir modeli, belirli bir branşın terminolojisi ve refleksleriyle donatır.

## Teknik Derinlik ve Eğitim Yöntemleri
Modern yapay zekâ mühendisliğinde fine-tuning teknikleri, donanım kaynaklarına ve hedeflere göre üç ana başlık altında toplanır:

1. Tam İnce Ayar (Full Fine-Tuning - FFT): Modelin tüm parametre ağırlıklarının güncellendiği yöntemdir. En yüksek performansı sunsa da modelin boyutu kadar devasa VRAM gerektirir. Ayrıca modelin eski bildiklerini unutması anlamına gelen 'feci unutma' (catastrophic forgetting) riski taşır.

2. Parametre Verimli İnce Ayar (PEFT) ve LoRA / QLoRA: Günümüz endüstri standardı haline gelen LoRA (Low-Rank Adaptation) tekniğinde, modelin orijinal devasa ağırlık matrisleri dondurulur (freeze). Araya çok daha küçük boyutlu, eğitilebilir düşük dereceli adaptör matrisleri eklenir. Parametrelerin yalnızca yüzde 0.1'i eğitilerek aynı başarı elde edilir. QLoRA ise modeli 4-bit kuantize ederek tek bir tüketici ekran kartında (RTX 4090 vb.) 70 milyar parametrelik modellerin bile eğitilmesine olanak tanır.

3. Gözetimli İnce Ayar (SFT) ve Hizalama: Modeller ham metin üreticiliğinden çıkarılıp talimat takip eden sistemlere dönüştürülür:
- SFT (Supervised Fine-Tuning): 'Soru - İdeal Yanıt' çiftlerinden oluşan yüksek kaliteli veri setleriyle modelin istenen formatta yanıt vermesi sağlanır.
- DPO ve KTO: İnsan tercihlerine göre modeli ödüllendiren doğrudan tercih optimizasyonu algoritmalarıyla güvenlik ve doğruluk pekiştirilir.

4. Veri Kalitesi ve LIMA Hipotezi: Araştırmalar, yüz binlerce gürültülü veri yerine özenle filtrelenmiş 1.000 kaliteli örneğin modeli çok daha iyi eğittiğini (LIMA - Less Is More for Alignment) kanıtlamıştır.

5. LoRA Hiperparametreleri ve Adaptör Birleştirme (Merging):
LoRA eğitiminde derecelendirme matrisinin boyutu ($r$) ve ölçekleme katsayısı ($lpha$) dengesi başarıyı doğrudan belirler. Eğitim tamamlandığında, eğitilen küçük adaptör ağırlıkları orijinal model matrisleriyle matematiksel olarak birleştirilebilir (merge); böylece çıkarım anında hiçbir ek gecikme yaşanmadan tam hızlı model elde edilir.

## Sosyolojik Boyut: Veri Egemenliği ve Kültürel Uyum
Fine-tuning, açık kaynak yapay zekâ modellerinin kurumsal dünyada bağımsızlık ve veri egemenliği kazanmasını sağlayan en güçlü kaldıraçtır. Şirketlerin müşteri sırlarını, ticari sözleşmelerini veya hasta kayıtlarını kapalı bulut API'lerine göndermek zorunda kalmadan, kendi yerel sunucularında çalışan modelleri eğitebilmesi yasal ve stratejik bir zorunluluktur.

Bunun yanı sıra fine-tuning, kültürel ve dilsel adaleti temsil eder. Küresel modellerin ağırlıkla İngilizce ve Batı kültürü odaklı eğitilmesine karşın, yerel kurumlar ve topluluklar fine-tuning sayesinde Türkçe gibi dillere ve yerel değerlere tam uyumlu, milli ve kurumsal modeller üretebilmektedir.

## Sık Yapılan Hatalar ve Yanılgılar
Fine-tuning süreçlerinde en sık karşılaşılan tuzaklar şunlardır:
- RAG ile Fine-Tuning'i Karıştırmak: Modele güncel bilgi (örneğin dünkü döviz kuru) yüklemek için fine-tuning yapılmaz; bilgi için RAG, davranış ve üslup kazandırmak için fine-tuning kullanılır.
- Çöp Veriyle Eğitmek (Garbage In, Garbage Out): Düşük kaliteli veya tutarsız veri setleriyle eğitilen modeller halüsinasyon görmeye ve temel muhakeme yeteneklerini kaybetmeye başlar.
- Aşırı Uyum (Overfitting): Modeli küçük bir veri setinde aşırı eğiterek genelleme yeteneğini yok etmek; model ezbercilik yapmaya başlar.

## Sıkça Sorulanlar

**Fine-Tuning ile RAG arasındaki temel fark nedir?**  
Fine-Tuning modelin ağırlıklarını kalıcı olarak değiştirerek üslup, format ve refleks kazandırır; RAG ise ağırlıklara dokunmadan güncel dokümanları anlık olarak modelin bağlam penceresine enjekte eder.

**LoRA ve QLoRA teknikleri maliyetleri nasıl düşürür?**  
Modelin ana ağırlıklarını dondurup araya yüzde 0.1 oranında küçük adaptör matrisleri ekleyerek bellek (VRAM) ihtiyacını katbekat azaltır; dev modellerin tek bir ekran kartında eğitilmesini sağlar.

**Feci unutma (catastrophic forgetting) nedir?**  
Modelin yeni bir uzmanlık alanını öğrenirken önceden bildiği genel dil ve mantık kurallarını unutması durumudur; LoRA gibi adaptör yöntemleriyle bu risk büyük oranda önlenir.

**Fine-Tuning yapmak için kaç adet veri örneği gerekir?**  
LIMA prensibine göre doğru seçilmiş, tutarlı ve yüksek kaliteli 500 ila 2.000 örnek, yüz binlerce vasat veriden çok daha başarılı sonuçlar verir; nitelik nicelikten önemlidir.

## İlgili terimler
- [Foundation Model](/dictionary/foundation-model/)
- [LLM](/dictionary/llm/)
- [RLHF](/dictionary/rlhf/)
- [Distillation](/dictionary/distillation/)
- [Quantization](/dictionary/quantization/)
- [RAG](/dictionary/rag/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/fine-tuning/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
