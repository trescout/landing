# Specification nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

Specification (kısaca **spec**, Türkçe karşılığıyla **şartname**), ürünün ne yapacağını ve kurallarını yazan teknik belgedir.

## Tanım ve Kelime Kökeni
Binanın mimari projesi gibidir: Yazılımcı koda başlamadan belgeye bakar, ne inşa edeceğini anlar. Hataları azaltır, beklentiyi netleştirir. API dünyasında OpenAPI, donanımda veri sayfaları (datasheet) bu işi görür.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Yazılım:** Özellik ve kural dokümanı.
- **İhale:** Teknik şartname dosyası.
- **Ürün:** Tasarım ve kabul ölçütü.

## Teknik Derinlik ve Mimari
İyi spec şunları içerir:
- **Kapsam:** Neler var, neler yok.
- **Kabul kriteri:** Bitti sayılması için test edilebilir koşullar.
- **Sınırlar:** Performans, güvenlik, uyumluluk.
- **Sürüm:** Değişiklik geçmişi.

API ucunun spec karşılığı:

```
paths:
  /siparis:
    post:
      summary: Yeni sipariş oluşturur
```

Kural: Ölçülemeyen madde spec değildir, dilektir. Her madde test edilebilir yazılır.

## Sık Karıştırılanlar
Requirement ile benzerdir. Requirement ne istendiğini söyler, specification nasıl yapılacağını anlatır. Biri hedef, diğeri plandır.

## Farklı Disiplinlerde Kullanımı
- **Yemek tarifi:** Malzeme ve adım listesi.
- **Montaj kılavuzu:** Parça ve sıra şeması.
- **İhale:** İdari ve teknik şartname.

## Bir benzetmeyle
Bir yemek tarifindeki malzeme listesi ve pişirme adımları gibidir; tarife uymazsanız yemeğin tadı farklı olur.

## Sıkça sorulanlar

**Spec değişebilir mi?**  
Evet, ancak her değişiklik maliyet ve takvim etkisiyle birlikte onaylanmalıdır.

**Spec dosyasını kim yazar?**  
Ürün yöneticisi, mühendis veya analist yazar. Önemli olan tek sahip ve sürüm disiplinidir.

**Ne kadar detay gerekir?**  
Belirsizliği bitirecek kadar. Aşırısı yazanı yorar, azı geliştiriciyi tıkar.

**Agile içinde spec olur mu?**  
Evet, hafifler. Kabul kriterli kullanıcı hikâyeleri ve API kontratları spec işlevi görür.

## İlgili terimler
- [Spec-driven Development](/dictionary/spec-driven-development/)
- [Framework](/dictionary/framework/)
- [Tech Stack](/dictionary/tech-stack/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/specification/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
