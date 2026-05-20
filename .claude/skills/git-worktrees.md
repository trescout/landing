---
name: git-worktrees
description: Paralel feature çalışma · git worktree ile izole branch'lerde çalışıp main'i kirletmeden iş yap.
trigger: Birden fazla feature paralel · experimentation · paralel agent dispatch
applies-to:
  - "**/*"
---

# Skill · Git Worktrees

## Ne zaman aktif

Aynı anda 2+ feature üzerinde çalışılacaksa, riskli experimentation yapılacaksa, paralel agent dispatch gerekiyorsa. Stash/checkout dance'ından kaçınmak için.

## Procedure

### Yeni worktree aç

```bash
# Mevcut branch'ten kopya
git worktree add ../trescout-app-experiment experiment-branch

# Yeni branch ile
git worktree add -b feat/new-feature ../trescout-app-feat-new

# Mevcut remote branch'i checkout
git worktree add ../trescout-app-hotfix origin/hotfix
```

### İzole çalış

```bash
cd ../trescout-app-experiment
npm install              # her worktree kendi node_modules'ünü kullanır
npm run dev              # ayrı port (3001 vb.) gerekebilir
```

### Test/lint passing olunca merge veya PR

```bash
# Test passing
npm run typecheck && npm run lint && npm test

# PR aç (orig dir'e dönmeden)
gh pr create --base main --title "feat: ..."

# Veya local merge
cd /Users/.../trescout-app  # orig
git merge experiment-branch
```

### Worktree temizle

```bash
# İşi bittiyse
git worktree remove ../trescout-app-experiment

# Force gerekirse (uncommitted changes varsa)
git worktree remove --force ../trescout-app-experiment
```

## İyi örnek

```bash
# 3 paralel iş
git worktree add ../trescout-app-mobile-nav feat/mobile-nav
git worktree add ../trescout-app-pdf-rewrite feat/pdf-rewrite
git worktree add ../trescout-app-hotfix-auth fix/auth-redirect

# 3 ayrı terminal'de paralel agent çalıştır
# (Claude Code session per worktree)
```

## Anti-patterns

- ❌ Main branch'te paralel feature (`git stash` dance, kaos)
- ❌ Worktree'ye `node_modules` paylaştırmaya çalışmak (her worktree kendi başına bağımsız)
- ❌ Worktree silmeden branch silmek (`git worktree remove` ile yap)
- ❌ Aynı port'a iki dev server (Next.js 3001/3002/3003 olarak çalıştır)

## Detay

- `git worktree --help` · resmi dökümanlar
- Kaynak: obra/superpowers `using-git-worktrees` skill'i
- TreScout için tipik: `trescout-app/` ana + `trescout-app-exp/` paralel
