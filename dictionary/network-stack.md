# Network Stack nedir, ne demek ve nasıl çalışır?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Network Stack (ağ yığını), bir işletim sisteminin veya donanımın ağ üzerinden veri paketlerini iletmesini, yönlendirmesini ve almasını sağlayan donanım sürücüsü, çekirdek (kernel) ve kullanıcı alanı protokol katmanları bütünüdür.

## 1. Katmanlı mimari: OSI 7 Katmanı vs TCP/IP 4 Katmanı

Ağ iletişiminde teorik olarak ISO tarafından tanımlanan **OSI 7 Katmanlı Modeli**, pratikte ise internetin omurgasını oluşturan **TCP/IP Modeli** kullanılır:

```
+---------------------------+-------------------------------+------------------------------+
| OSI 7 Katmanı             | TCP/IP Katmanı                | Protokoller ve Protokol Veri Birimi (PDU)
+---------------------------+-------------------------------+------------------------------+
| 7. Uygulama (Application) |                               | HTTP/HTTPS, DNS, SSH, gRPC   |
| 6. Sunum (Presentation)   | Uygulama (Application)        | TLS/SSL Şifreleme, JSON, Protobuf
| 5. Oturum (Session)       |                               | Sockets, RPC oturumları      | (Veri / Data)
+---------------------------+-------------------------------+------------------------------+
| 4. Taşıma (Transport)     | Taşıma (Transport)            | TCP, UDP, QUIC               | Segment / Datagram
+---------------------------+-------------------------------+------------------------------+
| 3. Ağ (Network)           | İnternet (Network)            | IPv4, IPv6, ICMP, BGP        | Paket (Packet)
+---------------------------+-------------------------------+------------------------------+
| 2. Veri Bağı (Data Link)  | Ağ Arayüzü (Link / Physical)  | Ethernet (802.3), Wi-Fi, ARP | Çerçeve (Frame)
| 1. Fiziksel (Physical)    |                               | Bakır kablo, Fiber, Radyo    | Bit akışı (0 ve 1)
+---------------------------+-------------------------------+------------------------------+
```

## 2. Paket kapsülleme (Encapsulation) ve çözme akışı

Bir istemci web sunucusuna HTTP isteği gönderdiğinde veri yığın boyunca aşağı doğru inerken her katman kendi başlığını (header) ekler:

```
[Kullanıcı Verisi: "GET / HTTP/1.1"]
                   ↓ (Taşıma Katmanı - TCP başlığı eklenir: Kaynak/Hedef Port, Sıra No)
[TCP Header | Payload]  --> TCP Segment (Maks. Segment Boyutu: MSS ~1460 bayt)
                   ↓ (Ağ Katmanı - IP başlığı eklenir: Kaynak/Hedef IP Adresi)
[IP Header | TCP Header | Payload]  --> IP Paketi (MTU: 1500 bayt)
                   ↓ (Veri Bağı Katmanı - Ethernet başlığı ve FCS sağlama toplamı eklenir)
[Ethernet Header | IP Header | TCP Header | Payload | FCS Tail]  --> Ethernet Frame
```

Karşı sunucunun ağ kartı bu bit dizisini yakaladığında işlem tersine döner (**Decapsulation**); katman katman başlıklar soyulur ve saf veri hedef web sunucusunun soketine teslim edilir.

## 3. Linux çekirdeğinde (Kernel) Network Stack yaşam döngüsü

Yüksek başarımlı sunucularda bir ağ paketinin çekirdekteki yolculuğu mikrosaniyeler içinde şu adımlarla gerçekleşir:

