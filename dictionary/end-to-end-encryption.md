# End-to-End Encryption nedir, ne demek?

> E2EE

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

End-to-end encryption (Türkçe karşılığıyla **uçtan uca şifreleme**), yalnız uçların okuduğu güvenlik düzenidir.

## Tanım ve Kelime Kökeni
Veri cihazda kilitlenir, hedefte açılır. Taşıyıcı ve sunucu içeriği göremez. Gizliliğin temel kalkanıdır. WhatsApp ve Signal bilinen örnekleridir.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Mesaj:** Özel sohbetler.
- **Dosya:** Güvenli aktarım.
- **Yedek:** Şifreli kopya.

## Teknik Derinlik ve Mimari
Düzen:
- **Anahtar çifti:** Açık ve gizli anahtar.
- **Doğrulama:** Karşı tarafın kimliği.
- **İletim gizliliği:** Oturum anahtarı tazelenir.

Kural: Yedek şifreli tutulur, anahtar ayrı saklanır. Cihaz kaybında kurtarma kodu gerekir.

## Sık Karıştırılanlar
TLS sanılır. TLS yolda korur, sunucu görür. Uçtan uca olanda sunucu bile göremez. Biri kurye zırhı, diğeri mühürlü zarftır.

## Farklı Disiplinlerde Kullanımı
- **Kilitli kutu:** Taşıyıcı göremez içerik.
- **Mühür:** Açılınca belli olan zarf.
- **Kapalı devre:** Dışa kapalı hat.

## Bir benzetmeyle
Kilidi yalnız ikinizde olan kutuyla mektuplaşmaya benzer.

## Sıkça sorulanlar

**Çalınırsa okunur mu?**  
Hayır. Anahtar uçlardadır, çalınan yığın anlamsızdır.

**Her uygulamada var mı?**  
Hayır. Ayarlardan denetlenir, varsayım yapılmaz.

**Yedekleme nasıl olur?**  
Şifreli yedek ve kurtarma kodu gerekir. Kodsuz geri dönüş yoktur.

**Kurumsal uygun mu?**  
Kayıt ve denetim ihtiyacıyla dengelenir. Politika belirlenir.

## İlgili terimler
- [Security Scanner](/dictionary/security-scanner/)
- [Linux Server Security](/dictionary/linux-server-security/)
- [SSO](/dictionary/sso/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/end-to-end-encryption/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
