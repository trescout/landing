# Full Text Search nedir, ne demek?

**Kategori:** Veri & Altyapı  
**Son güncelleme:** 2026-09-22

Full text search (Türkçe karşılığıyla **tam metin arama**), belgelerin tüm içeriğinde geçen kelimeleri bulan arama yöntemidir.

## Tanım ve Kelime Kökeni
Basit arama dosya adına bakarken, tam metin arama belgenin içindeki her cümleyi tarar. Büyük arşivlerde bilgiye ulaşmanın en etkili yoludur. Modern altyapısı ters dizin (inverted index) denen yapıya dayanır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Site içi arama:** Blogda konu aramak.
- **E-posta:** Yıllar öncesinin iletisini bulmak.
- **Kod:** Depoda fonksiyon aramak.
- **Hukuk:** İçtihat arşivi taramak.

## Teknik Derinlik ve Mimari
Hat şöyledir:
- **Tokenizasyon:** Metin kelimelere bölünür, ekler köke indirilir.
- **Ters dizin:** Her kelimenin hangi belgede geçtiği önceden yazılır.
- **Sıralama:** BM25 gibi algoritmalar başlık ve sıklık ağırlığıyla dizer.

Postgres ile örnek:

```
SELECT baslik FROM yazilar
WHERE to_tsvector('turkish', icerik) @@ to_tsquery('turkish', 'yapay & zeka');
```

Anlam benzerliği (ör. "otomobil" yazınca "araba" çıkması) istendiğinde vektör arama gerekir. İkisi birlikte de kullanılır: Önce anahtar kelime daraltır, sonra vektör sıralar.

## Sık Karıştırılanlar
Metadata aramasıyla karıştırılabilir. Metadata dosya bilgisine (ad, tarih, boyut) bakar, tam metin arama içeriğe bakar. Vektör arama ise kelimeye değil anlama bakar.

## Farklı Disiplinlerde Kullanımı
- **Kütüphane:** Fiş kataloğu yerine tüm metin taraması.
- **Kitap:** Sonundaki dizin (index) bölümü.
- **Arşiv:** Gazete küpür koleksiyonunda konu aramak.

## Bir benzetmeyle
Bir kitabın sadece içindekiler kısmına bakmak yerine, tüm sayfaları tarayarak aradığınız cümleyi bulmaya benzer.

## Sıkça sorulanlar

**Çok yavaş çalışmaz mı?**  
Önceden kurulan dizin sayesinde saniyeler içinde sonuç verir. Dizinsiz tarama yavaş olur, bu yüzden dizin şarttır.

**Her türlü dosyada çalışır mı?**  
Metin çıkarılabilen dosyalarda evet. Taranmış belgelerde önce OCR ile metin elde edilir.

**Türkçe ekler sorun çıkarır mı?**  
Nitelikli çözümlemede ekler köke indirilir. Dil desteği zayıf motorda isabet düşer, Türkçe destekli yapılandırma gerekir.

**Ne zaman vektör arama gerekir?**  
Eş anlam ve kavram arandığında. Anahtar kelime bulunamazsa vektör devreye girer, ikisi birlikte güçlüdür.

## İlgili terimler
- [RAG](/dictionary/rag/)
- [Vector Index](/dictionary/vector-index/)
- [Document Parsing](/dictionary/document-parsing/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/full-text-search/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
