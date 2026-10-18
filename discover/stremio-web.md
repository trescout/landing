# Tarayıcı üzerinden medya oynatma

Stremio, farklı içerik sağlayıcılarını tek bir arayüzde birleştiren bir medya oynatıcı (media player) uygulamasıdır. Web tabanlı bu sürüm, kullanıcıların herhangi bir kurulum yapmadan tarayıcı üzerinden dizi ve film izlemesine olanak tanır.

- ★ 14.524
- JavaScript
- GitHub Trending · 2026-09-07

## Güncelleme

- **12 Ekim 2026:** Yıldız 14.129 → 14.524, son sürüm v5.0.0-beta.42 (12 Ekim 2026).
- **5 Ekim 2026:** Yıldız 13.968 → 14.129, son sürüm v5.0.0-beta.41 (5 Ekim 2026).
- **27 Eylül 2026:** Yıldız 13.631 → 13.968, son sürüm v5.0.0-beta.40 (23 Eylül 2026).
- **7 Eylül 2026:** Yıldız 13.627 → 13.631, son sürüm v5.0.0-beta.39 (27 Temmuz 2026).

## Ne kazandırır?

- Farklı içerik sağlayıcılarını tek bir arayüzde toplar
- İzleme geçmişini ve kütüphaneyi cihazlar arasında senkronize eder
- Chromecast ile televizyona görüntü aktarımı sağlar

## Kurulum

**Yerel geliştirme ortamı kurulumu**

```
pnpm install
pnpm start
```

**Docker ile konteyner kurulumu**

```
docker build -t stremio-web .
docker run -p 8080:8080 stremio-web
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Stremio Web arayüzünü kullanarak dizi ve film izleme deneyimimi nasıl kişiselleştirebilirim? Eklentileri nasıl yönetebileceğim, izleme listemi nasıl senkronize edeceğim ve klavye kısayollarını kullanarak oynatıcıyı nasıl daha verimli kontrol edebileceğim konusunda bana rehberlik et.

Depo: https://github.com/Stremio/stremio-web. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Çeşitli kaynaklardaki dizi ve filmleri tek bir platform üzerinden, kurulum gerektirmeden tarayıcıda izlemek isteyen kullanıcılar içindir.
- **Lisans:** GPL-2.0

## Bağlantılar

- [GitHub deposu →](https://github.com/Stremio/stremio-web)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-09-07 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/stremio-web/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
