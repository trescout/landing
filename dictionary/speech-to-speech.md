# Speech-to-Speech nedir, ne demek?

**Kategori:** Yapay Zekâ  
**Son güncelleme:** 2026-09-19

Speech-to-Speech (S2S / sesten sese yapay zekâ), ses dalgalarını ara bir metin katmanına dönüştürmeden doğrudan kaynaktan hedefe analiz edip yeni bir ses sinyali üreten uçtan uca derin öğrenme teknolojisidir.

## Geleneksel kaskat mimariden uçtan uca mimariye
Geleneksel sesli çeviri ve diyalog sistemleri, "kaskat" (cascade) adı verilen üç bağımsız aşamadan oluşuyordu:
1. **STT (Speech-to-Text):** Konuşmanın dinlenip metne dökülmesi.
2. **LLM / MT (Çeviri / Metin İşleme):** Metnin anlaşılması, yanıt üretilmesi veya başka bir dile çevrilmesi.
3. **TTS (Text-to-Speech):** Üretilen metnin sentetik bir ses motoruyla yeniden seslendirilmesi.

Bu üç adımlı kaskat yaklaşımın iki temel sorunu vardı:
- **Yüksek Gecikme (Latency):** Her bir modelin çıktısı diğerinin girdisi olduğundan, yanıt süresi 2 ila 4 saniyeyi buluyor ve doğal sohbet akışını imkânsız kılıyordu.
- **Duygu ve Akustik Bilgi Kaybı:** Metin yalnızca kelimeleri taşır. Konuşmacının ses tonundaki heyecan, ironi, fısıltı, soru vurgusu ve nefes aralıkları metne dönüştürülürken tamamen buharlaşıyordu.

**Modern Uçtan Uca S2S (Speech-to-Speech):**
Yeni nesil multimodal mimariler (OpenAI GPT-4o Ses Modu, Meta SeamlessM4T, Kyutai Moshi, Google Gemini Live) metin ara katmanını tamamen ortadan kaldırır. Ses dalgası modele doğrudan girer ve model doğrudan ses dalgası üretir. Bu sayede gecikme 200-300 milisaniye seviyesine (insan konuşma aralığına) iner ve konuşmacının ses tonundaki nüanslar korunur.

## Bir benzetmeyle
Geleneksel sistem, konuşmanızı önce steno ile kağıda döken, sonra başka bir odaya koşup bu kağıdı tercümana çevirten, son olarak da üçüncü bir kişiye bu çeviriyi mikrofondan okutan hantal bir bürokrasiye benzer. Uçtan uca S2S ise konuşmanızı dinlerken aynı anda sizin ses tonunuzla, duygularınızla ve aksanınızla diğer dilde konuşabilen telepatik bir eşzamanlı tercümandır.

## Teknik altyapı: Ses tokenizasyonu ve sürekli gizil uzay
Sesten sese sistemlerin arkasındaki temel mühendislik adımları şunlardır:

1. **Nöral Ses Kodekleri (Neural Audio Codecs):** EnCodec, SoundStream veya Descript Audio Codec (DAC) gibi mimariler, ham ses dalgalarını sıkıştırarak saniyede binlerce ayrık veya sürekli "ses token'ına" dönüştürür.
2. **Anlamsal ve Akustik Ayrıştırma (Semantic vs Acoustic Tokens):** Gelişmiş modeller sesi iki vektöre ayırır: Ne söylendiğini temsil eden anlamsal (semantic) vektör ve nasıl söylendiğini (tını, duygu, ortam akustiği) temsil eden akustik vektör.
3. **Sıfır Örnekli Ses Klonlama (Zero-Shot Voice Transfer):** Model, konuşmacının birkaç saniyelik referans sesini analiz ederek o kişinin ses tınısını, vurgularını ve frekans profilini öğrenir. Çeviriyi veya üretilen yanıtı doğrudan orijinal konuşmacının sesiyle sentezler.
4. **Çift Yönlü Tam İletişim (Full-Duplex & Interruption Handling):** WebRTC tabanlı düşük gecikmeli veri hatları üzerinden model hem dinler hem konuşur. Kullanıcı konuşurken araya girdiğinde model insan gibi duraksar ve kullanıcının lafını kesmesine izin verir.

## Kullanım alanları ve geleceğe bakış
- **Evrensel Canlı Tercüme (Babel Fish):** Farklı dilleri konuşan iki insanın, kendi ses tonları ve duygusal ifadeleri korunarak anlık sohbet edebilmesi.
- **Duygusal Etkileşimli Asistanlar:** Yalnızca komut alan değil; kullanıcının sesindeki üzüntüyü, telaşı veya sevinci anlayıp ona uygun şefkatli veya enerjik bir tonla yanıt veren yardımcılar.
- **Dublaj ve Medya Üretimi:** Aktörlerin seslerinin ve dudak senkronizasyonlarının diğer dillere orijinal duygu ve ton bozulmadan otomatik uyarlanması.

## Sıkça sorulanlar

**Speech-to-Speech ne demek ve nasıl çalışır?**  
Speech-to-Speech (Sesten Sese), konuşmayı metne çevirme zorunluluğunu ortadan kaldıran, ses dalgasını doğrudan analiz edip yine ses olarak çıktı üreten uçtan uca yapay zekâ modelidir.

**Geleneksel STT-TTS kaskatından farkı nedir?**  
Kaskat sistemler sesi önce metne, sonra tekrar sese çevirir; bu da saniyeler süren gecikmeye ve duygu/vurgu kaybına yol açar. S2S ise 200-300 ms gibi anlık bir gecikmeyle çalışır ve konuşmacının ses karakterini korur.

**S2S sisteminde konuşurken araya girilebilir mi (Interruption)?**  
Evet; tam çift yönlü (Full-Duplex) ses akışı sayesinde model, kullanıcı araya girdiğinde ses üretimini anında durdurup dinleme moduna geçebilir.

**Sesten sese çeviride güvenlik riskleri nelerdir?**  
Gerçekçi ses klonlama teknolojisi kimlik taklidi ve dolandırıcılık riski taşır. Bu sebeple modern S2S sistemlerinde sentezlenen sese insan kulağının duyamayacağı kriptografik filigranlar (audio watermarking) yerleştirilir.

## İlgili terimler
- [STT](/dictionary/stt/)
- [Speech-to-Text](/dictionary/speech-to-text/)
- [Voice Cloning](/dictionary/voice-cloning/)
- [Whisper](/dictionary/whisper/)
- [Tokenizer](/dictionary/tokenizer/)
- [Apple Silicon](/dictionary/apple-silicon/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/speech-to-speech/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
