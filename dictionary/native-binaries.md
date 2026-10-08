# Native Binaries nedir?

*Sözlük · Geliştirme · Son güncelleme: 6 Ekim 2026*

Belirli bir işletim sistemi ve işlemci mimarisi için doğrudan çalıştırılabilir şekilde derlenmiş program dosyalarıdır.

## Tanım

Native binaries (yerel ikili dosyalar), yazılan kodların herhangi bir aracı yazılıma ihtiyaç duymadan doğrudan bilgisayarın donanımı tarafından anlaşılmasını sağlayan dosyalardır. Bu dosyalar, hedef işletim sistemi ve işlemci türüne özel olarak hazırlandığı için en yüksek performansı sunar. Java veya Python gibi dillerin aksine, çalışmak için bilgisayarda yüklü bir sanal makineye veya yorumlayıcıya gereksinim duymazlar.

*Bunu, çevirmene ihtiyaç duymadan doğrudan sizinle aynı ana dili konuşan bir insanla sohbet etmeye benzetebilirsiniz. Arada hiç vakit kaybetmez ve doğrudan iletişime geçersiniz.*

## Nasıl çalışır?

Geliştiriciler, yazdıkları kodları derleyici adı verilen araçlar yardımıyla doğrudan makine diline dönüştürürler. Bu işlem sırasında hedef donanım belirtilir ve derleyici sadece o donanımın anlayacağı sıfır ve birlerden oluşan bir dosya üretir. Oluşan bu dosya, kullanıcı tarafından çift tıklanarak doğrudan çalıştırılabilir.

## Nerede kullanılır?

Hız ve verimliliğin kritik olduğu sistem programlamasında, oyun motorlarında ve gömülü sistemlerde sıkça kullanılır. Ayrıca TreScout üzerinde incelediğiniz modern komut satırı araçları ve hızlı çalışan masaüstü uygulamaları da genellikle bu yapıyla dağıtılır.

## Sık karıştırılanlar

Sanal makine üzerinde çalışan ara kod dosyalarıyla karıştırılır. Ara kod dosyaları her bilgisayarda çalışabilmek için bir aracıya ihtiyaç duyarken, yerel ikili dosyalar sadece üretildikleri özel sistemde doğrudan çalışır.

## Sıkça sorulanlar

**Yerel ikili dosyalar her bilgisayarda çalışır mı?**

Hayır. Sadece derlendikleri işletim sistemi ve işlemci mimarisinde çalışırlar. Örneğin Windows için derlenmiş bir dosya Mac bilgisayarda doğrudan çalıştırılamaz.

**Hangi diller yerel ikili dosyalar üretir?**

Rust, C++, Go ve Zig gibi sistem programlama dilleri doğrudan yerel ikili dosyalar üretmek üzere tasarlanmıştır.

## İlgili terimler

- [Binary](https://trescout.com/dictionary/binary/)
- [Native](https://trescout.com/dictionary/native/)
- [Compiler](https://trescout.com/dictionary/compiler/)
- [Executables](https://trescout.com/dictionary/executables/)

## İlgili araçlar

- [REA](https://trescout.com/discover/rea/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/native-binaries/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
