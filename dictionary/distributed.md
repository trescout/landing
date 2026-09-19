# Distributed ne demek, nedir?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Distributed (dağıtık), bilgi işlemde donanım veya yazılım bileşenlerinin tek bir merkez yerine ağ üzerinden birbirine bağlı birden fazla bağımsız bilgisayara (düğüme) paylaştırılarak tek bir bütün sistem gibi çalışmasıdır.

## Tanım ve Türkçe Anlamı
"Distributed" kelimesi Türkçede **dağıtık** anlamına gelir. Yazılım ve sistem mühendisliğinde **dağıtık sistemler** (distributed systems); fiziksel olarak farklı konumlarda bulunabilen, birbirleriyle yerel ağ veya internet üzerinden mesajlaşarak haberleşen ve son kullanıcıya sanki tek bir güçlü bilgisayarmış gibi hizmet veren düğümler (node) bütünüdür.

## Bir benzetmeyle
Devasa bir kütüphanenin tüm kitaplarını tek bir memurun düzenlemesi yerine; onlarca memurun farklı koridorları paylaşarak aynı anda çalışması ve aranan bir kitabı ortak bir katalog üzerinden saniyeler içinde el birliğiyle bulup getirmesine benzer.

## Neden Dağıtık Sistemler Kullanılır?
- **Yatay Ölçeklenebilirlik (Horizontal Scaling):** Tek bir sunucunun işlemcisini ve belleğini yükseltmek (dikey ölçekleme) hızla fiziksel ve mali sınırlara ulaşır. Dağıtık mimaride sisteme yeni ucuz sunucular ekleyerek kapasite sınırsızca artırılabilir.
- **Yüksek Erişilebilirlik ve Hata Toleransı:** Bir sunucu bozulsa, elektriği kesilse veya veri merkezinde yangın çıksa bile diğer düğümler yükü devralır ve hizmet kesintisiz sürer (SPOF - Tek Hata Noktası oluşmaz).
- **Düşük Gecikme (Latency):** Veriler kullanıcılara coğrafi olarak en yakın sunucularda barındırılarak (CDN, uç bilişim) küresel çapta anlık yanıt süreleri elde edilir.

## Temel Dağıtık Sistem Kavramları
- **CAP Teoremi:** Bir dağıtık sistemin ağ bölünmesi (Network Partition) anında ya Tutarlılık (Consistency) ya da Erişilebilirlik (Availability) arasında bir tercih yapmak zorunda olduğunu açıklar.
- **Konsensüs Algoritmaları (Raft, Paxos):** Ağdaki bağımsız sunucuların hangi verinin güncel olduğu ve kimin lider düğüm seçileceği konusunda anlaşmasını sağlayan matematiksel protokollerdir.
- **Nihai Tutarlılık (Eventual Consistency):** Bir düğümde yapılan güncellemenin diğer tüm düğümlere belirli bir gecikmeyle yayılması ve zamanla tüm sistemin tutarlı hale gelmesi prensibidir.

## Nerede ve Hangi Teknolojilerde Kullanılır?
- **Dağıtık Veritabanları:** Apache Cassandra, CockroachDB, MongoDB, Elasticsearch
- **Mesaj Kuyrukları ve Veri Akışı:** Apache Kafka, RabbitMQ, Apache Flink
- **Konteyner Orkestrasyonu:** Kubernetes, etcd, Nomad
- **Sürüm Kontrol Sistemleri:** Git (her klonun tam bir repo kopyası taşıması)

## Sık karıştırılanlar
Merkezi (Centralized) mimarilerle karıştırılmamalıdır. Merkezi mimaride tüm işlemler ve veriler tek bir sunucu havuzunda toplanır; bu sunucu çöktüğünde tüm sistem durur. Dağıtık sistemlerde ise sorumluluk ve veri parçaları bağımsız düğümler arasında paylaşılmıştır.

## Sıkça sorulanlar

**Distributed ne demek (Türkçe anlamı)?**  
Bilişim terminolojisinde "dağıtık" anlamına gelir; işlemlerin, verilerin veya hesaplama gücünün tek bir makine yerine ağa bağlı birden çok bilgisayara paylaştırılmasıdır.

**CAP Teoremi ne anlama gelir?**  
Dağıtık bir sistemin aynı anda Tutarlılık (C), Erişilebilirlik (A) ve Bölünme Toleransı (P) özelliklerinin üçünü birden mükemmel sağlayamayacağını, ağ kopması durumunda C veya A arasında seçim yapılması gerektiğini ifade eder.

**Git neden dağıtık bir sistemdir?**  
Git'te merkezi bir sunucu zorunlu değildir. Projeyi klonlayan her geliştirici, kod tabanının tüm commit geçmişini ve veritabanını kendi bilgisayarında yerel bir kopya olarak taşır.

**Dağıtık sistemlerin en zor tarafı nedir?**  
Ağ gecikmeleri, sunucular arasındaki saat senkronizasyonu farklılıkları, veri tutarsızlıkları ve kısmi çökme (partial failure) durumlarını yönetmektir.

## İlgili terimler
- [Cloud Native](/dictionary/cloud-native/)
- [Service Mesh](/dictionary/service-mesh/)
- [Multi-tenancy](/dictionary/multi-tenancy/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/distributed/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
