# Açık kaynaklı iş arama motoru

Go diliyle geliştirilen freehire, iş arayanlar için tasarlanmış açık kaynaklı (kaynak kodları herkesin erişimine ve geliştirmesine açık) bir arama motorudur. Kullanıcıların iş ilanlarını taramasına ve bulmasına olanak tanıyan bir platform sunar.

- ★ 2.880
- Go
- GitHub Trending · 2026-10-22

## Güncelleme

- **23 Ekim 2026:** Yıldız 2.661 → 2.880, son sürüm extension-v0.1.12 (23 Ekim 2026).
- **22 Ekim 2026:** Yıldız 2.643 → 2.661, son sürüm extension-v0.1.10 (21 Ekim 2026).

## Ne kazandırır?

- Şirketlerin kariyer sayfalarından doğrudan toplanan teknoloji iş ilanlarına aracısız ve güncel olarak ulaşırsınız.
- Farklı kariyer sitelerindeki tekrarlanan ilanları tekilleştirerek temiz ve filtrelenebilir bir listede incelersiniz.
- Öz geçmiş uyumluluk incelemesi ve yapay zekâ destekli başvuru takip panosuyla iş arama sürecinizi yönetirsiniz.

## Kurulum

**Tüm sistemi konteyner ortamında kurma ve**

```
make up        # build + start the whole stack in Docker:
               # api, web, postgres, meilisearch, redis, s3
curl localhost:8080/health
curl localhost:8080/api/v1/jobs
```

## Çalıştırma

**Varsayılan port meşgulse farklı port ile**

```
HIRE_HOST_PORT=8090 make up
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Açık kaynaklı iş arama platformu Freehire uygulamasını kendi sistemimde çalıştırmak istiyorum. Konteyner yönetim yazılımı Docker ve otomasyon aracı Make kullanarak tüm hizmetleri başlatmak ve API durumunu doğrulamak için şu komutları sırasıyla çalıştır: make up # build + start the whole stack in Docker:
# api, web, postgres, meilisearch, redis, s3
curl localhost:8080/health
curl localhost:8080/api/v1/jobs

Depo: https://github.com/strelov1/freehire. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Şirketlerin kendi kariyer sayfalarındaki yazılım ve teknoloji ilanlarını aracısız takip etmek veya kendi bağımsız iş arama motorunu çalıştırmak isteyenler içindir.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/strelov1/freehire)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-10-22 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Localhost](https://trescout.com/dictionary/localhost/)
- [API](https://trescout.com/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/freehire/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
