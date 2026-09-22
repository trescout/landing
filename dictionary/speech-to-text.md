# Speech-to-Text nedir, ne demek?

**Kategori:** Yapay Zekâ  
**Son güncelleme:** 2026-09-22

Speech-to-text (kısaca **STT**, konuşmadan metne), sesi yazılı metne çeviren teknolojidir.

## Tanım ve Kelime Kökeni
Ses dalgaları sayısal özniteliklere çevrilir, model kelimeleri tanır. Yapay zekâ tonlama ve bağlamı da okur. Hatasız değildir, ancak temiz kayıtta isabeti yüksektir.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Toplantı:** Otomatik tutanak.
- **Asistan:** Sesli komut.
- **Altyazı:** Video metni.

## Teknik Derinlik ve Mimari
Hat:
- **Önişleme:** Gürültü temizliği.
- **Akustik model:** Sesin sese, sesin harfe eşlenmesi.
- **Dil modeli:** Cümle olasılığı.

Yerel deneme:

```
whisper toplanti.mp3 --language tr --model base
```

Model büyüdükçe isabet artar, süre uzar. Gizli kayıt için izin ve bilgilendirme şarttır.

## Sık Karıştırılanlar
Text-to-speech sanılır. O metni sese çevirir, bu sesi metne. İkisi ters yöndür.

## Farklı Disiplinlerde Kullanımı
- **Sekreter:** Konuşurken not tutma.
- **Daktilo:** Söyleneni yazma.
- **Altyazı odası:** Yayına metin yetiştirme.

## Bir benzetmeyle
Konuşurken yerinize not tutan hızlı sekreter gibidir.

## Sıkça sorulanlar

**Her aksanı anlar mı?**  
Yaygın aksanlarda iyidir, nadir dil ve bozuk kayıtta hata artar.

**Doğruluğu nedir?**  
Temiz kayıtta yüksektir, gürültü ve jargon düşürür. Kritik metin gözden geçirilir.

**Türkçe destekler mi?**  
Evet. Büyük modeller Türkçede güçlüdür, aksan ve terminoloji test edilir.

**Gizlilik riski var mı?**  
Bulut serviste ses dışarı gider. Hassas toplantıda yerel model tercih edilir.

## İlgili terimler
- [Text-to-Speech](/dictionary/text-to-speech/)
- [Speech Synthesis](/dictionary/speech-synthesis/)
- [NLP](/dictionary/nlp/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/speech-to-text/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
