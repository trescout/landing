# Deployment ne demek, nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Deployment (yazılım dağıtımı), geliştirilen ve test edilen bir uygulamanın sunuculara yüklenerek son kullanıcıların erişimine açılması sürecidir.

## Tanım ve modern dağıtım mimarisi
Deployment (Türkçede dağıtım veya canlıya alma), yazılım geliştirme yaşam döngüsünün (SDLC) üretim aşamasıdır. Kodunuzu yerel geliştirme ortamınızdan (localhost) çıkarıp, dünyanın her yerinden kesintisiz erişilebilen canlı sunuculara, bulut servislerine (AWS, Vercel vb.) veya mobil uygulama mağazalarına taşıma sürecini ifade eder. Modern yazılım dünyasında deployment tek seferlik bir eylem değil; CI/CD hatları ile günde onlarca kez tekrarlanan otomatik bir standarttır.

## Bir benzetmeyle
Bir otomobil fabrikasını düşünün: Tasarım ve parça üretimi geliştirme aşamasıdır; üretilen otomobillerin tırlarla yetkili bayilere sevk edilip anahtar teslim müşterilere sunulması ise deployment aşamasıdır.

## Nasıl çalışır ve stratejileri nelerdir?
1. **Sürekli Dağıtım (Continuous Deployment):** Kod ana dala (main branch) birleştirildiğinde otomatik testler koşar; testler geçerse insan müdahalesi olmadan canlıya alınır.
2. **Mavi-Yeşil Dağıtım (Blue-Green Deployment):** Biri canlıda (mavi), diğeri yeni sürümü test eden (yeşil) iki özdeş ortam tutulur. Yeni sürüm hazır olduğunda yönlendirici (router) trafiği anında yeşile çevirerek sıfır kesinti sağlar.
3. **Kademeli Dağıtım (Canary Deployment):** Yeni sürüm önce kullanıcıların %5'ine açılır; hata oranı izlenir ve sorun yoksa tüm kullanıcılara yayılır.

## Nerede kullanılır?
Web sitelerinin yayınlanmasında, mikroservis ve API güncellemelerinde, mobil uygulamaların App Store/Google Play sürümlerinde ve yapay zekâ model ağırlıklarının servis edilmesinde kullanılır.

## Sık karıştırılanlar
- **Development vs Deployment:** Development (geliştirme) mutfakta yemeğin pişirilmesidir; Deployment ise yemeğin müşterinin masasına servis edilmesidir.
- **Release vs Deployment:** Deployment kodun teknik olarak sunucuya kurulmasıdır; Release ise özelliğin pazarlama ve iş birimleri tarafından kullanıcıya resmi olarak duyurulmasıdır.

## Sıkça sorulanlar

**Deployment ne demek ve Türkçe karşılığı nedir?**  
İngilizce kökenli bir kelime olup 'dağıtım' veya 'canlıya alma' anlamına gelir. Yazılım paketinin çalışır halde hedef ortama kurulmasıdır.

**Deployment sırasında hata çıkarsa ne yapılır (Rollback nedir)?**  
Kritik bir hata tespit edildiğinde otomatik 'rollback' (geri alma) mekanizması devreye girer ve sistem saniyeler içinde sorunsuz çalışan bir önceki stabil sürüme geri döner.

**Sıfır kesintili (Zero-Downtime) deployment nasıl sağlanır?**  
Konteyner orkestrasyonu (Kubernetes, Docker Swarm) ve yük dengeleyiciler (load balancer) sayesinde yeni sürüm ayağa kalkmadan eski sunucular kapatılmaz, böylece kullanıcılar hiçbir kesinti hissetmez.

## İlgili terimler
- [Runtime](/dictionary/runtime/)
- [Compile-time](/dictionary/compile-time/)
- [API](/dictionary/api/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/deployment/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
