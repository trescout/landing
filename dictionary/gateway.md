# Gateway nedir, ne demek?

*Sözlük · Geliştirme · Son güncelleme: 22 Eylül 2026*

Gateway (Türkçe karşılığıyla **ağ geçidi**), farklı ağlar arasında trafiği yöneten bağlantı noktasıdır.

## Tanım ve Kelime Kökeni

"Gate" **kapı**, "way" ise **yol** demektir. İki ağın birbiriyle konuşmasını sağlayan köprüdür: Evinizdeki internet ile dış dünyayı birbirine bağlayan cihaz tipik örnektir. Gelen veriyi inceler, hangi ağa gideceğine karar verir.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?

**Ev modemi:** Evinizi sağlayıcı ağına bağlar.
**Kurumsal giriş:** Ofis trafiğinin denetim noktası.
**Bulut:** Sanal ağların birbirine açılan kapısı.

## Teknik Derinlik ve Mimari

Geçidin işleri:

**Adres çevirisi (NAT):** İç adresleri dışa tek adresten çıkarır.
**Filtreleme:** İstenmeyen trafiği kapıda tutar.
**Yönlendirme:** Paketi doğru ağa verir.

Varsayılan yol bilgisi şöyledir:

```
default via 192.168.1.1 dev eth0
```

Bu satır, tanınmayan hedefin modem üzerinden gönderileceğini söyler. API gateway ise farklı katmandadır: Ağ değil, servis isteklerini yönetir.

## Sık Karıştırılanlar

API Gateway ile karıştırılabilir. API Gateway yazılım servislerini yönetir, ağ geçidi ağ seviyesinde çalışır. Biri uygulama kapısı, diğeri yol kapısıdır.

## Farklı Disiplinlerde Kullanımı

**Sınır kapısı:** Gelenlerin denetlenip yönlendirilmesi.
**Liman:** Gemilerin gümrükten geçişi.
**Resepsiyon:** Ziyaretçinin doğru kata yönlendirilmesi.

*Bir ülkenin sınır kapısı gibidir; gelenleri kontrol eder ve doğru yöne gitmelerini sağlar.*

## Sıkça Sorulanlar

**Gateway olmadan internete girilir mi?**

Hayır. Yerel ağ dış dünyaya bağlanamaz, izole kalır.

**API gateway ile farkı nedir?**

Ağ geçidi paket taşır, API gateway istek yönetir. Biri yol, diğeri uygulama katmanıdır.

**Evde hangisi kullanılır?**

Modeminizin içindeki geçit iş görür. Ek ayar gerekmez, adres otomatik dağıtılır.

**İki ağ ayrı tutulabilir mi?**

Evet. Güvenlik duvarı kurallarıyla geçiş kapatılır, ağlar izole çalışır.

## İlgili terimler

- [API Gateway](https://trescout.com/dictionary/api-gateway/)
- [Network Stack](https://trescout.com/dictionary/network-stack/)
- [Proxy](https://trescout.com/dictionary/proxy/)

## İlgili araçlar

- [OmniRoute](https://trescout.com/discover/omniroute/)
- [Fanqiang](https://trescout.com/discover/fanqiang/)
- [Gitdiagram](https://trescout.com/discover/gitdiagram/)
- [OpenWA](https://trescout.com/discover/openwa/)
- [Grok2api](https://trescout.com/discover/grok2api/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/gateway/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
