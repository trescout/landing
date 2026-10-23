# Kodlama ajanlarınızı yapay zekâ ile izleyin

Agentsview, kodlama ajanları için yerel öncelikli (local-first) oturum zekası ve analitik verileri sunan bir izleme aracıdır. Claude Code ve Codex dahil yirmiden fazla ajanı destekleyen bu yazılım, ccusage aracına kıyasla daha hızlı bir performans vadediyor.

- ★ 6.241
- Go
- GitHub Trending · 2026-06-12

## Güncelleme

- **23 Ekim 2026:** Yıldız 6.086 → 6.241, son sürüm v0.46.1 (23 Ekim 2026).
- **9 Ekim 2026:** Yıldız 5.999 → 6.086, son sürüm v0.45.0 (9 Ekim 2026).
- **27 Eylül 2026:** Yıldız 5.905 → 5.999, son sürüm v0.44.0 (21 Eylül 2026).
- **15 Eylül 2026:** Yıldız 5.720 → 5.905, son sürüm v0.43.0 (14 Eylül 2026).

## Ne kazandırır?

- Tüm yapay zekâ kodlama ajanlarınızın oturumlarını tek merkezden izleyin.
- Kullanılan token miktarlarını ve maliyetleri hızlıca hesaplayın.
- Verilerinizi yerel bilgisayarınızda tutarak gizliliği koruyun.

## Kurulum

**macOS / Linux**

```
curl -fsSL https://agentsview.io/install.sh | bash
```

**Windows**

```
powershell -ExecutionPolicy ByPass -c "irm https://agentsview.io/install.ps1 | iex"
```

## Çalıştırma

**Sunucuyu başlatma ve arayüze erişim**

```
agentsview serve
```

**Günlük maliyet özetini görüntüleme**

```
agentsview usage daily
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Agentsview aracını kullanarak yapay zekâ kodlama ajanlarımın oturum geçmişini ve maliyet verilerini analiz etmek istiyorum. Bilgisayarımda yüklü olan ajanların oturumlarını keşfetmek, günlük maliyet özetimi görmek ve belirli bir ajan filtresiyle token kullanım detaylarını incelemek için hangi komutları kullanmalıyım? Lütfen bana agentsview usage daily ve agentsview session usage \<id> komutlarının nasıl kullanılacağını ve sonuçları nasıl yorumlayacağımı adım adım açıkla.

Depo: https://github.com/kenn-io/agentsview. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Bir API anahtarı gerekirse onu sohbete yazmamı isteme. .env dosyasına nasıl ekleyeceğimi göster ve bu dosyanın Git'e gönderilmediğinden emin ol.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Birden fazla yapay zekâ kodlama ajanı kullanan ve bu araçların harcadığı token ile maliyetleri yerel olarak takip etmek isteyen yazılımcılar içindir.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/kenn-io/agentsview)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-06-12 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [CCUsage](https://trescout.com/dictionary/ccusage/)
- [Local-first](https://trescout.com/dictionary/local-first/)
- [Token](https://trescout.com/dictionary/token/)
- [API](https://trescout.com/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/agentsview/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
