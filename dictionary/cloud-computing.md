# Cloud Computing nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Cloud Computing (bulut bilişim), sunucu, depolama, veritabanı, ağ ve yazılım gibi bilgi işlem kaynaklarının fiziksel yerel altyapılar yerine internet üzerinden uzaktaki veri merkezlerinden anlık ihtiyaç doğrultusunda (on-demand) sunulmasıdır.

## Tanım, etimolojik köken ve kavramsal doğuş
Bulut bilişim (Cloud Computing), şirketlerin ve mühendislerin kendi sunucu odalarını inşa edip fiziksel donanım satın almak yerine; internet üzerinden saniyeler içinde hesaplama gücü, bellek, depolama alanı ve yapay zekâ GPU kümeleri kiralamasını sağlayan modern bilgi işlem modelidir.

Kavramsal olarak kökleri 1961 yılına, yapay zekânın babalarından John McCarthy'nin MIT'deki konuşmasına dayanır. McCarthy, bilişim gücünün gelecekte tıpkı elektrik ve su gibi bir kamu hizmeti (utility) olarak sunulacağını öngörmüştü. "Bulut" kelimesinin bu sektöre yerleşmesi ise telekomünikasyon ve ağ mühendisliğine dayanır: 1990'lı yıllarda sistem mimarları, detaylarını soyutlamak istedikleri karmaşık telefon santrallerini ve internet omurgasını diyagramlara bir "bulut ikonu" çizerek yerleştirirdi. 2006 yılında Amazon'un Simple Storage Service (S3) ve Elastic Compute Cloud (EC2) hizmetlerini geliştiricilere açmasıyla birlikte, sermaye yatırımı (CapEx) odaklı sunucu satın alma modeli yerini kullandığın kadar öde (OpEx) prensibine bıraktı.

## Bir benzetmeyle
Kendi fabrikanızın veya evinizin bahçesine özel bir hidroelektrik santrali ya da jeneratör kurmak yerine doğrudan ulusal elektrik şebekesine bağlanmak gibidir. Prize fişi taktığınız anda elektrik akar, makineniz ne kadar güç harcarsa ay sonunda yalnızca o tüketimin bedelini ödersiniz; jeneratörün arızası, yakıtı veya trafo bakımıyla siz uğraşmazsınız.

## Temel hizmet ve dağıtım modelleri (IaaS, PaaS, SaaS, Serverless)
Bulut bilişim mimarisi, soyutlama seviyelerine göre dört ana hizmet modeline ayrılır:

1. **IaaS (Infrastructure as a Service - Altyapı Hizmeti):** En alt seviye ham sanal makineler, blok depolama diskleri ve sanal ağ topolojileridir. AWS EC2, Google Compute Engine ve Azure VM bu kategoridedir. Donanım ve sanallaştırma katmanını bulut sağlayıcısı yönetir; işletim sisteminin kurulumu, güvenlik yamaları ve yazılım yığınından geliştirici sorumludur.
2. **PaaS (Platform as a Service - Platform Hizmeti):** Geliştiriciyi sunucu yapılandırması, işletim sistemi ve çalışma ortamı (runtime) dertlerinden kurtaran platformlardır. Vercel, Heroku ve AWS Elastic Beanstalk örnek gösterilebilir. Mühendis yalnızca kaynak kodunu gönderir; ölçekleme, SSL sertifikaları ve yük dengeleme arka planda otomatik halledilir.
3. **SaaS (Software as a Service - Yazılım Hizmeti):** Son kullanıcının doğrudan web tarayıcısı veya API aracılığıyla eriştiği, bakımını tamamen üreticinin üstlendiği anahtar teslim yazılımlardır. Google Workspace, Slack, Salesforce ve Figma bu modelin en bilinen örnekleridir.
4. **Serverless (FaaS - Fonksiyon Hizmeti):** Sunucu kavramını tamamen soyutlayan olay güdümlü (event-driven) mimaridir. AWS Lambda veya Cloudflare Workers üzerinde yazılan kod, sadece tetikleyici bir HTTP isteği veya veritabanı olayı geldiğinde ayağa kalkar, milisaniyeler içinde çalışır ve kapanır. Trafik yokken sıfır maliyet üretir.

