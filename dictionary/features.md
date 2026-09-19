# Features ne demek, nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Features (özellikler), bilişim dünyasında iki kritik alanda temel yapı taşıdır: Yazılım mühendisliği ve ürün yönetiminde kullanıcıya sunulan fonksiyonel yetenekler; veri bilimi ve makine öğreniminde ise modellerin tahmin üretmek için kullandığı matematiksel özniteliklerdir.

## Etimoloji ve İkili Anlam Alanı
İngilizce kökenli *feature* sözcüğü, köken olarak bir nesnenin veya yüzün belirgin niteliğini, karakteristik çizgisini ifade eder. Bilişim ve teknoloji ekosisteminde bu terim arama motorlarında sıklıkla "ne demek" sorgusuyla aratılmakta olup, karşılaşılan bağlama göre tamamen farklı iki disipline işaret eder:
1. **Yazılım ve Ürün Geliştirme:** Bir uygulamanın ne yapabildiğini, kullanıcının hangi problemini çözdüğünü belirten fonksiyonel kabiliyetler (arama çubuğu, tek tıkla ödeme, karanlık mod).
2. **Yapay Zekâ ve Makine Öğrenimi:** Bir veri örneğini tanımlayan ölçülebilir değişkenler, yani matematiksel **öznitelikler** (bir evin metrekaresi, kelime frekansı, piksel renk vektörü).

## 1. Yazılım Mühendisliği ve Ürün Yönetiminde Features
Modern ürün yönetiminde bir özellik, salt kod satırlarından ibaret değildir; kullanıcı ihtiyacı ile iş değeri arasındaki köprüdür.

### Özellik Hiyerarşisi ve MVP Kapsamı
Çevik (Agile) ürün yönetiminde özellikler katmanlı bir piramit içinde modellenir:
- **Tema ve Girişim (Initiative):** "Platform güvenliğini artırmak".
- **Epik (Epic):** "İki faktörlü kimlik doğrulama altyapısı".
- **Özellik (Feature):** "SMS ve Authenticator uygulaması ile doğrulama ekranı".
- **Kullanıcı Hikâyesi (User Story):** "Bir son kullanıcı olarak, hesabımı korumak için tek kullanımlık kod girmek istiyorum".

Yeni bir dijital ürün inşa edilirken yapılan en büyük hata, tüm hayal edilen özellikleri aynı anda kodlamaya çalışmaktır. **MVP (Minimum Viable Product)** felsefesi, pazara en yalın haliyle çıkan ve yalnızca temel değer önerisini karşılayan çekirdek özellikler (core features) üzerine kurulmalıdır.

### Feature Flags (Özellik Bayrakları) Mimarisi
Modern sürekli dağıtım (Continuous Deployment) süreçlerinde kodun canlıya alınması ile kullanıcılara açılması birbirinden ayrılmıştır. Bu ayrımı sağlayan mimari modele **Feature Flags (Feature Toggles)** adı verilir:
- **Sıfır Kesintiyle Yayınlama:** Yeni bir özellik kodlanır ve ana dala (trunk) birleştirilip canlıya gönderilir; ancak bayrak kapalı olduğu için son kullanıcılar bunu görmez.
- **Canary ve A/B Testleri:** Bayrak aracılığıyla yeni özellik önce şirket çalışanlarına, ardından trafiğin %5'ine açılır. Hata oranı ve performans metrikleri izlenir.
- **Acil Durum Düğmesi (Kill Switch):** Canlı ortamda bir çökme veya veritabanı darboğazı yaşandığında, kodu geri almaya (rollback) gerek kalmadan bayrak kapatılarak özellik milisaniyeler içinde devreden çıkarılır.
- **Teknik Borç Uyarısı:** Süresi dolmuş ve herkese açılmış bayrakların kod tabanından temizlenmemesi, "Dead Flag" teknik borcuna yol açar.

## 2. Makine Öğrenimi ve Veri Biliminde Features (Öznitelikler)
Yapay zekâ ve veri biliminde "feature", tahminleme algoritmalarının girdi olarak aldığı sayısal veya kategorik niteliklerdir ($X = [x_1, x_2, \dots, x_n]$).

