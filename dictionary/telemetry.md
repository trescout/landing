# Telemetry nedir, ne demek?

*Sözlük · Geliştirme · Son güncelleme: 22 Eylül 2026*

Telemetry (Türkçe karşılığıyla **uzaktan ölçüm**), yazılım ve cihazların durum bilgisini otomatik toplayıp merkeze iletmesidir.

## Tanım ve Kelime Kökeni

Sözcük, Yunanca **tele** (uzak) ve **metron** (ölçü) köklerinden gelir. Uygulamalar, yazılımın nasıl çalıştığına dair raporları geliştiriciye gönderir: Hangi özellik çok kullanılıyor, uygulama nerede çöküyor. Kullanıcı için genellikle arka planda sessizce akan bir veri akışıdır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?

**Hata ayıklama:** Çökme raporlarının otomatik toplanması.
**Ürün kararı:** Az kullanılan düğmenin sadeleştirilmesi.
**Performans:** Açılış süresinin sürüm sürüm izlenmesi.

## Teknik Derinlik ve Mimari

Gözlemlenebilirliğin üç sütunu:

**Log:** Olay satırları ("ödeme başladı", "ödeme bitti").
**Metrik:** Sayısal ölçüler (istek sayısı, gecikme ortalaması).
**Trace:** İsteğin servisler arası yolculuğunun kaydı.

Toplama için **OpenTelemetry** gibi açık standartlar kullanılır. İki kurala dikkat edilir: Yüksek trafikte her isteği değil örneğini (sampling) göndermek ve kişisel veriyi (e-posta, konum) kayda almamak. Hangi verinin gittiğini uygulamanın ayarlar bölümünden görebilir ve kapatabilirsiniz.

## Sık Karıştırılanlar

Logging ile karıştırılabilir. Log, tekil olay satırıdır. Metrik sayısal özettir. Trace, isteğin yolculuğudur. Telemetry ise bu üçünü toplama ve iletme işinin adıdır.

## Farklı Disiplinlerde Kullanımı

**Hastane:** Hasta monitörünün nabzı hemşire ekranına taşıması.
**Havacılık:** Uçuş verilerinin kara kutuda saklanması.
**Enerji:** Sayaçların tüketimi merkeze bildirmesi.

*Bir arabanın içindeki sensörlerin, motorun sıcaklığını ve yakıt durumunu sürekli olarak sürücü paneline bildirmesi gibidir.*

## Sıkça Sorulanlar

**Gizliliğimi etkiler mi?**

Genellikle anonim ve toplu veri toplanır. Hangi verilerin gönderildiğini uygulamanın ayarlar bölümünden görebilir, kapatabilirsiniz.

**Observability ile farkı nedir?**

Telemetry veriyi toplar ve iletir. Observability, toplanan veriyle sistemin içini anlama yeteneğidir. Biri araç, diğeri amaçtır.

**Kapatılabilir mi?**

Çoğu uygulamada evet, ayarlardan kapatılır. Kurumsal cihazlarda politika gereği açık kalabilir.

**Maliyeti var mıdır?**

Evet. Veri taşıma ve saklama bedeli vardır. Bu yüzden yüksek trafikte örnekleme yapılır, her olay değil bir kısmı gönderilir.

## İlgili terimler

- [Logs](https://trescout.com/dictionary/logs/)
- [Observability](https://trescout.com/dictionary/observability/)
- [Traces](https://trescout.com/dictionary/traces/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/telemetry/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
