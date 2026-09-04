# WiFi Sinyalleriyle Kablosuz Algılama Platformu

WiFi Channel State Information (CSI) kullanarak ortam değişimlerini incelemenize yardımcı olur. ESP32 veya araştırma NIC’leriyle çalışabilir; donanımınız yoksa simüle edilmiş verilerle değerlendirme yapabilirsiniz.

- ★ 92.471
- GitHub Trending · 2026-05-30

## Kurulum

**Docker imajını çekin**

```
docker pull ruvnet/wifi-densepose:latest
```

**Kaynak kodunu alın**

```
git clone https://github.com/ruvnet/RuView.git
```

## Çalıştırma

**Donanımsız demo sunucusu**

```
docker run -p 3000:3000 ruvnet/wifi-densepose:latest
```

**Deterministik doğrulama**

```
./verify
```

Kaynak: Komutlar RuView resmî kullanıcı ve build rehberlerinden 24 Ağustos 2026’da kontrol edildi; Docker varsayılan olarak simüle edilmiş verilerle çalışabilir.

## Güncelleme
- 4 Eylül 2026: Yıldız 92.317 → 92.471, son sürüm v2475 (3 Eylül 2026).
- 2 Eylül 2026: Yıldız 92.231 → 92.317, son sürüm v2456 (2 Eylül 2026).
- 1 Eylül 2026: Yıldız 92.175 → 92.231, son sürüm v2434 (31 Ağustos 2026).
- 31 Ağustos 2026: Yıldız 91.815 → 92.175, son sürüm v2428 (31 Ağustos 2026).

## Bu araç ne yapar?

RuView, WiFi Channel State Information (CSI) verileriyle sensing çalışmaları için kullanılan MIT lisanslı bir platformdur. ESP32 ve araştırma NIC’leriyle çalışabilir; Docker veya kaynak kodu yoluyla kurulabilir. Donanım olmadan simüle edilmiş verilerle değerlendirme yapabilirsiniz. Yetenekler kullanılan donanıma göre değişir: laptopta yalnızca RSSI kullanımı kaba varlık ve hareket algılama içindir; gelişmiş sensing için tam CSI destekli donanım gerekir.

## Kimin için?

WiFi sinyalleriyle varlık, hareket veya ortam değişimi üzerine sensing denemeleri yapmak isteyen araştırmacılar ve geliştiriciler için uygundur.

## Ne beklememeli?

Tıbbi izleme amacıyla doğruluk beklentisi olan çalışmalar veya standart laptopun RSSI modunda pose kestirimi bekleyenler için uygun değildir.

## Öne çıkanlar
- ESP32 ve araştırma NIC’leriyle CSI tabanlı sensing seçenekleri sunar.
- Donanımınız olmadan simüle edilmiş verilerle değerlendirme yapabilirsiniz.
- Resmî build rehberinde deterministik referans sinyal doğrulaması için `./verify` adımı belgelenir.
- Laptop RSSI modu ile tam CSI donanımının sunduğu sensing kapsamı birbirinden ayrılır.

## İlk kullanım akışı
- Docker veya kaynak kodu yolundan, resmî kurulum belgelerine göre ortamınızı hazırlayın.
- Donanımınız yoksa simüle edilmiş verilerle değerlendirme akışını inceleyin.
- Build rehberinde açıklanan deterministik referans sinyal doğrulaması için `./verify` adımını çalıştırın.
- Kullandığınız donanıma göre RSSI-only veya tam CSI sensing akışını seçin.

## Güvenli başlangıç

Laptopta RSSI-only mod, kaba varlık ve hareket algılama içindir; pose desteği sunmaz. Pose ve bazı benchmark yetenekleri deneysel, ilk sürüm niteliğinde veya açık sınırlılıklarla belgelenir; sonuçları kullandığınız donanım moduna göre değerlendirin.

## İlk görev istemi
İlk adım için hazır istem 
WiFi CSI verileriyle basit bir hareket algılama senaryosunu simüle edilmiş veri üzerinden nasıl değerlendirebilirsiniz?

## Bağlantılar
- [GitHub deposu →](https://github.com/ruvnet/RuView)
- [RuView resmî GitHub deposu →](https://github.com/ruvnet/RuView)
- [RuView kullanıcı rehberi →](https://github.com/ruvnet/RuView/blob/main/docs/user-guide.md)
- [RuView build rehberi →](https://github.com/ruvnet/RuView/blob/main/docs/build-guide.md)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-05-30 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
WiFi Benchmark

---
Kaynak: TreScout Keşif · https://trescout.com/discover/ruview/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
