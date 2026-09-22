# Durable Objects nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

Durable objects (Türkçe karşılığıyla **kalıcı nesneler**), durumunu koruyan küçük bulut birimleridir.

## Tanım ve Kelime Kökeni
"Durable" **kalıcı** demektir. Geçici işlevlerin tersine veri birimde yaşar, istek bitince unutulmaz. Tutarlılık gereken dağıtık işlerin ilacıdır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Oyun:** Oda durumu takibi.
- **Sohbet:** Bağlantı oturumu.
- **Servis:** Sayaç ve kilit.

## Teknik Derinlik ve Mimari
Düzen:
- **Kimlik:** Her birimin adı vardır.
- **Tek yazıcı:** Aynı anda tek el yazar.
- **WebSocket:** Sürekli bağlantı.

Akış:

```
istek → oda-nesnesi → durum güncellenir → yanıt
```

Serverless farkı: İşlev sıfırdan başlar, nesne kaldığı yerden devam eder.

## Sık Karıştırılanlar
Serverless sanılır. İşlev geçicidir, nesne kalıcıdır. Biri günübirlikçi, diğeri kiracıdır.

## Farklı Disiplinlerde Kullanımı
- **Sekreter:** Defteri bırakmayan yardımcı.
- **Kasa defteri:** Gün sonu bakiyesi.
- **Emanet:** Sahibini bekleyen dolap.

## Bir benzetmeyle
Not defterini hiç bırakmayan tetikte sekreter gibidir.

## Sıkça sorulanlar

**Veri nerede saklanır?**  
Birimin içinde, çalışma ortamının parçası olarak tutulur.

**Ne zaman kullanılır?**  
Durum gerektiren gerçek zamanlı işte: Oda, sayaç ve kilit.

**Maliyeti nedir?**  
Sürekli yaşadığı için boşta da yazar. Trafik desenine göre hesaplanır.

**Serverless farkı nedir?**  
İşlev unutur, nesne hatırlar. Durum varsa nesne seçilir.

## İlgili terimler
- [Runtime](/dictionary/runtime/)
- [State Management](/dictionary/state-management/)
- [Distributed](/dictionary/distributed/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/durable-objects/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
