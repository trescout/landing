# Hooks nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-06

Yazılımın çalışma sürecinde belirli anlarda devreye girip özel işlemler yapmanıza olanak tanıyan bağlantı noktalarıdır.

## Tanım
Bir yazılım çalışırken, geliştiricilerin kendi kodlarını ana akışın içine enjekte edebilmesi için bıraktığı özel kapılardır. Bu sayede ana programı değiştirmeden, belirli bir olay gerçekleştiğinde kendi komutlarınızın çalışmasını sağlayabilirsiniz. Örneğin bir dosya kaydedildiğinde otomatik olarak yedek almasını söylemek için bir kanca kullanabilirsiniz.

## Bir benzetmeyle
Bir binanın güvenlik sistemine eklenen gizli bir geçit gibidir; ana kapıdan girmek yerine, belirli bir alarm çaldığında devreye girecek özel bir mekanizma kurarsınız.

## Nasıl çalışır?
Yazılım geliştiricileri, ana kodun içine 'buraya geldiğinde şu fonksiyonu çalıştır' şeklinde işaretler koyar. Siz de bu işaretlere kendi kodunuzu bağlayarak süreci kişiselleştirirsiniz. Bu yöntem sayesinde ana yazılım güncellense bile sizin eklediğiniz özellikler çalışmaya devam eder.

## Nerede kullanılır?
Web sitelerinin arka planında, uygulama geliştirme çatılarında ve eklenti sistemlerinde sıkça karşınıza çıkar.

## Sık karıştırılanlar
Eklentiler (plugins) ile karıştırılabilir; kancalar daha çok kod düzeyinde bir bağlantı noktasıyken, eklentiler daha geniş kapsamlı özellikler sunar.

## Sıkça sorulanlar

**Neden doğrudan ana kodu değiştirmiyoruz?**  
Ana kodu değiştirmek, yazılım güncellendiğinde tüm değişikliklerinizin silinmesine neden olur; kancalar ise güncellemelerden etkilenmez.

## İlgili terimler
- [Plugin](/dictionary/plugin/)
- [Framework](/dictionary/framework/)
- [API](/dictionary/api/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/hooks/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
