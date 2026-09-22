# Testing Framework nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

Testing framework (Türkçe karşılığıyla **test çatısı**), test yazıp koşturan hazır altyapıdır.

## Tanım ve Kelime Kökeni
"Framework" **çatı** demektir. Tek tek komut yazmak yerine kurallar ve koşucu hazır gelir. Sonuç raporlanır, hata işaretlenir. Test düzeni standartlaşır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Geliştirme:** Her committe koşan set.
- **CI:** Hattaki kalite kapısı.
- **Sürüm:** Yayın öncesi tarama.

## Teknik Derinlik ve Mimari
Parçalar:
- **Koşucu (Runner):** Testleri bulup çalıştırır.
- **İddia (Assertion):** Beklenenle gerçek kıyaslanır.
- **Rapor:** Geçen ve kalan listesi.

Örnek:

```
test("toplama", () => {
  expect(topla(2, 3)).toBe(5);
});
```

Seçim ölçütü: Dil uyumu, topluluk ve CI desteği. Popüler olan bakımlı olur.

## Farklı Disiplinlerde Kullanımı
- **Alet çantası:** İşe göre takım.
- **Ölçü seti:** Kalibreli aletler.
- **Spor salonu:** Programlı ekipman.

## Bir benzetmeyle
Tek tornavida yerine düzenli alet çantasıyla işe başlamaya benzer.

## Sıkça sorulanlar

**Hangisi seçilmeli?**  
Dile ve ihtiyaca göre popüler olanı. Bakım ve dokümantasyon belirleyicidir.

**Ne zaman yazılır?**  
Kodla birlikte. Sonraya kalan test yarım kalır.

**E2E farkı nedir?**  
Birim parça dener, uçtan uca yolculuğu dener. İkisi birlikte kullanılır.

**Kapsam hedefi nedir?**  
Ekipçe belirlenir. Kritik yol yüksek, kenar düşük tutulur.

## İlgili terimler
- [Unit Testing](/dictionary/unit-testing/)
- [End-to-End Testing](/dictionary/end-to-end-testing/)
- [Framework](/dictionary/framework/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/testing-framework/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
