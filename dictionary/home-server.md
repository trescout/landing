# Home Server nedir, ne demek?

*Sözlük · Geliştirme · Son güncelleme: 22 Eylül 2026*

Home server (Türkçe karşılığıyla **ev sunucusu**), evde sürekli çalışan kişisel sunucudur.

## Tanım ve Kelime Kökeni

"Home" **ev** demektir. Kendi bulutunuz kurulur, dosya yedeklenir, medya yönetilir. Abonelikten kurtulma ve tam kontrol motivasyonu taşır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?

**Medya:** Film ve müzik arşivi.
**Yedek:** Aile fotoğrafları.
**Otomasyon:** Ev cihazları.

## Teknik Derinlik ve Mimari

Kurulum:

**Donanım:** Eski PC, mini cihaz veya NAS.
**Sistem:** Hafif Linux dağıtımı.
**Servis:** Konteynerle yönetim.
**Erişim:** Güvenli tünel.

Çalışanlar:

```
docker ps --format "table {{.Names}}	{{.Status}}"
```

Kural: Yedek ev dışında da tutulur. Tek kopya yedek sayılmaz.

## Sık Karıştırılanlar

Masaüstü sanılır. O ara ara açılır, bu 7/24 hizmet verir. Biri çalışma masası, diğeri nöbetçidir.

## Farklı Disiplinlerde Kullanımı

**Görevli:** Düzeni tutan yardımcı.
**Arşiv:** Evrak odası.
**Kiler:** Stok deposu.

*Dijital eşyaları düzenleyip sunan ev kütüphanecisi gibidir.*

## Sıkça Sorulanlar

**Neden sunucu gerekir?**

Kontrol ve abonelikten kurtulma için. Veri evde kalır.

**Elektrik harcar mı?**

Küçük cihaz az harcar. Ölçümle takip edilir.

**İnternet gerekli mi?**

Ev içi hayır, dış erişimde evet. Tünel güvenli kurulur.

**Güvenli mi?**

Güncelleme ve parola disipliniyle evet. Dışa açık port denetlenir.

## İlgili terimler

- [Self-hosting](https://trescout.com/dictionary/self-hosting/)
- [NAS](https://trescout.com/dictionary/nas/)
- [Personal Cloud](https://trescout.com/dictionary/personal-cloud/)
- [Backup Program](https://trescout.com/dictionary/backup-program/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/home-server/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
