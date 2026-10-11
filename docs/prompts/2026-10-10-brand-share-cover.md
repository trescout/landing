# Brand share cover · 2026-10-10

## Brief and scope

The user requested a stronger default link-preview cover for trescout.com: make
TreScout immediately recognizable, explain that it is a daily technology report,
and retain the existing teal palette, simple composition, and canonical logo.

The app repository owns the renderer in `scripts/gen-og-image.ts`. Landing serves
its 1200 × 630 output at `/og-image.png`. The six homepages use
`?v=20261010-brand` in `og:image`, `twitter:image`, and the Organization schema's
`image` field. Other default-image consumers retain their existing URLs. Dated
report images and their metadata are outside this change.

## Copy and review status

- New descriptor: “Günlük teknoloji raporu” (draft).
- Existing hero tagline retained: “Teknoloji takibi artık bir iş yükü değil.”
- Gemini CLI was attempted by the coordinating Codex agent but could not run
  because `GEMINI_API_KEY` was not configured. No Gemini copy review occurred.
- Claude CLI was attempted by the coordinating Codex agent but could not run
  because it was not logged in. No Claude copy review occurred.
- Codex inspected the repository's brand and copy-review instructions. That
  inspection does not replace either required model review.
- The descriptor remains a draft pending the required copy review or an explicit
  user exception. This work does not authorize merging or publishing it.

## Implementation and verification brief

Change only the three default-image URL references on each existing homepage
(`index.html`, `en/`, `fr/`, `pt/`, `es/`, and `de/`). Preserve all other page
content. Run the SEO/GEO guard and verify that the homepage generator preserves
each complete `<head>` after regeneration using an isolated output fixture.

The metadata audit identified `scripts/ana-sayfa.py` as a body-only generator,
with existing homepage heads as the canonical metadata source. The locale shell
refresher changes nav and footer only. No generator edit is required to preserve
these versioned URLs.

Verification completed locally:

- `python3 scripts/check-seo-geo.py`: passed for 9,510 HTML pages, 623 tools,
  705 terms, and 1,385 unique report descriptions; no endpoint request sent.
- `scripts/ana-sayfa.py`: regenerated all six homepages against the current
  report data in an isolated temporary output tree. Every complete `<head>` was
  unchanged and retained all three versioned image references.
- Exact comparison with the original six homepage files: only the 18 requested
  URL replacements changed.
- `git diff --check`: passed.

## AI traceability

- Plan and implementation: OpenAI Codex, with separate rendering and metadata
  work delegated within the same task.
- Repository skills consulted: `brand-voice-check`, `gemini-translation`,
  `ai-traceability-fill`, and `code-review-pre`.
- Human input: design direction and scope. No human-written implementation is
  claimed.
- Gemini review: not completed.
- Claude review: not completed.
- Commit, push, merge, and publication: not performed by the metadata agent.
