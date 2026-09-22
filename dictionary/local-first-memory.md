# Local-first Memory nedir, ne demek?

**Kategori:** Veri & Altyapı  
**Son güncelleme:** 2026-09-22

Local-first memory (Türkçe karşılığıyla **önce-yerel bellek**), verinin cihazda durduğu yaklaşımdır.

## Tanım ve Kelime Kökeni
"Local-first" **önce yerel** demektir. Bulut yerine cihaz esas alınır. Kesintide çalışır, gizlilik korunur. Not uygulamaları ve yerel yapay zekâ bu düzendendir.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Not:** Çevrimdışı defter.
- **Görev:** Yerel liste.
- **Medya:** Cihaz arşivi.

## Teknik Derinlik ve Mimari
Düzen:
- **Yerel veritabanı:** Cihaz içi dosya.
- **Senkron:** CRDT ile çakışmasız birleşme.
- **Yedek:** Ayrı kopya disiplini.

Tarayıcı kaydı:

```
localStorage.setItem("not", metin);
```

Kural: Cihaz bozulursa veri gider. Yedek bulutta veya diskte tutulur.

## Sık Karıştırılanlar
Çevrimdışı mod sanılır. O geçici durumdur, bu sahiplik düzenidir. Veri sizindir, kirada değildir.

## Farklı Disiplinlerde Kullanımı
- **Çekmece:** Kilitli ev çekmecesi.
- **Kasa:** Kişisel emanet.
- **Cüzdan:** Cepte taşınan değer.

## Bir benzetmeyle
Bilgiyi banka kasası yerine evdeki kilitli çekmecede tutmaya benzer.

## Sıkça sorulanlar

**Cihaz bozulursa ne olur?**  
Veri gider. Yedek ayrı yerde tutulur, bulut otomatik sanılmaz.

**Senkron nasıl olur?**  
CRDT ile çakışmasız birleşir. Cihazlar buluşunca eşitlenir.

**Ne zaman bulut?**  
Paylaşım ve yedek gerektiğinde. Yerel esas, bulut kopyadır.

**Güvenli mi?**  
Cihaz şifrelemesiyle evet. Kayıp cihaza karşı kilit şarttır.

## İlgili terimler
- [Local-first](/dictionary/local-first/)
- [Memory System](/dictionary/memory-system/)
- [Self-hosting](/dictionary/self-hosting/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/local-first-memory/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
