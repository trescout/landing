# Working Memory nedir, ne demek?

*Sözlük · Yapay Zekâ · Son güncelleme: 22 Eylül 2026*

Working memory (Türkçe karşılığıyla **çalışma belleği**), modelin o anki iş için tuttuğu geçici bilgidir.

## Tanım ve Kelime Kökeni

Görev bitince veya bağlam değişince içerik temizlenir. Bağlam penceresi kabı, çalışma belleği içindeki aktif bilgidir. Sohbet geçmişi ve ara sonuçlar burada durur.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?

**Sohbet:** Önceki mesajların hatırlanması.
**Akıl yürütme:** Ara adımların tutulması.
**Araç:** Çağrı sonuçlarının bekletilmesi.

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

**Kenar notu:** Problem bitince atılan karalama.
**Tezgah:** İş bitince toplanan alet.
**RAM:** Güç kesilince silinen alan.

*Matematik çözerken kenara alınan geçici notlar gibidir; problem bitince önemi kalmaz.*

## Sıkça Sorulanlar

**Dolarsa ne olur?**

Eski bilgi unutulur, bağlam kayar. Özetleme ve budama ile yönetilir.

**Nasıl büyütülür?**

Büyük pencereli model seçilir veya RAG ile dış bilgi eklenir.

**RAG farkı nedir?**

RAG dışarıdan getirir, bellek o anı tutar. İkisi tamamlayıcıdır.

**Unutur mu?**

Evet. Geçici alandır, kalıcılık beklenmez. Kalıcı bilgi dışarı yazılır.

## İlgili terimler

- [Memory](https://trescout.com/dictionary/memory/)
- [Context Window](https://trescout.com/dictionary/context-window/)
- [Long-term Memory](https://trescout.com/dictionary/long-term-memory/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/working-memory/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
