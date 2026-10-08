# Clean Code nedir, ne demek?

*Sözlük · Geliştirme · Son güncelleme: 22 Eylül 2026*

Clean code (Türkçe karşılığıyla **temiz kod**), insanın okuyabildiği koddur.

## Tanım ve Kelime Kökeni

Makine her kodu çalıştırır, insan her kodu okuyamaz. Anlamlı isim, küçük fonksiyon ve sade akış okunabilirliği getirir. Robert Martin bu disiplinin referans adıdır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?

**Ekip:** Ortak kod tabanı.
**İnceleme:** Okunabilirlik denetimi.
**Bakım:** Eski koda dönüş.

## Teknik Derinlik ve Mimari

İlkeler:

**İsim:** Niyeti anlatan ad.
**Boyut:** Tek işlik fonksiyon.
**Tekrar:** Ortak parça tek yerde.

Örnek:

```
# önce
def h(a, b):
    return a + a*b
# sonra
def indirimli_fiyat(fiyat, oran):
    return fiyat + fiyat * oran
```

Kural: Çalışan kod ilk adım, okunan kod ikinci adımdır.

## Farklı Disiplinlerde Kullanımı

**Masa:** Derli çalışma alanı.
**Raflar:** Tür ve yazara göre dizim.
**Bahçe:** Budanmış dal düzeni.

*Kütüphane raflarının tür ve yazara göre dizili olması gibidir.*

## Sıkça Sorulanlar

**Çalışması yetmez mi?**

Yetmez. Çalışan kod bugünü, okunan kod yarını kurtarır.

**Yavaşlatır mı?**

Başta evet, bakımda hayır. Toplamda kazandırır.

**Nasıl ölçülür?**

İnceleme süresi ve hata oranıyla. Sayı tek başına yetmez.

**Nereden başlanır?**

İsim ve fonksiyondan. Dokunulan kod temizlenir.

## İlgili terimler

- [Refactoring](https://trescout.com/dictionary/refactoring/)
- [Unit Testing](https://trescout.com/dictionary/unit-testing/)
- [Engineering Skills](https://trescout.com/dictionary/engineering-skills/)

## İlgili araçlar

- [Clean Code Javascript](https://trescout.com/discover/clean-code-javascript/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/clean-code/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
