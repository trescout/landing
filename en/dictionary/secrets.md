# What is Secrets?

These are the passwords, API keys and access codes that software applications need to operate securely.

## Overview
Secrets are confidential information that a program uses to authenticate itself when connecting to another system. These can often be database passwords, private keys, or service access tokens. Since embedding this information in the code poses a security risk, it is usually stored in special vault systems.

*Analogy: It is like the key you use to open the door of your house; If you put this key under the doormat anyone can break in, so you need to keep it in a safe safe.*

## How it works
Instead of writing this confidential information into code files, developers securely define it to the application using environment variables or confidential management tools.

## Where it is used
It is used in cloud services, database connections and application authentication processes.

## Commonly confused with
It can be confused with regular user passwords, but these are digital identities designed for machines, not people.

## Frequently asked questions
**Why aren't Secrets kept within the code?**
When you share your code or accidentally upload it to the internet, anyone can obtain these keys and infiltrate your systems.

**What should I do if Secrets is stolen?**
You should immediately cancel that key, create a new one, and check if there is any infiltration in your system.


## Related terms
- [API](/en/dictionary/api/)
- [Self-hosting](/en/dictionary/self-hosting/)
- [Observability](/en/dictionary/observability/)

## Related tools
- [Trivy](/en/discover/trivy/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/secrets/
