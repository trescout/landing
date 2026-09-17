# Git çalışma ağaçlarını yönetin

Worktrunk, Git çalışma ağacı (worktree) yönetimini kolaylaştıran, Rust diliyle yazılmış bir komut satırı arayüzü (CLI). Özellikle paralel yapay zekâ ajanı iş akışlarını desteklemek için geliştirilen bu araç, aynı anda birden fazla görev üzerinde çalışmayı hızlandırıyor.

- ★ 7.964
- Rust
- GitHub Trending · 2026-09-13

## Güncelleme
- 17 Eylül 2026: Yıldız 7.379 → 7.964, son sürüm v0.78.0 (16 Eylül 2026).
- 13 Eylül 2026: Yıldız 7.376 → 7.379, son sürüm v0.77.0 (8 Eylül 2026).

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
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Worktrunk kullanarak mevcut Git projemde yeni bir çalışma ağacı oluşturmak ve bu alanda paralel bir görev başlatmak istiyorum. Çalışma ağaçlarını dallar kadar kolay yönetebilmem için wt komutlarını nasıl kullanmalıyım ve iş akışımı otomatize etmek için kancalardan nasıl faydalanabilirim?

- **Kimin için:** Aynı anda birden fazla yazılım görevi veya yapay zekâ ajanı üzerinde çalışan geliştiriciler için tasarlanmıştır. 

## Bağlantılar
- [GitHub deposu →](https://github.com/max-sixty/worktrunk)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-09-13 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Worktree CLI Rust Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/worktrunk/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
