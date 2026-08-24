#!/usr/bin/env bash
set -Eeuo pipefail

# Rebuild the generated tree after another writer advances main.
# The caller must reset the checkout to origin/main before invoking this script.
ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

git config user.name "TreScout Bot"
git config user.email "hello@trescout.com"
export GH_TOKEN="${GH_TOKEN:-${GITHUB_TOKEN:-}}"

python3 scripts/dict-sync.py
python3 scripts/dict-cards.py
python3 scripts/discover-sync.py

if [[ -n "${REPROCESS_SLUGS:-}" ]]; then
  python3 scripts/discover-sync.py --reprocess="${REPROCESS_SLUGS}"
fi

if [[ -n "${HEADLINES_LIMIT:-}" && "${HEADLINES_LIMIT}" != "0" ]]; then
  python3 scripts/discover-sync.py --headlines --limit="${HEADLINES_LIMIT}"
fi

python3 scripts/discover-sync.py --refresh || echo "refresh skipped after GitHub API failure"
python3 scripts/cross-link.py
python3 scripts/catalog-render.py
node scripts/translate-i18n.js

LANG_CODES="$(python3 scripts/diller.py --liste)"
for d in $LANG_CODES; do
  [[ "$d" == "en" ]] && continue
  node scripts/translate-i18n.js --lang="$d"
done

for d in $LANG_CODES; do
  python3 scripts/kapak-gorselleri.py --lang="$d"
done

for d in $LANG_CODES; do
  python3 scripts/dictionary-en.py --lang="$d"
  python3 scripts/discover-en.py --lang="$d"
done

for d in $LANG_CODES; do
  python3 scripts/dictionary-en.py --lang="$d"
done

for d in $LANG_CODES; do
  node scripts/build-en.js --lang="$d"
  if [[ -f "$d/index.html" ]]; then
    python3 scripts/dil-kabuk-tazele.py --lang="$d"
  fi
done

for d in $LANG_CODES; do
  node scripts/build-reports-en.js --lang="$d"
done

python3 scripts/discover-index.py
python3 scripts/discover-md.py
python3 scripts/llms-txt.py
python3 scripts/redirect-uret.py
python3 scripts/sitemap-sync.py
node scripts/fix-all-headers-and-footers.js
python3 scripts/hreflang-normalize.py

python3 scripts/check-no-inline-csp.py
python3 scripts/check-nav-consistency.py
python3 scripts/check-footer-consistency.py
python3 scripts/check-logo-consistency.py
python3 scripts/check-headline-consistency.py
python3 scripts/check-brand-typography.py
python3 scripts/check-consent-consistency.py
python3 scripts/check-sayfa-paritesi.py
python3 scripts/check-bolum-paritesi.py || true
python3 scripts/check-birlesmis-terimler.py
python3 scripts/ikiz-tara.py || true
python3 scripts/check-hreflang.py
python3 scripts/check-seo-geo.py
python3 scripts/check-discovery-language.py
python3 scripts/check-discovery-sort.py

if [[ -n "$(git status --porcelain)" ]]; then
  git add -A
  git commit -m "chore(content-sync): rapordan yeni sözlük/keşif içeriği eklendi [skip ci]"
else
  echo "No generated changes after recovery."
fi
