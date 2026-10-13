# Prompt archive

## site-navigation-notifications

- Date: 2026-10-10
- Tool: OpenAI Codex with focused implementation and read-only audit agents.
- Scope: homepage, shared navigation/footer generators, privacy styles, favicon declarations and cache headers.
- User request: merge the approved standard-logo PRs; investigate the old search icon; add contact and team links to the footer; move comparison out of the top navigation; describe the signup section as notifications rather than early access itself; inspect optional analytics consent; align the privacy footer; place discovery above the sidebar dictionary.
- Constraints: preserve report/editorial and legal content, keep the same changes across all six languages, update publisher templates, do not submit forms or inspect private subscriber records.
- Verification: all read-only CSP workflow commands; favicon normalization self-test and drift guard; 36 browser page/viewport combinations (six locales, homepage/privacy, 1440/390/320 pixels); embedded privacy footer hidden; live favicon hashes matched the merged standard assets.
- Copy provenance: contact/team labels supplied by the user; notification headings drafted by Codex. Gemini CLI was attempted but had no configured API key. Gemini and Claude copy review remain pending and must not be claimed complete.

## Brand share cover · 2026-10-10

[Brief, specialist prompts, review limitations and validation](prompts/2026-10-10-brand-share-cover.md).

## Catalogue browsing · 2026-10-12

Detail follow-up (2026-10-13): user approved the neutral reading-first layout, contextual links/facts/related terms above signup in the right column, with mobile content first. Use a small progressive enhancement that moves the original DOM nodes and preserves form handlers, consent and source attribution. Include the external script in detail pages and final publishing normalization; do not rewrite protected editorial HTML or its generator ownership stamps. No-JS retains the complete original single-column document. Copy reuses the six localized homepage title/intro/button labels; no new claims, no logo changes. Repository design, brand voice, pre-review and traceability workflow applied by Codex; no Gemini/Claude review claimed. Tests cover inclusion/idempotence, complete static fallback and one consent form across all detail pages, and localized copy parity.

Follow-up: user approved a homepage-like right sidebar for dictionary, discovery and report indexes, with signup at the top and 16 catalogue results. Mobile stays content-first. Reuse localized homepage signup copy and canonical consent; retain full static lists and random exploration. Shared layout normalization runs in index generation and final publishing normalization. Test single form, localized privacy, stable regeneration and responsive widths. Detail pages and logo remain a separate task. Codex implementation/review; repository brainstorming, brand voice, traceability and pre-PR workflow applied; no Gemini/Claude review claimed.

CI found pre-existing favicon whitespace drift in 256 report pages from the daily publisher. Preserve already-valid single ICO/SVG pairs regardless of separating whitespace; missing/duplicate fallback repair and self-tests remain. No logo assets changed. Browser validation: 42 route/viewport checks, all six locales at 1280/390 and Turkish/German at 320; no horizontal overflow.

- User approved shortening long dictionary/discovery lists while keeping playful random exploration, then asked to continue after homepage fixes.
- Scope: first 24 matching records, explicit 24-record increments, search/filter across the full collection, filter/sort reset, random navigation from the full matched pool, keyboard focus on the first newly revealed result. Retain full server-rendered HTML for JavaScript-disabled readers and indexing.
- Codex implementation and self-review; six localized short control labels. User waived Gemini review in this conversation. No Gemini/Claude review claimed. Unrelated apple-touch-icon.png edit preserved and excluded.
- Tests: 13 Node regression tests cover both catalogues/six languages, batches, search, empty states, unavailable localized pages, full-pool random target, focus and static fallback. Browser checked 24 locale/type/viewport combinations; live filter/load-more/search interactions verified separately. No subscription submissions or content changes.
- Still deferred: detail-page signup/sidebar redesign and logo orientation comparison.

## Homepage signup layout · 2026-10-12

Follow-up: user requested two items per source instead of 3/2/2/1 and the existing latest-report label parenthesized beside the date. Change generator/CSS across six locales; preserve reports, consent and the user's unrelated apple-touch-icon.png edit. Add snapshot-backed item-count and inline-caption assertions. Codex implementation/review; no new translated copy.

- User approved moving the single signup form to the upper right and history strip to the sidebar, then requested swapping the introduction and latest-report block.
- Final user revision: full-report link and AI note move to the sidebar, immediately above publication history at the very bottom. Logo deferred; merge explicitly requested.
- Preserve report data, legal consent and subscription behavior in six locales. Keep the existing caption below the date. Remove only the second uncertainty sentence from the existing signup copy.
- Tool: Codex. Repository brainstorming, brand-voice, pre-review and traceability guidance used. No new marketing promises.
- Gemini CLI was unavailable (missing configured key); user explicitly waived that check. Claude CLI review was also attempted but unavailable (not logged in); Codex self-review and executable/browser checks are recorded instead, not represented as a Claude review.
- Validation: homepage contract added to CI; subscription/provider/telemetry tests and site guards; responsive DOM checks at 320/390/1440 px across six locales; desktop/mobile screenshot inspection. Live consent-negative request returned 400 without submitting an email or creating a subscriber. This does not prove end-to-end production delivery or a cause for declining signups.
- Deferred: catalogue pagination/random browsing, detail-page sidebars, rotated logo comparison, analytics/Audience investigation. Existing navigation spacing measured and left unchanged.
