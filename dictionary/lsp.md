# LSP nedir?

> Language Server Protocol

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-06-03

Kod yazarken editörünüze akıllı özellikler kazandıran standart bir iletişim protokolüdür.

## Tanım
LSP, kod yazma araçları (editörler) ile kodun mantığını anlayan sunucular arasında bir köprüdür. Bu protokol sayesinde, kullandığınız editör; hata bulma, otomatik tamamlama ve tanımlara gitme gibi özellikleri tüm dillerde standart bir şekilde sunabilir. Editörünüzün hangi dili kullandığınızı bilmesine gerek kalmadan akıllı davranmasını sağlar.

## Bir benzetmeyle
Bir tercümanın, farklı dilleri konuşan iki kişi arasında ortak bir dil kullanarak iletişimi sağlaması gibidir; editör ne derseniz deyin, tercüman sayesinde sizi anlar.

## Nasıl çalışır?
Editörünüz, yazdığınız kodu arka planda çalışan bir 'dil sunucusuna' gönderir. Sunucu kodu analiz eder ve size öneriler sunar. Siz hiçbir şey hissetmeden kodunuzu daha hızlı ve hatasız yazarsınız.

## Nerede kullanılır?
VS Code gibi modern kod editörlerinin arka planında sürekli çalışır.

## Sık karıştırılanlar
Sadece bir editör özelliği değil, editör ile dil arasındaki evrensel bir konuşma dilidir.

## Sıkça sorulanlar

**Neden bu kadar önemli?**  
Her editör için ayrı ayrı özellik geliştirmek yerine, bir kez yazılan dil desteğinin her yerde çalışmasını sağlar.

**Hızımı etkiler mi?**  
Hayır, aksine hata yapmanızı engelleyerek kod yazma sürecinizi hızlandırır.

## İlgili terimler
- [Agentic Coding Tool](/dictionary/agentic-coding-tool/)
- [CLI](/dictionary/cli/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/lsp/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
