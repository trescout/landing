# Speaker Diarization nedir, ne demek?

**Kategori:** Yapay Zekâ  
**Son güncelleme:** 2026-09-19

Speaker Diarization (konuşmacı ayrımı veya günlükleme), çok katılımcılı bir ses kaydında ses dalgalarını analiz ederek "kim, ne zaman konuştu?" sorusunu yanıtlayan ve konuşma dilimlerini konuşmacı kimliklerine göre etiketleyen yapay zekâ teknolojisidir.

## Tanım ve Kavramın Kökeni (Diarization Definition)
Kelime kökeni Fransızca "günlük tutmak" (diariser) eyleminden gelen **Diarization**, ses mühendisliğinde ses akışını zamana bağlı segmentlere bölerek her bir parçayı belirli bir konuşmacı kimliğiyle (örneğin Konuşmacı 1, Konuşmacı 2) eşleştirme işlemidir. Konuşmanın içeriğinden bağımsız olarak, doğrudan sesin biyometrik tınısı ve frekans özellikleri üzerinden kimlik ayrımı yapar.

## Bir benzetmeyle
Bir tiyatro oyununu kapalı bir perdenin arkasından dinleyen bir seyircinin; sahnedeki oyuncuları görmeden sadece ses tonlarından ve konuşma ritimlerinden "Şu anda doktor konuşuyor, şimdi hasta yanıt verdi" diyerek diyalogları metin üzerinde konuşmacılara ayırmasına benzer.

## Nasıl Çalışır? (Adım Adım Diarizasyon)
1. **Ses Aktivitesi Algılama (VAD - Voice Activity Detection):** Kayıttaki müzik, arka plan gürültüsü ve nefes boşlukları elenerek yalnızca insan sesi içeren bölümler ayıklanır.
2. **Segmentasyon (Bölümleme):** Ses sinyali küçük, homojen zaman pencerelerine bölünür.
3. **Konuşmacı Vektörü Çıkarma (Speaker Embeddings):** Derin öğrenme modelleri her bir ses parçasından kişinin ses izini temsil eden çok boyutlu matematiksel vektörler (x-vectors / d-vectors) üretir.
4. **Kümeleme (Clustering Algoritmaları):** Benzer akustik vektörler gruplanır ve her gruba bir konuşmacı etiketi atanır.

## Nerede ve Hangi Alanlarda Kullanılır?
- **Akıllı Toplantı Asistanları:** Zoom, Google Meet veya Teams toplantılarında kimin hangi kararı veya görevi üstlendiğini çıkaran yapay zekâ özet araçları (Otter.ai, Meetily).
- **Çağrı Merkezleri:** Müşteri ile temsilci arasındaki konuşmaları ayrıştırarak duygu analizi ve kalite denetimi yapma.
- **Podcast ve Röportaj Transkripsiyonu:** Çok katılımcılı ses ve video içeriklerinde otomatik profesyonel altyazı ve konuşmacı ayrımı oluşturma.
- **Hukuk ve Adli Bilişim:** Mahkeme kayıtları ve güvenlik sorgularında konuşmacı geçişlerini belgeleme.

## Sık karıştırılanlar
Transcription (Ses-Metin Dönüşümü / STT) ile Speaker Diarization sıklıkla karıştırılır. Klasik bir Speech-to-Text motoru sadece "ne söylendiğini" metne döker ancak kimin söylediğini ayıramaz. Diarization ise "kimin söylediğini" bulur. Örneğin OpenAI Whisper saf transkripsiyon yaparken; `pyannote.audio` veya `WhisperX` gibi araçlarla birleştirildiğinde hem metin hem de konuşmacı kimlikleri eksiksiz elde edilir.

## Sıkça sorulanlar

**Diarization definition (Diarization ne anlama gelir)?**  
Çok katılımcılı ses kayıtlarında ses dalgalarını analiz ederek "kim ne zaman konuştu?" ayrımını yapan ve konuşmacı geçişlerini zaman damgasıyla etiketleyen yapay zekâ sürecidir.

**Sistem konuşmacıların gerçek isimlerini kendi bulabilir mi?**  
Hayır, önceden ses örneği tanıtılmamışsa sistem konuşmacıları "Konuşmacı 1", "Konuşmacı 2" şeklinde ayırt eder; isimleri kullanıcının veya entegre takvim sisteminin eşleştirmesi gerekir.

**Whisper modeli tek başına diarization yapabilir mi?**  
Hayır, resmi Whisper modelleri yalnızca transkripsiyon yapar; konuşmacı ayrımı için `pyannote.audio` gibi özel diarization modelleriyle birlikte kullanılır.

**Diarization sistemlerinin en zorlandığı durum nedir?**  
Birden fazla kişinin aynı anda konuştuğu (overlapping speech), sözlerin birbirine karıştığı veya yankılı ortamlarda doğru ayrım yapmaktır.

## İlgili terimler
- [Transcription](/dictionary/transcription/)
- [Speech-to-Text](/dictionary/speech-to-text/)
- [NLP](/dictionary/nlp/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/speaker-diarization/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