1. **Donanım ve Ring Buffer:** Paket fiziksel kablodan NIC'e (Ağ Kartı) ulaşır. NIC, paketi DMA (Direct Memory Access) ile doğrudan RAM'deki dairesel arabelleğe (RX Ring Buffer) yazar.
2. **Hard IRQ & SoftIRQ (NAPI):** NIC bir donanım kesmesi (Interrupt) tetikler. Linux çekirdeği CPU'yu kitlememek için NAPI (New API) moduna geçer ve `ksoftirqd` alt sistemini devreye sokarak paketleri toplu olarak (polling) işler.
3. **`sk_buff` (Socket Buffer):** Çekirdek, her paket için `sk_buff` veri yapısını tahsis eder. Bu yapı paketin tüm katmanlardaki işaretçilerini taşır.
4. **Filtreleme ve Yönlendirme:** `iptables` / `nftables` kuralları ve yönlendirme tablosu (Routing Table) taranır. Paket yerel makineye aitse TCP durum makinesine (`ESTABLISHED`, `TIME_WAIT` vb.) aktarılır.
5. **Soket Kuyruğu ve Sistem Çağrısı:** Paket soketin alma tamponuna (`recv-Q`) koyulur. Uygulama `read()` veya `epoll_wait()` sistem çağrısıyla veriyi kullanıcı alanına (user space) çeker.

## 4. Kernel Bypass ve yeni nesil ağ: eBPF / XDP ve DPDK

Geleneksel Linux çekirdeği saniyede yüz binlerce paketi yönetebilir; ancak 100 Gbps hatlarda çekirdek içerik değiştirme (context switch) ve bellek kopyalama maliyetleri darboğaz yaratır. Bu sorunu aşmak için iki modern teknoloji doğmuştur:

- **eBPF ve XDP (eXpress Data Path):** Paket daha `sk_buff` haline gelmeden doğrudan ağ kartı sürücüsü katmanında eBPF programlarıyla taranır. Cloudflare gibi devler, devasa DDoS saldırılarını çekirdeğe hiç yük bindirmeden bu katmanda düşürür (Drop).
- **DPDK (Data Plane Development Kit):** Linux çekirdeğini tamamen baypas eder. Kullanıcı alanındaki yazılım, sıfır kopyayla (Zero-Copy) doğrudan ağ kartının belleğini okur.
- **QUIC / HTTP/3:** Taşıma katmanında çekirdeğe bağımlı TCP yerine, kullanıcı alanında çalışan ve Head-of-Line engellemesini aşan UDP tabanlı şifreli protokole geçiş yapılmıştır.

## Bir benzetmeyle

Uluslararası bir kargo operasyonuna benzer: Mektubu yazarsınız (Uygulama), mektubu zarfa koyup iadeli taahhütlü fişi eklersiniz (TCP), zarfı uluslararası adres yazılı bir koliye yerleştirirsiniz (IP), koli bir konteynere yüklenir (Ethernet Frame) ve kargo gemisiyle okyanusu aşar (Fiziksel hat).

## Sıkça sorulanlar

**Network stack ne demek, Türkçe karşılığı nedir?**  
Türkçede "ağ yığını" veya "protokol yığını" olarak adlandırılır. Bir bilgisayarın ağ üzerinden iletişim kurmasını sağlayan, birbirinin üzerine binen donanımsal ve yazılımsal kurallar hiyerarşisidir.

**TCP ile UDP arasındaki temel fark network stack içinde nerededir?**  
İletim katmanında (Transport Layer / L4) yer alır. TCP paketlerin eksiksiz ve sıralı ulaştığını onay mekanizmasıyla (ACK) garanti eder; UDP ise onay beklemeden en yüksek hızla paket fırlatır.

**MTU (Maximum Transmission Unit) nedir?**  
Bir ağ arayüzünün parçalanma (fragmentation) olmadan tek bir çerçevede taşıyabileceği en büyük paket boyutudur. Standart Ethernet için MTU değeri 1500 bayttır.

**Kernel Bypass mimarisi neden kullanılır?**  
100 Gbps gibi aşırı yüksek veri hacimlerinde Linux çekirdeğinin kesme ve bellek kopyalama maliyetlerini bertaraf etmek; DPDK ve eBPF/XDP ile paketleri doğrudan donanım seviyesinde sıfır gecikmeyle işlemek için kullanılır.

## İlgili terimler

- [Networking Stack](/dictionary/networking-stack/)
- [Runtime](/dictionary/runtime/)
- [Memory Management](/dictionary/memory-management/)
- [Packet Fragmentation](/dictionary/packet-fragmentation/)
- [API](/dictionary/api/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/network-stack/  
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
