# LSP nedir ve nasıl çalışır?

> Language Server Protocol

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

LSP (Language Server Protocol), kod editörleri ile programlama dillerinin analiz motorları arasında standart iletişim sağlayan açık protokoldür.

## Tanım ve temel işlevi
Language Server Protocol (LSP), Microsoft öncülüğünde geliştirilen ve günümüzde tüm modern geliştirici editörleri (VS Code, Neovim, Emacs vb.) tarafından desteklenen evrensel bir protokoldür. Her programlama dili için her editöre ayrı eklenti yazmak yerine; tek bir dil sunucusunun (Language Server) tüm editörlerle JSON-RPC tabanlı standart bir dille konuşmasını sağlar. Bu sayede otomatik kod tamamlama, tanıma gitme (go to definition), hata ayıklama ve refactoring yetenekleri standartlaşır.

## Bir benzetmeyle
Bir tercümanın, farklı dilleri konuşan iki kişi arasında ortak bir dil kullanarak iletişimi sağlaması gibidir; editör ne derseniz deyin, tercüman sayesinde sizi anlar.

## Nasıl çalışır?
Editörünüz, yazdığınız kodu arka planda çalışan bir dil sunucusuna gönderir. Sunucu kodu gerçek zamanlı analiz eder, sözdizimi hatalarını belirler ve önerileri editöre geri iletir. Bu ayrım sayesinde editör arayüzü asla donmaz.

## Nerede kullanılır?
VS Code, Neovim, Sublime Text gibi modern kod editörlerinin ve yapay zekâ destekli kodlama ortamlarının arka planında sürekli çalışır.

## Sık karıştırılanlar
Sadece bir editör eklentisi değildir; editör ile dil analiz motorları arasındaki evrensel konuşma protokolüdür.

## Sıkça sorulanlar

**LSP ne anlama gelir ve açılımı nedir?**  
Language Server Protocol (Dil Sunucusu Protokolü) anlamına gelir. Kod editörleri ile programlama dillerinin akıllı özelliklerini sağlayan arka plan motorları arasındaki köprüdür.

**LSP neden bu kadar önemlidir?**  
N adet editör ve M adet programlama dili için N x M yerine N + M entegrasyon formülü sunar; bir dil sunucusu bir kez yazıldığında tüm uyumlu editörlerde çalışır.

**Hız ve performansı nasıl etkiler?**  
Ağır dil analiz işlemlerini editörün ana arayüzünden ayırarak arka planda yürüttüğü için editörün donmasını engeller ve akıcı bir yazım deneyimi sunar.

## İlgili terimler
- [Agentic Coding Tool](/dictionary/agentic-coding-tool/)
- [CLI](/dictionary/cli/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/lsp/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
