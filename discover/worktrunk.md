# Git çalışma ağaçlarını yönetin

Worktrunk, Git çalışma ağacı (worktree) yönetimini kolaylaştıran, Rust diliyle yazılmış bir komut satırı arayüzü (CLI). Özellikle paralel yapay zekâ ajanı iş akışlarını desteklemek için geliştirilen bu araç, aynı anda birden fazla görev üzerinde çalışmayı hızlandırıyor.

- ★ 9.348
- Rust
- GitHub Trending · 2026-09-13

## Güncelleme

- **21 Ekim 2026:** Yıldız 8.444 → 9.348, son sürüm v0.81.0 (20 Ekim 2026).
- **28 Eylül 2026:** Yıldız 8.424 → 8.444, son sürüm v0.80.0 (27 Eylül 2026).
- **27 Eylül 2026:** Yıldız 7.964 → 8.424, son sürüm v0.79.0 (21 Eylül 2026).
- **17 Eylül 2026:** Yıldız 7.379 → 7.964, son sürüm v0.78.0 (16 Eylül 2026).

## Ne kazandırır?

- Birden fazla görevi aynı anda yürütmek için çalışma alanlarını kolayca oluşturur
- Otomatik kancalarla yerel iş akışlarını hızlandırır
- Yapay zekâ ajanlarının paralel çalışmasını destekler

## Kurulum

**Homebrew ile kurulum**

```
brew install worktrunk && wt config shell install
```

**Cargo ile kurulum**

```
cargo install worktrunk && wt config shell install
```

## Çalıştırma

**Çalışma ağaçları arasında geçiş yapma**

```
wt switch feat
```

**Yeni çalışma ağacı oluşturma ve başlatma**

```
wt switch -c -x claude feat
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Worktrunk kullanarak mevcut Git projemde yeni bir çalışma ağacı oluşturmak ve bu alanda paralel bir görev başlatmak istiyorum. Çalışma ağaçlarını dallar kadar kolay yönetebilmem için wt komutlarını nasıl kullanmalıyım ve iş akışımı otomatize etmek için kancalardan nasıl faydalanabilirim?

Depo: https://github.com/max-sixty/worktrunk. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Aynı anda birden fazla yazılım görevi veya yapay zekâ ajanı üzerinde çalışan geliştiriciler için tasarlanmıştır.

## Bağlantılar

- [GitHub deposu →](https://github.com/max-sixty/worktrunk)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-09-13 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Worktree](https://trescout.com/dictionary/worktree/)
- [CLI](https://trescout.com/dictionary/cli/)
- [Rust](https://trescout.com/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/worktrunk/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
