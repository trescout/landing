# LSP nedir, ne demek ve nasıl çalışır?

> Language Server Protocol

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

LSP (Language Server Protocol), modern kod editörleri ile programlama dillerinin analiz motorları arasında standart iletişim sağlayan JSON-RPC tabanlı açık protokoldür.

## 1. Tanım ve çözdüğü matematiksel problem: M × N karmaşıklığı

Language Server Protocol (LSP), 2016 yılında Microsoft (VS Code ekibi), Red Hat ve Codenvy öncülüğünde geliştirilen ve günümüzde geliştirici araçlarının temel taşı haline gelen evrensel bir protokoldür.

LSP'nin getirdiği en büyük devrim, yazılım dünyasının yıllardır muzdarip olduğu **$M \times N$ karmaşıklık krizini $M + N$ düzeyine indirmesidir**:

- **LSP Öncesi ($M \times N$):** Eğer piyasada 5 popüler kod editörü (VS Code, Neovim, Sublime Text, Emacs, Eclipse) ve 10 popüler programlama dili (Python, Rust, Go, TypeScript, C++ vb.) varsa; her dilde otomatik tamamlama ve sözdizimi denetimi sağlamak için **5 × 10 = 50 farklı eklenti** yazılması ve ayrı ayrı güncellenmesi gerekiyordu.
- **LSP Sonrası ($M + N$):** Her dil topluluğu yalnızca tek bir "Language Server" (Dil Sunucusu) yazar; her editör geliştiricisi ise yalnızca bir "LSP Client" (İstemci) entegre eder. Sonuç: **5 + 10 = 15 bileşen**. Yeni çıkan bir programlama dili tek bir LSP sunucusu yazarak piyasadaki onlarca editörün tamamında ilk günden kusursuz çalışır hale gelir.

## 2. LSP nasıl çalışır? Protokol mimarisi ve JSON-RPC 2.0

LSP, editör (Client) ile dil analiz motoru (Server) arasında genellikle yerel standart girdi/çıktı (`stdin`/`stdout`) veya yerel soketler (IPC) üzerinden çalışan **JSON-RPC 2.0** mesajlaşma protokolüdür.

Ağır semantik analiz ve tip çözümleme işlemleri editörün ana iş parçacığından (UI thread) ayrı bir işletim sistemi sürecinde (process) yürütülür; bu sayede 100 bin satırlık projelerde dahi editörünüz asla donmaz veya takılmaz.

### Temel Protokol Döngüsü ve İstek Tipleri

```
   Editör (LSP Client)                   Dil Sunucusu (Language Server)
          │                                            │
          │─────── textDocument/didOpen ──────────────>│ (Dosya açıldı, AST kurulur)
          │─────── textDocument/didChange ───────────>│ (Kullanıcı harf yazdı, artımlı senk.)
          │<────── textDocument/publishDiagnostics ────│ (Kırmızı dalgalı alt çizgi / Hatalar)
          │                                            │
          │─────── textDocument/completion ───────────>│ (Ctrl+Space: Öneriler istendi)
          │<────── CompletionItem[] ───────────────────│ (Metot ve değişken listesi döner)
          │                                            │
          │─────── textDocument/definition ───────────>│ (F12: Tanıma git / Go to definition)
          │<────── Location (Dosya, Satır, Sütun) ────│ (İlgili kaynak kod konumu açılır)
```

1. **İlklendirme (`initialize`):** Editör başlatıldığında sunucuya yeteneklerini (`client capabilities`) bildirir; sunucu da hangi özellikleri desteklediğini (`server capabilities`) onaylar.
2. **Belge Senkronizasyonu (`didChange`):** Kullanıcı kod yazdıkça dosyanın tamamı yerine yalnızca değişen satır ve karakter aralığı (incremental document sync) sunucuya aktarılır.
3. **Tanılama (`publishDiagnostics`):** Dil sunucusu, kodu derlemeden arka planda Soyut Sözdizimi Ağacını (AST - Abstract Syntax Tree) ve tip tablosunu günceller. Bir hata varsa kırmızı hata çizgilerini editöre asenkron bildirim olarak yollar.
4. **Zengin İstekler (`hover`, `completion`, `rename`):** Kullanıcı bir fonksiyonun üzerine fareyle geldiğinde veya yeniden adlandırma (symbol rename) yaptığında sunucu projedeki tüm referansları hesaplayarak yanıt döner.

