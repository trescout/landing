# Self-hosted nedir, ne demek Türkçe?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Self-hosted (öz barındırma veya yerel barındırma), bir yazılımı veya dijital servisi üçüncü taraf bir bulut sağlayıcısı (SaaS) yerine, tamamen kendi kontrolünüzdeki fiziksel sunucuda, sanal sunucuda (VPS) veya yerel bilgisayarda çalıştırmaktır.

## Tanım ve Türkçe Anlamı
"Self-hosted" kavramı Türkçede en yaygın karşılığıyla **öz barındırma** veya **kendi sunucusunda barındırma** olarak ifade edilir. Geleneksel SaaS (Hizmet Olarak Yazılım) modellerinde verileriniz ve yazılım yabancı şirketlerin altyapılarında tutulurken, self-hosted mimaride veritabanı, depolama, yapılandırma ve yedekleme dahil olmak üzere tüm altyapı sizin mülkiyetinizdedir.

## Bir benzetmeyle
Bir otelde oda kiralamak (SaaS bulut hizmetleri) yerine kendi arsanıza ev inşa etmek ve anahtarını yalnızca cebinizde taşımak gibidir. Kimse kurallarınızı değiştiremez, gizliliğinizi ihlal edemez veya hizmeti ansızın kapatamaz; ancak tesisat, temizlik ve bakım işleri de tamamen size aittir.

## Neden Tercih Edilir? (Avantajları)
- **Tam Veri Gizliliği ve Egemenliği:** Hassas kişisel veya kurumsal verileriniz üçüncü taraf şirketlerin sunucularına iletilmez, analiz edilmez veya yapay zekâ eğitimi için kullanılmaz.
- **Maliyet Tasarrufu:** Kullanıcı başına aylık yinelenen abonelik ücretleri ödemek yerine, sabit bir donanım veya uygun fiyatlı bir VPS ile sınırsız kullanıcı ve veri yönetimi sağlanabilir.
- **Bağımsızlık (Vendor Lock-in Önleme):** Şirketlerin fiyat artışlarına, arayüz değişikliklerine veya aniden hizmeti durdurmalarına karşı tam koruma sağlar.
- **Özelleştirme:** Çoğunlukla açık kaynaklı projeler kullanıldığından, kaynak koduna müdahale edilebilir ve kurumsal ihtiyaçlara göre uyarlanabilir.

## Nasıl çalışır ve kurulur?
1. **Donanım/Sunucu Seçimi:** Evdeki bir Raspberry Pi, mini PC veya bir bulut sağlayıcısından kiralanan sanal sunucu (VPS) işletim sistemiyle (genellikle Ubuntu/Debian) hazırlanır.
2. **Konteynerleştirme (Docker):** Yazılımlar Docker ve Docker Compose dosyalarıyla izole konteynerler halinde saniyeler içinde kurulur.
3. **Ağ ve Güvenlik:** Dış erişim için Reverse Proxy (Nginx, Traefik, Caddy) ve SSL şifrelemesi (Let's Encrypt) yapılandırılır veya Tailscale/WireGuard gibi VPN araçlarıyla yalnızca özel ağa açılır.

## Nerede kullanılır?
- **Kişisel Bulut ve Fotoğraf:** Nextcloud, Immich, OwnCloud
- **Şifre Yönetimi:** Vaultwarden (Bitwarden uyumlu)
- **Akıllı Ev ve Otomasyon:** Home Assistant, Node-RED
- **Yerel Yapay Zekâ:** Ollama, Open WebUI, LocalAI
- **Medya ve Akış:** Plex, Jellyfin

## Sık karıştırılanlar
Geleneksel web hosting hizmetleriyle karıştırılmamalıdır. Standart web hosting paketleri genellikle sadece basit web siteleri barındırmak için tasarlanmıştır. Self-hosted ise tam kök (root) erişimi olan ortamlarda veritabanından arka uç motorlarına kadar tüm servisleri yönetmeyi kapsar.

## Sıkça sorulanlar

**Self-hosted Türkçe karşılığı nedir?**  
Türkçede en yaygın olarak "öz barındırma", "kendi sunucusunda barındırma" veya "yerel barındırma" terimleriyle ifade edilir.

**Teknik bilgi gerektirir mi?**  
Evet, kurulum ve sunucu bakımı için temel Linux komutları, Docker ve ağ bilgisi faydalıdır; ancak CasaOS ve Umbrel gibi modern arayüzler tek tıkla mağazadan uygulama kurma kolaylığı sunmaktadır.

**Self-hosted daha mı güvenlidir?**  
Veri gizliliği açısından en üst düzey çözümdür çünkü verileriniz dışarı sızmaz; fakat güvenlik duvarı, port yönlendirme, güçlü parolalar ve düzenli güncellemeler tamamen sizin sorumluluğunuzdadır.

**Evdeki eski bir bilgisayarla self-hosted yapılabilir mi?**  
Evet; eski bir dizüstü bilgisayar, Raspberry Pi veya mini PC kullanarak evinizde (Home Lab ortamında) kendi bulut depolamanızı veya medya sunucunuzu rahatlıkla çalıştırabilirsiniz.

## İlgili terimler
- [Self-hosting](/dictionary/self-hosting/)
- [Open Source](/dictionary/open-source/)
- [Offline](/dictionary/offline/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/self-hosted/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
