# Verilerinizi şifreleyerek güvenle yedekleyin

Go diliyle geliştirilen Restic, verileri şifreleyerek hızlı ve verimli bir şekilde yedekleyen açık kaynaklı bir yedekleme programı (backup program) sunuyor. Farklı depolama sistemlerini destekleyen bu araç, artımlı yedekleme (incremental backup) yöntemiyle depolama alanından tasarruf sağlıyor.

- ★ 35.302
- GitHub Trending · 2026-06-12

TreScout notu: Yedeklerinizi şifreleyerek saklar ve aynı dosyayı iki kez yazmadığı için yer kaplamaz. Tıklanacak bir arayüzü yok, komut satırından çalışır ve eski yedekleri temizleme işini siz ayarlarsınız, ayarlamazsanız depolama zamanla şişer. Kurduğunuz gün bir dosyayı geri yüklemeyi deneyin: Yedeğin gerçekten çalıştığını başka türlü anlayamazsınız.

## Güncelleme
- 2 Ağustos 2026: Yıldız 34.273 → 35.302, son sürüm v0.19.1 (5 Temmuz 2026).

## Ne kazandırır?
- Verileri şifreleyerek yüksek güvenlik sağlar
- Artımlı yedekleme ile depolama alanından tasarruf eder
- Farklı bulut ve yerel depolama sistemleriyle uyumludur

## Kurulum

**macOS · Homebrew**

```
brew install restic
```

**Windows · winget**

```
winget install restic.restic
```

## Çalıştırma

**Yedek deposu oluştur**

```
restic init --repo /path/to/repo
```

Kaynak: Resmî kaynak: https://github.com/restic/restic

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Verilerimi Restic kullanarak güvenli bir şekilde yedeklemek istiyorum. Yerel bir klasörü veya belirli bir dizini şifreli bir yedekleme deposuna nasıl aktarabilirim? Yedekleme deposunu oluşturma ve ilk yedekleme işlemini başlatma adımlarını, verilerimin şifrelenmesini sağlayacak şekilde adım adım açıklar mısın?

- **Kimin için:** Verilerini şifreleyerek hızlı ve verimli bir şekilde yedeklemek isteyen tüm kullanıcılar için uygundur. 
- **Lisans:** BSD-2-Clause 

## Bağlantılar
- [GitHub deposu →](https://github.com/restic/restic)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-12 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Backup Program Incremental Backup Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/restic/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
