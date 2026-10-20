# Yapay zekâ model ayarlarını tek ekrandan yönetin

Codex-X, OpenAI Codex modellerini yönetmek için geliştirilen, Rust diliyle yazılmış görsel bir masaüstü ve komut satırı arayüzü aracıdır. Yazılım; API yönetimi, oturum senkronizasyonu, istem enjeksiyonu (prompt injection) ve yetenek (skills) yönetimi gibi özelliklerle geliştirici deneyimini merkezileştirir.

- ★ 4.262
- GitHub Trending · 2026-09-20

## Güncelleme

- **20 Ekim 2026:** Yıldız 4.233 → 4.262, son sürüm v0.3.28 (20 Ekim 2026).
- **17 Ekim 2026:** Yıldız 4.124 → 4.233, son sürüm v0.3.27 (16 Ekim 2026).
- **9 Ekim 2026:** Yıldız 4.006 → 4.124, son sürüm v0.3.26 (9 Ekim 2026).
- **1 Ekim 2026:** Yıldız 3.999 → 4.006, son sürüm v0.3.24 (1 Ekim 2026).

## Ne kazandırır?

- İstem şablonlarını ve eklentileri arayüz üzerinden kolayca yönetin
- Farklı yapay zekâ sağlayıcıları arasında hızlıca geçiş yapın
- Oturum geçmişini ve token kullanım trendlerini takip edin

## Kurulum

**Bağımlılıkları yükleme**

```
pnpm install
```

## Çalıştırma

**Geliştirme ortamını başlatma**

```
pnpm dev
```

**Masaüstü uygulamasını derleme**

```
pnpm --dir apps/desktop tauri build
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Codex-X kullanarak yapay zekâ kodlama asistanım için hazırladığım istem şablonlarını ve sağlayıcı ayarlarını tek bir görsel arayüzde toplamak istiyorum. Uygulamayı yerel ortamımda kurup başlatarak API anahtarlarımı yapılandırmama ve oturum geçmişimi senkronize etmeme yardım et.

Depo: https://github.com/yynxxxxx/Codex-X. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Bir API anahtarı gerekirse onu sohbete yazmamı isteme. .env dosyasına nasıl ekleyeceğimi göster ve bu dosyanın Git'e gönderilmediğinden emin ol.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Kodlama asistanı kullanan geliştiriciler
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/yynxxxxx/Codex-X)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-09-20 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Prompt Injection](https://trescout.com/dictionary/prompt-injection/)
- [Prompt](https://trescout.com/dictionary/prompt/)
- [Token](https://trescout.com/dictionary/token/)
- [AI Skills](https://trescout.com/dictionary/ai-skills/)
- [Rust](https://trescout.com/dictionary/rust/)
- [API](https://trescout.com/dictionary/api/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/codex-x/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
