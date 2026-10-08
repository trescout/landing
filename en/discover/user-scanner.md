# OSINT user analysis on more than 465 platforms

Python-based User-Scanner performs open source intelligence (OSINT) scanning across more than 465 social networks, forums, and code repositories from a single username or email.

- ★ 5,007
- Python
- GitHub Trending · 2026-08-31

## Updates

- **September 27, 2026:** Stars 3,910 → 5,007, latest release v1.5.2 (September 17, 2026).

## What you get

- Broad platform coverage: Verify account presence on GitHub, Reddit, Twitter, Steam, Telegram and 465+ sites in one go.
- Asynchronous high-speed scanning: parallel querying hundreds of targets in seconds with asyncio and aiohttp based architecture.
- False positive filtering: Intelligent detection mechanism that verifies error texts in the response body as well as HTTP status codes.
- JSON and CSV report export: Saving analysis results in configured formats for use in forensics and security reports.
- Privacy and local execution: Possibility to run any queries entirely from the local machine, without sending them to third-party servers.

## Installation

**Cloning the repository and installing dependencies**

```
git clone https://github.com/kaifcodec/user-scanner.git
cd user-scanner
pip install -r requirements.txt
```

## Running it

**Scan target username and email**

```
python3 user_scanner.py -u hedef_kullanici
# veya e-posta ile:
python3 user_scanner.py -e hedef@ornek.com
```

## Technical architecture and working principle

- Database Templates (JSON Site Manifests): Modular configuration containing URL patterns, error codes, and profile regexes for 465+ platforms.
- Concurrent Request Pooling: Using network bandwidth most efficiently by caching DNS resolutions and TCP sockets.
- Custom HTTP Headers and User-Agent Rotation: Realistic browser headers simulation to avoid WAF and rate limit obstructions.

## OSINT investigation scenarios and data analysis

- Personal Data Breach and Tracking: Map which social channels the leaked profiles are active on with username correlation.
- Corporate Security Audits: Determine whether company employees open accounts on external platforms with their corporate e-mail addresses.
- Social Engineering Defense: Identify unauthorized imitation accounts early against spear phishing attacks.

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

Can you explain step by step how I can scan more than 465 platforms using a single username using the User-Scanner tool in a security audit, export the findings in JSON format and list suspicious profiles?

## Frequently asked questions

- Is it legal to use User-Scanner? Yes. User-Scanner only queries publicly visible account presence status on public web pages; It does not provide any unauthorized system access or crack passwords.
- Is there Tor or proxy support? Yes. You can mask your IP address and avoid speed limits by routing requests through SOCKS5 or HTTP proxy chains.
- How long does it take to complete the results? Thanks to its asynchronous architecture, scanning of more than 465 platforms is typically completed in 20 to 45 seconds, depending on your internet connection.
- How does email search work? In email mode, public authentication signals are examined at the password reset or account registration endpoints of supported services.

## Related dictionary terms

- [OSINT](https://trescout.com/en/dictionary/osint/)
- [Proxy](https://trescout.com/en/dictionary/proxy/)
- [Open Source](https://trescout.com/en/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** Cybersecurity researchers, OSINT analysts, computer forensics experts and ethical hackers.
- **License:** GPL-3.0 (Açık kaynak copyleft lisansı)
- **Framework:** Python Asynchronous OSINT Scanner
- **Platforms:** Linux, macOS, Windows

## Links

- [GitHub repository →](https://github.com/kaifcodec/user-scanner)
- [Read in Turkish →](https://trescout.com/discover/user-scanner/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-08-31: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/user-scanner/
