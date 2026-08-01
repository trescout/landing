# verilerinizi şifreleyerek güvenle yedekleyin

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
Restic kullanarak verilerimi nasıl yedekleyebilirim? Yedekleme havuzunu oluşturmak için hangi komutu kullanmalıyım ve ardından belirli bir klasörü yedekleme havuzuna eklemek için izlemem gereken adımlar nelerdir? Lütfen yedekleme sırasında şifreleme ve artımlı yedekleme özelliklerinin nasıl devreye girdiğini açıklayarak, başlangıç için en temel komutları içeren bir rehber hazırla.

- **Kimin için:** Verilerini şifreli, hızlı ve verimli bir şekilde yedeklemek isteyen tüm kullanıcılar için uygundur. 
- **Lisans:** BSD-2-Clause 

## Bağlantılar
- [GitHub deposu →](https://github.com/restic/restic)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-12 tarihindeki hâlini anlatır: yıldız, sayılar ve metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Backup Program Incremental Backup Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/restic/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
