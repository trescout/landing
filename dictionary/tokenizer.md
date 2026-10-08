# Tokenizer nedir, ne demek ve nasıl çalışır?

*Sözlük · Yapay Zekâ · Son güncelleme: 19 Eylül 2026*

Tokenizer (jetonlaştırıcı veya simgeleştirici), doğal dildeki metinleri büyük dil modellerinin (LLM) ve sinir ağlarının matematiksel olarak işleyebileceği sayısal jetonlara (token ID) dönüştüren temel veri işleme bileşenidir.

## 1. Tanım ve temel problem: Neden doğrudan kelimeler değil?

Büyük dil modelleri (GPT-4, Claude, Llama vb.) metinleri insan gibi harf harf veya kelime kelime okumaz. Sinir ağları yalnızca matrisler, tensörler ve sayılarla işlem yapabilir. Bu nedenle metnin önce sayılara dökülmesi gerekir.

Tarihsel olarak doğal dil işlemede (NLP) üç farklı yaklaşım denenmiştir:

1. **Karakter Bazlı İşleme:** Metin tek tek harflere bölünür (`k`, `i`, `t`, `a`, `p`). Sözlük boyutu çok küçüktür (birkaç yüz karakter), ancak cümleler çok uzar. Transformer mimarisinde dikkat mekanizmasının (Self-Attention) işlem karmaşıklığı dizilim uzunluğunun karesiyle (O(N²)) arttığından modelin belleği hızla tükenir.
2. **Kelime Bazlı İşleme:** Her kelime ayrı bir birim kabul edilir. Ancak bu durumda dildeki her çekim eki, yazım hatası ve yeni kelime için sözlük milyonlarca girdiye fırlar; sözlükte olmayan her kelime "bilinmeyen" (`<unk>` - Out of Vocabulary) etiketine düşer ve model anlamı kaybeder.
3. **Alt Kelime (Subword) Çözümü:** Günümüzün modern standardıdır. Sık kullanılan kelimeler tek bir parça ("kitap"), nadir veya türetilmiş kelimeler ise anlamlı alt kök ve eklere ("kitap" + "çı" + "lık") bölünür. Böylece 32.000 ile 128.000 arasında sabit bir sözlük boyutuyla sonsuz sayıda kelime temsil edilebilir.

## 2. Tokenizer algoritmaları ve matematiksel mantıkları

Modern dil modellerinin kalbinde yer alan başlıca tokenizer algoritmaları şunlardır:

- **Byte Pair Encoding (BPE):** Orijinalinde bir veri sıkıştırma algoritması olan BPE, günümüzde GPT serisi ve Llama modellerinin temelidir. Metindeki tüm temel karakterlerle başlar ve korpusta en sık art arda gelen karakter çiftlerini yinelemeli olarak birleştirip sözlüğe ekler.
- **WordPiece:** Google tarafından BERT modelinde yaygınlaştırılan bu yöntem, frekans yerine olasılık temellidir. Çiftleri birleştirirken dil modelinin eğitim verisi üzerindeki olabilirlik (likelihood) puanını en çok artıran alt kelime parçalarını seçer.
- **SentencePiece ve Byte-Fallback:** Boşlukları da özel bir alt karakter olarak kabul eder ve metni ham bayt akışı olarak ele alır. Sözlükte bulunmayan herhangi bir nadir Unicode karakteri görüldüğünde doğrudan UTF-8 baytına (Byte-Fallback) geri düşerek `<unk>` hatasını sıfıra indirir.

## 3. Türkçede "Tokenizer Vergisi" (The Tokenizer Tax)

Büyük dil modellerinin eğitim verilerinin %85'inden fazlası İngilizcedir. Bu durum, tokenizer sözlüğünün ağırlıklı olarak İngilizce kök ve kelimelerle dolmasına yol açar.

Türkçe gibi zengin eklemeli ve morfolojik dillerde bu durum ciddi bir maliyet ve bağlam eşitsizliği yaratır:

- **İngilizce:** *"Artificial intelligence is transforming software engineering."* cümlesi yaklaşık **7 token** tutar.
- **Türkçe:** *"Yapay zekâ yazılım mühendisliğini dönüştürüyor."* cümlesi eklerin parçalanması nedeniyle **14-16 token** tüketebilir.

Bu sebeple Türkçe konuşan kullanıcılar aynı bağlam penceresine daha az doküman sığdırabilir ve API servislerine 2 kat daha fazla ücret öder. Llama 3 ve GPT-4o ile sözlük boyutunun 128k üzerine çıkması Türkçe token verimliliğini belirgin şekilde artırmıştır.

## 4. Güvenlik ve Uç Durumlar: Glitch Tokens

Tokenizer sözlüğünde yer alan ancak modelin ön eğitimi sırasında metin gövdesinde nadiren veya anlamsız bağlamlarda geçen özel token'lara **"Glitch Token"** adı verilir.

Örneğin Reddit forumlarındaki kullanıcı adlarından veya e-ticaret sitelerindeki kodlardan türeyen `SolidGoldMagikarp` gibi token'lar modele sorulduğunda; yapay zekâ bu token'ın embedding uzayındaki vektörünü doğru konumlandıramadığı için halüsinasyon görmeye başlar, anlamsız küfürler sıralayabilir veya kilitlenebilir.

*Tokenizer, bir kütüphaneye giren yüz binlerce farklı kitabı tek tek harflere bölmek yerine; en sık kullanılan hece ve kelime köklerine özel barkodlar basan bir tasnif makinesidir. Model metni okurken doğrudan harfleri görmez, her parça için okuttuğu barkod numaralarını hafızasına kaydeder.*

## Sıkça sorulanlar

**Tokenizer ne demek, Türkçe karşılığı nedir?**

Türkçede "jetonlaştırıcı" veya "simgeleştirici" olarak adlandırılır. Doğal dil metinlerini yapay zekâ modelinin anlayacağı en küçük sayısal indekslere (token) bölen yazılımdır.

**1 token kaç kelime veya harfe denk gelir?**

İngilizce metinlerde 1 token ortalama 4 karaktere veya 0,75 kelimeye eşittir (100 kelime yaklaşık 130 token). Türkçe gibi sondan eklemeli dillerde ise eklerin parçalanması nedeniyle 1 kelime ortalama 2 ila 3 token tutabilir.

**BPE (Byte Pair Encoding) nasıl çalışır?**

En temel karakterlerle başlayıp eğitim kümesinde en sık yan yana gelen karakter çiftlerini adım adım birleştirerek sabit büyüklükte bir alt kelime sözlüğü inşa eden istatistiksel algoritmadır.

**Tokenizer-free (tokensız) modeller mümkün müdür?**

Evet; son dönemde geliştirilen MambaByte ve MegaByte gibi yeni nesil sinir ağı mimarileri, tokenizer katmanını tamamen kaldırıp doğrudan ham baytlar (bytes) üzerinde işlem yaparak dil eşitsizliğini ortadan kaldırmayı amaçlar.

## İlgili terimler

- [Token](https://trescout.com/dictionary/token/)
- [NLP](https://trescout.com/dictionary/nlp/)
- [Tokenizer-free](https://trescout.com/dictionary/tokenizer-free/)
- [Prompt Engineering](https://trescout.com/dictionary/prompt-engineering/)
- [Context](https://trescout.com/dictionary/context/)

## İlgili araçlar

- [AI Engineering from Scratch](https://trescout.com/discover/ai-engineering-from-scratch/)
- [Minimind](https://trescout.com/discover/minimind/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/tokenizer/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
