# Production Pipeline nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Production pipeline (üretim boru hattı), yazılım geliştiricilerin yazdığı kaynak kodların otomatik olarak derlenmesi, test edilmesi, güvenlik taramalarından geçirilmesi, paketlenmesi ve canlı (production) ortama sıfır kesintiyle dağıtılmasını sağlayan entegre mühendislik süreçleri zinciridir.

## Kavramsal köken, etimoloji ve üretim hattı felsefesi
"Pipeline" sözcüğü petrol ve su taşımacılığındaki boru hatlarından; "production" ise endüstriyel fabrikalardaki montaj hatlarından (assembly line) yazılım mühendisliğine ödünç alınmıştır. Henry Ford'un 20. yüzyılın başında seri üretim bandıyla otomotivde yarattığı devrim neyse; production pipeline da yazılım sektöründe manuel, hataya açık ve belirsiz dağıtım süreçlerini sonlandıran modern endüstriyel üretim standardıdır.

Geleneksel yazılım süreçlerinde geliştiriciler kodu yazar, ardından elle bir sunucuya SSH veya FTP ile bağlanarak dosyaları kopyalardı. Bu "el yapımı" yaklaşım, konfigürasyon sapmalarına (configuration drift), ortam uyumsuzluklarına ve öngörülemeyen sistem çökmelerine yol açıyordu. Production pipeline, kaynak kodun depoya (Git) girdiği ilk saniyeden son kullanıcıya ulaştığı ana kadar her aşamayı kodlanabilir, tekrarlanabilir ve denetlenebilir (declarative) bir fabrika bandına dönüştürür.

## Bir benzetmeyle
Modern ve tam otomatik bir uçak fabrikasını düşünün: Ham titanyum parçalar (kaynak kod) banda girer; lazer ölçüm cihazları her mikronu tarar (statik kod analizi ve linting), dayanıklılık simülasyonları yapılır (birim ve entegrasyon testleri), kabin montajı tamamlanır (derleme ve konteynerizasyon), rüzgar tünelinde test uçuşu gerçekleştirilir (staging ortamı) ve son olarak uluslararası havacılık sertifikası onaylanınca yolcu taşımaya başlar (canlıya çıkış / production).

## Bir üretim hattının 5 kritik istasyonu
Eksiksiz bir kurumsal production pipeline şu adımlardan oluşur:

1. **Kaynak ve Tetikleme (Source & Trigger):** Geliştirici kodunu ana dala (main branch) gönderdiğinde veya bir Pull Request (PR) açtığında webhook'lar aracılığıyla süreç otomatik başlar.
2. **Statik Analiz ve Derleme (Build & Lint):** Kod derlenir, stil kuralları denetlenir ve güvenlik açıkları taranır (SAST ve bağımlılık taraması - Trivy, Snyk). Ardından imutatif (değiştirilemez) bir Docker imajı oluşturulup imaj deposuna (Container Registry) yüklenir.
3. **Kapsamlı Test Piramidi (Automated Testing):** Hızlı çalışan birim testleri (unit tests), servisler arası entegrasyon testleri ve kullanıcı senaryolarını simüle eden uçtan uca (E2E) testler çalıştırılır. Testlerden biri dahi başarısız olursa boru hattı üretimi derhal durdurur (Andon Kordonu ilkesi).
4. **Staging / Geçici Doğrulama Ortamı (Preview Environments):** Üretim ortamının birebir kopyası olan izole bir alanda duman testleri (smoke tests) ve yük testleri icra edilir.
5. **Kademeli Canlıya Dağıtım (Progressive Delivery):** Kod, Mavi-Yeşil (Blue-Green) ya da Kanarya (Canary) dağıtım teknikleriyle canlıya aktarılır. Sistem sağlık metrikleri (hata oranı, gecikme) anlık gözlemlenerek herhangi bir sorunda otomatik geri alma (rollback) tetiklenir.

## Sektörel ayrımlar: Production Pipeline vs Data Pipeline vs VFX Pipeline
"Pipeline" kelimesi farklı teknik disiplinlerde farklı anlamlara gelir:
- **Yazılım Production Pipeline:** Yazılım kodunun derlenmesi, test edilmesi ve sunuculara dağıtılması sürecidir (CI/CD).
- **Veri Boru Hattı (Data Pipeline):** Verinin çeşitli kaynaklardan toplanması, temizlenmesi, dönüştürülmesi ve analitik veritabanlarına aktarılması (ETL / ELT) sürecidir.
- **Görsel Efekt ve 3D Pipeline (VFX / Animation):** 3D modelleme, render, doku kaplama ve kompozitleme yazılımları (Maya, Houdini, Blender) arasındaki dijital varlıkların (assets) işlenme zinciridir.

## DORA metrikleri ve mühendislik verimliliği
Bir organizasyonun production pipeline olgunluğu, Google'ın DORA (DevOps Research and Assessment) araştırmasında belirlenen dört altın metrik ile ölçülür:
- **Dağıtım Sıklığı (Deployment Frequency):** Kodun canlıya alınma hızı (ayda bir yerine günde birden çok kez).
- **Değişiklik Teslim Süresi (Lead Time for Changes):** İlk commit'ten canlıya geçişe kadar geçen süre.
- **Değişiklik Başarısızlık Oranı (Change Failure Rate):** Canlıya alınan sürümlerin ne kadarında düzeltme veya geri alma gerektiği.
- **Hizmet Geri Yükleme Süresi (MTTR):** Canlıda bir aksaklık çıktığında sistemin yeniden ayağa kalkma hızı.

## Sıkça sorulanlar

**Production pipeline ne demek ve temel amacı nedir?**  
Yazılım üretim boru hattı demektir. Geliştirilen kaynak kodun insan hatasından arındırılmış biçimde otomatik olarak test edilip derlenmesini ve canlı sunuculara güvenle ulaştırılmasını amaçlar.

**Production pipeline ile CI/CD arasındaki fark nedir?**  
CI/CD (Sürekli Entegrasyon / Sürekli Dağıtım), pipeline'ın temel metodolojisi ve omurgasıdır. Production pipeline ise CI/CD'nin yanı sıra ortam provizyonu, güvenlik taramaları (DevSecOps), onay mekanizmaları ve gözlemlenebilirlik araçlarını da kapsayan geniş sistemin adıdır.

**Production pipeline hangi araçlarla kurulur?**  
Sürüm kontrolünde GitHub ve GitLab; orkestrasyonda GitHub Actions, Jenkins ve ArgoCD; paketlemede Docker; altyapıda Kubernetes ve Terraform en yaygın araçlardır.

**Dağıtım sırasında sistemde kesinti yaşanır mı?**  
İyi tasarlanmış bir production pipeline'da Mavi-Yeşil veya Kanarya dağıtım yöntemleri kullanılır; bu sayede kullanıcılar kesinti hissetmeden yeni sürüme aktarılır (zero-downtime).

## İlgili terimler
- [Deployment](/dictionary/deployment/)
- [Data Pipeline](/dictionary/data-pipeline/)
- [Cloud Computing](/dictionary/cloud-computing/)
- [Tech Stack](/dictionary/tech-stack/)
- [Git Push](/dictionary/git-push/)
- [Runtime](/dictionary/runtime/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/production-pipeline/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
