# Download iOS IPA packages directly

Ipatool is an open-source command-line tool that allows you to search, license, and download iOS, iPadOS, tvOS, and visionOS application packages (IPA files) directly from the Apple App Store. Written in Go, it facilitates app archival and security research without requiring a physical iPhone or iTunes.

- ★ 10,388
- Go
- GitHub Trending · 2026-08-31

## Updates
- August 31, 2026: Stars 10,388, stable release v2.1.4 (Apple StoreKit API compatibility and 2FA enhancements).

## What you get
- Device-independent IPA downloads: Fetch official IPA packages directly from Apple servers without physical iPhones, iPads, or Macs.
- Account authentication with 2FA support: Authenticate securely to the App Store directly through your local terminal with two-factor verification.
- Free app licensing (Purchase): Acquire free app licenses on your Apple ID account with a single command before downloading.
- Cross-platform compatibility: Built with pure Go, running seamlessly across macOS, Linux, and Windows with zero Apple software dependencies.
- Automation & CI/CD friendly: Fully scriptable CLI ready to integrate into mobile security auditing and archiving pipelines.

## Installation

**Install via Homebrew or Go**

```
brew tap majd/repo https://github.com/majd/repo
brew install ipatool
# or with Go:
go install github.com/majd/ipatool@latest
```

## Running it

**Login with Apple ID**

```
ipatool auth login --email user@icloud.com
```

**Search for an app**

```
ipatool search "Telegram"
```

**Download IPA package**

```
ipatool download -b org.telegram.Telegram-iOS
```

## Technical architecture and working principle

Ipatool parses Apple's private client protocols to interact directly with App Store cloud endpoints:
- Apple StoreKit and Bag protocol emulation: Emulates iTunes Bag, buyProduct, and downloadProduct API endpoints to authenticate as a genuine iOS client.
- FairPlay DRM sinf packaging: Downloaded IPAs preserve Apple's official DRM encryption signatures and purchase metadata exactly as delivered to devices.
- OS Keyring integration: Safely stores session authentication tokens within the operating system keychain rather than plain text files.

## Security analysis and sideloading scenarios

Downloaded IPA files unlock valuable capabilities for security researchers and independent developers:
- Static code and vulnerability analysis: Rename the IPA extension to .zip to extract Info.plist, embedded frameworks, and Mach-O binaries for inspection in Ghidra.
- Sideloading and resign: Re-sign legitimate IPA binaries with TrollStore, AltStore, or custom enterprise certificates for testing on personal hardware.
- Legacy version archival: Archive historical releases of critical applications using exact version identifiers.

## If you do not code
🤖 If you do not code
I want to download an iOS IPA package using ipatool, inspect its contents, and examine the Info.plist permissions and embedded frameworks for security auditing. Can you guide me step by step on how to log in with ipatool, search and download the IPA, and unpack it for static analysis?

- **Who it is for:** iOS security researchers, mobile developers, reverse engineers, and IPA archivers.
- **License:** MIT (Permissive open source license)
- **Framework:** Go-based cross-platform CLI
- **Platforms:** macOS, Linux, Windows

## Frequently asked questions
- Is it safe to enter Apple ID credentials? Ipatool is open source and never sends credentials to third-party servers; it communicates directly with official Apple endpoints and saves tokens in your local OS Keychain. For security audits, using a secondary Apple ID is standard practice.
- Can it download paid apps for free? No. Ipatool is not a piracy tool. It only licenses and downloads apps that are already owned by your Apple ID or available for free.
- Are downloaded IPAs decrypted (DRM-free)? No. Downloaded IPAs contain Apple's original FairPlay DRM encryption. Decrypting the binary requires dumping from memory on a jailbroken or Corellium device.
- Does it run on Linux servers without Xcode? Yes. Since it is written in pure Go without Xcode dependencies, it runs out of the box on Linux and Windows servers.

## Links
- [GitHub →](https://github.com/majd/ipatool)

## Related dictionary terms
Sideloader CLI Open Source API Apple Silicon

---
Source: TreScout Discover · https://trescout.com/en/discover/ipatool/
