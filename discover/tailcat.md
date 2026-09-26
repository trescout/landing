# Tailscale ağlarında güvenli Netcat tünelleme

Tailcat, klasik netcat işlevselliğini Tailscale VPN mesh katmanına taşıyarak kontrol düzlemi veya açık port zorunluluğu olmadan güvenli veri aktarımı sağlar.

- ★ 2.435
- Go
- GitHub Trending · 2026-08-28

## Güncelleme
- 28 Ağustos 2026: Yıldız 2.435, yerleşik WireGuard şifrelemesi ve tsnet kütüphanesi entegrasyonu.

## Ne kazandırır?
- Sıfır port yönlendirme (Port Forwarding): NAT arkasındaki veya güvenlik duvarı kısıtlı cihazlar arasında açık port açmadan doğrudan iletişim.
- Uçtan uca WireGuard şifrelemesi: Tüm TCP ve ham veri aktarımlarını otomatik olarak Tailscale kimlik doğrulaması ve WireGuard ile şifreleme.
- Gömülü tsnet kütüphanesi: İşletim sistemi düzeyinde Tailscale istemcisi kurmaya gerek olmadan bağımsız bir Tailscale düğümü gibi çalışma.
- Hızlı dosya ve boru hattı aktarımı: Standart giriş/çıkış (stdin/stdout) boruları ile tar, gzip veya dd komutlarını makineler arasında akıtma.
- Ağ hata ayıklama ve teşhis: Geleneksel netcat benzeri pratik komutlarla mikroservisler ve uzak makineler arasındaki port erişilebilirliğini test etme.

## Kurulum

**Go ile doğrudan kurulum**

```
go install tailscale.com/cmd/tailcat@latest
```

## Çalıştırma

**Dinleme modunu başlatma ve istemci bağlama**

```
# Sunucu düğümde dinle:
tailcat -l 8080
# İstemci düğümden bağlan:
tailcat hedef-node 8080
```

## Teknik mimari ve çalışma prensibi

Tailcat, geleneksel netcat sözdizimini Tailscale'in kullanıcı alanı ağ kütüphanesi tsnet ile birleştirir:
- tsnet Kullanıcı Alanı Ağı: Kök (root) yetkilerine veya sanal TUN aygıtına ihtiyaç duymadan doğrudan uygulama içinde VPN oturumu oluşturur.
- MagicDNS Düğüm Çözümleme: IP adresleri yerine 'sunucu-node' gibi Tailscale makine adlarıyla anında bağlantı kurabilme.
- DERP Röle Desteği: Doğrudan P2P bağlantının mümkün olmadığı aşırı kısıtlayıcı ağlarda Tailscale DERP röleleri üzerinden veri aktarımını sürdürme.

## Güvenli ağ tünelleme ve uçtan uca senaryolar

Tailcat, geliştiricilere ve sistem yöneticilerine karmaşık VPN yapılandırmalarına gerek kalmadan hızlı çözümler sunar:
- Hızlı Güvenli Dosya Gönderimi: Alıcıda `tailcat -l 9000 > yedek.tar.gz` ve göndericide `tailcat hedef 9000 

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Tailcat aracını kullanarak iki farklı sunucu arasında Tailscale mesh ağı üzerinden şifreli bir dosya transferi tüneli kurmak istiyorum. Sunucu tarafında dinleyiciyi nasıl başlatacağımı, istemci tarafında tar arşivini standart çıktıdan nasıl aktaracağımı ve tsnet kimlik doğrulamasını nasıl yöneteceğimi açıklar mısın?

- **Kimin için:** Sistem yöneticileri, DevOps mühendisleri, ağ uzmanları ve bulut mimarları. 
- **Lisans:** BSD 3-Clause (Esnek açık kaynak lisansı) 
- **Çatı:** Go & Tailscale tsnet Kütüphanesi 
- **Platformlar:** Linux, macOS, Windows 

## Sıkça sorulan sorular
- Makinemde kurulu bir Tailscale istemcisine ihtiyaç var mı? Hayır. Tailcat içinde yerleşik tsnet motoru barındırır; bağımsız bir ikili dosya olarak kendi Tailscale bağlantısını başlatır.
- Trafik gerçekten uçtan uca şifreli midir? Evet. Tailcat, Tailscale ağının çekirdeğindeki WireGuard protokolünü kullanır; veriler cihazlar arasında doğrudan şifrelenir.
- UDP trafiğini destekliyor mu? Tailcat öncelikli olarak TCP akışları ve soket tünelleme için optimize edilmiştir; klasik netcat'in TCP yeteneklerini güvenli hale getirir.
- Bağlantı için kimlik doğrulama nasıl yapılır? Tailcat ilk çalıştırıldığında terminalde bir Tailscale giriş bağlantısı verir veya TAILSCALE_AUTHKEY ortam değişkeni ile otomatik kimlik doğrular.

## Bağlantılar
- [GitHub deposu →](https://github.com/tailscale/tailcat)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-28 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
CLI Açık Kaynak API Framework CI/CD

---
Kaynak: TreScout Keşif · https://trescout.com/discover/tailcat/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
