# İnternet videolarını kendi sunucunuzda indirin

Averygan tarafından geliştirilen Reclip, neredeyse tüm internet sitelerinden video indirmeye yarayan hafif ve kendi sunucunuzda barındırabileceğiniz bir araçtır. Sade bir web arayüzü üzerinden medya dosyalarını yerel cihazınıza kaydetmenizi sağlar.

- ★ 7.951
- HTML
- GitHub Trending · 2026-09-02

## Ne kazandırır?
- YouTube ve Instagram gibi 1000'den fazla siteden video ve ses dosyası indirir.
- İndirilen dosyaları MP4 video veya MP3 ses formatında kaydeder.
- Web tarayıcısı üzerinden çalışan sade ve hızlı bir arayüz sunar.

## Kurulum

**Standart kurulum**

```
brew install yt-dlp ffmpeg # or apt install ffmpeg && pip install yt-dlp
git clone https://github.com/averygan/reclip.git
cd reclip
./reclip.sh
```

**Docker ile kurulum**

```
docker build -t reclip . && docker run -p 8899:8899 reclip
```

## Çalıştırma

**Arayüze erişim**

```
http://localhost:8899
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Reclip aracını kullanarak internet üzerindeki video bağlantılarını MP4 veya MP3 formatında yerel cihazıma indirmek istiyorum. İndirme işlemini başlatmak için bağlantıları giriş kutusuna yapıştırıp format seçimi yaptıktan sonra Fetch butonuna basarak video bilgilerini yüklemem ve ardından Download butonunu kullanmam gerekiyor. Bu süreçte toplu indirme yapabilir ve video çözünürlüğünü tercihlerime göre ayarlayabilirim.

- **Kimin için:** İnternet üzerindeki medya içeriklerini kendi yerel depolama alanına yedeklemek isteyen kullanıcılar için uygundur. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/averygan/reclip)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-09-02 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/reclip/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
