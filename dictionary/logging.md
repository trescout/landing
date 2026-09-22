# Logging nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

Logging (Türkçe karşılığıyla **kayıt tutma**), programın olaylarını kronolojik yazmasıdır.

## Tanım ve Kelime Kökeni
"Log" **kütük, kayıt** demektir. Program sessizce hata verdiğinde, o ana kadar ne yaptığı kayıttan okunur. Uçağın kara kutusu gibidir: Kaza sonrası ilk bakılan yerdir.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Sunucu:** Hata ayıklama.
- **Ürün:** Kullanım izleme.
- **Güvenlik:** Olay kaydı.

## Teknik Derinlik ve Mimari
Seviyeler:
- **DEBUG:** Geliştirici detayı.
- **INFO:** Normal akış.
- **WARN:** Şüpheli durum.
- **ERROR:** Başarısız iş.

Kurallar:
- **Yapılandırılmış kayıt:** JSON format, aranabilirlik.
- **PII yasağı:** Parola ve kimlik kayda girmez.
- **Döndürme:** Dosya büyüyünce arşivlenir.

Örnek:

```
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Ödeme alındı: sipariş=%s", siparis_id)
```

Fazla kayıt sistemi yavaşlatır, az kayıt kör bırakır. Üretimde INFO, sorunda DEBUG açılır.

## Sık Karıştırılanlar
Observability sanılır. Oysa logging onun yapı taşıdır: Log ham malzemedir, gözlem yeteneği üründür.

## Farklı Disiplinlerde Kullanımı
- **Kara kutu:** Uçuş verisi kaydı.
- **Günlük:** Tarih sıra notlar.
- **Kamera kaydı:** Olay arşivi.

## Bir benzetmeyle
Uçağın uçuş verilerini kaydeden kara kutusu gibidir; programın hareketleri günlüğe işlenir.

## Sıkça sorulanlar

**Her şeyi kaydetmek iyi midir?**  
Hayır. Fazlası yavaşlatır ve önemliyi gizler, dengeli kayıt tutulur.

**Seviye nedir?**  
Kaydın aciliyet etiketidir. Aramada süzgeç görevi görür.

**Kayıtlar nereye yazılır?**  
Dosya, merkezi sistem veya bulut servisine. Üretimde merkezi toplama önerilir.

**Ne kadar saklanır?**  
Politikaya göre değişir. Hata ayıklama haftalar, denetim yıllar ister.

## İlgili terimler
- [Observability](/dictionary/observability/)
- [Traces](/dictionary/traces/)
- [Logs](/dictionary/logs/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/logging/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
