# Environment Variables nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-08-08

Programların çalışma anında ihtiyaç duyduğu ayarları ve gizli anahtarları tutan küçük tanımlayıcılardır.

## Tanım
Kodunuzun içine yazmamanız gereken şifreler, API anahtarları veya farklı sunucu adresleri gibi bilgileri sistem düzeyinde tutmanızı sağlar. Program çalışırken bu değişkenleri okur ve ona göre davranır. Böylece aynı kod farklı ortamlarda farklı ayarlarla çalışabilir.

## Bir benzetmeyle
Bir cihazın içine sabit kodlanmış ayarlar yerine, cihazın içine yerleştirilen ve her seferinde değiştirilebilen bir ayar kartı gibidir.

## Nasıl çalışır?
İşletim sistemi veya özel bir dosya üzerinden tanımlanır, program başladığında bu değerleri hafızasına alır.

## Nerede kullanılır?
Sunucu kurulumlarında, uygulama yapılandırmalarında ve güvenlik gerektiren tüm yazılım projelerinde kullanılır.

## Sık karıştırılanlar
Kodun içine yazılan sabit değerler (hardcoded) ile karıştırılmamalıdır, çünkü bu yöntem güvenlik riski yaratır.

## Sıkça sorulanlar

**Neden bu değişkenleri gizli tutmalıyız?**  
Kodunuzu paylaştığınızda şifrelerinizin başkalarının eline geçmesini önlemek için.

## İlgili terimler
- [Secrets](/dictionary/secrets/)
- [Runtime](/dictionary/runtime/)
- [API](/dictionary/api/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/environment-variables/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
