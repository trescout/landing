# Borrow Checker nedir?

*Sözlük · Geliştirme · Son güncelleme: 13 Ekim 2026*

Rust dilinde yazılan programların bellek hataları yapmasını engelleyen ve verilerin nasıl kullanıldığını denetleyen mekanizma.

## Tanım

Borrow checker, Rust derleyicisinin en önemli parçalarından biridir ve belleğin güvenli kullanılmasını garanti eder. Yazdığınız kodda aynı veriye aynı anda birden fazla yerin müdahale edip etmediğini, verinin ömrünün yetip yetmediğini titizlikle inceler. Güvenlik kuralına uymayan bir durum bulduğunda programın çalışmasına izin vermez ve sizi uyarır.

*Hassas bir laboratuvarda, aynı anda sadece tek bir araştırmacının özel bir ekipmanı ödünç alabilmesini ve işi bitince geri getirmesini sağlayan katı bir takip defteridir.*

## Nasıl çalışır?

Kodunuzu derlemeye çalıştığınızda arka planda devreye girer. Değişkenlerin sahiplik kurallarına ve ödünç alma sürelerine bakar. Eğer kurallara aykırı bir veri paylaşımı tespit ederse derlemeyi durdurup hatanın nerede olduğunu gösterir.

## Nerede kullanılır?

Sistem programlamada, bellek sızıntılarını ve çökmeleri en baştan önlemek isteyen Rust projelerinin derleme aşamasında aktif olarak çalışır.

## Sık karıştırılanlar

Normal hata ayıklayıcılardan farklıdır, program çalışırken değil, kod yazılıp derlenirken çalışır.

## Sıkça sorulanlar

**Neden bu kadar katıdır?**

Çalışma anında bellek çökmelerini tamamen ortadan kaldırmak için erken aşamada önlem alır.

**Yavaş çalışmama neden olur mu?**

Hayır, sadece derleme aşamasında çalışır ve çalışma zamanında ekstra maliyet yaratmaz.

## İlgili terimler

- [Rust](https://trescout.com/dictionary/rust/)
- [Compiler](https://trescout.com/dictionary/compiler/)
- [Thread-safety](https://trescout.com/dictionary/thread-safety/)
- [Systems Programming](https://trescout.com/dictionary/systems-programming/)
- [Memory Management](https://trescout.com/dictionary/memory-management/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/borrow-checker/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
