# Self-hosted nedir, ne demek Türkçe?

**Kategori:** Geliştirme  
**Son güncelleme:** 2026-09-19

Self-hosted (öz barındırma veya yerel barındırma), bir yazılımı, veritabanını veya dijital servisi üçüncü taraf bir bulut şirketine (SaaS) bağımlı olmadan, tamamen kendi kontrolünüzdeki fiziksel sunucuda, yerel donanımda (homelab) veya sanal özel sunucuda (VPS) çalıştırma ve yönetme mimarisidir.

## Etimoloji ve Türkçe Karşılığı
İngilizce kökenli *self* (kendi) ve *host* (ev sahipliği yapmak, barındırmak) sözcüklerinin birleşiminden oluşan terim, Türkçede **öz barındırma**, **kendi sunucusunda barındırma** veya **yerel barındırma** olarak adlandırılır.

Geleneksel SaaS (Hizmet Olarak Yazılım) modelinde kullanıcılar yalnızca birer kiracıdır; veriler ve altyapı yabancı şirketlerin veri merkezlerinde kilitlidir. Self-hosted yaklaşımında ise sistem yöneticisi ve mülk sahibi doğrudan sizsinizdir: Veritabanı, depolama diskleri, ağ kuralları ve şifreleme anahtarları tamamen sizin fiziksel veya mantıksal mülkiyetinizdedir.

## 1. SaaS Yorgunluğundan Bulut Geri Dönüşüne (Cloud Repatriation)
Son on yılda her yazılımın aylık yinelenen abonelik (subscription) modeline geçmesi, bireyler ve kurumlar nezdinde ciddi bir abonelik yorgunluğu yaratmıştır:
- **Maliyet Çıkmazı:** Kullanıcı başına aylık 10-50 dolar ödenen SaaS araçları, ekip büyüdükçe yüz binlerce dolarlık kontrolsüz maliyetlere dönüşür. Nitekim 37signals (Basecamp) gibi küresel teknoloji liderlerinin buluttan çıkıp kendi donanımlarına dönmesi (**Cloud Repatriation**), self-hosted yaklaşımının ekonomik rasyonelliğini kanıtlamıştır.
- **Veri Egemenliği ve Gizlilik:** Şirketlerin kullanım koşullarını tek taraflı değiştirmesi, verileri yapay zekâ modellerine eğitim verisi yapması veya hesapları aniden kapatması riskine karşı en güçlü kalkan öz barındırmadır. KVKK ve GDPR standartlarına göre hassas müşteri verilerini kendi sınırlarınızda tutmak yasal uyumluluğu da güvenceye alır.

## 2. Donanım Mimarisi ve Homelab Ekosistemi
Self-hosted dünyası günümüzde pahalı kurumsal sunucu kabinlerinden çıkıp oturma odalarına ve ev laboratuvarlarına (Homelab) inmiştir:
- **Düşük Güç Tüketen Donanımlar:** Intel N100 tabanlı mini PC'ler, Raspberry Pi 5 veya eski dizüstü bilgisayarlar; yılda yalnızca birkaç yüz liralık elektrik tüketimiyle 7/24 kesintisiz çalışabilir.
- **Depolama ve Veri Güvenliği (ZFS & RAID):** Birden fazla sabit diskin aynalandığı RAID dizilimleri ve ZFS dosya sistemi, bir disk fiziksel olarak yansa dahi veri kaybını imkânsız kılar. TrueNAS ve unRAID gibi işletim sistemleri bu donanımları profesyonel depolama havuzlarına dönüştürür.
- **Bulut VPS Alternatifi:** Evinde donanım barındırmak istemeyenler için Hetzner veya OVH gibi sağlayıcılardan kiralanan ucuz sanal sunucular (VPS), self-hosted özgürlüğünü bulut güvenilirliğiyle birleştirir.

