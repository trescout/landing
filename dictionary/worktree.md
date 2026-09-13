# Worktree nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-13

Aynı proje klasörünü değiştirmeden, projenin farklı sürümleri üzerinde aynı anda çalışmanızı sağlayan bir yapıdır.

## Tanım
Worktree, yazılım geliştirirken ana çalışma alanınızı bozmadan projenin farklı dallarını (branch) ayrı klasörlerde açmanıza olanak tanır. Örneğin, ana projede bir özellik geliştirirken, aynı anda başka bir klasörde eski bir hatayı düzeltebilirsiniz. Bu, sürekli dal değiştirmekten kaynaklanan zaman kaybını ve karmaşayı ortadan kaldırır.

## Bir benzetmeyle
Aynı anda iki farklı kitap üzerinde çalışırken, her birini farklı bir masada açık tutmak gibi; birinden diğerine geçmek için sayfaları çevirmekle uğraşmazsınız.

## Nasıl çalışır?
Git gibi sürüm kontrol sistemleri üzerinden yeni bir worktree eklersiniz. Sistem sizin için projenin bir kopyasını farklı bir dizine bağlar ve siz ana dizine dokunmadan orada çalışmaya devam edersiniz.

## Nerede kullanılır?
Karmaşık yazılım projelerinde, uzun süren özellik geliştirmeleri sırasında acil hata düzeltmeleri yapılması gereken durumlarda kullanılır.

## Sık karıştırılanlar
Sadece klasör kopyalamakla aynı değildir; worktree'ler aynı Git deposuna bağlıdır ve birbirleriyle senkronize çalışır.

## Sıkça sorulanlar

**Neden ayrı klasör kopyalamıyoruz?**  
Kopyalamak disk alanını boşa harcar ve Git geçmişini yönetmeyi zorlaştırır; worktree ise çok daha verimlidir.

**Her Git projesinde çalışır mı?**  
Evet, modern Git sürümlerinin tamamında bu özellik desteklenir.

## İlgili terimler
- [Source Control](/dictionary/source-control/)
- [Git Push](/dictionary/git-push/)
- [Repository Checkout](/dictionary/repository-checkout/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/worktree/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
