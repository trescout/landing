# Distributed ne demek, nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Distributed (dağıtık), bilgi işlem dünyasında donanım, veri ve hesaplama süreçlerinin tek bir merkezi makine yerine ağ üzerinden birbirine bağlı çok sayıda bağımsız sunucuya (düğüme) paylaştırılması ve bu sistemin son kullanıcıya tek bir bütün bilgisayarmış gibi hizmet vermesidir.

## Etimoloji ve Dağıtık Sistemlerin Doğası
"Distributed" sözcüğü Türkçede **dağıtık** anlamına gelir. Bilgisayar bilimlerinin öncülerinden Leslie Lamport, dağıtık sistemleri tarihe geçen şu veciz sözüyle tanımlamıştır: *"Dağıtık sistem; varlığından bile haberdar olmadığınız bir bilgisayarın çökmesinin, kendi bilgisayarınızı kullanılamaz hale getirebildiği sistemdir."*

Merkezi (monolitik) mimarilerde tüm işlemler tek bir ana bellek ve işlemci üzerinde gerçekleşir. Dağıtık sistemlerde ise fiziksel olarak dünyanın farklı kıtalarındaki veri merkezlerine yayılmış yüzlerce düğüm (node), güvenilmez ağ kabloları üzerinden haberleşerek ortak bir amaca hizmet eder.

## Dağıtık Hesaplamanın 8 Yanılgısı (8 Fallacies)
1990'lı yıllarda Sun Microsystems mühendisleri L. Peter Deutsch ve James Gosling, dağıtık sistem geliştiren yazılımcıların düştüğü "8 Ölümcül Yanılgı"yı sıralamıştır. Modern bulut ve mikroservis mimarilerinin tüm savunma hatları bu yanılgılara göre kurulur:
1. **Ağ güvenilirdir:** Gerçekte paketler kaybolur, fiber hatlar kopar, yönlendiriciler kilitlenir.
2. **Gecikme (latency) sıfırdır:** İki makine arasındaki ışık hızı ve ağ anahtarlama gecikmesi her zaman mevcuttur.
3. **Bant genişliği sonsuzdur:** Veri hacmi arttıkça ağ boruları tıkanır.
4. **Ağ güvenlidir:** Tüm dağıtık iletişim açık hatlardan geçer ve kriptografik koruma gerektirir.
5. **Topoloji değişmez:** Sunucular sürekli açılıp kapanır, IP adresleri değişir.
6. **Yalnızca bir sistem yöneticisi vardır:** Çoklu ekipler ve bulut sağlayıcıları işin içindedir.
7. **Taşıma maliyeti sıfırdır:** Serileştirme ve CPU paketleme maliyetleri göz ardı edilemez.
8. **Ağ homojendir:** Sistemde Linux, Windows, ARM, x86 ve farklı protokoller bir arada çalışır.

## CAP Teoremi ve PACELC Modeli
Eric Brewer tarafından ortaya atılan **CAP Teoremi**, dağıtık veri yönetiminin temel sınırlarını çizer. Bir ağ bölünmesi (Network Partition - P) yaşandığında sistem iki seçenekten birini seçmek zorundadır:
- **CP (Consistency + Partition Tolerance):** Sistem tutarlılığı seçer. Verisi güncel olmayan düğümler cevap vermeyi reddeder; erişilebilirlik feda edilir (örneğin finans ve bankacılık işlemleri).
- **AP (Availability + Partition Tolerance):** Sistem erişilebilirliği seçer. Düğümler cevap vermeye devam eder ancak bazı kullanıcılar birkaç saniye önceki bayat veriyi görebilir (örneğin sosyal medya akışları).

Modern sistemlerde Daniel Abadi'nin **PACELC Modeli** kullanılır: Ağ bölündüğünde (P) Availability mi Consistency mi; sistem normal çalışırken Else (E) Latency (düşük gecikme) mi yoksa Consistency (anlık tutarlılık) mi hedeflenecektir?

