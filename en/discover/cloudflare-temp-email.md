# Free temporary email on Cloudflare

Cloudflare Temp Email is an open-source platform that allows you to set up a completely free, serverless disposable email service running on your own domain using Cloudflare Workers, Pages, and D1/KV database infrastructure. It protects your personal privacy with inbox management, attachment storage, Telegram bot integration, and automatic cleanup mechanisms.

- ★ 11,734
- TypeScript
- GitHub Trending · 2026-07-23

## Updates

- **September 13, 2026:** Stars 11,391 → 11,734, latest release v1.12.0 (September 13, 2026).
- **August 23, 2026:** Stars 11,332 → 11,391, latest release v1.11.1 (August 22, 2026).
- **August 19, 2026:** Stars 11,156 → 11,332, latest release v1.11.0 (August 19, 2026).
- **August 2, 2026:** Stars 10,884 → 11,156, latest release v1.10.0 (July 31, 2026).

## What you get

- Zero server and operational cost: It runs on Cloudflare's generous free tier (100,000 Workers requests per day, free Email Routing, and Pages hosting) without renting an external server.
- Custom domain and unblockable addresses: Unlike general disposable email services, it generates single-use addresses with your own domain that do not get caught in websites' blacklists.
- Fast email parsing with Rust and WASM: Processes complex incoming MIME, multipart, and HTML-content emails in milliseconds thanks to a WebAssembly module compiled with Rust.
- Telegram bot and instant notifications: Receive notifications directly via Telegram when a new email arrives, read the message content, or instantly create a new address using bot commands.
- Automatic cleaning and secure access: Automatically clears old messages and attachments after a set period; prevents unauthorized access with an admin password.

## How to get started and installation options

To deploy the project, having a Cloudflare account and a domain name managed on Cloudflare DNS is sufficient. You can either deploy via a graphical interface by connecting a GitHub repository with a single click using Cloudflare Pages, or you can publish the D1 database and Worker functions from your local environment via the Wrangler CLI.

- [Resmî kurulum rehberi →](https://temp-mail-docs.awsl.uk)
- [Canlı demo arayüzü →](https://mail.awsl.uk)

## Technical architecture and working principle

- Cloudflare Email Routing integration: All MX traffic destined for your domain is handled by Cloudflare infrastructure and routed directly to the catcher Worker function via the catch-all rule.
- Edge Worker and Rust WASM parser: The incoming email stream (raw stream) is transferred to the optimized Rust WASM engine running inside the Worker to quickly parse headers, body, HTML, and attachments.
- Cloudflare D1 and R2 storage: Email texts and metadata are stored on Cloudflare D1, which is an edge SQLite database. File attachments are optionally written to Cloudflare R2 object storage.
- Modern single-page application (SPA): The user-friendly web interface is served with zero latency via Cloudflare Pages' global CDN network.
- REST APIs and external integrations: Offers the ability to generate new email addresses and query the inbox via REST API endpoints for automated tests or third-party software.

## Installation and sample deployment

**Deployment Steps with Wrangler CLI**

```
# 1. Depoyu klonlayin ve bagimliliklari kurun
git clone https://github.com/dreamhunter2333/cloudflare_temp_email.git
cd cloudflare_temp_email
pnpm install

# 2. Cloudflare D1 veritabanini olusturun
npx wrangler d1 create temp_email_db

# 3. Veritabani semasini calistirin ve yayinlayin
npx wrangler d1 execute temp_email_db --file=./db/schema.sql
pnpm run deploy
```

## If you don't write code

Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to set up the open-source temporary email project dreamhunter2333/cloudflare_temp_email running on Cloudflare with my own domain. I have a Cloudflare account and a domain connected to Cloudflare DNS. Can you explain step by step how to set up Email Routing, D1 database, and the Cloudflare Pages interface from scratch via the Cloudflare dashboard? Also, which configuration steps should I follow to forward incoming emails to my Telegram bot?

## Frequently asked questions

- Is Cloudflare's free plan enough for personal use? Yes. The Cloudflare free tier offers 100,000 Worker requests per day, free Email Routing, and a D1 database quota. For personal use and small teams, it is nearly impossible to exceed these limits, and the system runs at completely zero cost.
- Is a custom domain required to use the service? Yes. To receive emails, you must have a domain name (or subdomain, e.g., mail.yourdomain.com) managed on Cloudflare DNS. This allows you to easily bypass sites that block public temporary email services.
- Are incoming emails stored permanently? No, this is a temporary email service. As the system administrator, you can set the retention period for emails from the panel (for example, 1 hour, 24 hours, or 7 days); expired records are automatically deleted from D1 and R2 storage.
- Can email replies be sent outbound via the service? Yes. Although Cloudflare Email Routing only supports receiving emails, when a project is connected to Resend, Brevo, or a custom SMTP server API, it also supports sending emails to the outside world and replying from the web panel.

## Related dictionary terms

- [CLI](https://trescout.com/en/dictionary/cli/)
- [Rust](https://trescout.com/en/dictionary/rust/)
- [API](https://trescout.com/en/dictionary/api/)
- [Open Source](https://trescout.com/en/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is intended for developers, test teams, and privacy-focused users who want to host a free, secure, and unblocked temporary email service with their own domain.
- **License:** MIT (Özgür açık kaynak lisansı)
- **Infrastructure:** Cloudflare Workers, Pages, D1 (SQLite) and Email Routing
- **Languages and Tools:** TypeScript, Rust (WASM), Vue 3, Wrangler

## Links

- [GitHub repository →](https://github.com/dreamhunter2333/cloudflare_temp_email)
- [Read in Turkish →](https://trescout.com/discover/cloudflare-temp-email/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-07-23: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/cloudflare-temp-email/
