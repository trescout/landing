# Yapay zekâ destekli hassas kod inceleme

Alibaba tarafından geliştirilen açık kaynaklı kod inceleme aracı, deterministik işlem hatları (pipelines) ile büyük dil modeli (LLM) ajanlarını hibrit bir yapıda birleştiriyor. Yazılım güvenliği kuralları ve satır bazlı yorumlama yetenekleriyle donatılan araç, Go diliyle yazılmış olup OpenAI ve Anthropic uyumlu bir altyapı sunuyor.

- ★ 47.998
- Go
- GitHub Trending · 2026-07-24

## Güncelleme

- **22 Ekim 2026:** Yıldız 47.696 → 47.998, son sürüm v1.13.3 (22 Ekim 2026).
- **20 Ekim 2026:** Yıldız 47.516 → 47.696, son sürüm v1.13.2 (20 Ekim 2026).
- **17 Ekim 2026:** Yıldız 46.806 → 47.516, son sürüm v1.13.1 (17 Ekim 2026).
- **13 Ekim 2026:** Yıldız 44.479 → 46.806, son sürüm v1.13.0 (13 Ekim 2026).

## Ne kazandırır?

- Satır bazlı hassas hata tespiti
- Düşük token tüketimi ile yüksek verimlilik
- Deterministik işlem hatları ile kararlı sonuçlar

## Kurulum

**CLI aracını küresel olarak yükleyin**

```
npm install -g @alibaba-group/open-code-review
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Open Code Review aracını kullanarak mevcut Git değişikliklerimi incele. Kod tabanındaki dosyaları analiz et, satır bazlı hata tespiti yap ve yapılandırılmış geri bildirimler oluştur. İnceleme sürecinde deterministik kuralları takip ederek yanlış pozitifleri en aza indir ve sadece kritik güvenlik veya mantık hatalarına odaklan.

Depo: https://github.com/alibaba/open-code-review. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Kod kalitesini artırmak ve büyük ölçekli projelerde güvenli kod incelemesi yapmak isteyen yazılım geliştiriciler için uygundur.
- **Lisans:** Apache-2.0

## Bağlantılar

- [GitHub deposu →](https://github.com/alibaba/open-code-review)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-07-24 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Code Review](https://trescout.com/dictionary/code-review/)
- [Token](https://trescout.com/dictionary/token/)
- [LLM](https://trescout.com/dictionary/llm/)
- [CLI](https://trescout.com/dictionary/cli/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/open-code-review/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
