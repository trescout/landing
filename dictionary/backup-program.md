# Backup Program nedir, ne demek?

*Sözlük · Veri & Altyapı · Son güncelleme: 22 Eylül 2026*

Backup program (Türkçe karşılığıyla **yedekleme programı**), veriyi düzenli kopyalayan yazılımdır.

## Tanım ve Kelime Kökeni

"Backup" **yedek** demektir. Dosyalar aralıklarla başka konuma kopyalanır. Arıza, saldırı veya silinmede geri dönülür. Güvenli dijital yaşamın temelidir.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?

**Kişisel:** Fotoğraf ve belge yedeği.
**Sunucu:** Gece otomatik kopya.
**Bulut:** Hesap eşitlemesi.

## Teknik Derinlik ve Mimari

Türler:

**Tam:** Her şeyin kopyası, yavaş ama basit.
**Artımlı:** Değişenin kopyası, hızlı.
**3-2-1 kuralı:** 3 kopya, 2 ortam, 1 uzak.

Örnek:

```
rsync -av belgeler/ /yedek/belgeler/
```

Kural: Yedek denenmeden güvenilmez. Geri yükleme periyodik test edilir.

## Farklı Disiplinlerde Kullanımı

**Fotokopi:** Kasada duran kopya.
**Kasa:** Değerli evrak saklama.
**Sigorta:** Felaket teminatı.

*Önemli evrakın fotokopisini başka kasada saklamaya benzer.*

## Sıkça Sorulanlar

**Neden önemlidir?**

Kayıp genelde dönüşüzdür. Yedek, hatanın bedelini küçültür.

**Nereye alınmalı?**

Orijinalden ayrı yere: Bulut veya harici disk. Aynı disk yedek sayılmaz.

**Ne sıklıkla alınmalı?**

Değişim hızına göre. Günlük işte günlük, kritik hatta saatlik alınır.

**Test edilir mi?**

Evet. Geri yükleme denenmeden yedek güven vermez.

## İlgili terimler

- [Incremental Backup](https://trescout.com/dictionary/incremental-backup/)
- [Data Pipeline](https://trescout.com/dictionary/data-pipeline/)
- [Secrets](https://trescout.com/dictionary/secrets/)

## İlgili araçlar

- [Restic](https://trescout.com/discover/restic/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/backup-program/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
