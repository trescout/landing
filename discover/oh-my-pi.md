# Terminalde yapay zekâ destekli kodlama

Oh-my-pi, terminal ortamında çalışan ve kod düzenleme süreçlerini otomatikleştiren bir yapay zekâ kodlama ajanıdır (AI coding agent). Araç, dil sunucusu protokolü (LSP), tarayıcı entegrasyonu ve alt ajan yönetimi gibi özelliklerle yazılım geliştirme iş akışlarını optimize etmeyi hedefler.

- ★ 37.121
- GitHub Trending · 2026-06-02

## Güncelleme

- **30 Ekim 2026:** Yıldız 37.005 → 37.121, son sürüm v18.14.0 (29 Ekim 2026).
- **29 Ekim 2026:** Yıldız 36.892 → 37.005, son sürüm v18.13.3 (28 Ekim 2026).
- **28 Ekim 2026:** Yıldız 36.754 → 36.892, son sürüm v18.13.2 (27 Ekim 2026).
- **27 Ekim 2026:** Yıldız 36.210 → 36.754, son sürüm v18.13.1 (27 Ekim 2026).

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

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Oh My Pi aracını terminalimde kullanmaya başladım. Bu yapay zekâ kodlama ajanı ile projelerimde LSP desteği, hata ayıklama ve alt ajan yönetimi gibi gelişmiş özellikleri kullanarak iş akışımı nasıl optimize edebilirim? Özellikle kod düzenleme, dosya okuma ve hata ayıklama süreçlerinde bu aracın sunduğu yerleşik araçları en verimli şekilde nasıl kullanacağımı adım adım açıkla.

Depo: https://github.com/can1357/oh-my-pi. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Terminal üzerinden kod geliştirme süreçlerini otomatikleştirmek ve yapay zekâ destekli bir kodlama ajanı ile iş akışını hızlandırmak isteyen yazılım geliştiriciler için uygundur.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/can1357/oh-my-pi)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-06-02 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [LSP](https://trescout.com/dictionary/lsp/)
- [AI Coding Agent](https://trescout.com/dictionary/ai-coding-agent/)
- [Coding Agent](https://trescout.com/dictionary/coding-agent/)
- [IDE](https://trescout.com/dictionary/ide/)
- [Agent](https://trescout.com/dictionary/agent/)
- [Terminal](https://trescout.com/dictionary/terminal/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/oh-my-pi/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
