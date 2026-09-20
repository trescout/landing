# Kişisel bulut sunucunuzu yönetin

CasaOS, ev sunucuları, mini PC'ler ve Raspberry Pi cihazlarında Docker tabanlı uygulamaları tek tıkla yönetmeyi sağlayan açık kaynaklı, hafif ve zarif bir kişisel bulut işletim sistemidir. Go diliyle geliştirilen platform, karmaşık terminal komutlarına ihtiyaç duymadan kendi dijital egemenliğinizi kurmanıza olanak tanır.

- ★ 36.953
- Go
- GitHub Trending · 2026-06-26

## Güncelleme
- 2 Ağustos 2026: Yıldız 34.992 → 36.953, son sürüm v0.4.15 (19 Aralık 2024).

## Ne kazandırır?
- Tek tıkla zengin uygulama mağazası: Nextcloud, Plex, Jellyfin, AdGuard Home, qBittorrent, Home Assistant ve 100'den fazla popüler kendi kendine barındırılan (self-hosted) servisi saniyeler içinde kurun.
- Zarif ve sezgisel web kontrol paneli: CPU, RAM yükü, disk doluluk oranları, ağ etkinliği ve çalışan konteynerleri şık widget kartları üzerinden canlı takip edin.
- Görsel depolama ve dosya yönetimi: Harici sabit diskleri ve USB sürücüleri otomatik olarak bağlayın, klasörlerinizi yerel ağda Samba (SMB) protokolüyle Windows/Mac cihazlarınızla paylaşın.
- Özel Docker Compose desteği: Resmî mağazada bulunmayan herhangi bir Docker Compose dosyasını web arayüzüne yapıştırarak özel konteynerlerinizi zahmetsizce hayata geçirin.
- Hafif Go çekirdeği ve sıfır sistem yükü: Arka planda minimum bellek tüketerek en mütevazı Raspberry Pi 4/5 veya eski dizüstü bilgisayarlarda dahi akıcı performans sergiler.

## Kurulum

**Kurulum komutu**

```
curl -fsSL https://get.casaos.io | sudo bash
```

## Çalıştırma

**Güncelleme komutu**

```
curl -fsSL https://get.casaos.io/update | sudo bash
```

## Teknik mimari ve çalışma prensibi

CasaOS sıfırdan bir Linux çekirdeği sunmak yerine, mevcut Debian, Ubuntu veya Raspberry Pi OS dağıtımınız üzerinde modern bir Docker orkestrasyon katmanı olarak görev yapar. Bu yaklaşım donanım sürücüsü uyumluluğunu korurken işletim sistemini modüler bir mikroservis yapısıyla yönetir:
- Go mikroservis mimarisi: CasaOS Çekirdeği (CasaOS-Gateway, MessageBus, LocalStorage ve UserService) birbirinden bağımsız çalışan hafif Go servislerinden oluşur. Servisler arası iletişim REST ve WebSocket üzerinden gerçekleşir.
- Konteyner yaşam döngüsü soyutlaması: Docker daemon ile doğrudan iletişim kurarak port çakışmalarını otomatik tespit eder, ortam değişkenlerini ve kalıcı disk bağlama (volume mount) yollarını kullanıcı dostu formlara dönüştürür.
- ZimaOS ve IceWhale ekosistemi: ZimaBoard ve ZimaBlade donanımlarının üreticisi IceWhale Technology tarafından desteklenen proje, yerel bulut donanımlarıyla tam uyum sağlar.
- Akıllı disk birleştirme: Farklı boyutlardaki sabit diskleri tek bir mantıksal depolama havuzunda birleştirerek ev medyası ve yedekleme için esnek alan yaratır.

## Adım adım kendi ev sunucunuzu kurma rehberi

Eski bir bilgisayarı veya mini PC'yi tam teşekküllü bir kişisel buluta dönüştürmek için şu temel adımları izleyebilirsiniz:
- Temel Linux kurulumu: Cihazınıza temiz bir Ubuntu Server veya Debian minimal kurun ve yerel ağınıza Ethernet kablosu ile bağlayın.
- Tek satırlık CasaOS kurulumu: Terminal üzerinden resmî kurulum betiğini çalıştırın; betik Docker ve bağımlılıkları otomatik olarak yapılandırır.
- Tarayıcıdan arayüze erişim: Ağdaki herhangi bir bilgisayardan sunucunuzun IP adresini (örneğin http://192.168.1.100 ) tarayıcınıza yazarak ilk yönetici hesabınızı oluşturun.
- Uygulamaları devreye alma: App Store sekmesine girerek Nextcloud ile kişisel bulutunuzu, Jellyfin ile film/dizi kütüphanenizi tek tıkla yükleyin.

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Kişisel ev sunucumda CasaOS kurulu. Evimdeki tüm cihazlar için AdGuard Home (reklam engelleyici), Jellyfin (medya yayını) ve Tailscale (ev dışından güvenli erişim) servislerini kurup yapılandırmak istiyorum. CasaOS web panelinden özel Docker Compose veya uygulama mağazası üzerinden bu servisleri nasıl kuracağımı, disk paylaşımını nasıl ayarlayacağımı adım adım açıklar mısın?

- **Kimin için:** Ev sunucusu (Homelab) veya kişisel bulut kurmak isteyen, terminal karmaşasından kaçınıp Docker uygulamalarını tek tıkla yönetmeyi hedefleyen kullanıcılar içindir. 
- **Lisans:** Apache-2.0 (Geniş özgürlük sunan açık kaynak lisansı) 
- **Geliştirici:** IceWhale Technology ve Açık Kaynak Topluluğu 
- **Desteklenen Sistemler:** Ubuntu, Debian, Raspberry Pi OS, Armbian (x86_64, aarch64, armv7) 

## Sıkça sorulan sorular
- CasaOS mevcut Linux işletim sistemimi veya verilerimi siler mi? Hayır. CasaOS mevcut işletim sisteminizi silmez; bir masaüstü ve Docker yönetim katmanı olarak üzerine kurulur. Disklerinizdeki mevcut dosyalar korunur ve panel üzerinden erişilebilir hale gelir.
- Ev dışındayken CasaOS sunucuma nasıl güvenli erişebilirim? Güvensiz port yönlendirme (port forwarding) yapmak yerine, CasaOS üzerine tek tıkla Tailscale veya WireGuard kurabilirsiniz. Bu sayede dünyanın her yerinden şifreli bir VPN tüneliyle sanki ev ağınızdaymış gibi panoya ulaşabilirsiniz.
- CasaOS ile TrueNAS veya Unraid arasındaki fark nedir? TrueNAS ve Unraid derin depolama yönetimi ve RAID yapılandırmalarına odaklanan bağımsız işletim sistemleridir. CasaOS ise hafif, kullanımı son derece kolay ve uygulama merkezli bir ev bulutu deneyimi sunar.
- Elektrik kesintisinden sonra kurulu uygulamalar otomatik başlar mı? Evet. CasaOS üzerindeki tüm Docker konteynerleri varsayılan olarak restart: unless-stopped politikasıyla başlatılır. Sunucunuz yeniden açıldığında tüm servisleriniz kendiliğinden kaldığı yerden çalışmaya devam eder.

## Bağlantılar
- [GitHub deposu →](https://github.com/IceWhaleTech/CasaOS)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-26 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Self-Hosted Offline Open Source Local

---
Kaynak: TreScout Keşif · https://trescout.com/discover/casaos/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
