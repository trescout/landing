# TreScout · Landing

Statik HTML landing page. `trescout.com`'a deploy edilir.

## Yapı

```
trescout-landing/
├── index.html                          · Landing page (tek dosya)
├── sample-report.pdf                   · Örnek günlük rapor (download link)
├── favicon.svg                         · Browser tab ikonu
├── README.md
├── AGENTS.md                           · Org-wide AI/insan kuralları (kanonik)
├── CLAUDE.md                           · Claude Code yönlendirmesi
├── .cursorrules                        · Cursor yönlendirmesi
└── .github/pull_request_template.md    · PR şablonu (özet, test, AI aracı)
```

## Deploy

Bu repo Vercel'a bağlı. `main` branch'a her push otomatik production deploy.

- Production: https://trescout.com
- Preview: her PR için ayrı URL

## Geliştirme

Dosya tek HTML; özel bir build adımı yok. Açmak için:

```bash
open index.html
```

veya local server:

```bash
python3 -m http.server 8000
# http://localhost:8000
```

## İlgili repo'lar

- `trescout/brand-kit` · marka kimliği, mockup'lar, sample report kaynak HTML, dokümantasyon
- `trescout/app` · Sürüm 1+ Next.js uygulaması (yakında)

## Versiyon

Bu landing **Sürüm 0.5** içindir: erken erişim listesi toplama. Sürüm 1'de Next.js uygulamasına dönüştürülecek (`trescout/app` repo'sunda).

## Kurallar

Bu repoya katkı yapmadan önce **[AGENTS.md](./AGENTS.md)** dosyasını okuyun.
