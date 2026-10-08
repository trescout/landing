# Logs nedir, ne demek?

*Sözlük · Geliştirme · Son güncelleme: 22 Eylül 2026*

Log (Türkçe karşılığıyla **kayıt**), sistem olaylarının zaman damgalı satırlarıdır.

## Tanım ve Kelime Kökeni

"Log" gemi jurnali demektir: Kaptan olanı biteni deftere yazar. Yazılım da arka planda ne yaptığını satır satır yazar. Hata anında defter açılır, saatine bakılır. Sistem sağlığının ilk kaynağıdır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?

**Sunucu:** Hata ayıklama.
**Uygulama:** Çökme raporu.
**Güvenlik:** Olay izi.

## Teknik Derinlik ve Mimari

İyi kaydın kuralları:

**Zaman damgası:** Her satırda saat.
**Seviye:** INFO ve ERROR ayrımı.
**Döndürme:** Dosya büyüyünce arşiv.
**PII yasağı:** Kişisel veri kayda girmez.

Örnek satır:

```
2026-09-22T10:00:01 sipariş=4521 sonuc=ok sure_ms=38
```

Arama bu formatta kolaylaşır. Dağınık metin aranamaz, düzenli kayıt aranır.

## Sık Karıştırılanlar

Trace sanılır. Log olay kaydıdır, trace olayın yoludur. Biri fotoğraf, diğeri filmdir.

## Farklı Disiplinlerde Kullanımı

**Kara kutu:** Uçuş verisi.
**Günlük:** Tarih sıra notlar.
**Kasa fişi:** İşlem dökümü.

*Uçağın kara kutusu gibidir; uçuş boyu kayıt tutulur, sorunda geriye sarılır.*

## Sıkça Sorulanlar

**Neden log gerekir?**

Çöküşün nedeni kayıttadır. Kayıtsız sistem kör uçar.

**Nereye yazılır?**

Dosya veya merkezi sisteme. Üretimde merkezi toplama önerilir.

**Ne kadar saklanır?**

Politikaya göre değişir. Hata ayıklama haftalar, denetim yıllar ister.

**Kişisel veri yazılır mı?**

Hayır. Parola ve kimlik kayda girmez, maskelenir.

## İlgili terimler

- [Observability](https://trescout.com/dictionary/observability/)
- [QA](https://trescout.com/dictionary/qa/)
- [Traces](https://trescout.com/dictionary/traces/)

## İlgili araçlar

- [Grafana](https://trescout.com/discover/grafana/)
- [Modly](https://trescout.com/discover/modly/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/logs/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
