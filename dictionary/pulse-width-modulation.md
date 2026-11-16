# Pulse-Width Modulation nedir?

*Geliştirme · Son güncelleme: 16 Kasım 2026*

> Pulse-Width Modulation

Dijital sinyallerin voltaj süresini değiştirerek gücü ve ekran parlaklığını kontrol eden bir sinyal düzenleme yöntemidir.

## Tanım

Pulse-Width Modulation (PWM), bir elektrik sinyalinin açık ve kapalı kalma sürelerini hızla değiştirerek ortalama voltajı ayarlama tekniğidir. Gerilim seviyesini doğrudan düşürmek yerine gücü milisaniyeler içinde açıp kapatarak kontrol sağlarsınız. Ekran parlaklığı ayarlarından motor hız denetimine kadar birçok donanım sisteminde yaygın olarak kullanılır.

*Bir lambanın ışık seviyesini düşürmek için düğmenizi saniyede bin defa açıp kapatmaya benzetebilirsiniz. Düğme ne kadar uzun süre açık kalırsa gözünüz ışığı o kadar parlak algılar.*

## Nasıl çalışır?

Sinyalin yüksek olduğu süre ile toplam periyot oranı olan görev döngüsü değiştirilir. Görev döngüsü %50 olduğunda güç yarı yarıya iletilmiş olur. Bu yüksek hızlı anahtarlama sayesinde enerji kaybı yaşanmadan hassas bir güç yönetimi elde edilir.

## Nerede kullanılır?

OLED ve LCD ekranların parlaklık denetiminde, soğutma fanlarının hız ayarlamalarında ve elektrikli motor kontrolünde sıklıkla tercih edilir.

## Sık karıştırılanlar

Doğrudan analog voltaj ayarı ile karıştırılabilir. PWM gerilim seviyesini kendisini düşürmez, voltajın aktif kalma süresini değiştirerek ortalama gücü yönetir.

## Sorular ve yanıtlar

**PWM ekranlarda neden göz yorulmasına yol açar?**

Düşük yenileme frekansına sahip PWM ekranlar fark edilmeyen hızlı bir kırpışma yaratır. Bu durum bazı kullanıcılarda göz yorgunluğu ve baş ağrısına sebep olabilir.

**PWM sinyali nasıl üretilir?**

Mikrodenetleyiciler ve özel donanım zamanlayıcıları yardımıyla dijital çıkış pinlerinden üretilir.

## İlgili terimler

- [Single-Board Computers](https://trescout.com/dictionary/single-board-computers/)
- [IoT](https://trescout.com/dictionary/iot/)
- [CPU](https://trescout.com/dictionary/cpu/)
- [System Design](https://trescout.com/dictionary/system-design/)

Bu açıklama TreScout için yapay zekâ ile sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/pulse-width-modulation/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
