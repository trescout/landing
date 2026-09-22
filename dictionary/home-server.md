# Home Server nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

Home server (Türkçe karşılığıyla **ev sunucusu**), evde sürekli çalışan kişisel sunucudur.

## Tanım ve Kelime Kökeni
"Home" **ev** demektir. Kendi bulutunuz kurulur, dosya yedeklenir, medya yönetilir. Abonelikten kurtulma ve tam kontrol motivasyonu taşır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Medya:** Film ve müzik arşivi.
- **Yedek:** Aile fotoğrafları.
- **Otomasyon:** Ev cihazları.

## Teknik Derinlik ve Mimari
Kurulum:
- **Donanım:** Eski PC, mini cihaz veya NAS.
- **Sistem:** Hafif Linux dağıtımı.
- **Servis:** Konteynerle yönetim.
- **Erişim:** Güvenli tünel.

Çalışanlar:

```
docker ps --format "table {{.Names}}\t{{.Status}}"
```

Kural: Yedek ev dışında da tutulur. Tek kopya yedek sayılmaz.

## Sık Karıştırılanlar
Masaüstü sanılır. O ara ara açılır, bu 7/24 hizmet verir. Biri çalışma masası, diğeri nöbetçidir.

## Farklı Disiplinlerde Kullanımı
- **Görevli:** Düzeni tutan yardımcı.
- **Arşiv:** Evrak odası.
- **Kiler:** Stok deposu.

## Bir benzetmeyle
Dijital eşyaları düzenleyip sunan ev kütüphanecisi gibidir.

## Sıkça sorulanlar

**Neden sunucu gerekir?**  
Kontrol ve abonelikten kurtulma için. Veri evde kalır.

**Elektrik harcar mı?**  
Küçük cihaz az harcar. Ölçümle takip edilir.

**İnternet gerekli mi?**  
Ev içi hayır, dış erişimde evet. Tünel güvenli kurulur.

**Güvenli mi?**  
Güncelleme ve parola disipliniyle evet. Dışa açık port denetlenir.

## İlgili terimler
- [Self-hosting](/dictionary/self-hosting/)
- [NAS](/dictionary/nas/)
- [Personal Cloud](/dictionary/personal-cloud/)
- [Backup Program](/dictionary/backup-program/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/home-server/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