Dağıtım modelleri ise verinin nerede barındırıldığına göre şekillenir:
- **Genel Bulut (Public Cloud):** Kaynakların çok kiracılı (multi-tenant) olarak dev sağlayıcıların küresel veri merkezlerinde paylaşıldığı yapı.
- **Özel Bulut (Private Cloud):** Finans, savunma ve sağlık gibi regülasyona tabi sektörlerin yalnızca kendilerine tahsis edilmiş veri merkezlerinde çalıştırdığı izole ortam.
- **Hibrit Bulut (Hybrid Cloud):** Hassas müşteri verilerinin özel yerel sunucularda (on-premise), yüksek işlem hacmi gerektiren web katmanının ise genel bulutta çalıştığı melez yapı.
- **Çoklu Bulut (Multi-Cloud):** Tek bir şirkete bağımlı kalmamak (vendor lock-in) için sistemlerin hem AWS hem Google Cloud hem de Azure üzerinde dağıtık kurgulanması.

## Bilgisayar bilimleri ve sistem mimarisi: Hypervisor, konteyner ve CAP
Bulut bilişimin altında yatan teknik mucize, donanımın yazılımsal olarak soyutlanmasıdır (sanallaştırma):
- **Hypervisor Katmanı:** Tek bir fiziksel sunucunun işlemci ve RAM kaynaklarını bölerek onlarca bağımsız sanal makineye (VM) paylaştıran çekirdek yazılımdır. Donanım üzerinde doğrudan koşan Type 1 Bare-metal (KVM, VMware ESXi) hypervisor'lar, bulut sağlayıcılarının performans omurgasıdır.
- **Konteynerler ve Orkestrasyon:** Sanal makinelerin işletim sistemi kopyalama yükünü aşmak için Linux çekirdeğinin `cgroups` (kaynak sınırlandırma) ve `namespaces` (süreç izolasyonu) yetenekleri kullanılarak Docker konteynerleri doğmuştur. Binlerce konteynerin otomatik dağıtımı ve kendi kendini onarması (self-healing) ise Kubernetes kümeleriyle sağlanır.
- **CAP Teoremi ve Dağıtık Dayanıklılık:** Küresel bulut altyapıları Eric Brewer'ın CAP Teoremi sınırları dahilinde çalışır. Bir ağ bölünmesi (Network Partition) anında sistem ya Veri Tutarlılığını (Consistency) ya da Kesintisiz Erişilebilirliği (Availability) öncelemek zorundadır. Bulut mimarları coğrafi olarak yedekli (Multi-Region / Availability Zone) mimarilerle felaket kurtarma senaryolarını hayata geçirir.
- **Paylaşımlı Sorumluluk Modeli (Shared Responsibility):** Güvenlik bulutta ikiye ayrılır. Sağlayıcı fiziksel veri merkezlerinin, sunucuların, hypervisor'ın ve ağ kablolarının güvenliğinden sorumludur ("Security OF the Cloud"). Müşteri ise işletim sistemi güncellemelerinden, şifrelemeden, IAM (erişim yönetimi) rollerinden ve uygulama kodunun zafiyetlerinden sorumludur ("Security IN the Cloud").

