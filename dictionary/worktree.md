# Worktree nedir?

*Sözlük · Geliştirme · Son güncelleme: 13 Eylül 2026*

Aynı proje klasörünü değiştirmeden, projenin farklı sürümleri üzerinde aynı anda çalışmanızı sağlayan bir yapıdır.

## Tanım

Worktree, yazılım geliştirirken ana çalışma alanınızı bozmadan projenin farklı dallarını (branch) ayrı klasörlerde açmanıza olanak tanır. Örneğin, ana projede bir özellik geliştirirken, aynı anda başka bir klasörde eski bir hatayı düzeltebilirsiniz. Bu, sürekli dal değiştirmekten kaynaklanan zaman kaybını ve karmaşayı ortadan kaldırır.

*Aynı anda iki farklı kitap üzerinde çalışırken, her birini farklı bir masada açık tutmak gibi; birinden diğerine geçmek için sayfaları çevirmekle uğraşmazsınız.*

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

- [Source Control](https://trescout.com/dictionary/source-control/)
- [Git Push](https://trescout.com/dictionary/git-push/)
- [Repository Checkout](https://trescout.com/dictionary/repository-checkout/)

## İlgili araçlar

- [Worktrunk](https://trescout.com/discover/worktrunk/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/worktree/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
