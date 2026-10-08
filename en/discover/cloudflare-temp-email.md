# Free temporary email service on Cloudflare

Cloudflare Temp Email is an open-source platform that lets you create a completely free, serverless temporary email (disposable email) service with your own domain using Cloudflare Workers, Pages, and D1/KV storage. It protects personal privacy with inbox management, attachment handling, Telegram bot integration, and automated cleanup mechanisms.

- ★ 11,734
- TypeScript
- GitHub Trending · 2026-07-23

## What you get
- Zero server and operational costs: Runs on Cloudflare's generous free tier (100,000 Workers requests/day, free Email Routing, and Pages hosting) without leasing external servers.
- Custom domain and unblockable addresses: Generates disposable addresses using your own domain that bypass blocklists targeting generic temp mail providers.
- Fast email parsing with Rust and WASM: Efficiently handles complex MIME, multipart, and HTML emails in milliseconds via a compiled WebAssembly module.
- Telegram bot and instant notifications: Receive incoming email notifications directly in Telegram, read message contents, or generate new addresses on the fly.
- Automated cleanup and secure access: Automatically purges expired messages and attachments after a designated retention period while safeguarding administration via access credentials.

## Getting started and deployment options
- Official documentation and setup guide →
- Live demo interface →
Deploying the project requires only a Cloudflare account and a domain managed on Cloudflare DNS. You can either deploy with one click by connecting the GitHub repository to Cloudflare Pages or deploy D1 databases and Worker functions locally using the Wrangler CLI.

## Technical architecture and inner workings
- Cloudflare Email Routing integration: Inbound MX traffic is routed through Cloudflare and directed to the catch-all Worker handler.
- Edge Worker & Rust WASM parser: Raw email streams are ingested into the optimized Rust WASM module to extract headers, body text, HTML, and attachments.
- Cloudflare D1 & R2 storage: Message text and metadata are stored in edge SQLite via Cloudflare D1, while attachments are optionally offloaded to Cloudflare R2.
- Modern Single Page Application (SPA): The frontend is delivered with zero latency through Cloudflare Pages' global edge CDN.
- REST API & external integrations: Programmatic endpoints allow external test suites or CI/CD pipelines to create disposable addresses and fetch validation tokens.
Cloudflare Temp Email eliminates the operational burden of hosting traditional SMTP servers (Postfix, Dovecot) through a modern serverless design:

## Setup and deployment example
**Wrangler CLI Deployment Steps**

```
# 1. Clone repository and install dependencies
git clone https://github.com/dreamhunter2333/cloudflare_temp_email.git
cd cloudflare_temp_email
pnpm install

# 2. Create Cloudflare D1 database
npx wrangler d1 create temp_email_db

# 3. Apply schema and deploy
npx wrangler d1 execute temp_email_db --file=./db/schema.sql
pnpm run deploy
```


## If you do not code
I want to set up the open-source dreamhunter2333/cloudflare_temp_email disposable email project on Cloudflare using my own domain. I have a Cloudflare account and a custom domain configured on Cloudflare DNS. Can you explain step by step how to configure Email Routing catch-all rules, provision the D1 database, and deploy the Cloudflare Pages frontend? Also, what configuration values do I need to integrate incoming notifications with a Telegram bot?

## Frequently asked questions
- Is Cloudflare's free tier sufficient for personal use? Yes. Cloudflare's free tier provides 100,000 Worker requests per day along with free Email Routing and D1 quotas. For individual users and small teams, exceeding these limits is virtually impossible; the setup runs at zero cost.
- Is a custom domain required? Yes. To receive inbound email, you need a domain or subdomain managed on Cloudflare DNS. This gives you a major advantage over shared temporary mail services that are blocked by web platforms.
- Are incoming emails stored permanently? No, this is a disposable email service. Administrators can configure retention windows (such as 1 hour, 24 hours, or 7 days); expired records are purged automatically from storage.
- Can the service send outgoing replies? Yes. While Cloudflare Email Routing only handles inbound delivery, the project supports outbound sending and replies when integrated with Resend, Brevo, or custom SMTP APIs.

## Links
- GitHub repository →
- Read in Turkish →

## Related dictionary terms

---
Source: TreScout Discover · https://trescout.com/en/discover/cloudflare-temp-email/
