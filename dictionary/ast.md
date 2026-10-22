# Abstract Syntax Tree nedir?

*Geliştirme · Son güncelleme: 22 Ekim 2026*

> Abstract Syntax Tree

Kaynak kodun dilbilgisi yapısını hiyerarşik bir ağaç şeklinde temsil eden veri modelidir.

## Tanım

Abstract Syntax Tree (AST), kaynak kodun derleyiciler veya yorumlayıcılar tarafından kolayca analiz edilebilmesi için sözdizim kurallarına göre yapılandırılmış ağaç biçimli bir temsilidir. Kodunuzdaki her değişken, işlem ve fonksiyon bu ağaç üzerinde birer düğüm olarak yer alır. Kodun anlamsal bütünlüğünü korurken gereksiz parantezleri veya boşlukları ayıklayarak analizi basitleştirir.

*Bir cümlenin öğelerini özne, yüklem ve nesne dallarına ayırdığınız dilbilgisi tahlil şemasına benzer.*

## Nasıl çalışır?

Kod ayrıştırıcı metin halindeki kodu okur ve sözcüksel analizden geçirerek belirteçlere dönüştürür. Ardından sözdizim kurallarına uygun biçimde bu belirteçleri üst ve alt düğümler halinde ağaç yapısına dizer. Derleyiciler, linter araçları ve kod analiz motorları optimizasyon veya hata denetimlerini bu ağacı gezerek gerçekleştirir.

## Nerede kullanılır?

Programlama dili derleyicilerinde, statik kod analiz ve güvenlik araçlarında sıkça kullanılır. Kod biçimlendirme araçları ve yapay zekâ destekli kod arama sistemlerinde de bu yapıdan yararlanılır.

## Sık karıştırılanlar

AST Parsing ile karıştırılabilir. AST Parsing bu ağacı inşa etme eylemi iken AST doğrudan ortaya çıkan hiyerarşik veri yapısını ifade eder.

## Sorular ve yanıtlar

**AST neden düz metin koddan daha avantajlıdır?**

Düz metin kodda yapısal ilişkileri takip etmek zorken AST sayesinde kodun mantıksal hiyerarşisi netleşir ve programatik olarak dönüştürülmesi kolaylaşır.

**Hangi araçlar AST kullanır?**

Babel, ESLint, TypeScript derleyicisi ve modern programlama dillerinin derleme aşamaları AST altyapısını kullanır.

## İlgili terimler

- [AST Parsing](https://trescout.com/dictionary/ast-parsing/)
- [Parser](https://trescout.com/dictionary/parser/)
- [Compiler](https://trescout.com/dictionary/compiler/)
- [Clean Code](https://trescout.com/dictionary/clean-code/)

Bu açıklama TreScout için yapay zekâ ile sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/ast/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
