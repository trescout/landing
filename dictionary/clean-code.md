# Clean Code nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

Clean code (Türkçe karşılığıyla **temiz kod**), insanın okuyabildiği koddur.

## Tanım ve Kelime Kökeni
Makine her kodu çalıştırır, insan her kodu okuyamaz. Anlamlı isim, küçük fonksiyon ve sade akış okunabilirliği getirir. Robert Martin bu disiplinin referans adıdır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Ekip:** Ortak kod tabanı.
- **İnceleme:** Okunabilirlik denetimi.
- **Bakım:** Eski koda dönüş.

## Teknik Derinlik ve Mimari
İlkeler:
- **İsim:** Niyeti anlatan ad.
- **Boyut:** Tek işlik fonksiyon.
- **Tekrar:** Ortak parça tek yerde.

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
- **Raflar:** Tür ve yazara göre dizim.
- **Masa:** Derli çalışma alanı.
- **Bahçe:** Budanmış dal düzeni.

## Bir benzetmeyle
Kütüphane raflarının tür ve yazara göre dizili olması gibidir.

## Sıkça sorulanlar

**Çalışması yetmez mi?**  
Yetmez. Çalışan kod bugünü, okunan kod yarını kurtarır.

**Yavaşlatır mı?**  
Başta evet, bakımda hayır. Toplamda kazandırır.

**Nasıl ölçülür?**  
İnceleme süresi ve hata oranıyla. Sayı tek başına yetmez.

**Nereden başlanır?**  
İsim ve fonksiyondan. Dokunulan kod temizlenir.

## İlgili terimler
- [Refactoring](/dictionary/refactoring/)
- [Unit Testing](/dictionary/unit-testing/)
- [Engineering Skills](/dictionary/engineering-skills/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/clean-code/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
