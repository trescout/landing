# Network Stack nedir, ne demek?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Network Stack (ağ yığını), bir bilgisayarın veya sunucunun ağ üzerinden diğer cihazlarla veri alışverişi yapmasını sağlayan yazılım ve donanım katmanları bütünüdür.

## Tanım ve katmanlı mimari
Ağ Yığını (Network Stack veya Networking Stack), bir verinin bir cihazdan çıkıp internet üzerinden hedef cihaza ulaşmasını ve karşı tarafta eksiksiz çözümlenmesini yöneten kurallar (protokoller) hiyerarşisidir. İşletim sistemi çekirdeğinde (kernel) yer alan bu katmanlar, donanım kartları ile tarayıcı veya mobil uygulamalar arasında köprü kurar. Günümüz internetinin omurgasını oluşturan standart model TCP/IP yığınıdır:
1. **Uygulama Katmanı (Application):** HTTP, HTTPS, WebSocket, DNS gibi kullanıcıyla doğrudan etkileşen protokoller.
2. **İletim Katmanı (Transport):** Verinin güvenle teslim edilmesini sağlayan TCP veya hızlı iletim sunan UDP.
3. **İnternet Katmanı (Network):** Paketlerin dünya genelinde yönlendirilmesini (routing) sağlayan IP (IPv4/IPv6).
4. **Bağlantı Katmanı (Link):** Ethernet, Wi-Fi gibi fiziksel sinyaller ve donanım sürücüleri.

## Bir benzetmeyle
Yurt dışına kırılabilir bir eşya gönderme sürecine benzer: Eşyayı kutulamak (veri paketleme), üzerine adres etiketi yapıştırmak (IP adresi), taahhütlü kargoya vermek (TCP garantisi) ve kargo uçağının havalanması (fiziksel ağ) aşamalarının her biri bir yığın katmanıdır.

## Nasıl çalışır?
Bir web sitesine tıkladığınızda işletim sistemi isteği network stack boyunca aşağı indirir (kapsülleme - encapsulation). Veri ağ kablosundan baytlar halinde karşı sunucuya ulaştığında ise tam tersine yığın boyunca yukarı çıkartılarak hedef sunucu yazılımına teslim edilir.

## Nerede kullanılır?
Tüm işletim sistemlerinde (Linux, macOS, Windows), bulut veri merkezlerinde, akıllı telefonlarda ve ağ yönlendiricilerinde (router/switch) temel iletişim bileşenidir.

## Sık karıştırılanlar
Sadece fiziksel ağ kartı (NIC) veya modem donanımı ile karıştırılmamalıdır; network stack donanımı kontrol eden ve paket trafiğini yöneten karmaşık bir çekirdek yazılım mimarisidir.

## Sıkça sorulanlar

**Network stack ne demek ve Türkçe karşılığı nedir?**  
Türkçede 'ağ yığını' veya 'protokol yığını' olarak adlandırılır. Birbirinin üzerine binen ve sıra ile çalışan ağ kuralları bütünüdür.

**TCP ile UDP arasındaki fark network stack içinde nerede yer alır?**  
İletim katmanında (Transport Layer) yer alır. TCP paketlerin ulaştığını teyit eder ve kayıpları yeniden gönderir (web, e-posta); UDP ise hız öncelikli akış sağlar (canlı yayın, oyun).

**Linux çekirdeğindeki (kernel) network stack neden performans için kritiktir?**  
Yüksek trafikli sunucularda saniyede milyonlarca paketi işleyebilmek için soket arabellekleri, bağlantı kuyrukları ve eBPF gibi teknolojiler doğrudan network stack üzerinde optimize edilir.

## İlgili terimler
- [Networking Stack](/dictionary/networking-stack/)
- [API](/dictionary/api/)
- [Packet Fragmentation](/dictionary/packet-fragmentation/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/network-stack/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
