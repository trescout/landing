# What is SBOM?

> Software Bill of Materials

It is an inventory document that lists all open source libraries and components used in a software.

## Overview
SBOM is the list of contents of the software. Just like an ingredient label that lists the ingredients in a product, it transparently reveals what parts the software consists of. In this way, when a security vulnerability arises in the software, you can immediately understand whether that part is in your system or not.

*Analogy: It's like the table of ingredients on the back of a ready-made meal you buy from the grocery store; It allows you to see which substances are used.*

## How it works
Automated tools scan your software, dump all used libraries into a file and keep this list up to date.

## Where it is used
It is used in software security audits, enterprise software supply chain management and open source projects.

## Commonly confused with
Not to be confused with the source code of the software; This is just an inventory list.

## Frequently asked questions
**Why is SBOM important?**
When a vulnerable library is found, it allows you to quickly detect all your systems that use that library.

**Should every software have SBOM?**
Yes, it is now becoming the standard for security transparency, especially in the modern software world.


## Related terms
- [Open Source](/en/dictionary/open-source/)
- [Observability](/en/dictionary/observability/)
- [API](/en/dictionary/api/)

## Related tools
- [Trivy](/en/discover/trivy/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/sbom/
