# What is Intermediate CA?

*Development · Last updated: October 21, 2026*

> Intermediate Certificate Authority

An intermediary authority situated between the root certificate, which verifies the identity of secure websites, and the end user.

## Overview

An intermediate certificate authority (intermediate CA) is an intermediate trust institution authorized by the root certificate authority that forms the basis of secure HTTPS connections on the internet. Since using the root certificate directly on servers open to the internet creates a security risk, this task is delegated to intermediate certificates. Thus, digital security certificates can be securely distributed to websites while protecting the main chain of trust.

***Analogy:** It is similar to the government giving an authorization certificate to a neighborhood headman (muhtar) to carry out approval processes instead of issuing IDs directly from its own central registry.*

## How it works

When your browser visits a website, the server presents you with a certificate chain. This chain starts from the end-user certificate, passes through the intermediate certificate, and reaches the pre-installed root certificate on your device, establishing a bond of trust.

## Where it is used

It takes an active part in SSL/TLS certificate management, web server configurations, and corporate security infrastructures.

## Commonly confused with

It is not the main root certificate itself, but an intermediate step acting as a bridge that carries trust between the root and the endpoint.

## Questions and answers

**Why isn't the root certificate used directly instead of an intermediate certificate?**

If the private key of the root certificate is compromised, all internet security could collapse; therefore, the risk is limited with intermediate certificates.

**How do browsers validate the intermediate certificate?**

The server transmits missing intermediate certificates to the browser, and the browser completes the validation using the built-in trust chain.

## Related terms

- [End-to-End Encryption](https://trescout.com/en/dictionary/end-to-end-encryption/)
- [Identity Provider](https://trescout.com/en/dictionary/identity-provider/)
- [OIDC](https://trescout.com/en/dictionary/oidc/)
- [Vulnerability Scanning](https://trescout.com/en/dictionary/vulnerability-scanning/)

This explanation was written in plain language for TreScout with AI and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/intermediate-ca/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/intermediate-ca/
