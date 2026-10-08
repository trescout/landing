# Durable Objects nedir, ne demek?

*Sözlük · Geliştirme · Son güncelleme: 22 Eylül 2026*

Durable objects (Türkçe karşılığıyla **kalıcı nesneler**), durumunu koruyan küçük bulut birimleridir.

## Tanım ve Kelime Kökeni

"Durable" **kalıcı** demektir. Geçici işlevlerin tersine veri birimde yaşar, istek bitince unutulmaz. Tutarlılık gereken dağıtık işlerin ilacıdır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?

**Oyun:** Oda durumu takibi.
**Sohbet:** Bağlantı oturumu.
**Servis:** Sayaç ve kilit.

## Teknik Derinlik ve Mimari

Düzen:

**Kimlik:** Her birimin adı vardır.
**Tek yazıcı:** Aynı anda tek el yazar.
**WebSocket:** Sürekli bağlantı.

Akış:

```
istek → oda-nesnesi → durum güncellenir → yanıt
```

Serverless farkı: İşlev sıfırdan başlar, nesne kaldığı yerden devam eder.

## Sık Karıştırılanlar

Serverless sanılır. İşlev geçicidir, nesne kalıcıdır. Biri günübirlikçi, diğeri kiracıdır.

## Farklı Disiplinlerde Kullanımı

**Sekreter:** Defteri bırakmayan yardımcı.
**Kasa defteri:** Gün sonu bakiyesi.
**Emanet:** Sahibini bekleyen dolap.

*Not defterini hiç bırakmayan tetikte sekreter gibidir.*

## Sıkça Sorulanlar

**Veri nerede saklanır?**

Birimin içinde, çalışma ortamının parçası olarak tutulur.

**Ne zaman kullanılır?**

Durum gerektiren gerçek zamanlı işte: Oda, sayaç ve kilit.

**Maliyeti nedir?**

Sürekli yaşadığı için boşta da yazar. Trafik desenine göre hesaplanır.

**Serverless farkı nedir?**

İşlev unutur, nesne hatırlar. Durum varsa nesne seçilir.

## İlgili terimler

- [Runtime](https://trescout.com/dictionary/runtime/)
- [State Management](https://trescout.com/dictionary/state-management/)
- [Distributed](https://trescout.com/dictionary/distributed/)

## İlgili araçlar

- [Celld](https://trescout.com/discover/celld/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/durable-objects/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
