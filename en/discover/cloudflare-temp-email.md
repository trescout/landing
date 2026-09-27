# Free temporary email on Cloudflare

Cloudflare Temp Email is an open-source platform that allows you to set up a completely free, serverless disposable email service running on your own domain using Cloudflare Workers, Pages, and D1/KV database infrastructure. It protects your personal privacy with inbox management, attachment storage, Telegram bot integration, and automatic cleanup mechanisms.

- ★ 11,734
- TypeScript
- GitHub Trending · 2026-07-23

## What you get
- Zero server and operational cost: It runs on Cloudflare's generous free tier (100,000 Workers requests per day, free Email Routing, and Pages hosting) without renting an external server.
- Custom domain and unblockable addresses: Unlike general disposable email services, it generates single-use addresses with your own domain that do not get caught in websites' blacklists.
- Fast email parsing with Rust and WASM: Processes complex incoming MIME, multipart, and HTML-content emails in milliseconds thanks to a WebAssembly module compiled with Rust.
- Telegram bot and instant notifications: Receive notifications directly via Telegram when a new email arrives, read the message content, or instantly create a new address using bot commands.
- Automatic cleaning and secure access: Automatically clears old messages and attachments after a set period; prevents unauthorized access with an admin password.

## How to get started and installation options
- Official installation guide →
- Live demo interface →

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
I want to set up the open-source temporary email project dreamhunter2333/cloudflare_temp_email running on Cloudflare with my own domain. I have a Cloudflare account and a domain connected to Cloudflare DNS. Can you explain step by step how to set up Email Routing, D1 database, and the Cloudflare Pages interface from scratch via the Cloudflare dashboard? Also, which configuration steps should I follow to forward incoming emails to my Telegram bot?

## Frequently asked questions
- Is Cloudflare's free plan enough for personal use? Yes. The Cloudflare free tier offers 100,000 Worker requests per day, free Email Routing, and a D1 database quota. For personal use and small teams, it is nearly impossible to exceed these limits, and the system runs at completely zero cost.
- Is a custom domain required to use the service? Yes. To receive emails, you must have a domain name (or subdomain, e.g., mail.yourdomain.com) managed on Cloudflare DNS. This allows you to easily bypass sites that block public temporary email services.
- Are incoming emails stored permanently? No, this is a temporary email service. As the system administrator, you can set the retention period for emails from the panel (for example, 1 hour, 24 hours, or 7 days); expired records are automatically deleted from D1 and R2 storage.
- Can email replies be sent outbound via the service? Yes. Although Cloudflare Email Routing only supports receiving emails, when a project is connected to Resend, Brevo, or a custom SMTP server API, it also supports sending emails to the outside world and replying from the web panel.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/cloudflare-temp-email/
