# Sistem ve servis izleme araci prometheus

Prometheus, sistem ve servis izleme işlemleri ile zaman serisi veritabanı (time series database) yönetimi sağlayan bir izleme aracıdır. Belirlenen aralıklarla hedeflerden metrik toplayan sistem, kuralları değerlendirerek sonuçları görüntüler ve tanımlanan koşullarda uyarılar oluşturabilir.

- ★ 67.226
- Go
- GitHub Trending · 2026-11-07

## Güncelleme

- **7 Kasım 2026:** Yıldız 67.225 → 67.226, son sürüm v3.16.0 (5 Kasım 2026).

## Ne kazandırır?

- belirlenen araliklarla hedeflerden metrik toplar
- kurallari degerlendirerek sonuclari goruntuler
- tanimlanan kosullarda uyarilar olusturabilir

## Kurulum

**docker ile calistirma**

```
docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus
```

## Çalıştırma

**kaynaktan derleme ve calistirma**

```
make build
./prometheus --config.file=your_config.yml
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

sistem ve servis izleme araci Prometheus uygulamasini Docker kullanarak baslatmak istiyorum. Bu amacla docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus komutunu calistir.

Depo: https://github.com/prometheus/prometheus. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** sistem ve servislerinin durumunu takip etmek isteyen gelistiriciler ile sistem yoneticileri
- **Lisans:** Apache-2.0

## Bağlantılar

- [GitHub deposu →](https://github.com/prometheus/prometheus)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-11-07 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Time Series Database](https://trescout.com/dictionary/time-series-database/)
- [Database](https://trescout.com/dictionary/database/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/prometheus/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
