# RBAC nedir?

> Role-Based Access Control

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-07-02

Kullanıcılara sistem içindeki görevlerine göre yetki verme ve erişim sınırlandırma yöntemidir.

## Tanım
RBAC, bir sistemde kimin neyi yapabileceğini belirleyen bir kural setidir. Örneğin, bir 'yönetici' sistemin her yerine erişebilirken, bir 'okuyucu' sadece içerikleri görebilir. Bu yöntem, güvenlik hatalarını azaltır ve karmaşık sistemlerde kimin neye yetkisi olduğunu takip etmeyi kolaylaştırır.

## Bir benzetmeyle
Bir oteldeki oda kartları gibidir; herkes sadece kendi odasına ve ortak alanlara girebilir, ancak başka bir misafirin odasına giremez.

## Nasıl çalışır?
Sistem yöneticisi önce rolleri tanımlar (yönetici, editör, kullanıcı gibi). Ardından her role belirli izinler atanır. En son, kullanıcılar bu rollere dahil edilerek otomatik olarak yetkileri belirlenir.

## Nerede kullanılır?
Kurumsal yazılımlarda, bulut sistemlerinde ve veri tabanı yönetiminde kullanılır.

## Sık karıştırılanlar
SSO (Single Sign-On) ile karıştırılabilir; SSO giriş yapma yöntemidir, RBAC ise giriş yaptıktan sonraki yetkilerinizdir.

## Sıkça sorulanlar

**Neden RBAC kullanmalıyım?**  
Güvenliği artırır ve kullanıcı yönetimi karmaşasını ortadan kaldırır.

**Rolleri sonradan değiştirebilir miyim?**  
Evet, sistem yöneticisi merkezi bir noktadan izinleri güncelleyebilir.

## İlgili terimler
- [SSO](/dictionary/sso/)
- [Security Scanner](/dictionary/security-scanner/)
- [API Gateway](/dictionary/api-gateway/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/rbac/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
