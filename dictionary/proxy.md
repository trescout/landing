# Proxy nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

Proxy (Türkçe karşılığıyla **vekil sunucu**), isteklerinizi sizin adınıza hedefe ileten aracıdır.

## Tanım ve Kelime Kökeni
"Proxy" **vekil** demektir. Bilgisayarınızla internet arasında bekçi gibi durur: Siteye doğrudan değil, vekil üzerinden bağlanırsınız. Kimlik gizleme ve trafik yönetiminde kullanılır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Şirket:** Çıkış trafiğinin denetimi.
- **Gizlilik:** Adres gizleme.
- **Erişim:** Bölgesel kısıt aşımı.

## Teknik Derinlik ve Mimari
İki yön vardır:
- **Forward:** İstemciyi gizler, dışarı çıkar.
- **Reverse:** Sunucuyu korur, içeri alır. Nginx bu işi yapar.

Türler: HTTP, HTTPS ve SOCKS. Ortam değişkeni örneği:

```
export https_proxy="http://vekil:8080"
```

Önbellek de tutar: Sık istenen içerik vekilden verilir, hat rahatlar.

## Sık Karıştırılanlar
VPN sanılır. VPN tüm cihazı tünele sokar, proxy genellikle uygulama veya tarayıcı düzeyinde çalışır. Gizlilik derinliği farklıdır.

## Farklı Disiplinlerde Kullanımı
- **Arkadaş:** Mesajı sizin adınıza ileten kişi.
- **Resepsiyon:** Ziyaretçiyi karşılayan görevli.
- **Tercüman:** Sözü aktaran aracı.

## Bir benzetmeyle
Mesajı doğrudan değil, arkadaşınız üzerinden iletmeniz gibidir; alıcı sizi değil aracıyı görür.

## Sıkça sorulanlar

**Güvenli mi?**  
Vekile bağlıdır. Güvenilmez sunucu trafiği izleyebilir, bu yüzden bilinen sağlayıcı seçilir.

**Neden kullanılır?**  
Denetim, gizlilik ve erişim için. Üçü de ayrı ihtiyaçtır.

**Reverse nedir?**  
Dışarıdan geleni sunucuya dağıtan yöndür. Yük dengeleme ve koruma sağlar.

**Hızlandırır mı?**  
Önbellekli içerikte evet, şifreli ve uzak trafikte genellikle yavaşlatır.

## İlgili terimler
- [Self-Hosting](/dictionary/self-hosting/)
- [Offline](/dictionary/offline/)
- [VPN](/dictionary/vpn/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/proxy/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
