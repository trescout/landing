# Durable Objects nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-08-08

İnternet üzerinde sürekli çalışan ve durumunu kaybetmeden veri saklayabilen küçük yazılım birimleridir.

## Tanım
Normalde internetteki programlar geçicidir, ancak bu yapılar veriyi kendi içinde tutarak kesintisiz çalışır. Bir kullanıcı etkileşimi bittiğinde bile veriyi unutmazlar. Dağıtık sistemlerde tutarlılığı korumak için idealdir.

## Bir benzetmeyle
Sadece gerektiğinde uyanan bir uygulama yerine, her zaman tetikte bekleyen ve not defterini hiç bırakmayan bir sekreter gibidir.

## Nasıl çalışır?
Sunucu üzerinde belirli bir kimlik ile yaşarlar ve gelen her isteği kendi hafızalarındaki güncel durumla işlerler.

## Nerede kullanılır?
Gerçek zamanlı oyunlarda, sohbet uygulamalarında ve durumu korunması gereken web servislerinde kullanılır.

## Sık karıştırılanlar
Geçici sunucu fonksiyonları (serverless) ile karıştırılmamalıdır; çünkü onlar her seferinde sıfırdan başlar.

## Sıkça sorulanlar

**Veri nerede saklanır?**  
Bu birimin kendi içinde, yani doğrudan çalışma ortamının bir parçası olarak saklanır.

## İlgili terimler
- [Runtime](/dictionary/runtime/)
- [State Management](/dictionary/state-management/)
- [Distributed](/dictionary/distributed/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/durable-objects/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
