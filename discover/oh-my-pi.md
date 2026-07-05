# Terminalde yapay zekâ destekli kodlama

Oh-my-pi, terminal ortamında çalışan ve kod düzenleme süreçlerini otomatikleştiren bir yapay zekâ kodlama ajanıdır (AI coding agent). Araç, dil sunucusu protokolü (LSP), tarayıcı entegrasyonu ve alt ajan yönetimi gibi özelliklerle yazılım geliştirme iş akışlarını optimize etmeyi hedefler.

- ★ 9.701
- GitHub Trending · 2026-06-02

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

## İlgili sözlük terimleri
LSP AI Coding Agent Coding Agent Terminal Artificial Intelligence 

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Yıldız ve sayılar keşif tarihindeki değerlerdir.

---
Kaynak: TreScout Keşif · https://trescout.com/discover/oh-my-pi/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
