# Claude Code ile otomatik iş başvurusu

Claude Code altyapısını kullanan ai-job-search, iş arama sürecini otomatikleştiren bir çerçeve (framework) sunuyor. Araç, kullanıcı profilini analiz ederek öz geçmiş düzenleme, ön yazı yazma ve mülakat hazırlığı gibi görevleri yapay zekâ desteğiyle gerçekleştiriyor.

- ★ 54.960
- TypeScript
- GitHub Trending · 2026-07-08

## Güncelleme

- **19 Ekim 2026:** Yıldız 49.169 → 54.960, son sürüm v1.7.2 (29 Eylül 2026).
- **17 Ekim 2026:** Yıldız 46.736 → 49.169, son sürüm v1.7.2 (29 Eylül 2026).
- **14 Ekim 2026:** Yıldız 44.486 → 46.736, son sürüm v1.7.2 (29 Eylül 2026).
- **29 Eylül 2026:** Yıldız 43.175 → 44.486, son sürüm v1.7.2 (29 Eylül 2026).

## Ne kazandırır?

- Kişisel profilinize göre öz geçmiş ve ön yazı hazırlar
- İş ilanlarını analiz ederek uygunluk puanı verir
- Mülakat hazırlığı için rehberlik sunar

## Kurulum

**İş arama araçlarını yükleyin**

```
cd .agents/skills/jobbank-search/cli && bun install && cd ../../../..
cd .agents/skills/jobdanmark-search/cli && bun install && cd ../../../..
cd .agents/skills/jobindex-search/cli && bun install && cd ../../../..
cd .agents/skills/jobnet-search/cli && bun install && cd ../../../..
cd .agents/skills/linkedin-search/cli && bun install && cd ../../../..
```

## Çalıştırma

**Profil kurulumunu başlatın**

```
/setup
```

**İş ilanlarını tarayın**

```
/scrape
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Claude Code içerisindeyken /setup komutunu kullanarak profilini oluştur. Ardından /scrape komutuyla uygun iş ilanlarını listele ve /apply komutunu kullanarak seçtiğin ilan için öz geçmiş ve ön yazı taslağını oluşturmasını sağla. Süreç boyunca yapay zekânın ilanla olan uyumunu değerlendirmesini ve mülakat hazırlığı için geri bildirim vermesini iste.

Depo: https://github.com/MadsLorentzen/ai-job-search. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** İş arama sürecini otomatikleştirmek ve yapay zekâ desteğiyle özelleştirilmiş başvurular hazırlamak isteyen profesyoneller için uygundur.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/MadsLorentzen/ai-job-search)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-07-08 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Framework](https://trescout.com/dictionary/framework/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/ai-job-search/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
