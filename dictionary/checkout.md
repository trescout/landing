# Checkout nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Checkout, e-ticarette ödeme ve siparişin onaylandığı son aşamayı; sürüm kontrolünde (Git) ise farklı bir çalışma dalına veya commit'e geçme eylemini ifade eder.

## Tanım ve iki temel kullanım alanı
Checkout terimi yazılım ve internet dünyasında iki kritik bağlamda yaygın olarak kullanılır:

1. **E-Ticaret ve SaaS (Ödeme Akışı):** Kullanıcının dijital sepetine eklediği ürün veya aboneliklerin fatura, teslimat ve kredi kartı bilgilerini girerek satın alma işlemini resmiyete kavuşturduğu son adımdır (Stripe, Lemon Squeezy vb.). Güvenli veri akışının (SSL, PCI-DSS) ve minimum sürtünmeli kullanıcı deneyiminin (UX) en kritik olduğu aşamadır.
2. **Sürüm Kontrol Sistemleri (Git Checkout):** Git'te üzerinde çalışılan geçerli dalı (branch) değiştirmek veya geçmişteki belirli bir commit durumuna göz atmak için kullanılan temel komuttur (`git checkout <dal-adı>`).

## Bir benzetmeyle
Süpermarkette sepetinizi doldurduktan sonra kasaya gidip ödemenizi yaparak fişinizi aldığınız o son nokta e-ticaret checkout'udur. Bir kütüphanede farklı bir kitabın sayfalarını incelemek için çalışma masanızı değiştirmek ise Git checkout'udur.

## Nasıl çalışır?
- **E-Ticaret Checkout:** Kullanıcı 'Satın Al' butonuna bastığında sipariş özeti doğrulanır, ödeme sağlayıcısına (gateway) şifreli token iletilir, banka onayı alınır ve webhooks ile sipariş veritabanına işlenir.
- **Git Checkout:** Komut verildiğinde Git, çalışma dizininizdeki (working directory) dosyaları hedef daldaki commit durumuna anında eşitler.

## Nerede kullanılır?
Tüm çevrim içi alışveriş ve SaaS platformlarında, ödeme ağ geçitlerinde ve yazılım geliştiricilerin terminal iş akışlarında kullanılır.

## Sıkça sorulanlar

**Checkout ne demek ve Türkçe karşılığı nedir?**  
İngilizce 'çıkış yapmak / kontrol edip ayrılmak' deyiminden gelir. E-ticarette 'ödeme tamamlama / sipariş onayı'; yazılımda ise 'dala geçiş' olarak ifade edilir.

**Checkout terk etme (Cart Abandonment) oranı nedir ve nasıl düşürülür?**  
Kullanıcıların ödeme sayfasına gelip satın almadan ayrılma oranıdır. Tek tıkla ödeme (Apple Pay, Google Pay), misafir alışveriş seçeneği ve şeffaf kargo/vergi bilgileriyle bu oran düşürülür.

**Git'te git checkout ile git switch arasındaki fark nedir?**  
Modern Git sürümlerinde branch değiştirmek için `git switch`, dosya değişikliklerini geri almak için `git restore` komutları getirilmiştir; ancak `git checkout` her iki işlevi de kapsayan köklü bir komuttur.

## İlgili terimler
- [API](/dictionary/api/)
- [SaaS](/dictionary/saas/)
- [CRM](/dictionary/crm/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/checkout/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
