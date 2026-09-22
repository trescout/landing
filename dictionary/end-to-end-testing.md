# End-to-End Testing nedir, ne demek?

> E2E Testing

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

End-to-end testing (kısaca **E2E test**), uygulamayı kullanıcı gibi baştan sona denemedir.

## Tanım ve Kelime Kökeni
"End-to-end" **uçtan uca** demektir. Parça değil bütün denenir: Giriş yapılır, düğmeye basılır, veri gider, sonuç döner. Yayın öncesi uyum kapısıdır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Yayın:** Sürüm öncesi tur.
- **Mağaza:** Satın alma yolu.
- **Form:** Kayıt akışı.

## Teknik Derinlik ve Mimari
Düzen:
- **Kritik yol:** Önce para eden akış.
- **Otomasyon:** Tarayıcı süren araç.
- **Veri:** Test hesabı ve sıfırlama.

Örnek:

```
test("giriş", async () => {
  await sayfa.goto("/giris");
  await bekle("#panel");
});
```

Yavaşlık nedeni: Gerçek tarayıcı açılır. Kritik yol seçilir, her şey test edilmez.

## Sık Karıştırılanlar
Birim test sanılır. O parçaya bakar, bu bütüne bakar. Biri vida, diğeri sürüş testidir.

## Farklı Disiplinlerde Kullanımı
- **Araba:** Anahtardan yola çıkış.
- **Prova:** Genel tekrar.
- **Final:** Yayın provası.

## Bir benzetmeyle
Motoru değil, anahtarı çevirip yola çıkmayı denemeye benzer.

## Sıkça sorulanlar

**Neden yalnızca bu yapılmıyor?**  
Yavaştır, arıza yeri bulanıktır. Birimle birlikte kullanılır.

**Ne sıklıkla koşar?**  
Yayın öncesi ve gecede. Her committe kritik alt küme koşar.

**Kim yazar?**  
Geliştirici ve testçi birlikte yazar. Sahibi bellidir.

**Kırılgan mıdır?**  
Arayüz değişince kırılır. Seçici ve dayanıklı yazılır.

## İlgili terimler
- [Unit Testing](/dictionary/unit-testing/)
- [Testing Framework](/dictionary/testing-framework/)
- [Web Interface](/dictionary/web-interface/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/end-to-end-testing/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
