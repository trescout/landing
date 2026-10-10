# Download iOS IPA packages directly

Ipatool is an open-source command-line tool that allows you to directly search, license, and download iOS, iPadOS, tvOS, and visionOS application packages (IPA files) via the Apple App Store. Developed in Go, the tool enables app archiving and security research without the need for a physical iPhone device or iTunes software.

- ★ 11,571
- Go
- GitHub Trending · 2026-08-31

## Updates

- **October 10, 2026:** Stars 11,407 → 11,571, latest release v2.7.0 (October 9, 2026).
- **September 27, 2026:** Stars 10,388 → 11,407, latest release v2.6.0 (September 13, 2026).

## What you get

- Device-independent IPA downloading: The ability to pull official IPA packages directly from Apple servers without being connected to a physical iPhone, iPad, or Mac computer.
- Account authorization and 2FA support: Securely manage two-factor authentication (2FA) via the local terminal while logging into the App Store.
- Acquiring a free license (Purchase): Associating previously undownloaded free apps with your Apple ID account with a single command.
- Multiplatform support: Compiled with pure Go to run on macOS, Linux, and Windows systems without any additional Apple dependencies.
- Automation and CI/CD compatibility: A scriptable CLI structure that easily integrates into mobile application security testing and archiving workflows.

## Installation

**Installation via Homebrew or Go**

```
brew tap majd/repo https://github.com/majd/repo
brew install ipatool
```

## Running it

**Sign in with Apple ID and download IPA**

```
ipatool auth login --email ornek@icloud.com
ipatool search "Telegram"
ipatool download -b org.telegram.Telegram-iOS
```

## Technical architecture and working principle

- Apple StoreKit and Bag protocol emulation: Authenticates like the official iOS client by mocking Apple Store API endpoints (iTunes Bag, buyProduct, and downloadProduct).
- FairPlay DRM class packaging: The downloaded IPA file preserves its original structure, including Apple's official DRM encryption blocks and account signature certificates.
- Operating system keyring integration: Stores session tokens and user credentials securely in the operating system's keyring vault instead of as plain text.

## Security analysis and sideloading scenarios

- Static code and vulnerability analysis: Change the extension of the downloaded IPA file to .zip and inspect Info.plist, embedded libraries, and Mach-O binaries using Ghidra.
- Sideloading and signing: Install official IPA files onto test devices by re-signing them using TrollStore, AltStore, or enterprise certificates.
- Legacy version archiving: Back up and store past versions of critical applications via version IDs.

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to download the IPA package of an iOS application to my computer using ipatool, unpack its contents, and examine the embedded libraries and permission configurations in the Info.plist file from a security perspective. Could you explain step-by-step how to log in, search, and download using ipatool in the terminal, and then how to extract the IPA file and perform static analysis?

## Frequently asked questions

- Is it safe to enter my Apple ID credentials? Ipatool is open-source and does not send passwords to a third-party server; it transmits them directly to official Apple servers and stores them in the local Keychain vault. Still, using a secondary or test Apple ID is recommended for security audits.
- Can it download paid apps for free? No. Ipatool is not a piracy tool. It can only license and download apps that your account has previously purchased or that are free in the store.
- Are downloaded IPA files decrypted of their FairPlay DRM? No. Downloaded files have Apple's original FairPlay DRM encryption. To decrypt (dump) the binary, it is necessary to run it on a jailbroken device.
- Does it run on Linux servers without Xcode? Yes. Since Ipatool is written in pure Go, it does not carry a macOS dependency; it runs smoothly as a standalone binary on Linux or Windows servers.

## Related dictionary terms

- [Xcode](https://trescout.com/en/dictionary/xcode/)
- [Sideloading](https://trescout.com/en/dictionary/sideloading/)
- [Binary](https://trescout.com/en/dictionary/binary/)
- [CI/CD](https://trescout.com/en/dictionary/ci-cd/)
- [Terminal](https://trescout.com/en/dictionary/terminal/)
- [CLI](https://trescout.com/en/dictionary/cli/)

- **Who it is for:** iOS security researchers, mobile developers, reverse engineering specialists, and IPA archivers.
- **License:** MIT (Özgür açık kaynak lisansı)
- **Framework:** Go-based cross-platform CLI
- **Platforms:** macOS, Linux, Windows

## Links

- [GitHub repository →](https://github.com/majd/ipatool)
- [Read in Turkish →](https://trescout.com/discover/ipatool/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-08-31: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/ipatool/
