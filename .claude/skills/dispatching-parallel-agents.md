---
name: dispatching-parallel-agents
description: Birden fazla bağımsız task için paralel subagent dispatch · context isolation, two-stage review, conflict resolution.
trigger: Birden fazla bağımsız (overlap'siz) task var ki paralel ilerletilebilir
applies-to:
  - "**/*"
---

# Skill · Dispatching Parallel Agents

## Ne zaman aktif

Aynı oturumda birbirinden bağımsız 2+ task var (örn. "auth ekle + ödeme entegre et + email template'i yenile"). Bunları seri yapmak yerine paralel subagent dispatch'le hızlandırılabilir. Kaynak: obra/superpowers `dispatching-parallel-agents` skill'i.

## Procedure

### 1. Bağımsızlık değerlendirmesi

Her task'ı listele, sor:

- [ ] Aynı dosyaya dokunuyor mu? · evet → seri yap, paralel değil
- [ ] Birinin çıktısı diğerinin input'u mu? · evet → seri (DAG)
- [ ] Test execution sırasında race condition var mı? · evet → izole et
- [ ] Aynı external service'i quota'sını tüketir mi? (Gemini RPD vb.) · evet → seri veya batch

Sadece **gerçekten bağımsız** task'ları paralel'e ayır.

### 2. Subagent dispatch

Claude Code'da `Agent` tool ile veya manuel: her task için **fresh context**. Subagent ana session'ın geçmişini bilmez · prompt self-contained olmalı.

İyi prompt yapısı (her subagent için):

```
Task: <kısa açıklama>

Context:
- Repo: trescout-app
- İlgili dosyalar: lib/auth/*, app/(auth)/login/page.tsx
- Mevcut pattern: <kısa not>

Done criteria:
- [ ] Type check geçiyor
- [ ] Test eklenmiş
- [ ] AI Traceability dolu

Çıktı: 
- Değişen dosyaların listesi
- Test sonuçları
- Açık sorular varsa kısa not

Constraints:
- Sadece lib/auth/* dokun, başka klasöre dokunma
- AGENTS.md §3.b Skills Agent pattern'ı kullan
```

### 3. Worktree ile fiziksel izolasyon (opsiyonel)

Subagent'lar dosya sistemine de yazacaksa çakışmaması için worktree:

```bash
git worktree add ../trescout-app-auth feat/auth
git worktree add ../trescout-app-payment feat/payment
git worktree add ../trescout-app-email feat/email
```

Her subagent kendi worktree'sinde çalışır. Sonra ana branch'e merge edersin. (Detay: [`git-worktrees`](git-worktrees.md))

### 4. Two-stage review (obra/superpowers pattern)

Subagent çıktısı geldiğinde, **iki aşamada review**:

#### Stage 1 · Spec compliance

- Done criteria sağlandı mı? (checklist'i fiilen kontrol et)
- Constraint'lere uyuldu mu? (örn. başka klasöre dokunmadı mı)
- Açık sorulara cevap verildi mi?

Spec compliance fail → subagent'a feedback ver, tekrar dispatch et. Code review'a geçme.

#### Stage 2 · Code quality

Spec geçince:

- [`code-review-pre`](code-review-pre.md) skill'ini çalıştır
- AGENTS.md §3.e DoD checklist
- AI Traceability bölümü dolu mu

### 5. Conflict resolution

Paralel subagent'lar farkında olmadan aynı dosyaya dokunduysa (planlamada gözden kaçtı):

- **Conflict bulunsun:** merge sırasında git conflict marker'lar görünür
- **Ana session resolve eder** · her iki versiyonu okur, mantıklı birleşim yapar
- **Subagent'lar yeniden dispatch edilmez** · ana session karar verir

### 6. Çıktı raporlama

Tüm subagent'lar bittikten sonra:

```markdown
## Parallel dispatch sonuç

- ✓ auth · feat/auth · 4 commit · merged
- ✓ payment · feat/payment · 7 commit · merged
- ⚠ email · feat/email · 2 conflict, ana session resolve etti
```

## İyi örnek

Senaryo: "trescout-app'e 3 paralel feature ekle"

```
1. Bağımsızlık check:
   - auth · lib/auth/*, app/(auth)/* · bağımsız
   - payment · lib/payment/*, app/api/checkout · bağımsız
   - email template · lib/email/templates/* · bağımsız
   ✓ Paralel uygun

2. 3 worktree aç:
   git worktree add ../trescout-app-auth feat/auth
   git worktree add ../trescout-app-payment feat/payment
   git worktree add ../trescout-app-email feat/email

3. 3 subagent dispatch (her biri kendi worktree'sinde)

4. Subagent'lar bitti, ana session:
   - Her birinin output'unu Stage 1 review et
   - Stage 1 pass → Stage 2 code review
   - Stage 2 pass → main'e merge

5. Worktree cleanup
```

## Anti-patterns

- ❌ Bağımsız olmayan task'ları paralel dispatch (çakışma kaçınılmaz)
- ❌ Subagent'a context taşımamak (self-contained prompt yazma)
- ❌ Spec compliance review'ı atlayıp doğrudan code review (constraint ihlali yakalayamaz)
- ❌ Subagent çıktısını blind merge (test/lint/typecheck kontrol etmeden)
- ❌ Conflict olunca subagent'ı yeniden dispatch (sonsuz döngü riski; ana session resolve)
- ❌ External service quota'sını paylaşan task'ları paralel (Gemini RPD vb.)

## Detay

- Kaynak: obra/superpowers `dispatching-parallel-agents` + `subagent-driven-development` skill'leri
- Cross-skill: [`git-worktrees`](git-worktrees.md) (fiziksel izolasyon), [`code-review-pre`](code-review-pre.md) (stage 2 review), [`brainstorming`](brainstorming.md) (önce iyi planlama)
- Anthropic `Agent` tool · Claude Code'da fresh subagent dispatch
- Worker pattern: 2-4 paralel subagent verimli, 5+'tan sonra context overhead artar
