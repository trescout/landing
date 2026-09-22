# AI Engineering nedir, ne demek?

**Kategori:** Yapay Zekâ  
**Son güncelleme:** 2026-09-22

AI engineering (Türkçe karşılığıyla **yapay zekâ mühendisliği**), modelleri yayında çalışan güvenilir sisteme dönüştürme disiplinidir.

## Tanım ve Kelime Kökeni
Veri bilimci veriden anlam çıkarır, yapay zekâ mühendisi bu anlamı işleyen sistemi kurar. Modeli alır, veriyle besler, arayüze bağlar, yayında izler. Teorik modeli pratik ürüne çeviren köprüdür. MLOps ve LLMOps bu disiplinin operasyonel adlarıdır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Şirket asistanı:** Kurum belgelerini yanıtlayan bot.
- **Öneri:** Size özel ürün ve içerik sıralaması.
- **Otonom sistem:** Karar destek ve otomasyon hatları.

## Teknik Derinlik ve Mimari
Üretim hattının parçaları:
- **Veri hattı:** Toplama, temizleme ve sürümleme.
- **Değerlendirme (Eval):** Yayın öncesi soru setiyle puanlama. Basit döngü şöyledir:

```
for soru, beklenen in testler:
    cevap = model.sor(soru)
    puanla(cevap, beklenen)
```

- **RAG:** Modele kurum belgesi okutma.
- **İzleme:** Hata oranı, gecikme ve maliyet takibi.
- **Korkuluk:** Zararlı ve saçma çıktıyı tutan filtreler.

Kural: Puanlanmayan iyileştirilmez. Her sürüm eval setinden geçer.

## Sık Karıştırılanlar
Veri bilimi ile karıştırılır. Veri bilimci veriden anlam çıkarır, yapay zekâ mühendisi bu anlamı işleyen sistemi kurar. Biri analiz, diğeri üretimdir.

## Farklı Disiplinlerde Kullanımı
- **İlaç:** Formülü bulan laboratuvar ve seri üreten fabrika.
- **İnşaat:** Projeyi çizen mimar ve şantiyeyi yöneten mühendis.
- **Mutfak:** Tarifi yazan şef ve zincire yayan operasyon.

## Bir benzetmeyle
Bilim insanı laboratuvarda yeni bir ilaç formülü bulur, yapay zekâ mühendisi ise o ilacı fabrikada seri üretime geçirip eczanelere ulaştırır.

## Sıkça sorulanlar

**AI mühendisi olmak için kod bilmek şart mı?**  
Evet. Sistem kurmak, model bağlamak ve izlemek için sağlam yazılım temeli gerekir.

**AI mühendisliği sadece model eğitmek midir?**  
Hayır. Yayınlama, izleme ve güncelleme işin büyük parçasıdır. Eğitim yalnızca başlangıçtır.

**MLOps ile farkı nedir?**  
MLOps operasyon pratiğidir, AI engineering disiplinin adıdır. İkisi aynı hattın iki ucudur.

**Nereden başlanmalı?**  
Bir API ile küçük bir RAG uygulaması kurup eval seti yazmakla. Ölçmeyi öğrenen büyütür.

## İlgili terimler
- [Machine Learning](/dictionary/machine-learning/)
- [Engineering Skills](/dictionary/engineering-skills/)
- [AI Agent](/dictionary/ai-agent/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/ai-engineering/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
