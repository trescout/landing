# Working Memory nedir, ne demek?

**Kategori:** Yapay Zekâ  
**Son güncelleme:** 2026-09-22

Working memory (Türkçe karşılığıyla **çalışma belleği**), modelin o anki iş için tuttuğu geçici bilgidir.

## Tanım ve Kelime Kökeni
Görev bitince veya bağlam değişince içerik temizlenir. Bağlam penceresi kabı, çalışma belleği içindeki aktif bilgidir. Sohbet geçmişi ve ara sonuçlar burada durur.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Sohbet:** Önceki mesajların hatırlanması.
- **Akıl yürütme:** Ara adımların tutulması.
- **Araç:** Çağrı sonuçlarının bekletilmesi.

## Teknik Derinlik ve Mimari
Bütçe hesabı:

```
bağlam: 128K token
geçmiş: 100K → kalan 28K
```

Taşınca model eskiye elveda der: Budama, özetleme veya kaydırma uygulanır. RAG farkı: RAG dışarıdan bilgi getirir, çalışma belleği o anki bilgiyi tutar. İkisi birlikte çalışır.

## Sık Karıştırılanlar
Uzun süreli hafız sanılır. O kalıcı profildir, bu geçici tezgahtır. Oturum kapanınca burası boşalır.

## Farklı Disiplinlerde Kullanımı
- **Kenar notu:** Problem bitince atılan karalama.
- **Tezgah:** İş bitince toplanan alet.
- **RAM:** Güç kesilince silinen alan.

## Bir benzetmeyle
Matematik çözerken kenara alınan geçici notlar gibidir; problem bitince önemi kalmaz.

## Sıkça sorulanlar

**Dolarsa ne olur?**  
Eski bilgi unutulur, bağlam kayar. Özetleme ve budama ile yönetilir.

**Nasıl büyütülür?**  
Büyük pencereli model seçilir veya RAG ile dış bilgi eklenir.

**RAG farkı nedir?**  
RAG dışarıdan getirir, bellek o anı tutar. İkisi tamamlayıcıdır.

**Unutur mu?**  
Evet. Geçici alandır, kalıcılık beklenmez. Kalıcı bilgi dışarı yazılır.

## İlgili terimler
- [Memory](/dictionary/memory/)
- [Context Window](/dictionary/context-window/)
- [Long-term Memory](/dictionary/long-term-memory/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/working-memory/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
