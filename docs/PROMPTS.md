# Prompt archive

## site-navigation-notifications

- Date: 2026-10-10
- Tool: OpenAI Codex with focused implementation and read-only audit agents.
- Scope: homepage, shared navigation/footer generators, privacy styles, favicon declarations and cache headers.
- User request: merge the approved standard-logo PRs; investigate the old search icon; add contact and team links to the footer; move comparison out of the top navigation; describe the signup section as notifications rather than early access itself; inspect optional analytics consent; align the privacy footer; place discovery above the sidebar dictionary.
- Constraints: preserve report/editorial and legal content, keep the same changes across all six languages, update publisher templates, do not submit forms or inspect private subscriber records.
- Verification: all read-only CSP workflow commands; favicon normalization self-test and drift guard; 36 browser page/viewport combinations (six locales, homepage/privacy, 1440/390/320 pixels); embedded privacy footer hidden; live favicon hashes matched the merged standard assets.
- Copy provenance: contact/team labels supplied by the user; notification headings drafted by Codex. Gemini CLI was attempted but had no configured API key. Gemini and Claude copy review remain pending and must not be claimed complete.
