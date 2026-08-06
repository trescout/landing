# What is Auto-fallback?

When an error occurs in a system or the main method fails, the system automatically switches to a safer or alternative method.

## Overview
Auto-fallback ensures the system doesn't 'give up'. For example, when your most advanced AI model fails to respond, the system automatically switches to a faster but simpler model to complete the process. This is a critical security measure to ensure that the user experience continues uninterrupted.

*Analogy: It's like when your car's main engine fails, it automatically switches to the electric engine with backup battery and doesn't leave you stranded.*

## How it works
A 'if it doesn't work, do this' rule is built into the software. The system constantly checks the status and activates the backup method whenever the main method returns an error code.

## Where it is used
It is used in artificial intelligence services, network connections and server management.

## Commonly confused with
It is similar to error handling; However, auto-fallback refers directly to an alternative solution.

## Frequently asked questions
**Does this feature cause slowness?**
Sometimes the transition process may cause a delay of milliseconds, but it is better than a complete halt of the system.

**Does it always work?**
If the backup method is also faulty, the system will continue to fail, so backups must also be reliable.


## Related terms
- [Observability](/en/dictionary/observability/)
- [Runtime](/en/dictionary/runtime/)
- [AI Gateway](/en/dictionary/ai-gateway/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/auto-fallback/
