# Stacked Pull Requests nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-08-02

Büyük yazılım değişikliklerini, birbirine bağlı küçük ve yönetilebilir parçalar halinde sırayla sisteme ekleme yöntemidir.

## Tanım
Yazılım geliştirirken devasa bir değişikliği tek seferde göndermek yerine, bu değişikliği mantıksal parçalara bölüp birbiri ardına dizerek gönderirsiniz. Her parça bir öncekinin üzerine inşa edilir. Bu sayede kodunuzu inceleyen kişiler karmaşık bir yapıyı tek seferde anlamaya çalışmak yerine, küçük ve odaklanmış adımları daha hızlı onaylayabilir.

## Bir benzetmeyle
Bir kitabı tek seferde yazıp editöre göndermek yerine, her bölümü bittikçe editöre gönderip onay alarak ilerlemek gibidir. Böylece hata yaparsanız tüm kitabı değil, sadece o bölümü düzeltmeniz yeterli olur.

## Nasıl çalışır?
Değişikliklerinizi mantıklı bloklara bölün. İlk bloğu gönderin ve o onaylanmadan bir sonrakini onun üzerine oluşturmaya başlayın. Bu süreç, kodun daha temiz kalmasını ve hataların daha erken fark edilmesini sağlar.

## Nerede kullanılır?
GitHub veya GitLab gibi platformlarda, özellikle büyük özellikler geliştirirken ekip içi kod inceleme süreçlerinde kullanılır.

## Sık karıştırılanlar
Tek bir büyük 'Pull Request' ile karıştırılabilir; ancak bu yöntem parçalı ve sıralı bir yaklaşım sunar.

## Sıkça sorulanlar

**Neden tek seferde göndermiyoruz?**  
Büyük değişiklikler hata yapmaya daha açıktır ve başkalarının kodu incelemesini zorlaştırır.

**Her şey birbirine bağlıysa bir parça bozulursa ne olur?**  
Sıralı olduğu için zincirin kopmaması adına değişikliklerinizi dikkatli yönetmeniz gerekir.

## İlgili terimler
- [Code Review](/dictionary/code-review/)
- [Git Push](/dictionary/git-push/)
- [Checkout](/dictionary/checkout/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/stacked-pull-requests/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
