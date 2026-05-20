---
name: code-review-pre
description: PR açmadan önce self-review checklist. Reviewer'ı boş yere yormamak için.
trigger: PR açmaya hazırlanırken, son commit'ten sonra
applies-to:
  - "**/*"
---

# Skill · Code Review (Pre-PR)

## Ne zaman aktif

PR açmaya hazırsın. Push'tan sonra, `gh pr create`'den önce. Reviewer kaybedeceği zamanı self-review ile telafi etmek.

## Procedure

### 1. Diff'i baştan oku

```bash
# Tüm değişiklikleri gör
git diff main...HEAD --stat
git diff main...HEAD

# Sadece dosya listesi
git diff main...HEAD --name-only
```

Sorular:
- Her satır gerçekten gerekli mi? (`CLAUDE.md §3 Cerrahi`)
- Komşu kod "iyileştirilmiş" mi? (atla, ayrı PR)
- Debug log, console.log, TODO bırakılmış mı?

### 2. AGENTS.md §3.e DoD kontrol

```markdown
- [ ] Kabul kriterleri sağlanıyor
- [ ] Type check geçiyor (`npm run typecheck`)
- [ ] Lint geçiyor (`npm run lint`)
- [ ] Birim test eklendi (kritik logic için)
- [ ] Preview deploy yeşil (Vercel)
- [ ] Türkçe içerik varsa Gemini → Claude akışından geçti
- [ ] PR açıklamasında AI Traceability dolduruldu
- [ ] `docs/AI_USAGE_LOG.md` güncellendi
```

### 3. Skills tetiklenmesi gereken alanlar

Türkçe metin değişti mi? → [`brand-voice-check`](brand-voice-check.md) tetikle  
Yeni Gemini call eklediniz mi? → [`gemini-rpd-budget`](gemini-rpd-budget.md) tetikle (app)  
Yeni source connector? → [`source-connector-add`](source-connector-add.md) tetikle (app)

### 4. Test komutlarını fiilen çalıştır

```bash
npm run typecheck && npm run lint && npm test
```

(Yeşilse devam, kırmızıysa PR'ı **açma** önce düzelt)

### 5. Commit history kontrol

```bash
git log main..HEAD --oneline
```

- Her commit message conventional formatta mı? `feat(claude-code): ...`
- "WIP", "fix typo", "trying again" gibi noise commit'ler varsa squash et
- AI tool scope'u doğru mu?

### 6. Secret tarama

```bash
git diff main...HEAD | grep -iE "sk-|api_key|password|token=" && echo "✗ Secret olabilir, kontrol et"
```

## İyi örnek (self-review yorumu)

> "Diff temiz, 3 dosyada değişiklik · sadece Gemini retry logic'i. Test eklendi (`lib/ai/gemini.test.ts`). DoD checklist 8/8 yeşil. AI Traceability: Plan claude-code, Skills claude-code (prompt arşivi `#gemini-retry`), Türkçe içerik yok. Manuel kısım: retry pattern'i AI önerisinden farklı, gerekçe PR'da."

## Anti-patterns

- ❌ "Reviewer bakar zaten" diye self-review atlamak
- ❌ Type check kırmızıyken PR açmak (Vercel preview de kırmızı olur)
- ❌ AI Traceability bölümünü boş bırakmak (`AGENTS.md §3.d` zorunlu)
- ❌ "Test'i sonra ekleyeceğim" PR'da (DoD eksik)
- ❌ Debug log, TODO, console.log bırakmak

## Detay

- `AGENTS.md §3.e` · Definition of Done
- `AGENTS.md §3.d` · AI Traceability zorunluluğu
- Kaynak: obra/superpowers `requesting-code-review` skill'i (PR review hazırlığı yönü)
