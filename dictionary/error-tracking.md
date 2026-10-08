# Error Tracking nedir?

*Sözlük · Geliştirme · Son güncelleme: 3 Ekim 2026*

Uygulamalarda meydana gelen çalışma zamanı hatalarını anlık olarak yakalayan, gruplayan ve geliştiricilere bildiren takip süreci.

## Tanım

Error tracking, canlı yayındaki yazılımlarda kullanıcıların karşılaştığı çökmeleri ve beklenmeyen durumları otomatik olarak kayıt altına alan bir izleme yaklaşımıdır. Sistem, hatanın kaynağını, işletim sistemi detaylarını ve hatayı tetikleyen kullanıcı hareketlerini adım adım belgeler. Bu sayede yazılım ekipleri, sorunlar kullanıcılar tarafından bildirilmeden önce müdahale etme şansı bulur.

*Bir binadaki yangın alarmının yalnızca duman algılamakla kalmayıp, itfaiyeye yangının tam oda numarasını ve çıkış nedenini bildirmesine benzer.*

## Nasıl çalışır?

Uygulamanın içine yerleştirilen küçük bir izleme kütüphanesi, yakalanmamış tüm yazılım istisnalarını dinler. Bir aksaklık yaşandığında yığın izi (stack trace) ve çevresel veriler paketlenip analiz sunucusuna gönderilir. Sunucu, birbirine benzeyen hataları tek bir çatı altında toplayarak geliştiricilere e-posta veya anlık mesaj yoluyla bildirim iletir.

## Nerede kullanılır?

Kullanıcı deneyiminin kritik olduğu mobil uygulamalarda, tek sayfalı web projelerinde (SPA) ve arka uçta çalışan mikroservis mimarilerinde aktif şekilde tercih edilir.

## Sık karıştırılanlar

Tüm sistem olaylarını kronolojik olarak depolayan loglama (logging) kavramından farklıdır: Error tracking doğrudan istisnalara odaklanır ve bu sorunları otomatik olarak analiz edip gruplandırır.

## Sıkça sorulanlar

**Hata takip araçları kullanıcıların gizli verilerini kaydeder mi?**

Doğru yapılandırılmış sistemler, şifre veya kredi kartı gibi kişisel verileri sunucuya göndermeden önce otomatik olarak filtreler ve gizler.

**Uygulama aniden kapandığında hata raporu kaybolur mu?**

Hayır, çökme anında toplanan bilgiler cihazın yerel hafızasına yazılır ve uygulama tekrar açıldığında merkeze iletilir.

## İlgili terimler

- [Logging](https://trescout.com/dictionary/logging/)
- [Observability](https://trescout.com/dictionary/observability/)
- [Traces](https://trescout.com/dictionary/traces/)
- [QA](https://trescout.com/dictionary/qa/)
- [Session Replay](https://trescout.com/dictionary/session-replay/)

## İlgili araçlar

- [Sentry](https://trescout.com/discover/sentry/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/error-tracking/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
