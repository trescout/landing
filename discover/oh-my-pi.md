# Terminalde yapay zekâ destekli kodlama

Oh-my-pi, terminal ortamında çalışan ve kod düzenleme süreçlerini otomatikleştiren bir yapay zekâ kodlama ajanıdır (AI coding agent). Araç, dil sunucusu protokolü (LSP), tarayıcı entegrasyonu ve alt ajan yönetimi gibi özelliklerle yazılım geliştirme iş akışlarını optimize etmeyi hedefler.

- ★ 21.651
- GitHub Trending · 2026-06-02

## Güncelleme
- 4 Ağustos 2026: Yıldız 21.400 → 21.651, son sürüm v17.2.7 (3 Ağustos 2026).
- 3 Ağustos 2026: Yıldız 21.226 → 21.400, son sürüm v17.2.5 (3 Ağustos 2026).
- 2 Ağustos 2026: Yıldız 9.701 → 21.226, son sürüm v17.2.4 (1 Ağustos 2026).

## Ne kazandırır?
- IDE özelliklerini terminale taşıyarak kod düzenleme süreçlerini otomatikleştirir.
- LSP entegrasyonu ile yeniden adlandırma ve referans takibi gibi işlemleri hatasız yapar.
- Hata ayıklama araçlarıyla doğrudan etkileşime girerek sorunları yerinde çözer.

## Kurulum

**macOS ve Linux için kurulum**

```
curl -fsSL https://omp.sh/install | sh
```

**Bun üzerinden kurulum**

```
bun install -g @oh-my-pi/pi-coding-agent
```

## Çalıştırma

**Kabuk tamamlayıcılarını yapılandırma**

```
# zsh — add to ~/.zshrc (or write the output into a file on your $fpath)
eval "$(omp completions zsh)"

# bash — add to ~/.bashrc
eval "$(omp completions bash)"

# fish
omp completions fish > ~/.config/fish/completions/omp.fish
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Oh My Pi aracını terminalimde kullanmaya başladım. Bu yapay zekâ kodlama ajanı ile projelerimde LSP desteği, hata ayıklama ve alt ajan yönetimi gibi gelişmiş özellikleri kullanarak iş akışımı nasıl optimize edebilirim? Özellikle kod düzenleme, dosya okuma ve hata ayıklama süreçlerinde bu aracın sunduğu yerleşik araçları en verimli şekilde nasıl kullanacağımı adım adım açıkla.

- **Kimin için:** Terminal üzerinden kod geliştirme süreçlerini otomatikleştirmek ve yapay zekâ destekli bir kodlama ajanı ile iş akışını hızlandırmak isteyen yazılım geliştiriciler için uygundur. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/can1357/oh-my-pi)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-02 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
LSP AI Coding Agent IDE Coding Agent Terminal Agent

---
Kaynak: TreScout Keşif · https://trescout.com/discover/oh-my-pi/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
