# Sunucu ve servis durumu izleme aracı

Uptime Kuma, kendi sunucunuzda barındırabileceğiniz görsel arayüzlü bir izleme aracıdır. İnternet sitelerinin ve servislerin çalışma durumunu takip etmeyi sağlayan bu JavaScript tabanlı uygulama, kullanıcı dostu bir deneyim sunar.

- ★ 93.936
- JavaScript
- GitHub Trending · 2026-11-14

## Güncelleme

- **14 Kasım 2026:** Yıldız 93.934 → 93.936, son sürüm 2.5.11 (12 Kasım 2026).

## Ne kazandırır?

- İnternet sitelerini ve servisleri anlık takip edin
- Çoklu dil ve bildirim desteği alın
- Görsel durumu gösteren sayfalar oluşturun

## Kurulum

**Docker Compose ile Kurulum**

```
mkdir uptime-kuma
cd uptime-kuma
curl -o compose.yaml https://raw.githubusercontent.com/louislam/uptime-kuma/master/compose.yaml
docker compose up -d
```

**Docker Komutu ile Kurulum**

```
docker run -d --restart=always -p 3001:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:2
```

## Çalıştırma

**Docker ile Çalıştırma**

```
docker compose up -d
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Uptime Kuma adlı izleme aracını kurmak istiyorum. Docker Compose kullanmak için şu komutu çalıştırmam gerekiyor: mkdir uptime-kuma
cd uptime-kuma
curl -o compose.yaml https://raw.githubusercontent.com/louislam/uptime-kuma/master/compose.yaml
docker compose up -d. Bu adımları tamamlamama yardım eder misin?

Depo: https://github.com/louislam/uptime-kuma. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Web sitelerinin ve sunucuların çalışıp çalışmadığını kendi sunucusunda takip etmek isteyen herkes için uygundur.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/louislam/uptime-kuma)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-11-14 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/uptime-kuma/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
