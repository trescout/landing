# Just-in-Time Compiler nedir?

*Geliştirme · Son güncelleme: 28 Ekim 2026*

> JIT Compiler

Yazılım kodunu program çalıştığı anda anlık olarak makine diline çevirip performansı artıran derleyici bileşenidir.

## Tanım

Just-in-Time Compiler, kaynak kodunu veya ara kodu programın yürütülmesi esnasında makine koduna dönüştüren yazılım mekanizmasıdır. Klasik önceden derleme yöntemlerinden farklı olarak kodun tamamını baştan çevirmek yerine ihtiyaç duyulan parçaları çalışma anında işler. Böylece hem hızlı başlangıç süresi hem de yüksek çalışma zamanı performansı elde edilmesini sağlar. Modern sanal makinelerde ve yorumlamalı dillerde sıkça tercih edilir.

*Yabancı dildeki bir kitabı önceden tamamen Türkçe diline çevirmek yerine sahnede konuşmacı konuştukça anında kulaklığa çeviri yapan bir mütercim gibidir.*

## Nasıl çalışır?

Program çalışmaya başladığında önce kod bayt kod seviyesinde yorumlanır. Sık çalışan ve performans kritik olan kod blokları tespit edildiğinde bu bileşen devreye girer. İlgili blokları doğrudan işlemcinin anlayacağı makine komutlarına dönüştürür ve hafızada saklayarak sonraki çağrılarda hızlıca çalıştırır.

## Nerede kullanılır?

Java Virtual Machine, .NET Common Language Runtime ve modern web tarayıcılarındaki JavaScript motorlarında yaygın olarak kullanılır.

## Sık karıştırılanlar

Çalışma anındaki derleme eyleminin kendisi olan JIT compilation kavramından farklı olarak bu işlemi gerçekleştiren somut yazılım motorunu ifade eder.

## Sorular ve yanıtlar

**JIT compiler programı neden hızlandırır?**

Sık tekrar eden kod parçalarını makine koduna çevirip önbelleğe aldığı için her defasında kodu yeniden yorumlama ihtiyacını ortadan kaldırır.

**AOT derleyicilerden farkı nedir?**

AOT derleyiciler kodu program çalışmadan önce tamamen makine diline dönüştürürken bu bileşen kod çalışırken dinamik olarak derleme yapar.

## İlgili terimler

- [Just-in-Time Compilation](https://trescout.com/dictionary/jit-compilation/)
- [Compiler](https://trescout.com/dictionary/compiler/)
- [Runtime](https://trescout.com/dictionary/runtime/)
- [Compile-time](https://trescout.com/dictionary/compile-time/)

Bu açıklama TreScout için yapay zekâ ile sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/just-in-time-compiler/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
