# AI Usage Log · TreScout Landing

| Tarih | Kişi | Görev | AI Aracı | Rol | PR/Commit |
|---|---|---|---|---|---|
| 2026-07-27 | Mustafa | Keşif enrichment · Parti A (Issue #30) | Antigravity | Skills Agent | Refs #30 |
| 2026-08-04/05 | Burhan | İngilizce çift dil hattı, Compare sayfası, düzen birleştirme | Antigravity | Skills Agent | main'e doğrudan (PR yok) |
| 2026-08-06 | Claude | CSP ihlalleri, eskimiş guard'lar, marka yazımı, eksik meta, beş PR'ın taşınması | Claude Code | Denetim | #57 #59 #61 #62 #63 #64 |
| 2026-08-23 | Manus | SEO/GEO metadata, hreflang, llms index, rapor açıklamaları ve read-only guard · erken erişim kayıt/bildirim akışı korundu | Manus AI | Plan Agent + Manual | `fix/seo-geo-early-access-safe` |
| 2026-08-24 | Manus | Oto-büyüme workflow'unda stale generated tree rebase çatışması recovery düzeltmesi · e-posta akışına dokunulmadı | Manus AI | Plan Agent + Manual | `fix/dict-sync-stale-main` |
| 2026-08-24 | Manus | Keşif katalog tagline dil kirliliği düzeltmesi · 14 kayıt × 6 dil, Türkçe lead/meta/JSON-LD ve OG kartları · dil kalite guard’ı | Gemini + Claude + Manus | Türkçe İçerik + Denetim + Manual | `fix/discovery-language-quality` |
| 2026-08-24 | Manus | Discovery “En yeni” sıralamasını son görülmeden ilk keşif tarihine düzeltme · ECC denetimi ve 6 dil sort guard’ı | Manus AI | Denetim + Manual | `fix/discovery-newest-sort` |
| 2026-08-24 | Manus | 2026-08-24 raporunun EN/FR/PT/ES/DE normal + fresh JSON/PDF backfill’i · Google Translate endpoint 429 verdiği için yalnız rapor metin alanlarında yapılandırılmış gpt-5-mini kullanıldı; URL, başlık, meta olguları, yıldız, sıralama ve capturedAt manuel validator ile korundu | gpt-5-mini + Manus AI | Structured translation + Manual validation | `fix/report-locale-backfill` |
| 2026-08-24 | Manus | Rapor snapshot provenance · localized chip sayılarını kendi immutable JSON’undan üretme, capturedAt note ve helper regression testleri · e-posta akışına dokunulmadı | Gemini + Claude + Manus AI | Türkçe İçerik + Denetim + Manual | `fix/report-snapshot-separation` |
| 2026-08-24 | Manus | Google/Bing Search Essentials and AI-search documentation audit; discovery Article JSON-LD visible-content/locale alignment, localized OG/Twitter metadata, explicit Claude SearchBot/Claude User robots access, diff-based sitemap lastmod refresh, and PR SEO/GEO guard | Manus AI + official Google/Bing/OpenAI/Anthropic/Perplexity docs | Research + Manual | `fix/seo-geo-crawler-schema` |
