# Proxy nedir, ne demek?

*Sözlük · Geliştirme · Son güncelleme: 22 Eylül 2026*

Proxy (Türkçe karşılığıyla **vekil sunucu**), isteklerinizi sizin adınıza hedefe ileten aracıdır.

## Tanım ve Kelime Kökeni

"Proxy" **vekil** demektir. Bilgisayarınızla internet arasında bekçi gibi durur: Siteye doğrudan değil, vekil üzerinden bağlanırsınız. Kimlik gizleme ve trafik yönetiminde kullanılır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?

**Şirket:** Çıkış trafiğinin denetimi.
**Gizlilik:** Adres gizleme.
**Erişim:** Bölgesel kısıt aşımı.

## Teknik Derinlik ve Mimari

İki yön vardır:

**Forward:** İstemciyi gizler, dışarı çıkar.
**Reverse:** Sunucuyu korur, içeri alır. Nginx bu işi yapar.

Türler: HTTP, HTTPS ve SOCKS. Ortam değişkeni örneği:

```
export https_proxy="http://vekil:8080"
```

Önbellek de tutar: Sık istenen içerik vekilden verilir, hat rahatlar.

## Sık Karıştırılanlar

VPN sanılır. VPN tüm cihazı tünele sokar, proxy genellikle uygulama veya tarayıcı düzeyinde çalışır. Gizlilik derinliği farklıdır.

## Farklı Disiplinlerde Kullanımı

**Arkadaş:** Mesajı sizin adınıza ileten kişi.
**Resepsiyon:** Ziyaretçiyi karşılayan görevli.
**Tercüman:** Sözü aktaran aracı.

*Mesajı doğrudan değil, arkadaşınız üzerinden iletmeniz gibidir; alıcı sizi değil aracıyı görür.*

## Sıkça Sorulanlar

**Güvenli mi?**

Vekile bağlıdır. Güvenilmez sunucu trafiği izleyebilir, bu yüzden bilinen sağlayıcı seçilir.

**Neden kullanılır?**

Denetim, gizlilik ve erişim için. Üçü de ayrı ihtiyaçtır.

**Reverse nedir?**

Dışarıdan geleni sunucuya dağıtan yöndür. Yük dengeleme ve koruma sağlar.

**Hızlandırır mı?**

Önbellekli içerikte evet, şifreli ve uzak trafikte genellikle yavaşlatır.

## İlgili terimler

- [Self-Hosting](https://trescout.com/dictionary/self-hosting/)
- [Offline](https://trescout.com/dictionary/offline/)
- [VPN](https://trescout.com/dictionary/vpn/)

## İlgili araçlar

- [OmniRoute](https://trescout.com/discover/omniroute/)
- [FlClash](https://trescout.com/discover/flclash/)
- [Nginx](https://trescout.com/discover/nginx/)
- [Freellmapi](https://trescout.com/discover/freellmapi/)
- [Headroom](https://trescout.com/discover/headroom/)
- [User Scanner](https://trescout.com/discover/user-scanner/)
- [OpenFlux](https://trescout.com/discover/openflux/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/proxy/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
