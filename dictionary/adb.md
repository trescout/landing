# ADB nedir, ne demek?

*Sözlük · Geliştirme · Son güncelleme: 22 Eylül 2026*

> Android Debug Bridge

ADB (**Android Debug Bridge**, Android hata ayıklama köprüsü), bilgisayar ile Android cihaz arasında komut ve hata ayıklama iletişimi sağlayan bir araçtır.

## Tanım ve Kelime Kökeni

"Debug" **hata ayıklama**, "bridge" ise **köprü** demektir. ADB, bilgisayardaki istemci ile cihazdaki `adb` daemon arasında iletişim kurar; uygulama yükleme, günlük toplama, hata ayıklama ve sınırlı cihaz yönetimi işlemlerinde kullanılır. Android SDK Platform-Tools paketinin parçasıdır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?

**Geliştirme:** Uygulama yükleme ve kayıt.
**Test:** Çok cihazda deneme.
**Özelleştirme:** İleri düzey ayar.

## Teknik Derinlik ve Mimari

Üçlü düzen:

**İstemci:** Bilgisayardaki komut.
**Sunucu:** Arka planda koşan yönetici.
**Daemon:** Cihazdaki karşılayıcı.

Akış:

```
adb devices
adb install uygulama.apk
```

İlki bağlı cihazları listeler, ikincisi uygulama paketini kurar. USB hata ayıklama cihazda etkinleştirilmelidir. Yanlış komutlar veri kaybına yol açabileceği için çalıştırmadan önce hedef cihazı ve komutu doğrulamak gerekir.

## Sık Karıştırılanlar

Dosya aktarımı sanılır. O yalnızca kopyalar, ADB sisteme müdahale eder. Yetki farkı büyüktür.

## Farklı Disiplinlerde Kullanımı

**Kablo:** Sinyal taşıyan hat.
**Tercüman:** İki tarafın dili.
**Kumanda:** Uzaktan yönetim.

*Bilgisayarı kumanda merkezi, cihazı uzay aracı sayarsanız ADB aradaki sinyal kablosudur.*

## Sıkça Sorulanlar

**Herkes kullanabilir mi?**

Temel komutlar öğrenilebilir; ancak özellikle `adb shell` ve silme işlemleri teknik bilgi gerektirir. Komutu çalıştırmadan önce etkisini doğrulamak gerekir.

**Kablosuz olur mu?**

Evet. Desteklenen Android sürümlerinde cihazla eşleştirdikten sonra Wi-Fi üzerinden bağlantı kurulabilir. Kararlılık ve hız, yerel ağın kalitesine bağlıdır.

**Güvenli mi?**

Cihaz sizdeyse evet. Bilinmeyen bilgisayara takılan cihazda onay verilmez.

**Fastboot farkı nedir?**

ADB, Android çalışırken işletim sistemiyle iletişim kurar. Fastboot ise cihaz bootloader modundayken bölüm görüntüsü veya ürün yazılımı işlemleri için kullanılır; desteklenen komutlar ve kilit açma süreci cihaza göre değişir.

## İlgili terimler

- [CLI](https://trescout.com/dictionary/cli/)
- [SDK](https://trescout.com/dictionary/sdk/)
- [Emulator](https://trescout.com/dictionary/emulator/)

## İlgili araçlar

- [Universal Android Debloater Next Generation](https://trescout.com/discover/universal-android-debloater-next-generation/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/adb/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
