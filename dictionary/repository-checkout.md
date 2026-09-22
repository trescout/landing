# Repository Checkout nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

Repository checkout, deponun belirli bir sürümünü çalışma alanınıza indirme işlemidir.

## Tanım ve Kelime Kökeni
Projenin o anki halini sunucudan alıp masanıza getirirsiniz. Kütüphaneden kitap ödünç almaya benzer: Kaynak yerinde durur, siz kopyayla çalışırsınız. Geçmiş ve sürüm bilgisi kopyayla birlikte gelir.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Yeni proje:** Depoyu ilk kez indirme.
- **Sürüm geçişi:** Eski etikete dönüp hatayı inceleme.
- **Dal deneme:** Arkadaşın dalını yerelde açma.

## Teknik Derinlik ve Mimari
Akış şöyledir:

```
git clone https://github.com/ornek/proje.git
cd proje
git checkout v2.0.0
```

Ayrımlar:
- **Clone:** Deponun tamamını ilk kez indirme.
- **Checkout:** İndirilmiş depoda sürüm veya dal değiştirme.
- **Switch/Restore:** Modern Git içinde dal geçme ve dosya geri alma komutları.
- **Sparse:** Devasa depoda yalnızca gerekli klasörü indirme.

Kural: Kayıtlı işiniz varken geçmeyin, önce commit yapın veya saklayın.

## Farklı Disiplinlerde Kullanımı
- **Kütüphane:** Kitabı raftan alıp masaya getirme.
- **Arşiv:** Klasörü depodan çıkarıp inceleme.
- **Fotoğraf:** Negatiften baskı alma.

## Bir benzetmeyle
Kütüphanedeki kitabı ödünç alıp masanıza getirerek sayfaları tek tek okumaya başlamak gibidir.

## Sıkça sorulanlar

**Sadece dosyaları mı indirir?**  
Hayır. Geçmiş ve sürüm bilgisi de gelir, bu yüzden eski hale dönebilirsiniz.

**Clone ile farkı nedir?**  
Clone ilk indirmedir, checkout indirilmiş depoda geçiştir. Sıralama bu yöndedir.

**Eski sürüme nasıl dönülür?**  
Etiket veya commit karmasıyla geçilir. Kayıtlı iş varsa önce saklanır.

**Switch nedir?**  
Dal geçmenin modern komutudur. Checkout çok iş yaptığı için Git ikiye böldü: switch dala, restore dosyaya.

## İlgili terimler
- [Git Push](/dictionary/git-push/)
- [Tech Stack](/dictionary/tech-stack/)
- [Cloning](/dictionary/cloning/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/repository-checkout/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
