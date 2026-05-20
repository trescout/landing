---
name: ai-traceability-fill
description: Her PR'da AGENTS.md §3.d zorunluluğu · AI Traceability bölümünün 4 alt başlığını sırayla doldur. Atlanamaz.
trigger: PR açılırken veya commit hazırlanırken
applies-to:
  - ".github/pull_request_template.md"
  - ".github/PULL_REQUEST_TEMPLATE.md"
---

# Skill · AI Traceability Fill

## Ne zaman aktif

Her PR açılırken. `AGENTS.md §3.d` org-wide zorunlu kural · atlanırsa PR reddedilir.

## Procedure

PR template'in 4 alt bölümünü sırayla doldur:

### 1. Plan Agent

- **Outputs used:** hangi tasarım çıktısı kullanıldı?
  - Örnek: `docs/ARCHITECTURE.md §4`, Issue `#42`, brand-kit `PRD-v2.md §3.e`
  - Eğer Plan Agent çağrılmadıysa: "yok"
- **Tool:** `claude-code` / `antigravity` / `cursor` / `manual`

### 2. Skills Agent

- [ ] Bu PR'da Skills Agent kullanıldı mı?
  - "Uzman yazılımcıya soruyormuş gibi" spesifik teknik soru çözüldüyse: **evet**
  - Tipik Skills alanları (`AGENTS.md §3.b`): API integration, performance, security, library-specific patterns
- Kullanıldıysa doldur:
  - **Konu:** ne yapıldı (örn. "Gemini retry/backoff + exponential delay")
  - **Tool:** `claude-code` / `antigravity` / `cursor`
  - **Dosyalar + satırlar:** `lib/ai/gemini.ts:96-121`
  - **Prompt arşivi:** `docs/PROMPTS.md#<id>` formatında link

### 3. Türkçe İçerik

- [ ] Bu PR'da Türkçe metin var mı?
  - "Kullanıcı-yüzü Türkçe": rapor, e-posta, UI, landing copy
  - Kod yorumu ve commit message istisna
- Varsa zorunlu işaretle:
  - [ ] Gemini'den geçti
  - [ ] Claude denetiminden geçti (`brand-voice-check` skill'i çalıştırıldı)
- İlgili skill: [`gemini-translation`](gemini-translation.md)

### 4. Manuel

- AI yapmadığı veya AI önerisini reddedip manuel yazılan kısım
- **Boş bırakma** · "tamamı AI" da geçerli cevap
- Reddedilen AI önerisi varsa gerekçe belirt (örn. "AI önerdiği regex pattern Türkçe karakter için bug'lı, manuel yazdım")

## İyi örnek

```markdown
## AI Traceability

### Plan Agent
- Outputs used: docs/ARCHITECTURE.md §6 (günlük rapor algoritması)
- Tool: claude-code

### Skills Agent
- [x] Bu PR'da Skills Agent kullanıldı
- Konu: Gemini RPD budget tracker · exponential backoff retry
- Tool: claude-code
- Dosyalar + satırlar: lib/utils/budget.ts:1-87, lib/ai/gemini.ts:96-121
- Prompt arşivi: docs/PROMPTS.md#gemini-retry

### Türkçe İçerik
- [x] Bu PR'da Türkçe içerik var (rapor template'i)
- [x] Gemini'den geçti
- [x] Claude denetiminden geçti

### Manuel
- Retry strategy'sindeki 503/429/UNAVAILABLE detect regex'i manuel yazıldı · AI önerisi `429|503` pattern'iyle UNAVAILABLE'ı kaçırıyordu.
```

## Anti-patterns

- ❌ AI Traceability bölümünü silmek veya atlamak
- ❌ "doldurmaya gerek yok" diye boş bırakmak
- ❌ Skills Agent kullanıldığı halde Prompt arşivi yazmamak
- ❌ "Manuel" bölümünü es geçmek
- ❌ Türkçe metin olduğu halde Gemini akışını işaretlememek

## Cross-skill referansı

Bu skill aşağıdaki skill'leri tetikleyebilir:
- **[`gemini-translation`](gemini-translation.md)** · Türkçe içerik varsa
- **[`brand-voice-check`](brand-voice-check.md)** · Claude denetimi adımı

## Detay

- `AGENTS.md §3.d` · "AI Traceability (org-wide zorunlu)"
- `AGENTS.md §3.e` · Definition of Done · Traceability dolmamış PR DoD'u geçemez
- Org-wide kural · `trescout-{landing,app,brand-kit,kit}` repolarının tamamında geçerli
