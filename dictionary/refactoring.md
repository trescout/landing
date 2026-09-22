# Refactoring nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

Refactoring (Türkçe karşılığıyla **yeniden düzenleme**), davranışı koruyup kodu sadeleştirmedir.

## Tanım ve Kelime Kökeni
Dış görünüş bozulmadan iç tesisat yenilenir. Kodun okunabilirliği artar, yeni özellik eklemek kolaylaşır. Teknik borcu kapatan temizlik sürecidir. Martin Fowler bu disiplinin referans adıdır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **İnceleme:** Kod gözden geçirme turları.
- **Borç ödeme:** Sprint içine serpiştirilen temizlik.
- **Devralma:** Eski koda girmeden önce sadeleştirme.

## Teknik Derinlik ve Mimari
Yaygın hamleler:
- **Fonksiyon çıkarma:** Uzun bloğu adlandırılmış parçaya bölme.
- **Yeniden adlandırma:** Niyeti anlatan isim.
- **Ölü kod:** Kullanılmayanı silme.

Örnek:

```
# önce
def f(a):
    return a*a*3.14
# sonra
def daire_alani(yaricap):
    return yaricap * yaricap * 3.14
```

Kural: Önce test yazılır, sonra dokunulur. Test yoksa ilk iş testtir.

## Sık Karıştırılanlar
Özellik veya hata düzeltme sanılır. Oysa çıktı değişmez, yalnızca iç yapı düzelir. Davranış aynı, kod farklıdır.

## Farklı Disiplinlerde Kullanımı
- **Tesisat:** Duvar dururken boru yenileme.
- **Redaksiyon:** Konu aynı, cümle akıcı.
- **Budama:** Ağaç aynı, dal düzenli.

## Bir benzetmeyle
Kitabın konusunu değiştirmeden cümleleri akıcı hale getirmeye benzer.

## Sıkça sorulanlar

**Neden yapıyoruz?**  
Temiz kod hata ve yavaşlamayı önler, yeni işi hızlandırır.

**Ne zaman yapılır?**  
Dokunulan kodda, küçük parçalar halinde. Büyük temizlik ayrı planlanır.

**Riski nedir?**  
Testsiz dokunuş davranışı bozar. Test güvencesi olmadan girilmez.

**Ne sıklıkla yapılır?**  
Sürekli, küçük dozda. Sprint içine serpiştirilir, ertelenmez.

## İlgili terimler
- [Agentic Coding Tool](/dictionary/agentic-coding-tool/)
- [Unit Testing](/dictionary/unit-testing/)
- [Tech Stack](/dictionary/tech-stack/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/refactoring/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
