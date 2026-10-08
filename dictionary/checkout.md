# Checkout nedir, ne demek?

*Sözlük · Geliştirme · Son güncelleme: 19 Eylül 2026*

**Checkout**, bağlama göre iki temel anlama sahip kritik bir terimdir: E-ticaret ve SaaS ekosisteminde müşterinin siparişini tamamladığı **ödeme akışı**; yazılım geliştirmede ise Git versiyon kontrolünde dal veya sürüm değiştirme komutudur (`git checkout`).

*Süpermarkette sepetinizi doldurduktan sonra kasaya gidip ödemenizi yaparak fişinizi aldığınız o son nokta e-ticaret checkout'udur. Bir kütüphanede farklı bir kitabın sayfalarını incelemek için çalışma masanızı değiştirmek ise Git checkout'udur.*

## 1. E-Ticaret ve Dijital Ürünlerde Checkout Mimarisi

E-ticaret ve dijital abonelik platformlarında (SaaS) checkout, kullanıcı yolculuğunun dönüşüme (conversion) dönüştüğü en kritik temas noktasıdır.

### Aşamalar ve Çalışma Mekanizması

Tipik bir modern ödeme akışı şu katmanlardan oluşur:

- **Sepet Özeti ve Doğrulama:** Ürünlerin stok durumu, vergi oranları, indirim kuponları ve kargo maliyetleri anlık olarak sunucu tarafında doğrulanır.
- **Form ve Güvenlik:** İstemci (tarayıcı/mobil uygulama), kart bilgilerini doğrudan satıcının sunucusuna göndermez. Bunun yerine Stripe, Iyzico veya Adyen gibi PCI-DSS uyumlu ödeme altyapılarının sağladığı güvenli iframe veya SDK'lar üzerinden **kart tokenizasyonu** (tokenization) gerçekleştirilir.
- **3D Secure ve Kimlik Doğrulama:** 3DS2 protokolüyle kullanıcının bankasıyla arka planda risk analizi yapılır ve gerekirse tek kullanımlık SMS/mobil onay şifresi istenir.
- **Idempotency (Çift Çekim Koruması):** Ağ kesintileri veya kullanıcının "Öde" butonuna art arda basması durumunda aynı siparişin mükerrer çekilmesini önlemek için benzersiz bir *Idempotency-Key* başlığı kullanılır.
- **Webhooks ve Sipariş Kesinleştirme:** Bankadan gelen başarılı işlem yanıtı sonrasında asenkron webhook çağrılarıyla sipariş durumu güncellenir, fatura kesilir ve envanter düşülür.

### Sepet Terk Oranı (Cart Abandonment) ve Optimizasyon

E-ticaret istatistiklerine göre kullanıcıların %70'e yakını ödeme aşamasında sepeti terk eder. Bu kaybı azaltmak için uygulanan en iyi pratikler:

- **Tek Sayfa Checkout (One-Step Checkout):** Tüm adımların gereksiz yönlendirmeler olmadan tek bir ekranda toplanması.
- **Misafir Alışverişi (Guest Checkout):** Kullanıcıyı zorunlu hesap oluşturma bariyerine takmadan hızlı sipariş imkanı.
- **Dijital Cüzdanlar:** Apple Pay, Google Pay gibi tek tıkla biyometrik doğrulama sunan ödeme yöntemlerinin entegre edilmesi.

## 2. Git Sürüm Kontrolünde Checkout (git checkout)

Yazılım geliştiriciler için `checkout`, Git'in en çok kullanılan fakat zaman içinde fazla sorumluluk yüklendiği için modern Git sürümlerinde özelleştirilmiş alternatifleri geliştirilmiş bir komutudur.

### Temel İşlevleri ve Kullanımı

- **Dallar Arasında Geçiş:**

```
git checkout feature/login
```

`HEAD` işaretçisini hedef dala taşır ve çalışma dizinindeki dosyaları o dalın son haline günceller.

- **Yeni Dal Oluşturup Geçiş Yapma:**

```
git checkout -b feature/odeme-entegrasyonu
```

- **Tek Bir Dosyayı Geri Alma (Discard Changes):**

```
git checkout -- dosya.txt
```

