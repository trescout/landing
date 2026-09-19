# STT nedir, ne demek?

> Speech-to-Text

**Kategori:** Yapay Zekâ  
**Son güncelleme:** 2026-09-19

STT (Speech-to-Text), mikrofon veya ses dosyalarından gelen insan konuşmalarını analiz edip otomatik olarak yazılı metne dönüştüren yapay zekâ teknolojisidir.

## Tanım ve çalışma mimarisi
STT (Konuşmadan Metne / Ses Tanıma), analog veya dijital ses dalgalarını işleyen ve insan telaffuzunu kelimelere döken sistemdir. Modern STT sistemleri (OpenAI Whisper vb.) ham ses sinyallerini spektrogramlara dönüştürür; ardından derin öğrenme ve Transformer tabanlı akustik modeller sayesinde farklı dilleri, şiveleri ve arka plan gürültülerini filtreleyerek yüksek doğrulukla metin üretir.

## Bir benzetmeyle
Siz konuşurken hızlıca not alan, kelimeleri asla kaçırmayan ve söylediğiniz her şeyi anında yazıya döken dünyanın en hızlı ve dikkatli stenografı gibidir.

## Nasıl çalışır?
1. **Ses Yakalama ve Ön İşleme:** Mikrofon ile alınan ses verisi filtrelenir ve frekans parçalarına (spektrogram) ayrılır.
2. **Akustik Modelleme:** Yapay zekâ modeli, ses frekanslarındaki fonemleri (harf ve ses birimlerini) tespit eder.
3. **Dil Modeli ve Düzeltme:** Kelimelerin cümle içindeki bağlamı (context) değerlendirilerek noktalama işaretleri ve doğru yazım kuralları eklenir.

## Nerede kullanılır?
Toplantı ve mülakat notu alan yapay zekâ asistanlarında (Otter, Fireflies), video altyazı üretiminde, müşteri hizmetleri ses analizlerinde ve akıllı sesli komut sistemlerinde (Siri, Alexa) kullanılır.

## Sık karıştırılanlar
- **STT vs TTS (Text-to-Speech):** STT sesi metne çevirir; TTS ise yazılı metni insan sesiyle seslendirir.
- **Ses Tanıma (Voice Recognition) vs STT:** Ses tanıma konuşanın kim olduğunu doğrulamaya odaklanırken; STT konuşmacının ne söylediğini metne dökmeye odaklanır.

## Sıkça sorulanlar

**STT ne demek ve açılımı nedir?**  
İngilizce 'Speech-to-Text' ifadesinin kısaltmasıdır; Türkçede 'Konuşmadan Metne' veya 'Ses-Metin Dönüşümü' olarak bilinir.

**Yapay zekâ destekli STT (Whisper vb.) arka plan gürültüsünde nasıl çalışır?**  
Derin öğrenme modelleri milyonlarca saatlik çeşitli ses verileriyle eğitildiğinden, arka plandaki müzik veya sokak gürültüsünü filtreleyerek ana konuşmacının sesine odaklanabilir.

**STT ile otomatik altyazı ve transkripsiyon nasıl üretilir?**  
Ses kaydı zaman damgalarıyla (timestamp) birlikte işlenerek her cümlenin başlangıç ve bitiş saniyesine göre `.srt` veya `.vtt` formatında altyazıya dönüştürülür.

## İlgili terimler
- [Speech-to-Text](/dictionary/speech-to-text/)
- [Voice Cloning](/dictionary/voice-cloning/)
- [Whisper](/dictionary/whisper/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/stt/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
