# Verilerinizi şifreli ve hızlı yedekleyin

Go diliyle geliştirilen Restic, verileri şifreleyerek hızlı ve verimli bir şekilde yedekleyen açık kaynaklı bir yedekleme programı (backup program) sunuyor. Farklı depolama sistemlerini destekleyen bu araç, artımlı yedekleme (incremental backup) yöntemiyle depolama alanından tasarruf sağlıyor.

- ★ 34.273
- GitHub Trending · 2026-06-12

TreScout notu: Yedeği şifreleyip tekrar eden veriyi ayıkladığı için depolama maliyeti düşük kalır. Arayüzü yoktur, zamanlanmış görevi ve saklama politikasını siz kurarsınız · forget ve prune adımlarını atlarsanız depo şişer. Geri yükleme senaryosunu kurduğunuz gün bir kez deneyin, yedeğin çalıştığını ancak öyle bilirsiniz.

## Ne kazandırır?
- Verileri şifreleyerek güvenli yedekleme sağlar
- Artımlı yedekleme ile depolama alanından tasarruf eder
- Farklı bulut ve yerel depolama sistemlerini destekler

## Kurulum

**macOS (Homebrew)**

```
brew install restic
```

**Debian/Ubuntu**

```
apt install restic
```

Kaynak: restic.readthedocs.io (resmî)

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Restic yedekleme programını kullanarak bir depo oluşturmak ve belirli bir klasörü yedeklemek istiyorum. Yedekleme sürecini başlatmak için gerekli olan depo oluşturma ve yedekleme komutlarını, depo yolu ve kaynak klasör bilgilerini nasıl yapılandırmam gerektiğini adım adım açıklar mısın?

- **Kimin için:** Verilerini güvenli, hızlı ve şifreli bir şekilde yedeklemek isteyen kullanıcılar için uygundur. 
- **Lisans:** BSD-2-Clause 

## Bağlantılar
- [GitHub deposu →](https://github.com/restic/restic)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-12 tarihindeki hâlini anlatır: yıldız, sayılar ve metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Backup Program Incremental Backup Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/restic/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
