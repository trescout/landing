# TreScout · Landing

[![Deploy Health Check](https://github.com/trescout/landing/actions/workflows/deploy-health.yml/badge.svg)](https://github.com/trescout/landing/actions/workflows/deploy-health.yml)

Statik HTML landing page. `trescout.com`'a deploy edilir.

## Yapı

```
landing/
├── index.html                  · Ana sayfa (TR)
├── en/ fr/ pt/ es/ de/         · Diğer dil sürümleri
├── discover/ dictionary/       · Keşif ve Sözlük sayfaları
├── reports/                    · Günlük raporlar (web + PDF, tarih bazlı)
├── compare/                    · Karşılaştırma sayfaları
├── api/                        · Vercel fonksiyonları (/api/subscribe)
├── assets/                     · CSS, JS, font, görseller
├── scripts/                    · Build ve tutarlılık kontrol betikleri
├── tests/                      · Testler
├── docs/                       · Ölçüm, ENV, SEO notları
├── sample-report.pdf           · Örnek günlük rapor
├── llms.txt, sitemap.xml, robots.txt
├── vercel.json                 · Başlıklar (CSP vb.) ve yönlendirmeler
├── AGENTS.md                   · Org-wide AI/insan kuralları (kanonik)
├── CLAUDE.md, .cursorrules     · AI araçları yönlendirmesi
└── .github/                    · Workflow'lar ve PR şablonu
```

## Deploy

Bu repo Vercel'a bağlı. `main` branch'a her push otomatik production deploy.

- Production: **https://trescout.com** ✅ canlı
- `www.trescout.com` → 308 Permanent Redirect → `trescout.com` (bare apex kanonik)
- Vercel default URL: `trescout-landing.vercel.app` (preview'lar için bu pattern)
- Her PR için ayrı preview URL

## İletişim

| Kanal | Adres |
|---|---|
| Genel iletişim | `hello@trescout.com` |
| Erken erişim formu | landing hero formu → `/api/subscribe` |

> Operasyonel hesaplar, e-posta yönlendirme topolojisi ve mail altyapısı detayları
> `trescout-internal` reposunda tutulur (bu repo public).

## Sosyal medya

| Platform | Handle | URL |
|---|---|---|
| Twitter / X | `@GetTreScout` | https://x.com/GetTreScout |
| Instagram | `@gettrescout` | https://instagram.com/gettrescout |
| LinkedIn | TreScout (Company Page) | https://linkedin.com/company/trescout |
| Bluesky | `@gettrescout.bsky.social` | https://bsky.app/profile/gettrescout.bsky.social |

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
