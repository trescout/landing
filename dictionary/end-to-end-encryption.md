# End-to-End Encryption nedir, ne demek?

*Sözlük · Geliştirme · Son güncelleme: 22 Eylül 2026*

> E2EE

End-to-end encryption (Türkçe karşılığıyla **uçtan uca şifreleme**), yalnız uçların okuduğu güvenlik düzenidir.

## Tanım ve Kelime Kökeni

Veri cihazda kilitlenir, hedefte açılır. Taşıyıcı ve sunucu içeriği göremez. Gizliliğin temel kalkanıdır. WhatsApp ve Signal bilinen örnekleridir.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?

**Mesaj:** Özel sohbetler.
**Dosya:** Güvenli aktarım.
**Yedek:** Şifreli kopya.

## Teknik Derinlik ve Mimari

Düzen:

**Anahtar çifti:** Açık ve gizli anahtar.
**Doğrulama:** Karşı tarafın kimliği.
**İletim gizliliği:** Oturum anahtarı tazelenir.

Kural: Yedek şifreli tutulur, anahtar ayrı saklanır. Cihaz kaybında kurtarma kodu gerekir.

## Sık Karıştırılanlar

TLS sanılır. TLS yolda korur, sunucu görür. Uçtan uca olanda sunucu bile göremez. Biri kurye zırhı, diğeri mühürlü zarftır.

## Farklı Disiplinlerde Kullanımı

**Kilitli kutu:** Taşıyıcı göremez içerik.
**Mühür:** Açılınca belli olan zarf.
**Kapalı devre:** Dışa kapalı hat.

*Kilidi yalnız ikinizde olan kutuyla mektuplaşmaya benzer.*

## Sıkça Sorulanlar

**Çalınırsa okunur mu?**

Hayır. Anahtar uçlardadır, çalınan yığın anlamsızdır.

**Her uygulamada var mı?**

Hayır. Ayarlardan denetlenir, varsayım yapılmaz.

**Yedekleme nasıl olur?**

Şifreli yedek ve kurtarma kodu gerekir. Kodsuz geri dönüş yoktur.

**Kurumsal uygun mu?**

Kayıt ve denetim ihtiyacıyla dengelenir. Politika belirlenir.

## İlgili terimler

- [Security Scanner](https://trescout.com/dictionary/security-scanner/)
- [Linux Server Security](https://trescout.com/dictionary/linux-server-security/)
- [SSO](https://trescout.com/dictionary/sso/)

## İlgili araçlar

- [Croc](https://trescout.com/discover/croc/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/end-to-end-encryption/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
