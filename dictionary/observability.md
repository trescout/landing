# Observability nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

Observability (Türkçe karşılığıyla **gözlemlenebilirlik**), sistemin içini dış veriyle anlama yeteneğidir.

## Tanım ve Kelime Kökeni
"Observe" **gözlemlemek** demektir. Hata ışığı sorunu söyler, gösterge paneli nedenini açıklar. Observability paneldir: Yavaşlığın ve sapmanın kaynağı veriyle bulunur.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Sunucu:** Yavaşlık kaynağı bulma.
- **Model:** Sapma izleme.
- **Ürün:** Kullanım takibi.

## Teknik Derinlik ve Mimari
Üç sütun:
- **Log:** Olay satırları.
- **Metrik:** Sayısal ölçüler.
- **Trace:** İsteğin yolculuğu.

Bağlayıcı korelasyon kimliğidir: Aynı istek üç sütunda da aynı kimlikle aranır.

```
istek_id=abc123 adım=odeme sonuc=ok sure_ms=42
```

OpenTelemetry ortak formattır. Maliyet kuralı: Her şeyi sonsuz saklamak yerine örnekleme ve süre politikası uygulanır.

## Sık Karıştırılanlar
Monitoring sanılır. Monitoring eşiği izler, observability nedeni açıklar. Biri alarm, diğeri teşhistir.

## Farklı Disiplinlerde Kullanımı
- **Panel:** Hız ve yakıt göstergeleri.
- **Hastane:** Hasta monitörü.
- **Kokpit:** Uçuş ekranları.

## Bir benzetmeyle
Motor arıza ışığı yerine sıcaklık, yağ ve yakıtı anlık gösteren panel gibidir.

## Sıkça sorulanlar

**Neden kayıt yetmiyor?**  
Kayıt sorunu söyler, nedeni açıklamaz. Üç sütun birleşince resim tamamlanır.

**Her sisteme gerekli mi?**  
Basit işte abartı olur, parçalı sistemde hayati olur. Ölçek kararı verir.

**Maliyeti nedir?**  
Taşıma ve saklama bedeli vardır. Örnekleme ve süre politikası maliyeti tutar.

**Nereden başlanır?**  
Yapılandırılmış kayıt ve korelasyon kimliğinden. Sonra metrik ve iz eklenir.

## İlgili terimler
- [Logs](/dictionary/logs/)
- [Traces](/dictionary/traces/)
- [State Management](/dictionary/state-management/)
- [Data Pipeline](/dictionary/data-pipeline/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/observability/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
