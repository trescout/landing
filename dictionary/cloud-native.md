# Cloud Native nedir, ne demek?

*Sözlük · Geliştirme · Son güncelleme: 22 Eylül 2026*

Cloud native (Türkçe karşılığıyla **bulut yerlisi**), uygulamayı bulutun esneklik ve ölçeklenebilirliğinden tam yararlanacak şekilde tasarlama yaklaşımıdır.

## Tanım ve Kelime Kökeni

Kavramı **CNCF** (Cloud Native Computing Foundation) şemsiyesi toplar. Buradaki kritik ayrım şudur: Bir yazılımı buluta yüklemek onu cloud native yapmaz. Cloud native, uygulamanın en baştan bulutun dinamik yapısına göre, küçük ve bağımsız parçalar halinde inşa edilmesidir.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?

**Yoğun günler:** Kampanya günü trafiği katlanınca kapasitenin kendiliğinden artması.
**Arıza anı:** Bir sunucu çökünce işin başka kopyaya sessizce devredilmesi.
**Güncelleme:** Uygulama kapalıyken değil, çalışırken parça parça yenilenmesi.

## Teknik Derinlik ve Mimari

Cloud native yığınının parçaları:

**Konteyner:** Uygulama ve bağımlılıklarının taşınabilir kutusu.
**Orkestrasyon:** Kutuların çalıştırılması, çoğaltılması ve sağlık denetimi (ör. Kubernetes).
**Mikro hizmet:** Büyük uygulamanın bağımsız dağıtılabilen küçük servislere bölünmesi.
**Gözlemlenebilirlik:** Log, metrik ve izleme ile sistemin içinin görünür tutulması.

Ölçek büyütme tek komutla olur:

```
kubectl scale deployment web --replicas=5
```

Bu komut, `web` servisinin kopya sayısını beşe çıkarır. Trafik düşünce sayı geri alınır.

## Farklı Disiplinlerde Kullanımı

**Prefabrik yapı:** İhtiyaca göre oda eklenebilen modüler ev.
**Elektrik şebekesi:** Talebe göre devreye giren santraller.
**Lojistik:** Yoğunluğa göre açılıp kapanan dağıtım hatları.

*Bir evi tek seferde bir yere yerleştirmek değil, her an başka yere taşınabilen ve ihtiyaca göre odaları genişletilebilen modüler bir yapı olarak tasarlamak gibidir.*

## Sıkça Sorulanlar

**Uygulamayı buluta taşımak cloud native yapar mı?**

Hayır. Eski tip uygulamayı aynen taşımak yalnızca yer değiştirir. Cloud native için mimarinin küçük parçalara bölünmesi ve otomatik yönetime uygun olması gerekir.

**Küçük projeye gerekli midir?**

Her zaman değil. Tek sunucuda rahat çalışan bir blog için bu düzenek fazla gelebilir. Trafik dalgalıysa veya ekip büyüyorsa anlam kazanır.

**Maliyeti artırır mı?**

Kurulum ve öğrenme maliyeti vardır. Karşılığında arıza süresi ve ölçekleme maliyeti düşer. Hesabı iş yükünüze göre yapmanız gerekir.

**Nereden başlanmalıdır?**

Uygulamayı konteynere koymakla başlayın. Sonra health check, loglama ve otomatik dağıtım ekleyin. Orkestrasyon en son adımdır.

## İlgili terimler

- [Containers](https://trescout.com/dictionary/containers/)
- [Virtual Machines](https://trescout.com/dictionary/virtual-machines/)
- [Runtime](https://trescout.com/dictionary/runtime/)

## İlgili araçlar

- [Meshery](https://trescout.com/discover/meshery/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/cloud-native/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