### Öznitelik Mühendisliği (Feature Engineering)
Ham veriler doğrudan makine öğrenimi modellerine beslenemez. Ham verinin modelin anlayabileceği matematiksel ifadelere dönüştürülmesine öznitelik mühendisliği denir:
- **Kategorik Dönüştürme:** Şehir isimleri veya ürün tiplerinin One-Hot Encoding ile ikili (0/1) vektörlere çevrilmesi.
- **Ölçekleme (Scaling):** Yaş (18-80) ile gelir (10.000-500.000) gibi farklı büyüklükteki sayısal değerlerin Standardizasyon veya Min-Max ölçekleme ile dengelenmesi.
- **Metin ve Görüntü Gömmeleri (Embeddings):** Doğal dildeki kelimelerin ve cümlelerin yüzlerce boyutlu yoğun vektörlere (Word2Vec, Transformer embeddings) dönüştürülmesi.

### Boyut Laneti ve Feature Selection
Veri kümesine rastgele onlarca yeni özellik eklemek başarıyı artırmaz; aksine **Boyut Laneti (Curse of Dimensionality)** problemine yol açar. Model aşırı öğrenme (overfitting) yaşar ve eğitim süresi katlanarak artar. Bu nedenle PCA (Temel Bileşen Analizi), Lasso regülasyonu veya Bilgi Kazanımı (Information Gain) gibi yöntemlerle en ayırt edici öznitelikler seçilir.

### Feature Store (Öznitelik Deposu) Mimarisi
Kurumsal yapay zekâ sistemlerinde (Feast, Hopsworks, Tecton) modellerin eğitiminde kullanılan veriler ile canlı çıkarım (inference) anındaki verilerin birebir tutarlı olması gerekir. Feature Store mimarisi, modeller arasındaki "Train-Serving Skew" (eğitim-hizmet sapması) riskini tamamen ortadan kaldırır.

## Feature Creep (Şişkinlik) ve Anti-Pattern'ler
Yazılım ürünlerinde karşılaşılan en kritik risklerden biri **Feature Creep (Kapsam ve Özellik Şişkinliği)** olarak adlandırılır:
- Kullanıcıların sadece %1'inin talep ettiği uç senaryolar için karmaşık butonlar ve ayarlar eklenmesi, arayüzü anlaşılmaz kılar.
- Kod tabanındaki karmaşıklık katsayısı (Cyclomatic Complexity) ve bakım maliyeti logaritmik olarak tırmanır.
- Unix felsefesinin en büyük öğretisi şudur: *"Tek bir iş yap ve onu mükemmel yap."* En başarılı dijital ürünler, yüzlerce vasat özelliğe değil; pürüzsüz çalışan birkaç kritik özelliğe sahip olanlardır.

## Sıkça Sorulanlar

**Features ne demek ve Türkçe karşılığı nedir?**  
İngilizce kökenli bir terim olup Türkçede "özellikler" anlamına gelir. Ürün geliştirmede bir yazılımın sunduğu işlevleri, makine öğreniminde ise tahminleme için kullanılan matematiksel "öznitelikleri" ifade eder.

**Feature flag (özellik bayrağı) mimarisi ne işe yarar?**  
Yeni kodları canlı sunucuya gönderip risk almadan, özelliği belirli kullanıcılara dinamik olarak açıp kapatmaya, A/B testi yapmaya ve olası hatalarda kodu geri çekmeden özelliği kapatmaya yarayan anahtarlama sistemidir.

**Makine öğreniminde feature engineering neden başarının yüzde seksenidir?**  
En gelişmiş derin öğrenme modeli bile kalitesiz ve gürültülü özniteliklerle doğru tahmin üretemez. Ham veriyi doğru matematiksel gösterimlere ve ayırt edici değişkenlere dönüştürmek model başarımını doğrudan belirler.

**Feature creep (özellik şişkinliği) ürünleri nasıl yok eder?**  
Her müşteri talebini plansızca ürüne eklemek, yazılımı yavaşlatır, arayüzü karmaşıklaştırır, test süreçlerini zorlaştırır ve ürünün odaklandığı ana değer önerisini yok eder.

## İlgili terimler
- [Tools](/dictionary/tools/)
- [Tech Stack](/dictionary/tech-stack/)
- [Deployment](/dictionary/deployment/)
- [Application](/dictionary/application/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/features/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
