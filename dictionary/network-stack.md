# Network Stack nedir, ne demek ve nasıl çalışır?

*Sözlük · Geliştirme · Son güncelleme: 19 Eylül 2026*

Network Stack (ağ yığını), bir işletim sisteminin veya donanımın ağ üzerinden veri paketlerini iletmesini, yönlendirmesini ve almasını sağlayan donanım sürücüsü, çekirdek (kernel) ve kullanıcı alanı protokol katmanları bütünüdür.

## 1. Katmanlı mimari: OSI 7 Katmanı vs TCP/IP 4 Katmanı

Ağ iletişiminde teorik olarak ISO tarafından tanımlanan **OSI 7 Katmanlı Modeli**, pratikte ise internetin omurgasını oluşturan **TCP/IP Modeli** kullanılır:

- **Uygulama Katmanı (L7):** HTTP/HTTPS, DNS, SSH, gRPC. Verinin kullanıcıya sunulduğu veya üretildiği seviyedir.
- **Taşıma Katmanı (L4):** TCP (güvenilir ve sıralı iletim), UDP (hız odaklı akış) ve QUIC (HTTP/3 tabanı). Protokol veri birimi *Segment* olarak adlandırılır.
- **İnternet / Ağ Katmanı (L3):** IPv4, IPv6, ICMP, BGP. Paketlerin dünya genelinde yönlendirilmesini sağlar. Protokol veri birimi *Paket (Packet)* adını alır.
- **Ağ Arayüzü / Bağlantı Katmanı (L2/L1):** Ethernet (802.3), Wi-Fi (802.11), fiber optik ve bakır hatlar. Protokol veri birimi *Çerçeve (Frame)* olarak tanımlanır.

## 2. Paket kapsülleme (Encapsulation) ve çözme akışı

Bir istemci web sunucusuna istek gönderdiğinde veri yığın boyunca aşağı inerken her katman kendi başlığını ekler:

```
[Kullanıcı Verisi: "GET / HTTP/1.1"]
                   ↓ (Taşıma Katmanı - TCP başlığı eklenir: Portlar, Sıra No)
[TCP Header | Payload]  --> TCP Segment (MSS ~1460 bayt)
                   ↓ (Ağ Katmanı - IP başlığı eklenir: Kaynak/Hedef IP)
[IP Header | TCP Header | Payload]  --> IP Paketi (MTU: 1500 bayt)
                   ↓ (Veri Bağı Katmanı - Ethernet başlığı ve FCS kuyruğu eklenir)
[Ethernet Header | IP Header | TCP Header | Payload | FCS Tail]  --> Ethernet Frame
```

Hedef sunucuya ulaştığında işlem tersine döner (**Decapsulation**); katman katman başlıklar soyulur ve veri sokete teslim edilir.

## 3. Linux çekirdeğinde (Kernel) Network Stack yaşam döngüsü

1. **Donanım ve Ring Buffer:** NIC paketi yakalar ve DMA ile RAM'deki RX Ring Buffer'a kopyalar.
2. **Hard IRQ & SoftIRQ (NAPI):** NIC donanım kesmesi atar; çekirdek CPU kilitlenmesini önlemek için NAPI modunda `ksoftirqd` ile paketleri toplu olarak (polling) işler.
3. **`sk_buff` (Socket Buffer):** Çekirdek her paket için işaretçileri taşıyan `sk_buff` veri yapısını tahsis eder.
4. **Filtreleme ve Yönlendirme:** `nftables` kuralları taranır ve paket yerel sokete aitse TCP durum makinesine devredilir.
5. **Sistem Çağrısı:** Paket soketin alma tamponuna (`recv-Q`) koyulur; uygulama `epoll_wait()` ile veriyi okur.

## 4. Kernel Bypass ve yeni nesil ağ: eBPF / XDP ve DPDK

- **eBPF ve XDP (eXpress Data Path):** Paket henüz `sk_buff` tahsis edilmeden ağ kartı sürücüsü katmanında filtrelenir; Cloudflare gibi devler DDoS saldırılarını çekirdeğe hiç yük bindirmeden burada düşürür.
- **DPDK (Data Plane Development Kit):** Çekirdeği tamamen baypas eder; kullanıcı alanındaki uygulama sıfır kopyayla doğrudan ağ kartı belleğine erişir.
- **QUIC / HTTP/3:** Taşıma katmanında çekirdek TCP yerine kullanıcı alanında çalışan ve Head-of-Line engellemesini aşan UDP tabanlı şifreli protokole geçilmiştir.

*Uluslararası bir kargo operasyonuna benzer: Mektubu yazarsınız (Uygulama), mektubu zarfa koyup iadeli taahhütlü fişi eklersiniz (TCP), zarfı uluslararası adres yazılı bir koliye yerleştirirsiniz (IP), koli bir konteynere yüklenir (Ethernet Frame) ve kargo gemisiyle okyanusu aşar (Fiziksel hat).*

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

- [VPN](https://trescout.com/dictionary/vpn/)
- [Runtime](https://trescout.com/dictionary/runtime/)
- [Memory Management](https://trescout.com/dictionary/memory-management/)
- [Packet Fragmentation](https://trescout.com/dictionary/packet-fragmentation/)
- [API](https://trescout.com/dictionary/api/)

## İlgili araçlar

- [OpenFlux](https://trescout.com/discover/openflux/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/network-stack/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
