# AWS nedir, ne demek?

> Amazon Web Services

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-22

AWS (**Amazon Web Services**), sunucu, depolama ve veritabanı gibi bilişim hizmetlerini internetten kiraladığınız bulut platformudur.

## Tanım ve Kelime Kökeni
Kendi fiziksel sunucunuzu kurmak yerine Amazon veri merkezlerini kiralarsınız. İhtiyaç artınca kapasite büyür, iş bitince küçülür. Ödeme kullandıkça artar modeliyle çalışır. Neredeyse tüm modern uygulamaların arka planında bu tür bir bulut altyapısı vardır.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Web sitesi:** Trafiğe göre büyüyen sunucular.
- **Yedekleme:** Sınırsız gibi görünen dosya kasası.
- **Video:** İzlendikçe dağıtılan içerik.
- **Startup:** Sunucu odası kurmadan yayına çıkma.

## Teknik Derinlik ve Mimari
Temel servisler:
- **EC2:** Kiralık sanal sunucu.
- **S3:** Nesne depolama, yedek ve statik dosya kasası.
- **RDS:** Yönetilen ilişkisel veritabanı.
- **Lambda:** Olay olunca çalışan sunucusuz işlev.

Kavramlar:
- **Bölge ve erişim bölgesi:** Verinin fiziksel konumu ve yedeklilik.
- **Paylaşımlı sorumluluk:** Bulutun güvenliği Amazon sorumluluğunda, içindeki verinin güvenliği sizde.
- **Ücretsiz katman:** Yeni hesaplara sınırlı ücretsiz kullanım.

Çalışan sunucuları listelemek için:

```
aws ec2 describe-instances --query "Reservations[].Instances[].State.Name"
```

Fatura sürprizine karşı bütçe alarmı kurmanız önerilir, çünkü açık unutulan kaynaklar ücret işlemeye devam eder.

## Sık Karıştırılanlar
Sadece site barındırma hizmeti sanılır. Oysa 200 üzeri servisle veritabanı, yapay zekâ, ağ ve güvenlik katmanlarını kapsayan tam bir altyapı platformudur.

## Farklı Disiplinlerde Kullanımı
- **Elektrik şebekesi:** Santral kurmak yerine prizden çekmek.
- **Kiralık depo:** İhtiyaç kadar raf kiralamak.
- **Taksi:** Araç sahibi olmadan yolculuk yapmak.

## Bir benzetmeyle
Kendi elektrik santralinizi kurmak yerine şebekeden elektrik satın almak gibidir; sadece kullandığınız kadar ödersiniz.

## Sıkça sorulanlar

**Neden AWS kullanmalıyım?**  
Donanım yatırımı yapmadan kurumsal altyapıya anında erişirsiniz. Trafik dalgalıysa ölçekleme ve hazır servisler zaman kazandırır.

**Ücretsiz başlanabilir mi?**  
Evet. Yeni hesaplar için ücretsiz plan, kredi ve süre koşulları zamanla değişebilir; başlamadan önce AWS Free Tier sayfasındaki güncel limitleri kontrol etmeniz gerekir.

**Verilerim nerede tutulur?**  
Seçtiğiniz bölgede tutulur. KVKK gibi düzenlemeler için bölge seçimini ve şifrelemeyi politikanıza göre yapmanız gerekir.

**Fatura nasıl kontrol altında tutulur?**  
Bütçe alarmları, kullanılmayan kaynak temizliği ve doğru boyutlandırma ile. Küçük ekiplerde etiketleme disiplini şarttır.

## İlgili terimler
- [Cloud Computing](/dictionary/cloud-computing/)
- [IaaS](/dictionary/iaas/)
- [PaaS](/dictionary/paas/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/aws/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
