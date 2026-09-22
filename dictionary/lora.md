# LoRA nedir, ne demek?

> Low-Rank Adaptation

**Kategori:** Yapay Zekâ  
**Son güncelleme:** 2026-09-22

LoRA (**Low-Rank Adaptation**, düşük sıralı uyarlama), modeli küçük ekle uzmanlaştırma tekniğidir.

## Tanım ve Kelime Kökeni
"Low-rank" **düşük sıralı** demektir. Dev model dondurulur, küçük adaptör eğitilir, üstüne takılır. Temel yetenek korunur, yeni stil eklenir. Maliyet tam eğitimin kesridir.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Görsel:** Kişisel stil üretimi.
- **Yazı:** Kurum dili uyarlaması.
- **Ses:** Karakter sesi.

## Teknik Derinlik ve Mimari
Düzen:
- **Dondurma:** Ana ağırlık sabitlenir.
- **Adaptör:** İki küçük matris eğitilir.
- **Rank:** Boyut ayarı, genelde 8 veya 16.
- **Birleştirme:** Çıktıda toplanır.

Yapılandırma:

```
rank: 8
hedef: dikkat katmanları
```

QLoRA sürümü belleği daha da kısar. Unutma riski tam eğitime göre düşüktür.

## Sık Karıştırılanlar
Fine-tuning sanılır. O tüm modeli kapsar, bu hafif ektir. Biri ev yenileme, diğeri oda boyamadır.

## Farklı Disiplinlerde Kullanımı
- **Not:** Kütüphaneye yapışan kağıt.
- **Lens:** Kameraya takılan filtre.
- **Yama:** Giysiye dikilen arma.

## Bir benzetmeyle
Koca kütüphaneye yapışan küçük not gibidir; kitap durur, bilgi eklenir.

## Sıkça sorulanlar

**Yavaşlatır mı?**  
Genellikle hayır. Ek küçüktür, gecikme fark edilmez.

**Birden fazla takılır mı?**  
Evet. Farklı işler için adaptörler birleştirilir.

**Unutma olur mu?**  
Tam eğitime göre azdır. Rank ve veri dengesi belirler.

**Ne zaman yetmez?**  
Derin bilgi gerekiyorsa tam eğitim veya RAG gerekir.

## İlgili terimler
- [Fine-tuning](/dictionary/fine-tuning/)
- [AI Models](/dictionary/ai-models/)
- [Generative AI](/dictionary/generative-ai/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/lora/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
