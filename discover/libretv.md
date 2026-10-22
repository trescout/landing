# Çevrim içi video arama ve izleme platformu kurun

LibreSpark/LibreTV, Docker gibi yöntemlerle bir dakika içinde film ve dizi sitesi kurmanıza olanak tanıyan TypeScript tabanlı bir yazılım projesidir. Kullanıcıların kendi içerik platformlarını hızlıca oluşturmalarını sağlayan bir altyapı sunar.

- ★ 20.940
- TypeScript
- GitHub Trending · 2026-10-16

## Güncelleme

- **22 Ekim 2026:** Yıldız 19.801 → 20.940.
- **19 Ekim 2026:** Yıldız 18.500 → 19.801.

## Ne kazandırır?

- farklı kaynaklardaki filmleri ve dizileri tek yerden arayın
- m3u ve m3u8 formatlı internet televizyonu yayınlarını izleyin
- izleme geçmişinizi ve kaldığınız yeri tarayıcınızda saklayın

## Kurulum

**docker ile hızlı kurulum**

```
docker compose pull && docker compose up -d
```

## Çalıştırma

**kaynaktan derleyerek çalıştırma**

```
npm install
PASSWORD=your-password npm run build
PASSWORD=your-password npm start   # 监听 8080
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Bu aracı kurmak ve yapılandırmak için gereken adımları özetle. Docker kullanarak hızlıca nasıl ayağa kaldıracağımı ve `.env` dosyası içinde şifre belirleme adımını açıkla.

Depo: https://github.com/LibreSpark/LibreTV. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Bir API anahtarı gerekirse onu sohbete yazmamı isteme. .env dosyasına nasıl ekleyeceğimi göster ve bu dosyanın Git'e gönderilmediğinden emin ol.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Kendi film, dizi ve canlı televizyon platformunu kurmak isteyen kişiler bu aracı kullanabilir.
- **Lisans:** AGPL-3.0

## Bağlantılar

- [GitHub deposu →](https://github.com/LibreSpark/LibreTV)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-10-16 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [API](https://trescout.com/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/libretv/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
