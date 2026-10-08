# BI nedir, ne demek?

*Sözlük · Veri & Altyapı · Son güncelleme: 22 Eylül 2026*

> Business Intelligence

BI (**Business Intelligence**, iş zekâsı), ham veriyi karar destekleyen raporlara dönüştüren disiplindir.

## Tanım ve Kelime Kökeni

Karmaşık veri yığınları grafik ve özetlere çevrilir. Geçmişin muhasebesi ve geleceğin tahmini bu ekranlardan okunur. Toplama aracı değil, karar rehberidir.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?

**Finans:** Aylık kapanış raporları.
**Satış:** Bölge ve ürün kırılımı.
**Operasyon:** Stok ve teslimat takibi.

## Teknik Derinlik ve Mimari

Hat:

**Toplama:** Kaynaklardan çekme.
**Temizleme:** Hatalı ve yinelenen kayıt ayıklama.
**Modelleme:** Tablo ve ilişki düzeni.
**Görselleştirme:** Dashboard ekranları.

Basit metrik örneği:

```
SELECT bolge, SUM(tutar) FROM satislar
GROUP BY bolge ORDER BY 2 DESC;
```

Self-service araçlarla iş birimi kendi raporunu kurar, teknik ekip altyapıyı tutar.

## Sık Karıştırılanlar

Veri analitiği sanılır. Analitik soru sorar, BI düzenli cevap verir. Biri keşif, diğeri rapor düzenidir.

## Farklı Disiplinlerde Kullanımı

**Şef:** Malzemeden menü çıkarma.
**Gösterge paneli:** Hız ve yakıt bilgisi.
**Hava durumu:** Ölçümden tahmin üretme.

*Mutfaktaki binlerce malzemeden müşteriye sunulacak menü çıkaran usta şef gibidir.*

## Sıkça Sorulanlar

**BI neden önemlidir?**

Tahmin yerine veriye dayalı karar verdirir. Geçmişi görünür, geleceği planlanır kılar.

**Herkes BI kullanabilir mi?**

Evet. Sürükle-bırak araçlarla iş birimleri kendi raporunu kurar.

**Hangi araçlar kullanılır?**

Power BI, Tableau, Metabase ve Looker yaygındır. Seçim veri kaynağı ve bütçeye göre yapılır.

**Küçük şirkete gerekli mi?**

Basit haliyle evet. Tek e-tablo raporu bile BI başlangıcıdır.

## İlgili terimler

- [Data Pipeline](https://trescout.com/dictionary/data-pipeline/)
- [Dashboard](https://trescout.com/dictionary/dashboard/)
- [CRM](https://trescout.com/dictionary/crm/)

## İlgili araçlar

- [WrenAI](https://trescout.com/discover/wrenai/)
- [Ossie](https://trescout.com/discover/ossie/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/bi/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