## Konsensüs Protokolleri: Raft ve Paxos
Birbirine güvenmeyen ve her an çökebilecek bağımsız sunucuların tek bir gerçek üzerinde anlaşabilmesi için konsensüs algoritmaları geliştirilmiştir:
- **Paxos:** Leslie Lamport tarafından geliştirilen, matematiksel olarak kanıtlanmış ancak pratikte uygulanması son derece karmaşık konsensüs algoritması.
- **Raft:** Paxos'un karmaşıklığını çözmek amacıyla Diego Ongaro ve John Ousterhout tarafından geliştirilen, insan zihnine uygun konsensüs protokolü. Lider seçimi (Leader Election), Günlük Çoğaltma (Log Replication) ve Güvenlik (Safety) durum makineleri üzerine kuruludur (etcd, Kubernetes, Consul gibi dev sistemlerin kalbinde çalışır).
- **Bizans Hata Toleransı (BFT):** Bazı düğümlerin kasıtlı olarak hatalı veya kötü niyetli bilgi yaydığı ortamlarda dahi konsensüsü sağlayan blokzincir protokollerinin temelidir.

## Dağıtık Sistemlerde Zaman Problemi ve Çözümler
Merkezi bir bilgisayarda donanım saati tek bir gerçeği gösterir. Dağıtık sistemlerde ise sunucu saatleri fiziksel sapmalar (clock drift) gösterir ve NTP (Network Time Protocol) milisaniyelik hassasiyet için yetersizdir.
- **Lamport Mantıksal Saatleri (Lamport Timestamps):** Fiziksel zaman yerine "olayların oluş sırasını" tanımlar.
- **Vektör Saatleri (Vector Clocks):** Hangi verinin diğerinin nedeni veya sonucu olduğunu belirleyerek veri çakışmalarını tespit eder.
- **Google TrueTime:** Google Spanner dağıtık veritabanında kullanılan atom saatleri ve GPS antenleri kombinasyonu. Belirsizlik payını birkaç milisaniyeye indirerek küresel ölçekte ACID işlemlerini mümkün kılar.

## Dağıtık Veri ve İşlem Yönetimi: Saga Deseni
Monolitik sistemlerdeki veritabanı işlemleri (ACID transactions), mikroservislerde yerini **Saga Deseni (Saga Pattern)** yaklaşımına bırakır. Uzun süren dağıtık adımlar iki aşamalı kilitler (2PC - Two Phase Commit) ile kilitlenmek yerine; her servisin yerel işlemini yaptığı ve bir hata anında geriye doğru Telafi Edici İşlemlerin (Compensating Transactions) tetiklendiği olay güdümlü mimariler kullanılır.

## Sıkça Sorulanlar

**Distributed ne demek (Türkçe anlamı)?**  
Bilişim terminolojisinde "dağıtık" anlamına gelir. Hesaplama gücünün, bellek alanının veya veritabanının tek bir sunucu yerine ağ üzerinden haberleşen çok sayıda bağımsız makineye paylaştırılmasıdır.

**CAP Teoremi pratikte neyi ifade eder?**  
Ağ bağlantısında bir kopma veya gecikme (bölünme) yaşandığında, sistemin ya en güncel veriyi garanti edip bazı istekleri bekletmesi (Tutarlılık) ya da bayat veri verme pahasına her isteğe anında yanıt dönmesi (Erişilebilirlik) gerektiğini ifade eder.

**Dağıtık sistemlerde Raft konsensüs algoritması neden kullanılır?**  
Ağdaki sunuculardan birkaçı çökse dahi, geriye kalan çoğunluk düğümlerin (Quorum) aralarından yeni bir lider seçmesini ve veritabanı loglarının tüm kümede kayıpsız eşitlenmesini sağlamak için kullanılır.

**İki Aşamalı Taahhüt (2PC) yerine neden Saga deseni tercih edilir?**  
2PC (Two-Phase Commit), dağıtık düğümlerde veritabanı kaynaklarını kilitler ve bir makine yanıt vermediğinde tüm sistemi kilitler. Saga deseni ise asenkron olaylar ve telafi adımları kullanarak sistemin yüksek erişilebilirliğini korur.

## İlgili terimler
- [Cloud Computing](/dictionary/cloud-computing/)
- [Network Stack](/dictionary/network-stack/)
- [Deployment](/dictionary/deployment/)
- [Runtime](/dictionary/runtime/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/distributed/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