## 3. Ekosistemde en yaygın kullanılan Language Server'lar

| Dil | Resmi / Popüler Dil Sunucusu | Öne Çıkan Özellikleri |
| :--- | :--- | :--- |
| **Rust** | `rust-analyzer` | Olağanüstü hızlı tip çıkarımı, makro açılımları ve borrow checker uyarıları. |
| **Python** | `pyright` / `basedpyright` / `ruff` | Statik tip doğrulaması ve Ruff ile mikrosaniye hızında lintleme. |
| **Go** | `gopls` | Go resmi ekibi tarafından geliştirilen, modül ve paket farkındalıklı sunucu. |
| **TypeScript / JS** | `vtsls` / `typescript-language-server` | Node ve tarayıcı API'leri için akıllı IntelliSense ve refactoring. |
| **C / C++** | `clangd` | LLVM tabanlı, `compile_commands.json` ile büyük C++ kod tabanlarında üstün doğruluk. |
| **Lua** | `lua-language-server` | Neovim eklenti geliştiricileri ve oyun motorları için özel tip annotasyonları. |

## 4. LSP vs DAP (Debug Adapter Protocol) vs LSIF / SCIP

Geliştirici ekosisteminde benzer harf kısaltmaları sıkça karıştırılır:

- **LSP (Language Server Protocol):** Kod yazımı esnasındaki dinamik akıllı özellikleri (tamamlama, hata tespiti, formatlama) yönetir.
- **DAP (Debug Adapter Protocol):** Çalışma zamanındaki hata ayıklama işlemlerini yönetir. Kesme noktaları (breakpoints), değişken izleme (watch expressions) ve adım adım yürütme (step into/over) DAP üzerinden editörle haberleşir.
- **SCIP / LSIF:** Zengin kod tabanlarının derleme anında önceden indekslenip GitHub veya Sourcegraph gibi web arayüzlerinde sunucu çalıştırmadan "kodda gezinme" (code navigation) yapmasını sağlayan statik indeksleme formatlarıdır.

## Bir benzetmeyle

LSP, dünyanın tüm dillerini kendi ülkesinin kurallarıyla konuşan yerel uzmanlar ile bu uzmanları dinleyen uluslararası bir diplomasi meclisi arasındaki simultane çevirmendir; meclisteki editörün kim olduğu fark etmeksizin mesaj kusursuzca iletilir.

## Sıkça sorulanlar

**LSP ne demek, açılımı nedir?**  
Language Server Protocol (Dil Sunucusu Protokolü) anlamına gelir. Kod editörleri ile programlama dillerinin sözdizimi, tip kontrolü ve otomatik tamamlama motorları arasındaki iletişimi standartlaştıran açık protokoldür.

**LSP neden $M \times N$ problemini çözer?**  
Eski modelde $M$ dil ve $N$ editör için her editöre özel $M \times N$ eklenti yazılması gerekiyordu. LSP ile her dil tek bir sunucu, her editör tek bir istemci yazarak $M + N$ entegrasyon formülüne kavuşur.

**LSP editörün yavaşlamasını nasıl engeller?**  
Dilin ağır sözdizimi ağacı (AST) analizi ve tip çözümlemeleri ana editör sürecinden izole edilmiş arka plan süreçlerinde (JSON-RPC üzerinden) yürütülür; böylece arayüz hiçbir zaman kilitlenmez.

**DAP ile LSP arasındaki fark nedir?**  
LSP kod yazma, kod tamamlama ve sözdizimi hatalarını analiz ederken; DAP (Debug Adapter Protocol) kodun çalışma zamanında kesme noktaları (breakpoints) koyularak adım adım debug edilmesini sağlar.

## İlgili terimler

- [Agentic Coding Tool](/dictionary/agentic-coding-tool/)
- [CLI](/dictionary/cli/)
- [Keybindings](/dictionary/keybindings/)
- [Code Snippets](/dictionary/code-snippets/)
- [Runtime](/dictionary/runtime/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/lsp/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
