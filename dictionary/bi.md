# BI nedir, ne demek?

> Business Intelligence

**Kategori:** Veri & Altyapı  
**Son güncelleme:** 2026-09-22

BI (**Business Intelligence**, iş zekâsı), ham veriyi karar destekleyen raporlara dönüştüren disiplindir.

## Tanım ve Kelime Kökeni
Karmaşık veri yığınları grafik ve özetlere çevrilir. Geçmişin muhasebesi ve geleceğin tahmini bu ekranlardan okunur. Toplama aracı değil, karar rehberidir.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Finans:** Aylık kapanış raporları.
- **Satış:** Bölge ve ürün kırılımı.
- **Operasyon:** Stok ve teslimat takibi.

## Teknik Derinlik ve Mimari
Hat:
- **Toplama:** Kaynaklardan çekme.
- **Temizleme:** Hatalı ve yinelenen kayıt ayıklama.
- **Modelleme:** Tablo ve ilişki düzeni.
- **Görselleştirme:** Dashboard ekranları.

Basit metrik örneği:

```
SELECT bolge, SUM(tutar) FROM satislar
GROUP BY bolge ORDER BY 2 DESC;
```

Self-service araçlarla iş birimi kendi raporunu kurar, teknik ekip altyapıyı tutar.

## Sık Karıştırılanlar
Veri analitiği sanılır. Analitik soru sorar, BI düzenli cevap verir. Biri keşif, diğeri rapor düzenidir.

## Farklı Disiplinlerde Kullanımı
- **Şef:** Malzemeden menü çıkarma.
- **Gösterge paneli:** Hız ve yakıt bilgisi.
- **Hava durumu:** Ölçümden tahmin üretme.

## Bir benzetmeyle
Mutfaktaki binlerce malzemeden müşteriye sunulacak menü çıkaran usta şef gibidir.

## Sıkça sorulanlar

**BI neden önemlidir?**  
Tahmin yerine veriye dayalı karar verdirir. Geçmişi görünür, geleceği planlanır kılar.

**Herkes BI kullanabilir mi?**  
Evet. Sürükle-bırak araçlarla iş birimleri kendi raporunu kurar.

**Hangi araçlar kullanılır?**  
Power BI, Tableau, Metabase ve Looker yaygındır. Seçim veri kaynağı ve bütçeye göre yapılır.

**Küçük şirkete gerekli mi?**  
Basit haliyle evet. Tek e-tablo raporu bile BI başlangıcıdır.

## İlgili terimler
- [Data Pipeline](/dictionary/data-pipeline/)
- [Dashboard](/dictionary/dashboard/)
- [CRM](/dictionary/crm/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/bi/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
