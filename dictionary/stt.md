# STT nedir, ne demek?

> Speech-to-Text

**Kategori:** Yapay Zekâ  
**Son güncelleme:** 2026-09-19

STT (Speech-to-Text / Konuşmadan Metne), analog veya dijital ses dalgalarındaki insan konuşmasını çözümleyerek yüksek doğrulukla yazılı metne dönüştüren yapay zekâ ve sinyal işleme teknolojisidir.

## Kavramsal köken, etimoloji ve tarihsel gelişim
STT, İngilizce **Speech-to-Text** ifadesinin baş harflerinden oluşur. Türkçede **"Konuşmadan Metne"**, **"Ses Tanıma"** veya **"Ses Transkripsiyonu"** olarak kullanılır. 

Ses tanıma araştırmalarının tarihi, bilgisayar bilimlerinin en zorlu problemlerinden biridir:
- **1952 (Audrey Sistemi):** Bell Laboratuvarları'nda geliştirilen ilk sistem, yalnızca tek bir konuşmacının telaffuz ettiği 0-9 arası rakamları tanıyabiliyordu.
- **1970 - 1990'lar (İstatistiksel Modeller & HMM):** Gizli Markov Modelleri (Hidden Markov Models - HMM) ve n-gram dil modelleriyle ses dalgaları fonemlere (en küçük ses birimleri) bölünerek analiz edilmeye başlandı. Ancak doğruluk oranı gürültülü ortamlarda ve farklı aksanlarda oldukça düşüktü.
- **2010'lar (Derin Öğrenme & Hibrit Modeller):** Derin sinir ağları (DNN, CNN, RNN) HMM ile birleştirilerek akıllı telefonlarda sesli asistanların (Siri, Google Assistant) doğuşunu sağladı.
- **2020'ler (Uçtan Uca Transformer Devrimi):** Ham ses dalgasını doğrudan spektrograma ve ardından metne dönüştüren uçtan uca mimariler (OpenAI Whisper, Google Chirp, Conformer) sahneye çıktı. Yüz binlerce saatlik çok dilli veriyle eğitilen bu modeller, fısıltıları, ağır aksanları ve gürültülü ortamları dahi hatasız yazıya dökebilmektedir.

## Bir benzetmeyle
STT, siz bir konferans salonunda konuşurken yanınızda oturan, her kelimenizi, duraksamanızı ve tonlamanızı ışık hızında steno daktilosuyla hatasız kaydeden; üstelik konuştuğunuz dili anında tanıyıp imla kurallarını otomatik uygulayan kusursuz bir başkatip gibidir.

## Akustik modelleme ve çalışma mimarisi
Modern bir STT motoru, analog ses dalgalarını dijital metne dönüştürürken şu katmanlardan geçer:

1. **Ses Ön İşleme ve Spektrogram Dönüşümü:** Ham ses sinyali (PCM formatında) kısa zamanlı Fourier dönüşümü (STFT - Short-Time Fourier Transform) ile analiz edilir. İnsan kulağının frekans algısına uygun Log-Mel Spektrogramlarına dönüştürülür. Bu işlem sesi görsel bir frekans haritasına çevirir.
2. **Akustik Kodlayıcı (Audio Encoder):** Spektrogram, Transformer tabanlı derin sinir ağına beslenir. Model, ses dalgalarındaki gürültüyü filtreleyerek her 20-30 milisaniyelik ses diliminin hangi foneme veya akustik temsile karşılık geldiğini (gizil uzayda - latent space) çıkarır.
3. **Dil Kodlayıcısı ve Bağlam Tahmini (Autoregressive Decoder):** Akustik modelden gelen sinyaller, eğitilmiş dil modeliyle birleştirilir. Türkçe gibi sesletimi zengin dillerde eşsesli kelimeler (homofonlar; örneğin "yüz" sayısı ile "yüz" fiili) cümlenin bağlamına (context) göre doğru tespit edilir.
4. **Noktalama ve Biçimlendirme:** Ham metne büyük/küçük harf, virgül, nokta, soru işareti eklenir ve sayısal ifadeler ("on beş" $\rightarrow$ "15") metin formatına dönüştürülür.

### Başarım Ölçütü: WER (Word Error Rate)
Bir STT modelinin doğruluğu Kelime Hata Oranı (Word Error Rate - WER) metriğiyle ölçülür:
$$\text{WER} = \frac{S + D + I}{N}$$
Burada $S$ yerine koyma (substitution), $D$ silme/atlama (deletion), $I$ ekleme/yanlış türetme (insertion) ve $N$ toplam referans kelime sayısıdır. Modern modellerde İngilizce WER oranı %3-5 seviyesine, Türkçe gibi sondan eklemeli dillerde ise %7-10 seviyelerine kadar inmiştir.

## Kullanım alanları ve açık kaynak ekosistemi
- **Toplantı ve Not Alma Asistanları:** Zoom, Google Meet veya Teams görüşmelerinin gerçek zamanlı dökümü ve özetlenmesi (Otter.ai, Fireflies).
- **Altyazı ve Çeviri:** Video ve podcast içeriklerine zaman damgalı (timestamp) `.srt` ve `.vtt` formatında otomatik altyazı üretimi.
- **Sağlık ve Hukuk:** Doktorların klinik muayene notlarını veya duruşma tutanaklarını ellerini kullanmadan dikte etmesi.
- **Açık Kaynak Lideri (Whisper & Whisper.cpp):** OpenAI'ın açık kaynaklı Whisper modeli ve Georgi Gerganov'un C/C++ ile tamamen optimize ettiği `whisper.cpp` kütüphanesi, sunucuya bağımlı olmadan yerel donanımda (Mac M-serisi, Raspberry Pi, tüketici GPU'ları) tam gizlilikle STT çalıştırma imkânı sunar.

## Sıkça sorulanlar

**STT ne demek ve açılımı nedir?**  
STT, "Speech-to-Text" (Konuşmadan Metne) ifadesinin kısaltmasıdır. Ses sinyallerini analiz edip kelimeleri çözümleyerek metin formatına dönüştüren yapay zekâ teknolojisidir.

**STT ile Ses Tanıma (Voice Recognition) arasındaki fark nedir?**  
Ses tanıma (Voice Recognition / Speaker Identification), konuşanın kim olduğunu (biyometrik kimlik) tespit etmeye odaklanır. STT ise konuşmacının kimliğinden bağımsız olarak konuşulan sözcüklerin içeriğini yazıya döker.

**STT modelleri Türkçe sesleri doğru anlar mı?**  
Whisper ve Conformer tabanlı modern modeller geniş Türkçe ses veri setleriyle eğitilmiştir; fonetik olarak zengin olan Türkçede yüksek doğrulukla transkripsiyon ve noktalama yapabilmektedir.

**Yerel (Local) STT çalıştırmak mümkün müdür?**  
Evet; `whisper.cpp` veya `faster-whisper` gibi optimize edilmiş motorlar sayesinde ses verilerinizi hiçbir bulut sunucusuna göndermeden, kendi bilgisayarınızda çevrimdışı ve tam gizlilikle çalıştırabilirsiniz.

## İlgili terimler
- [Speech-to-Text](/dictionary/speech-to-text/)
- [Speech-to-Speech](/dictionary/speech-to-speech/)
- [Voice Cloning](/dictionary/voice-cloning/)
- [Whisper](/dictionary/whisper/)
- [Tokenizer](/dictionary/tokenizer/)
- [Apple Silicon](/dictionary/apple-silicon/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/stt/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
