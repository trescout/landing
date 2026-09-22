# Backup Program nedir, ne demek?

**Kategori:** Veri & Altyapı  
**Son güncelleme:** 2026-09-22

Backup program (Türkçe karşılığıyla **yedekleme programı**), veriyi düzenli kopyalayan yazılımdır.

## Tanım ve Kelime Kökeni
"Backup" **yedek** demektir. Dosyalar aralıklarla başka konuma kopyalanır. Arıza, saldırı veya silinmede geri dönülür. Güvenli dijital yaşamın temelidir.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Kişisel:** Fotoğraf ve belge yedeği.
- **Sunucu:** Gece otomatik kopya.
- **Bulut:** Hesap eşitlemesi.

## Teknik Derinlik ve Mimari
Türler:
- **Tam:** Her şeyin kopyası, yavaş ama basit.
- **Artımlı:** Değişenin kopyası, hızlı.
- **3-2-1 kuralı:** 3 kopya, 2 ortam, 1 uzak.

Örnek:

```
rsync -av belgeler/ /yedek/belgeler/
```

Kural: Yedek denenmeden güvenilmez. Geri yükleme periyodik test edilir.

## Farklı Disiplinlerde Kullanımı
- **Fotokopi:** Kasada duran kopya.
- **Kasa:** Değerli evrak saklama.
- **Sigorta:** Felaket teminatı.

## Bir benzetmeyle
Önemli evrakın fotokopisini başka kasada saklamaya benzer.

## Sıkça sorulanlar

**Neden önemlidir?**  
Kayıp genelde dönüşüzdür. Yedek, hatanın bedelini küçültür.

**Nereye alınmalı?**  
Orijinalden ayrı yere: Bulut veya harici disk. Aynı disk yedek sayılmaz.

**Ne sıklıkla alınmalı?**  
Değişim hızına göre. Günlük işte günlük, kritik hatta saatlik alınır.

**Test edilir mi?**  
Evet. Geri yükleme denenmeden yedek güven vermez.

## İlgili terimler
- [Incremental Backup](/dictionary/incremental-backup/)
- [Data Pipeline](/dictionary/data-pipeline/)
- [Secrets](/dictionary/secrets/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/backup-program/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
