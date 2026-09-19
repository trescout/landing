# Tokenizer nedir, ne demek?

**Kategori:** Yapay Zekâ  
**Son güncelleme:** 2026-09-19

Tokenizer, metinleri büyük dil modellerinin ve yapay zekâ sistemlerinin anlayabileceği sayısal jetonlara (token) bölen temel veri işleme bileşenidir.

## Tanım ve temel işlevi
Tokenizer (jetonlaştırıcı / simgeleştirici), doğal dilde yazılmış metinleri yapay zekâ modellerinin matematiksel olarak işleyebileceği sayısal indekslere (token ID) dönüştüren temel bir araçtır. Derin öğrenme ve büyük dil modelleri (LLM) harfleri veya kelimeleri doğrudan insan gibi kavramaz; bunun yerine kelimeleri, heceleri veya alt kelime parçacıklarını sözlükteki sayısal kodlarıyla temsil eder.

## Bir benzetmeyle
Bir kitabı okumadan önce onu tek tek harflere, hecelere veya anlamlı kök parçalarına ayırıp, her bir parçaya özel bir barkod numarası vererek dijital bir katalog oluşturmak gibidir. Model metni okurken doğrudan kelimelere değil, bu barkodlara bakar.

## Nasıl çalışır?
1. **Normalizasyon ve Bölme:** Girdi metni temizlenir ve Byte Pair Encoding (BPE), WordPiece veya SentencePiece gibi algoritmalarla alt kelimelere bölünür.
2. **Sözlük Eşleştirmesi:** Her parça, tokenizer'ın önceden eğitilmiş sözlüğündeki (vocabulary) benzersiz bir sayısal ID ile eşleştirilir.
3. **Vektörleştirme:** Üretilen sayısal diziler modelin gömme (embedding) katmanına aktarılarak çok boyutlu anlamsal vektörlere dönüştürülür.

## Nerede kullanılır?
Tüm büyük dil modellerinin (GPT, Claude, Gemini, Llama) ve doğal dil işleme (NLP) hatlarının ilk ve son adımıdır. Prompt gönderdiğinizde girdi tokenizer ile sayılara çevrilir; model cevap ürettiğinde ise bu sayılar detokenizer ile yeniden okunabilir metne dönüştürülür.

## Sık karıştırılanlar
Sıradan bir boşluk ayırıcı (string split) ile karıştırılmamalıdır. Modern tokenizer'lar dillerin morfolojik yapısına göre bir kelimeyi eklerine ayırabilir veya sık kullanılan kelime gruplarını tek bir token olarak işleyebilir.

## Sıkça sorulanlar

**Tokenizer ne demek ve Türkçe karşılığı nedir?**  
Türkçede 'jetonlaştırıcı' veya 'simgeleştirici' olarak ifade edilir; metin bloklarını anlamlı en küçük sayısal işlem birimlerine ayıran yazılımdır.

**Token nedir ve kelimelerden farkı nedir?**  
Token, dil modelinin temel işlem birimidir. Bir kelime tek bir token olabileceği gibi, özellikle Türkçe gibi eklemeli dillerde kelimenin kökü ve ekleri ("kitap-lık-lar-ımız") birden fazla token oluşturabilir. Ortalama olarak 100 kelime yaklaşık 130-140 token eder.

**Büyük dil modellerinde tokenizer neden kritiktir?**  
Modelin bağlam penceresi kapasitesi ve API maliyetleri doğrudan token adedi üzerinden hesaplanır. Verimli ve dili iyi anlayan bir tokenizer, daha düşük maliyet ve daha yüksek anlama başarımı sağlar.

## İlgili terimler
- [Token](/dictionary/token/)
- [NLP](/dictionary/nlp/)
- [Tokenizer-free](/dictionary/tokenizer-free/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/tokenizer/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
