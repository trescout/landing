# Kodlama ajanlarınızı yapay zekâ ile izleyin

Agentsview, kodlama ajanları için yerel öncelikli (local-first) oturum zekası ve analitik verileri sunan bir izleme aracıdır. Claude Code ve Codex dahil yirmiden fazla ajanı destekleyen bu yazılım, ccusage aracına kıyasla daha hızlı bir performans vadediyor.

- ★ 5.064
- Go
- GitHub Trending · 2026-06-12

## Güncelleme
- 17 Ağustos 2026: Yıldız 4.714 → 5.064, son sürüm v0.41.0 (17 Ağustos 2026).
- 6 Ağustos 2026: Yıldız 4.683 → 4.714, son sürüm v0.40.1 (4 Ağustos 2026).
- 3 Ağustos 2026: Yıldız 4.672 → 4.683, son sürüm v0.40.0 (3 Ağustos 2026).
- 2 Ağustos 2026: Yıldız 1.867 → 4.672, son sürüm v0.39.0 (27 Temmuz 2026).

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
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Agentsview aracını kullanarak yapay zekâ kodlama ajanlarımın oturum geçmişini ve maliyet verilerini analiz etmek istiyorum. Bilgisayarımda yüklü olan ajanların oturumlarını keşfetmek, günlük maliyet özetimi görmek ve belirli bir ajan filtresiyle token kullanım detaylarını incelemek için hangi komutları kullanmalıyım? Lütfen bana agentsview usage daily ve agentsview session usage komutlarının nasıl kullanılacağını ve sonuçları nasıl yorumlayacağımı adım adım açıkla.

- **Kimin için:** Birden fazla yapay zekâ kodlama ajanı kullanan ve bu araçların harcadığı token ile maliyetleri yerel olarak takip etmek isteyen yazılımcılar içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/kenn-io/agentsview)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-12 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
CCUsage Local-first Token Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/agentsview/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