## Ekonomik, ekolojik ve jeopolitik boyut
Bulut bilişim yalnızca teknik bir devrim değil, küresel kaynak tahsisinde de devasa bir kırılmadır:
- **Jevons Paradoksu:** 19. yüzyıl iktisatçısı William Stanley Jevons'ın kömür tüketimi için ortaya koyduğu ilke bulutta da geçerlidir: Bilişim gücüne erişim ucuzlayıp kolaylaştıkça toplam tüketim azalmaz, aksine katlanarak artar. Bugün yüz milyarlarca parametreli yapay zekâ modellerinin eğitilebilmesi, bulut bilişimin sunduğu ölçek ekonomisinin doğrudan sonucudur.
- **Enerji ve Su Tüketimi:** Hiperscaler veri merkezleri küresel elektrik tüketiminin yaklaşık %1-2'sini harcamakta olup, dev GPU kümelerinin soğutulması için milyonlarca metreküp saf su kullanılmaktadır. Bu durum veri merkezlerinin yenilenebilir enerji kaynaklarının ve soğuk iklimlerin yakınına kurulmasını zorunlu kılmıştır.
- **Dijital Egemenlik ve Hukuki Rejimler:** Verinin fiziksel olarak nerede durduğu jeopolitik bir meseledir. ABD CLOUD Act yasası Amerikan firmalarının yurt dışındaki sunucularına müdahale yetkisi verirken; Avrupa Birliği GDPR ve GAIA-X inisiyatifiyle, Türkiye ise KVKK mevzuatıyla kritik verilerin ulusal sınırlar içerisinde kalmasını teşvik etmektedir.

## Sık karıştırılanlar
- **Bulut Depolama vs Bulut Bilişim:** Google Drive, iCloud veya Dropbox yalnızca depolama (storage) servisleridir; bulut bilişim ise depolamanın yanında dinamik işlemci gücü, yapay zekâ eğitimi, ağ yönetimi ve veritabanı orkestrasyonunu içeren devasa bir ekosistemdir.
- **Serverless (Sunucusuz) vs Gerçekten Sunucusuz:** Serverless mimaride fiziksel sunucular elbette vardır; "sunucusuz" terimi geliştiricinin artık bir sunucuyu yapılandırmak, güncellemek veya izlemekle uğraşmadığını, sunucu yönetiminin sağlayıcı tarafından görünmez hale getirildiğini ifade eder.

## Sıkça sorulanlar

**Cloud computing ne demek ve Türkçe karşılığı nedir?**  
Türkçede 'bulut bilişim' anlamına gelir. Bilgi işlem gücünün, sunucuların ve depolama kaynaklarının yerel bilgisayarlar yerine internet omurgası üzerinden ihtiyaca göre anlık kiralanması modelidir.

**Bulut bilişimin 3 ana hizmet modeli (IaaS, PaaS, SaaS) arasındaki temel fark nedir?**  
IaaS ham donanım ve sanal sunucu kiralama (AWS EC2), PaaS doğrudan kod çalıştırma ve barındırma ortamı (Vercel), SaaS ise son kullanıcıya web üzerinden sunulan anahtar teslim yazılımdır (Google Docs).

**Paylaşımlı Sorumluluk Modeli (Shared Responsibility Model) ne anlama gelir?**  
Bulut sağlayıcısının fiziksel altyapıyı, veri merkezini ve donanımı korumakla yükümlü olduğu; kullanıcının ise kendi uygulama güvenliği, kullanıcı izinleri (IAM) ve veri şifrelemesinden sorumlu olduğu güvenlik iş bölümüdür.

**Bulut sağlayıcı bağımlılığı (Vendor Lock-in) nasıl engellenir?**  
Açık kaynak standartları (Docker konteynerleri, Kubernetes), bağımsız veritabanı motorları (PostgreSQL) ve Altyapı Kod Olarak (Terraform / OpenTofu) araçları kullanılarak yazılımlar sağlayıcıya özel tescilli API'lardan izole edilir.

## İlgili terimler
- [SaaS](/dictionary/saas/)
- [PaaS](/dictionary/paas/)
- [IaaS](/dictionary/iaas/)
- [Personal Cloud](/dictionary/personal-cloud/)
- [Runtime](/dictionary/runtime/)
- [Network Stack](/dictionary/network-stack/)
- [Memory Management](/dictionary/memory-management/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/cloud-computing/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