Henüz commit'lenmemiş yerel değişiklikleri silerek dosyayı son commit durumuna döndürür.

- **Geçmiş Bir Commit'e Geçme (Detached HEAD Durumu):** Belirli bir commit ID'sine dönüldüğünde Git `detached HEAD` (ayrık baş) durumuna geçer. Bu durumda yapılan yeni commit'ler hiçbir dala bağlı olmaz ve dal oluşturulmazsa çöp toplayıcı tarafından silinebilir.

### Modern Alternatifler: git switch ve git restore

Git 2.23 sürümünden itibaren `git checkout` komutunun kafa karıştıran çoklu görevleri iki amaca yönelik komuta ayrılmıştır:

- **`git switch`:** Yalnızca dal değiştirme ve yeni dal açma işlemlerine odaklanır (`git switch main`, `git switch -c yeni-dal`).
- **`git restore`:** Dosyaları eski haline getirme ve staging area'dan çıkarma işlemlerini yürütür (`git restore dosya.txt`, `git restore --staged dosya.txt`).

## E-Ticaret vs Git: Karşılaştırmalı Kavram Tablosu

| Boyut | E-Ticaret / SaaS Checkout | Git Sürüm Kontrolü (git checkout) |
|---|---|---|
| **Kapsam** | Alışveriş & Ödeme İşlemleri | Kod Tabanı & Versiyon Takibi |
| **Hedef Kitle** | Son kullanıcılar, müşteriler | Yazılım mühendisleri, DevOps ekipleri |
| **Kritik Süreç** | Tokenizasyon, 3D Secure, Webhook | Dal değiştirme, HEAD taşıma, dosya kurtarma |
| **En Büyük Risk** | Sepet terk etme, mükerrer çekim | Kaydedilmemiş çalışma dizini değişikliklerini kaybetme |
| **Modern Yaklaşım** | Apple/Google Pay, Headless Checkout | `git switch` ve `git restore` kullanımı |

## Sıkça sorulanlar

**Checkout kelimesinin genel anlamı nedir?**

İngilizce "check out" kökeninden gelen terim, otelden çıkış yapma veya süpermarkette alışverişi ödeyip ayrılma eylemlerini tanımlar. Dijital dünyada ise e-ticaretteki "satın alma kasası" ile Git'teki "projenin belirli bir sürümünü incelemek üzere çekip alma" anlamlarında terimleşmiştir.

**E-ticarette checkout adımı nasıl optimize edilir?**

Form alanlarını asgariye indirmek, misafir alışverişi (guest checkout) sunmak, gizli masrafları önceden net göstermek, sayfa yükleme hızını optimize etmek ve Apple Pay/Google Pay gibi hızlı ödeme seçenekleri sağlamak dönüşüm oranlarını artırır.

**git checkout yaparken "error: Your local changes would be overwritten" hatası nasıl çözülür?**

Bu hata, hedef dal ile yerelinizdeki değiştirilmiş dosyaların çakıştığını belirtir. Çözüm için değişikliklerinizi git stash ile geçici olarak saklayabilir, commit'leyebilir (git commit) ya da değişikliklerden vazgeçmek istiyorsanız git restore . ile sıfırlayabilirsiniz.

**git checkout yerine neden git switch kullanılması önerilir?**

git checkout hem dal değiştirmek hem de dosya içeriklerini sıfırlamak için kullanıldığından yanlışlıkla veri kaybına yol açabiliyordu. Git geliştiricileri bu kafa karışıklığını önlemek için dal geçişlerini git switch komutuna tahsis etmiştir.

**Headless Checkout nedir?**

Geleneksel e-ticaret platformlarının monolitik yapısından ayrılarak, ödeme deneyiminin API'ler aracılığıyla tamamen özelleştirilmiş arayüzlerde (mobil uygulama, IoT cihazı veya özel web arayüzü) sunulmasıdır.

## İlgili terimler

- [API](https://trescout.com/dictionary/api/)
- [SaaS](https://trescout.com/dictionary/saas/)
- [CRM](https://trescout.com/dictionary/crm/)
- [Git Push](https://trescout.com/dictionary/git-push/)

## İlgili araçlar

- [Checkout](https://trescout.com/discover/checkout/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/checkout/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
