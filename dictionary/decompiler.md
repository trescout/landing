# Decompiler nedir?

*Sözlük · Geliştirme · Son güncelleme: 16 Eylül 2026*

Makine kodunu tekrar okunabilir bir yazılım diline dönüştüren bir çeviri aracıdır.

## Tanım

Bir bilgisayar programı derlendiğinde, insanlar için anlaşılır olan kodlar makine diline yani sadece işlemcinin anlayacağı sayılara dönüşür. Decompiler, bu süreci tersine çevirerek karmaşık ve anlamsız görünen bu sayıları, yazılımcıların üzerinde çalışabileceği kaynak kod formatına geri getirmeye çalışır. Bu işlem, genellikle orijinal kaynak kodun kaybolduğu durumlarda veya bir programın nasıl çalıştığını anlamak için kullanılır.

*Yabancı bir dilde yazılmış bir kitabı, tekrar ana dilinize çeviren bir tercüme makinesi gibidir; ancak çeviri bazen orijinal kelimeleri tam karşılamayabilir.*

## Nasıl çalışır?

Programın çalıştırılabilir dosyasını alır ve içindeki komut dizilerini analiz eder. Ardından bu komutları, benzer işlevi gören programlama dili yapılarıyla eşleştirir. Sonuçta ortaya çıkan metin, orijinal kodun birebir aynısı olmasa da mantığını anlamanızı sağlayan bir taslak sunar.

## Nerede kullanılır?

Yazılım güvenliği araştırmalarında, bir uygulamanın nasıl çalıştığını anlamak veya eski ve kaynak kodu kaybolmuş yazılımları güncellemek için kullanılır.

## Sık karıştırılanlar

Derleyici (Compiler) ile karıştırılır; derleyici kodu makineye çevirir, decompiler ise makine kodunu insana çevirir.

## Sıkça sorulanlar

**Decompiler ile orijinal kodun aynısını alabilir miyim?**

Genellikle hayır; çünkü derleme sırasında bazı değişken isimleri ve yorum satırları silinir, bu yüzden çıkan sonuç biraz daha karmaşık ve isimsiz olabilir.

**Her program decompile edilebilir mi?**

Teknik olarak çoğu edilebilir ancak bazı yazılımlar, bu işlemi zorlaştıran 'obfuscation' yani kod karıştırma yöntemleriyle korunur.

## İlgili terimler

- [Compiler](https://trescout.com/dictionary/compiler/)
- [Binary](https://trescout.com/dictionary/binary/)
- [Software Reverse Engineering](https://trescout.com/dictionary/software-reverse-engineering/)

## İlgili araçlar

- [Ghidra](https://trescout.com/discover/ghidra/)
- [ASC](https://trescout.com/discover/asc/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/decompiler/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
