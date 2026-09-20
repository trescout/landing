# Deployment ne demek, nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Deployment (yazılım dağıtımı / canlıya alma), yerel ortamda geliştirilen ve test edilen bir yazılım bileşeninin, derlenerek hedef sunuculara veya bulut altyapısına kurulması ve son kullanıcıların erişimine açılması sürecidir.

## Kavramsal çerçeve, etimoloji ve tarihsel dönüşüm
Deployment terimi etimolojik olarak askeri terminolojiye dayanır; birliklerin, mühimmatın veya donanmanın stratejik muharebe pozisyonlarına sevk edilip harekâta hazır hale getirilmesini ("to deploy") ifade eder. Yazılım mühendisliğinde ise 1970'li ve 80'li yıllarda delikli kartların veya manyetik bantların ana bilgisayarlara (mainframe) yüklenmesiyle başlamış; 1990'larda elle çalıştırılan FTP/SSH dosya aktarımlarına, günümüzde ise tamamen deklaratif ve otomatik bulut boru hatlarına (GitOps) evrilmiştir.

Modern yazılım mühendisliğinde deployment tek seferlik, sancılı ve gece yarısı yapılan riskli bir operasyon olmaktan çıkmıştır. Sürekli Entegrasyon ve Sürekli Dağıtım (CI/CD) mekanizmaları sayesinde, günde yüzlerce kez kodun üretim ortamına güvenle aktarıldığı standart bir iş akışıdır.

## Bir benzetmeyle
Yolcularla dolu yüksek hızlı bir trenin ray değiştirme operasyonuna benzer. Geleneksel yöntemde treni istasyonda durdurup rayları kaynakla birleştirmek (kesinti süresi / downtime) gerekirdi; modern dağıtım ise tren saatte 300 kilometre hızla giderken otomatik ray makasının milisaniyeler içinde yeni hatta geçmesi ve yolcuların bir sarsıntı dahi hissetmemesidir.

## Sıfır kesintili (Zero-Downtime) dağıtım stratejileri
Uygulamaların güncellenirken kullanıcıların hizmet kesintisi yaşamaması için geliştirilen temel dağıtım desenleri şunlardır:

