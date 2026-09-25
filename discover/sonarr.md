# Dizi arşivinizi ve medya akışınızı otomatik yönetin

Sonarr, Usenet (haber grupları) ve BitTorrent kullanıcıları için geliştirilmiş açık kaynaklı, akıllı bir kişisel video kaydedici (PVR) ve medya otomasyon yöneticisidir. C# ve .NET altyapısıyla geliştirilen platform; yeni yayınlanan bölümleri takip eder, indirme istemcileriyle iletişim kurar, dosyaları yeniden adlandırıp Plex ve Jellyfin kütüphanelerine düzenli şekilde aktarır.

- ★ 16.274
- C#
- GitHub Trending · 2026-09-12

## Güncelleme
- 17 Eylül 2026: Yıldız 16.274, son kararlı sürüm v4.0.20.3014 (.NET 8 çalışma zamanı optimizasyonları ve özel biçim puanlama güncellemeleri).

## Ne kazandırır?
- Otomatik bölüm takibi ve takvim: Favori dizilerinizin yayın tarihlerini entegre takvim üzerinden izleyip yeni bölümler çıktığı anda otomatik indirme.
- Akıllı kalite yükseltme (Quality Upgrades): Düşük çözünürlüklü bölümleri (720p HDTV) zamanla daha yüksek kaliteli sürümlerle (1080p / 4K HDR WEB-DL) kendiliğinden değiştirme.
- Sabit bağlantı (Hardlinking) desteği: İndirilen dosyaları çoğaltmadan aynı disk üzerinde hem torrent paylaşımında tutma hem de medya sunucusuna sunma.
- Geniş istemci ve indeksleyici entegrasyonu: qBittorrent, Transmission, Deluge, SABnzbd ve NZBGet ile sıfır sürtünmeyle çalışma.
- Özelleştirilebilir dosya adlandırma: Bölüm dosyalarını medya sunucularının (Plex, Jellyfin, Emby) standartlarına göre otomatik adlandırma ve klasörleme.

## Kurulum seçenekleri: Docker ve yerel servis

**Docker Compose ile kurulum**

```yaml
services:
  sonarr:
    image: lscr.io/linuxserver/sonarr:latest
    container_name: sonarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Istanbul
    volumes:
      - /opt/sonarr/data:/config
      - /mnt/storage/media/tv:/tv
      - /mnt/storage/downloads:/downloads
    ports:
      - 8989:8989
    restart: unless-stopped
```

## Çalıştırma ve temel yapılandırma

**Konteyneri başlatma**

```
docker compose up -d
```

**Web arayüzüne erişim**

```
http://localhost:8989
```

## Teknik mimari ve çalışma prensibi

Sonarr, modern bir mikroservis medya pipeline'ının orkestrasyon beyni olarak görev yapar:
- Torznab ve Newznab protokol köprüsü: İndeksleyicilerle (Jackett veya Prowlarr üzerinden) RSS beslemeleri ve arama sorguları üzerinden standart XML/JSON API ile iletişim kurar.
- Atomik dosya taşıma ve Hardlink: İndirme bittiğinde dosyayı kopyalamak yerine dosya sistemi inode'unu bağlayarak disk yazma yükünü ve depolama israfını sıfıra indirir.
- Özel biçim (Custom Formats) puanlama motoru: Tercih edilen ses kodekleri (Atmos, DTS-HD), video formatları (AV1, HEVC) ve yayıncı gruplarına puan vererek en iyi sürümü seçer.

## Medya ekosistemi entegrasyonu (Plex, Jellyfin, Prowlarr)

Kusursuz bir ev medya sunucusu (Homelab) için Sonarr diğer açık kaynak araçlarla zincirleme bağlanır:
- Prowlarr ile indeksleyici senkronizasyonu: Torrent takipçilerini ve Usenet indeksleyicilerini tek merkezden Sonarr'a otomatik aktarın.
- qBittorrent / SABnzbd ile indirme yönetimi: Belirlenen kategoriler üzerinden indirme hızını ve paylaşım oranını kontrol edin.
- Plex veya Jellyfin kütüphane bildirimi: Yeni bir bölüm diske yazıldığında medya sunucusuna anında bildirim gönderip kütüphaneyi taratın.

## Kod bilmiyorsanız
🤖 Kod bilmiyorsanız
Ev sunucumda Docker üzerinde Sonarr, qBittorrent, Prowlarr ve Jellyfin servislerini birlikte çalıştırmak istiyorum. Sabit bağlantıların (hardlink) sorunsuz çalışması için tek bir kök dizin bağlama (volume mount) yapısını içeren eksiksiz bir docker-compose.yml dosyası ve Sonarr web panelinde yapmam gereken ilk ayarları adım adım açıklar mısın?

- **Kimin için:** Ev sunucusu (Homelab) sahipleri, medya tutkunları ve dizi arşivlerini zahmetsizce yönetmek isteyenler.
- **Lisans:** GPL-3.0 (Açık kaynak lisansı)
- **Altyapı:** C# ve .NET tabanlı web servisi
- **Web Portu:** Varsayılan 8989

## Sıkça sorulan sorular
- Sonarr dosyanın kendisini doğrudan indirir mi? Hayır. Sonarr bir indirme istemcisi değildir; bir yöneticidir. Arama yapar, torrent/NZB dosyasını qBittorrent veya SABnzbd gibi istemcilere iletir ve inen dosyayı arşiv klasörüne taşır.
- Hardlink nedir ve diski iki kat doldurur mu? Hayır. Hardlink, dosyanın diskteki fiziksel verisine ikinci bir yol işaretçisi koymaktır. Hem downloads hem tv klasöründe görünür ancak diskte tek bir dosya kadar yer kaplar.
- Sonarr ile Radarr arasındaki fark nedir? Sonarr televizyon dizilerini, sezonları ve bölümleri yönetirken; Radarr aynı mimariyi sinema filmleri için sunar.
- VPN kullanmak gerekir mi? Sonarr sadece RSS ve meta veri sorguları yaptığı için genellikle VPN gerektirmez; ancak torrent indirme istemcisinin (qBittorrent) bir VPN tüneli arkasında çalışması tavsiye edilir.

## Bağlantılar
- [GitHub →](https://github.com/Sonarr/Sonarr)

## İlgili sözlük terimleri
Self-Hosted Offline Open Source Local

---
Source: TreScout Discover · https://trescout.com/discover/sonarr/
