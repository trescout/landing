# Environment Variables nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

Environment variables (Türkçe karşılığıyla **ortam değişkenleri**), ayarları kod dışında tutan tanımlayıcılardır.

## Tanım ve Kelime Kökeni
"Environment" **ortam** demektir. Parola ve adres kodda durmaz, sistemde durur. Aynı kod farklı ortamda farklı davranır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Sunucu:** Bağlantı dizgileri.
- **Uygulama:** Mod seçimi.
- **CI:** Gizli anahtarlar.

## Teknik Derinlik ve Mimari
Düzen:
- **.env:** Yerel dosya, depoya girmez.
- **Öncelik:** Ortam sistem dosyayı ezer.
- **Şema:** Gerekli ad listesi.

Örnek değer:

```
DATABASE_URL=postgres://kullanici:parola@localhost:5432/db
```

Kural: Gerçek değer örneğe yazılmaz, yer tutucu konur. Sızan anahtar iptal edilir.

## Sık Karıştırılanlar
Sabit değer sanılır. Sabit kodda durur, değişken dışarıdadır. Biri dövme, diğeri rozettir.

## Farklı Disiplinlerde Kullanımı
- **Kart:** Değişen ayar kartı.
- **Kumanda pili:** Tak çıkar güç.
- **Anahtarlık:** Taşınan erişim.

## Bir benzetmeyle
Cihaza gömülü ayar yerine takılıp değişen kart gibidir.

## Sıkça sorulanlar

**Neden gizli tutulur?**  
Paylaşımda ele geçer, hesap açılır. Gizli kalır, risk küçülür.

**.env nedir?**  
Yerel değer dosyasıdır. Depoya girmez, örneği girer.

**Sızarsa ne olur?**  
Anahtar iptal edilir, kayıt denetlenir. Gecikme büyüktür.

**Öncelik nedir?**  
Sistem ortamı dosyayı ezer. Canlı değer sistemden gelir.

## İlgili terimler
- [Secrets](/dictionary/secrets/)
- [Runtime](/dictionary/runtime/)
- [API](/dictionary/api/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/environment-variables/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
