# Monorepo nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

Monorepo (**mono repository**, tek depo), çok projeyi tek depoda tutma düzenidir.

## Tanım ve Kelime Kökeni
"Mono" **tek** demektir. Bağlı kodlar merkezde toplanır, paylaşım ve güncelleme hızlanır. Kütüphane değişimi anında projelere yansır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Şirket:** Çok takımlı kod tabanı.
- **Mikro hizmet:** Ortak kütüphaneler.
- **Mobil:** Paylaşılan modüller.

## Teknik Derinlik ve Mimari
Düzen:

```
depo/
├── uygulamalar/web
├── uygulamalar/api
└── kutuphaneler/ortak
```

Araçlar: Bazel, Nx ve Turborepo. Bedeli: Depo büyür, derleme zekası gerekir. Atomik değişiklik kazancı bedeli karşılar.

## Sık Karıştırılanlar
Karışıklık sanılır. Oysa düzenli merkeziyettir. Dağınıklık disiplinsizliktendir, düzenden değil.

## Farklı Disiplinlerde Kullanımı
- **Bina:** Kategorili tek kütüphane.
- **AVM:** Ortak çatılı mağazalar.
- **Kampüs:** Ortak alanlı binalar.

## Bir benzetmeyle
Kitapları binalara dağıtmak yerine tek dev binada kategorili tutmaya benzer.

## Sıkça sorulanlar

**Herkese uygun mu?**  
Hayır. Dev projede yönetim zorlaşır, küçükte fazla gelir.

**Güvenli mi?**  
Yetkiyle evet. Tek merkez denetimi kolaylaştırır.

**Ne zaman seçilir?**  
Paylaşım yoğunsa. Bağımsız işte ayrı depo yeterlidir.

**Hangi araçlar?**  
Bazel, Nx ve Turborepo yaygındır. Ekosistem belirler.

## İlgili terimler
- [Repository Checkout](/dictionary/repository-checkout/)
- [Git Push](/dictionary/git-push/)
- [Code Review](/dictionary/code-review/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/monorepo/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