## 3. Modern Self-Hosted Yazılım Yığını
Eski dönemlerde Linux üzerinde elle PHP ve MySQL derlemek gereken günler geride kalmıştır. Modern mimari üç sütun üzerine kuruludur:
- **Konteynerleştirme (Docker & Docker Compose):** Her servis (Nextcloud, Vaultwarden, Jellyfin) kendi kütüphaneleriyle izole bir Docker konteyneri içinde çalışır. `docker-compose.yml` dosyası sayesinde onlarca servis tek bir komutla ayağa kaldırılır.
- **Tersine Vekil Sunucu (Reverse Proxy):** Nginx, Traefik veya Caddy; gelen web isteklerini karşılar, alan adlarını doğru konteynere yönlendirir ve Let's Encrypt üzerinden ücretsiz SSL/TLS sertifikalarını otomatik yeniler.
- **Güvenli Ağ Tünelleri (Zero-Trust & Mesh VPN):** Ev modeminde dışarıya port açmak siber saldırılara davetiye çıkarır. Modern self-hosted kullanıcıları Tailscale, WireGuard veya Cloudflare Tunnels kullanarak sistemlerini dış dünyaya kapalı, yalnızca yetkili cihazlarına açık bir iç ağda (Mesh VPN) güvenle çalıştırır.

## 4. Popüler Self-Hosted Çözümleri
- **Kişisel Bulut ve Fotoğraf:** Google Drive yerine Nextcloud, Google Photos yerine yapay zekâ yüz tanımalı Immich.
- **Şifre Yönetimi:** 1Password yerine açık kaynaklı ve hafif Vaultwarden (Bitwarden uyumlu).
- **Medya Akışı:** Netflix ve Spotify yerine kendi arşivinizi yönettiğiniz Jellyfin ve Plex.
- **Yerel Yapay Zekâ:** ChatGPT aboneliği yerine kendi ekran kartınızda çalışan Ollama ve Open WebUI.
- **Akıllı Ev:** Bulut bağımlı üreticiler yerine tamamen yerel çalışan Home Assistant.

## 5. Sorumluluklar: 3-2-1 Yedekleme Kuralı
Özgürlük sorumluluk getirir. Bir donanım arızasında arkanızda destek bileti açabileceğiniz bir bulut şirketi yoktur. Bu nedenle **3-2-1 Yedekleme Kuralı** zorunludur:
- Verilerinizin en az **3** kopyasını tutun.
- Bu kopyaları **2** farklı fiziksel ortamda (örneğin dahili disk ve harici USB) saklayın.
- Kopyalardan en az **1** tanesini yangın ve hırsızlığa karşı farklı bir fiziksel konumda (şifreli uzak sunucu veya harici depolama) barındırın.

## Sıkça Sorulanlar

**Self-hosted nedir ve Türkçe karşılığı ne demek?**  
İngilizce kökenli bir kavram olup Türkçede 'öz barındırma' veya 'kendi sunucusunda barındırma' anlamına gelir. Yazılımların üçüncü taraf bulut sağlayıcıları yerine kullanıcının kendi donanımında veya sunucusunda çalıştırılmasıdır.

**Self-hosted kurmak için ileri düzey kodlama bilmek gerekir mi?**  
Hayır, kod yazmanız gerekmez. Temel Linux komut satırı bilgisi ve Docker mantığını anlamak yeterlidir. Ayrıca CasaOS ve Umbrel gibi modern sistemler uygulama mağazası mantığıyla tek tıkla kurulum imkânı sunar.

**Ev sunucusunda (Homelab) self-hosted çalıştırmak güvenli midir?**  
Doğru yapılandırıldığında ticari bulutlardan daha güvenlidir çünkü verileriniz şirketlerle paylaşılmaz. Ancak modeme doğrudan port açmak yerine Tailscale gibi VPN tünelleri kullanmak ve güvenlik güncellemelerini aksatmamak şarttır.

**3-2-1 yedekleme kuralı neden hayati önem taşır?**  
Self-hosted sistemlerde donanım bozulduğunda veriyi kurtaracak bir müşteri hizmetleri yoktur. 3 kopya, 2 farklı ortam ve 1 harici lokasyon kuralı donanım yangın veya arızalarında veri kaybını önler.

## İlgili terimler
- [Local](/dictionary/local/)
- [Offline](/dictionary/offline/)
- [Open Source](/dictionary/open-source/)
- [Deployment](/dictionary/deployment/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/self-hosted/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
