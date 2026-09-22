# Harness nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

Harness (Türkçe karşılığıyla **test koşum takımı**), kodu otomatik test eden çerçevedir.

## Tanım ve Kelime Kökeni
"Harness" **koşum takımı** demektir. Kod her güncellendiğinde testler koşar, bozulma uyarısı verir. Sistemin sağlık kontrolünü yapan güvenlik ağıdır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Geliştirme:** Her commit sonrası test.
- **CI:** Hattaki otomatik kapı.
- **Kalite:** Sürüm öncesi tarama.

## Teknik Derinlik ve Mimari
Parçalar:
- **Test senaryosu:** Beklenen davranış tanımı.
- **Fixture:** Hazır test verisi.
- **Mock:** Dış servisin taklidi.
- **Rapor:** Geçen ve kalan listesi.

Örnek:

```
def test_toplama():
    assert topla(2, 3) == 5
```

Kural: Hızlı testler her committe, yavaşlar gecede koşar. Kapsam hedefi ekipçe belirlenir.

## Sık Karıştırılanlar
Yazılımın kendisi sanılır. Oysa harness kodu değil, kodu denetleyen çevredir. Biri oyuncu, diğeri hakemdir.

## Farklı Disiplinlerde Kullanımı
- **Fabrika hattı:** Her aracın fren ve far denetimi.
- **Emniyet kemeri:** Çarpışmada tutan düzenek.
- **Antrenman:** Performans ölçüm parkuru.

## Bir benzetmeyle
Fabrikada her aracın fren ve farını denetleyen otomatik kontrol hattı gibidir.

## Sıkça sorulanlar

**Neden gereklidir?**  
İnsan hatasını azaltır, her değişimde bozulmayı yakalar.

**Her yazılımda şart mı?**  
Profesyonel işte standarttır. Deneme kodunda abartı olur.

**Ne zaman yazılır?**  
Kodla birlikte, tercihen önce. Sonraya kalan test yarım kalır.

**Kapsam hedefi nedir?**  
Ekipçe belirlenir. Kritik yolda yüksek, kenarda düşük tutulur.

## İlgili terimler
- [Testing Framework](/dictionary/testing-framework/)
- [Unit Testing](/dictionary/unit-testing/)
- [QA](/dictionary/qa/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/harness/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
