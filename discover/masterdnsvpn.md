# yapay zekâ ile sansürleri aşın

MasterDnsVPN, sansür engellerini aşmak için geliştirilen ve düşük yükle çalışan bir alan adı sistemi tünelleme (DNS tunneling) sanal özel ağ (VPN) çözümüdür. Go diliyle yazılan araç, veri iletiminde yüksek paket kaybı kararlılığı ve çözümleyici yük dengeleme (resolver load balancing) özellikleri sunar.

- ★ 6.870
- Go
- GitHub Trending · 2026-06-11

## Güncelleme
- 2 Ağustos 2026: Yıldız 5.411 → 6.870, son sürüm v2026.06.13.234407-7de2476 (13 Haziran 2026).

## Ne kazandırır?
- DNS tünelleme yöntemiyle sansürlü ağlarda veri iletimi sağlar.
- Düşük paket kaybı ve yüksek hız için çoklu yol ve yük dengeleme sunar.
- Kısıtlı ağ koşullarında bile kararlı bağlantı için optimize edilmiştir.

## Kurulum

**Otomatik Sunucu Kurulumu**

```
bash 
**Docker ile Çalıştırma**

```
docker run -d \
--name masterdnsvpn \
--restart unless-stopped \
-e DOMAIN=v.example.com \
-v $(pwd)/data:/data \
-p 53:53/tcp \
-p 53:53/udp \
ghcr.io/masterking32/masterdnsvpn:latest
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
MasterDnsVPN aracını kullanarak sansürlü bir ağda DNS tünelleme üzerinden güvenli bağlantı kurmak istiyorum. Paylaşılan otomatik kurulum betiğini kullanarak sunucu tarafını nasıl yapılandırabilirim ve istemci tarafında bağlantıyı sağlamak için hangi temel adımları izlemeliyim? Lütfen kurulum sürecinde dikkat etmem gereken ağ gereksinimlerini ve Docker üzerinden çalıştırma yöntemini detaylandır.

- **Kimin için:** Kısıtlı ağ koşullarında yüksek kararlılıkla internet erişimi sağlamak isteyen araştırmacılar ve ileri düzey kullanıcılar içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/masterking32/MasterDnsVPN)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-11 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
DNS Tunneling Resolver Load Balancing VPN Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/masterdnsvpn/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
