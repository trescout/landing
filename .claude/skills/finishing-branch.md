---
name: finishing-branch
description: Feature task tamamlandı · branch nereye gidecek? Merge/PR/discard karar matrisi.
trigger: Feature/fix tamamlandı, "iş bitti, sırada ne var?"
applies-to:
  - "**/*"
---

# Skill · Finishing Branch

## Ne zaman aktif

Feature task tamamlandı (test pass, DoD complete). Branch'in akıbeti belirlenecek: merge mi, PR mi, discard mi?

## Procedure

### 1. Final test çalıştır

```bash
npm run typecheck && npm run lint && npm test
git log main..HEAD --oneline   # commit history özet
git diff main...HEAD --stat    # değişen dosyalar
```

Bir adımda kırmızı varsa **durup düzelt** önce.

### 2. Karar matrisi

| Durum | Aksiyon |
|---|---|
| Production-ready, başkalarının inceleyeceği | **PR aç** · `gh pr create` |
| Solo proje, lokal merge OK | **Doğrudan merge** · `git checkout main && git merge` |
| Çalıştı ama düşündüğümden farklı, başlangıca dön | **Discard** · `git checkout main && git branch -D` |
| Henüz tamam değil, devam | **Devam** · branch'i koru, push et |

### 3. PR yolu (en yaygın)

`code-review-pre` skill'ini çalıştır (self-review). Sonra:

```bash
git push -u origin <branch>
gh pr create --base main --title "feat(claude-code): ..." --body "$(cat <<EOF
## Özet
<...>

## AI Traceability
<doldur · AGENTS.md §3.d>

## Test planı
<...>
EOF
)"
```

PR URL'sini kullanıcıya ver. Reviewer atayıp bekle.

### 4. Doğrudan merge yolu

```bash
git checkout main
git pull
git merge --no-ff <branch>      # merge commit kalır, history net
git push
git branch -d <branch>          # local branch sil
git push origin --delete <branch>  # remote branch sil
```

### 5. Discard yolu

```bash
git checkout main
git branch -D <branch>          # force delete (uncommitted'ı umursamaz)
```

Worktree varsa: `git worktree remove --force ../<dir>`

### 6. AI Usage Log

Merge sonrası `docs/AI_USAGE_LOG.md`'ye satır ekle (`AGENTS.md §3.e DoD`):

```markdown
| 2026-MM-DD | Burhan | <görev> | claude-code | Skills Agent | #PR_NUMBER |
```

## İyi örnek

> "Test passing, AI Traceability dolu, Vercel preview yeşil. Düşman tarama yok. PR yolu seçildi · `gh pr create` ile açıldı, Burhan'a atandı. AI_USAGE_LOG.md'ye yeni satır eklendi. Branch local'de duruyor, merge sonrası silinecek."

## Anti-patterns

- ❌ Test passing olmadan PR/merge
- ❌ AI Traceability boşken PR
- ❌ Merge sonrası branch'i silmemek (clutter)
- ❌ Worktree silmeden branch silmek (`git worktree remove` ile yap)
- ❌ AI Usage Log güncellemeyi atlamak (`AGENTS.md §3.e DoD` ihlali)
- ❌ Force push to main (branch protection olmasa bile)

## Detay

- `AGENTS.md §7 PR akışı`
- `AGENTS.md §3.e DoD` · AI_USAGE_LOG zorunlu
- Kaynak: obra/superpowers `finishing-a-development-branch` skill'i
- Cross-skill: [`code-review-pre`](code-review-pre.md), [`ai-traceability-fill`](ai-traceability-fill.md)
