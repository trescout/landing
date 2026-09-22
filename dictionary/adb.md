# ADB nedir, ne demek?

> Android Debug Bridge

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

ADB (**Android Debug Bridge**, Android hata ayıklama köprüsü), bilgisayardan cihaza komut köprüsüdür.

## Tanım ve Kelime Kökeni
"Debug" **hata ayıklama**, "bridge" ise **köprü** demektir. Bilgisayar ile cihaz arası komut dili kurar: Uygulama yüklenir, kayıt alınır, ayar değişir. Geliştirici setinin parçasıdır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Geliştirme:** Uygulama yükleme ve kayıt.
- **Test:** Çok cihazda deneme.
- **Özelleştirme:** İleri düzey ayar.

## Teknik Derinlik ve Mimari
Üçlü düzen:
- **İstemci:** Bilgisayardaki komut.
- **Sunucu:** Arka planda koşan yönetici.
- **Daemon:** Cihazdaki karşılayıcı.

Akış:

```
adb devices
adb install uygulama.apk
```

İlki cihazı listeler, ikincisi kurar. USB hata ayıklama cihazda açılır. Yanlış komut veriyi silebilir, yol iki kez denetlenir.

## Sık Karıştırılanlar
Dosya aktarımı sanılır. O yalnızca kopyalar, ADB sisteme müdahale eder. Yetki farkı büyüktür.

## Farklı Disiplinlerde Kullanımı
- **Kablo:** Sinyal taşıyan hat.
- **Tercüman:** İki tarafın dili.
- **Kumanda:** Uzaktan yönetim.

## Bir benzetmeyle
Bilgisayarı kumanda merkezi, cihazı uzay aracı sayarsanız ADB aradaki sinyal kablosudur.

## Sıkça sorulanlar

**Herkes kullanabilir mi?**  
Teknik bilgi ister. Yanlış komut veriyi silebilir, yol denetlenir.

**Kablosuz olur mu?**  
Evet. Eşleşme sonrası Wi-Fi üzerinden bağlanılır, hız kabloyu tutmaz.

**Güvenli mi?**  
Cihaz sizdeyse evet. Bilinmeyen bilgisayara takılan cihazda onay verilmez.

**Fastboot farkı nedir?**  
Fastboot sistem altı yazar, ADB sistem üstünde çalışır. İlki derin, ikincisi günlüktür.

## İlgili terimler
- [CLI](/dictionary/cli/)
- [SDK](/dictionary/sdk/)
- [Emulator](/dictionary/emulator/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/adb/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
