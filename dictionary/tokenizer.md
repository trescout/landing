# Tokenizer nedir, ne demek ve nasıl çalışır?

**Kategori:** Yapay Zekâ  
**Son güncelleme:** 2026-09-19

Tokenizer (jetonlaştırıcı veya simgeleştirici), doğal dildeki metinleri büyük dil modellerinin (LLM) ve sinir ağlarının matematiksel olarak işleyebileceği sayısal jetonlara (token ID) dönüştüren temel veri işleme bileşenidir.

## 1. Tanım ve temel problem: Neden doğrudan kelimeler değil?

Büyük dil modelleri (GPT-4, Claude, Llama vb.) metinleri insan gibi harf harf veya kelime kelime okumaz. Sinir ağları yalnızca matrisler, tensörler ve sayılarla işlem yapabilir. Bu nedenle metnin önce sayılara dökülmesi gerekir.

Tarihsel olarak doğal dil işlemede (NLP) üç farklı yaklaşım denenmiştir:

1. **Karakter Bazlı İşleme:** Metin tek tek harflere bölünür (`k`, `i`, `t`, `a`, `p`). Sözlük boyutu çok küçüktür (birkaç yüz karakter), ancak cümleler çok uzar. Transformer mimarisinde dikkat mekanizmasının (Self-Attention) işlem karmaşıklığı dizilim uzunluğunun karesiyle ($O(N^2)$) arttığından modelin belleği hızla tükenir.
2. **Kelime Bazlı İşleme:** Her kelime ayrı bir birim kabul edilir. Ancak bu durumda dildeki her çekim eki, yazım hatası ve yeni kelime için sözlük milyonlarca girdiye fırlar; sözlükte olmayan her kelime "bilinmeyen" (`<unk>` - Out of Vocabulary) etiketine düşer ve model anlamı kaybeder.
3. **Alt Kelime (Subword) Çözümü:** Günümüzün modern standardıdır. Sık kullanılan kelimeler tek bir parça ("kitap"), nadir veya türetilmiş kelimeler ise anlamlı alt kök ve eklere ("kitap" + "çı" + "lık") bölünür. Böylece 32.000 ile 128.000 arasında sabit bir sözlük boyutuyla sonsuz sayıda kelime temsil edilebilir.

## 2. Tokenizer algoritmaları ve matematiksel mantıkları

Modern dil modellerinin kalbinde yer alan başlıca tokenizer algoritmaları şunlardır:

### A. Byte Pair Encoding (BPE)
Orijinalinde bir veri sıkıştırma algoritması olan BPE, günümüzde GPT serisi ve Llama modellerinin temelidir. Metindeki tüm temel karakterlerle başlar ve korpusta en sık art arda gelen karakter çiftlerini yinelemeli olarak birleştirip sözlüğe ekler. Örneğin `e` ve `r` sık yan yana geliyorsa `er` tek bir token olur; ardından `er` ile `k` birleşerek `erk` token'ını oluşturur.

### B. WordPiece
Google tarafından BERT modelinde yaygınlaştırılan bu yöntem, frekans yerine olasılık temellidir. Çiftleri birleştirirken dil modelinin eğitim verisi üzerindeki olabilirlik (likelihood) puanını en çok artıran alt kelime parçalarını seçer. Kelime başlangıcı olmayan alt parçaları `##` ön ekiyle (ör. `öğren` + `##ci`) etiketler.

### C. SentencePiece ve Byte-Fallback
Geleneksel tokenizer'lar kelimeleri boşluklara göre ayırırken, dillerin çoğunda (Çince, Japonca vb.) kelime ayracı boşluk değildir. Google'ın SentencePiece kütüphanesi boşlukları da özel bir alt karakter (`_`) olarak kabul eder ve metni ham bayt akışı olarak ele alır. Sözlükte bulunmayan herhangi bir nadir Unicode karakteri görüldüğünde doğrudan UTF-8 baytına (Byte-Fallback) geri düşerek `<unk>` hatasını sıfıra indirir.

## 3. Türkçede "Tokenizer Vergisi" (The Tokenizer Tax)

Büyük dil modellerinin eğitim verilerinin %85'inden fazlası İngilizcedir. Bu durum, tokenizer sözlüğünün ağırlıklı olarak İngilizce kök ve kelimelerle dolmasına yol açar.

Türkçe gibi zengin eklemeli ve morfolojik dillerde bu durum ciddi bir adaletsizlik yaratır:

- **İngilizce:** *"Artificial intelligence is transforming software engineering."* cümlesi yaklaşık **7 token** tutar.
- **Türkçe:** *"Yapay zekâ yazılım mühendisliğini dönüştürüyor."* cümlesi eklerin parçalanması nedeniyle **14-16 token** tüketebilir.

Bu durum iki kritik soruna yol açar:
1. **Maliyet:** Kullanıcılar aynı anlamı iletmek için API sağlayıcılarına 2 kat daha fazla para öder.
2. **Bağlam Daralması:** Modelin 128k token'lık bağlam penceresine İngilizce metinlerden çok daha az Türkçe doküman sığdırılabilir.

*Not: Llama 3 ve GPT-4o ile birlikte sözlük boyutunun 128k ve üzerine çıkarılması, Türkçe token verimliliğini %40'a yakın oranda iyileştirmiştir.*

## 4. Güvenlik ve Uç Durumlar: Glitch Tokens

Tokenizer sözlüğünde yer alan ancak modelin ön eğitimi sırasında metin gövdesinde nadiren veya anlamsız bağlamlarda geçen özel token'lara **"Glitch Token"** adı verilir.

Örneğin Reddit forumlarında kullanıcı adlarından veya e-ticaret sitelerindeki kodlardan türeyen `SolidGoldMagikarp` gibi token'lar modele sorulduğunda; yapay zekâ bu token'ın embedding uzayındaki vektörünü doğru konumlandıramadığı için halüsinasyon görmeye başlar, anlamsız küfürler sıralayabilir veya kilitlenebilir.

## Bir benzetmeyle

Tokenizer, bir kütüphaneye giren yüz binlerce farklı kitabı tek tek harflere bölmek yerine; en sık kullanılan hece ve kelime köklerine özel barkodlar basan bir tasnif makinesidir. Model metni okurken doğrudan harfleri görmez, her parça için okuttuğu barkod numaralarını hafızasına kaydeder.

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

- [Token](/dictionary/token/)
- [NLP](/dictionary/nlp/)
- [Tokenizer-free](/dictionary/tokenizer-free/)
- [Prompt Engineering](/dictionary/prompt-engineering/)
- [Context](/dictionary/context/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/tokenizer/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
