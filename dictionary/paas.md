# PaaS nedir, ne demek?

> Platform as a Service

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

PaaS (**Platform as a Service**, hizmet olarak platform), kodu koşturan hazır ortamın kiralanmasıdır.

## Tanım ve Kelime Kökeni
Sunucu ve güvenlik işiyle uğraşmadan kod yüklenir, platform çalıştırır. Tek tuşla dünyaya açılma vaadi buradan gelir. Heroku, Vercel ve App Engine bilinen örnekleridir.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Web:** Hızlı yayınlanan siteler.
- **API:** Bakımsız arka uçlar.
- **Prototip:** Fikir denemeleri.

## Teknik Derinlik ve Mimari
Platformun sundukları:
- **Derleme:** Kodu alıp koşar hale getirme.
- **Ölçek:** Trafiğe göre kopya açma.
- **Eklenti:** Veritabanı ve kuyruk bağlama.

Yayın örneği:

```
npx vercel --prod
```

Kilitlenme notu: Platforma özel servislere gömülmek taşınmayı zorlaştırır. Kritik parçalar standartta tutulur.

## Sık Karıştırılanlar
IaaS sanılır. IaaS donanım verir, PaaS koşar ortam sunar. Biri arsa, diğeri hazır mutfaktır.

## Farklı Disiplinlerde Kullanımı
- **Mutfak:** Ekipmanlı hazır mutfak.
- **Daire:** Mobilyalı kiralık.
- **Sahne:** Işıklı hazır sahne.

## Bir benzetmeyle
Hazır mutfak kiralamaya benzer; ekipman hazırdır, siz yalnızca yemeği yaparsınız.

## Sıkça sorulanlar

**PaaS şart mı?**  
Hayır. Sunucu işinden kurtulmak isteyene zaman kazandırır, kontrol isteyene dar gelir.

**IaaS farkı nedir?**  
IaaS donanım verir, PaaS ortam sunar. Kontrol ve hız arası tercihtir.

**Kilitlenme olur mu?**  
Özel servislere gömülünce evet. Taşınabilir parçalar standart tutulur.

**Maliyeti nedir?**  
Küçük işte cüzi, büyük trafikte artar. Fatura izlenir, limit konur.

## İlgili terimler
- [SaaS](/dictionary/saas/)
- [IaaS](/dictionary/iaas/)
- [Deployment](/dictionary/deployment/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/paas/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