1. **Mavi-Yeşil Dağıtım (Blue-Green Deployment):** Biri canlı trafiği karşılayan (Mavi), diğeri ise boşta duran (Yeşil) iki özdeş sunucu ortamı tutulur. Yeni kod yeşil ortama kurulur, duman testleri (smoke tests) yapılır ve her şey kusursuz çalıştığında yük dengeleyici (Load Balancer) trafiği milisaniyeler içinde yeşile yönlendirir. Bir sorun çıkarsa anında maviye geri dönülür (anlık rollback).
2. **Kanarya Dağıtımı (Canary Deployment):** İsmini 19. yüzyıl kömür madencilerinin zehirli gaz kaçaklarını erkenden tespit etmek için kafeste kanarya taşımasından alır. Yeni sürüm önce toplam kullanıcı trafiğinin yalnızca %1 ila %5'ine açılır. Hata oranları (HTTP 5xx), bellek tüketimi ve yanıt süreleri izlenir; sistem kararlıysa oran kademeli olarak %25, %50 ve %100'e çıkarılır.
3. **Kayan Güncelleme (Rolling Deployment):** Kubernetes kümelerinde veya sunucu filolarında konteynerlerin teker teker (örneğin %20'lik porsiyonlar halinde) güncellenmesidir. Eski pod'lar sırayla kapatılıp yerlerine yeni sürüm pod'ları açılır. Fazladan yedek donanım maliyeti gerektirmez ancak aynı anda iki farklı sürümün canlıda çalıştığı geçiş sürecinin yönetilmesini gerektirir.
4. **Gölge Dağıtım (Shadow / Dark Deployment):** Canlı kullanıcı trafiği kopyalanarak (traffic mirroring) arka planda çalışan yeni sürüme de gönderilir. Ancak yeni sürümün ürettiği yanıtlar kullanıcıya iletilmez, yalnızca sistemin gerçek dünya yükü altındaki performansı ve algoritma doğruluğu ölçülür.

## CI/CD boru hattı, GitOps ve veritabanı geçişleri
Başarılı bir dağıtım mimarisi üç kritik mühendislik temeli üzerine inşa edilir:
- **CI/CD Otomasyonu ve DORA Metrikleri:** Bir mühendis Git deposuna commit attığında, kod otomatik olarak lint kontrolünden geçer, birim testleri ve entegrasyon testleri koşar, Docker konteyner imajı derlenir ve hedef ortama fırlatılır. DevOps Araştırma ve Değerlendirme (DORA) metriklerine göre yüksek performanslı ekipler dağıtım sıklığını (Deployment Frequency) saatler seviyesine indirirken, değişiklik teslim süresini (Lead Time) ve başarısızlık oranını minimuma çeker.
- **GitOps İlkesi:** Altyapının ve uygulama sürümlerinin ArgoCD veya Flux gibi araçlarla doğrudan bir Git deposu tarafından deklare edilmesidir. Git deposu tek doğruluk kaynağıdır (Single Source of Truth); sunuculardaki gerçek durum Git'teki durumdan saparsa sistem kendini otomatik eşitler.
- **Veritabanı Şema İkilemi (Expand-Contract Deseni):** Kod sıfır kesintiyle güncellenebilir ancak veritabanı tablolarında yapılan bir kolon silme işlemi eski sürümün çökmesine yol açabilir. Bu nedenle mühendisler "Genişlet-Daralt" (Parallel Run) desenini uygular: Önce yeni kolon eklenir ve her iki sürüme de yazılır, tüm sunucular yeni sürüme geçtikten sonra eski kolon güvenle silinir.

## Hata yönetimi, gözlemlenebilirlik ve Rollback mimarisi
En gelişmiş test ortamlarında dahi gözden kaçan üretim ortamı hataları için iki temel can simidi vardır:
- **Otomatik Rollback (Geri Alma):** APM araçları (Datadog, Prometheus) hata eşiklerinde (örneğin hata oranının %1'i aşması) anormallik tespit ettiği anda insan müdahalesine gerek kalmadan önceki kararlı Docker imajına veya Git etiketine geri döner.
- **Feature Flags (Özellik Bayrakları):** Dağıtım (deployment) ile yayına alma (release) süreçlerini birbirinden ayırır. Kod sunucuda çalışıyor olsa bile yeni özellik kullanıcı arayüzünde kapalı tutulabilir; riskli bir anda tek bir dashboard anahtarıyla anında devreden çıkarılabilir.

## Sık karıştırılanlar
- **Development vs Deployment:** Development (geliştirme) mutfakta şefin yemeği hazırlaması ve tatmasıdır; Deployment ise yemeğin masaya servis edilip müşterinin tüketimine sunulmasıdır.
- **Deployment vs Release:** Deployment teknik bir eylemdir; kodun sunucuya yüklenmesini ifade eder. Release ise bir özelliğin kullanıcılara görünür kılınması, pazarlama duyurusunun yapılması ve iş birimi tarafından resmen açılmasıdır.

## Sıkça sorulanlar

**Deployment ne demek ve Türkçe karşılığı nedir?**  
İngilizce kökenli bir kelime olup 'dağıtım' veya 'canlıya alma' anlamına gelir. Yazılım paketinin derlenerek hedef sunucularda veya bulut ortamında çalışır hale getirilmesi sürecidir.

**Deployment ile Release arasındaki fark nedir?**  
Deployment kodun sunucuya teknik olarak kurulması ve çalıştırılmasıdır. Release ise özelliğin Feature Flag veya pazarlama adımlarıyla son kullanıcının erişimine resmen açılmasıdır.

**Mavi-Yeşil (Blue-Green) ve Canary dağıtım arasındaki temel fark nedir?**  
Mavi-Yeşil dağıtımda iki özdeş ortam bulunur ve trafik tek bir anda yük dengeleyiciyle %100 yeni ortama aktarılır. Canary dağıtımda ise yeni sürüm kademeli olarak önce %1-5'lik küçük bir kullanıcı dilimine sunulur ve metrikler gözlemlenerek oran artırılır.

**Sıfır kesintili (Zero-Downtime) dağıtımda veritabanı şema değişiklikleri nasıl yönetilir?**  
Expand-Contract (Genişlet ve Daralt) deseniyle yönetilir. Önce geriye dönük uyumlu yeni alanlar eklenir, sistemin tüm sunucuları yeni koda geçtikten ve veri akışı sağlandıktan sonra eski alanlar temizlenir.

## İlgili terimler
- [Runtime](/dictionary/runtime/)
- [Compile-time](/dictionary/compile-time/)
- [Cloud Computing](/dictionary/cloud-computing/)
- [Production Pipeline](/dictionary/production-pipeline/)
- [Tech Stack](/dictionary/tech-stack/)
- [Git Push](/dictionary/git-push/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/deployment/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
