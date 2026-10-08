# What is Logging?

*Dictionary · Dev · Last updated: September 22, 2026*

Logging means writing down the program's events chronologically.

## Definition and Word Origin

"Log" means log, record. When the program silently fails, what it has done so far is read from the log. It is like the plane's black box: It is the first place checked after an accident.

***Analogy:** It is like the plane's black box that records flight data; The program's transactions are logged.*

## How to Know and Use in Daily Life?

**Presenter:** Debugging.
**Product:** Usage tracking.
**Security:** Event log.

## Technical Depth and Architecture

Levels:

**DEBUG:** Developer detail.
**INFO:** Normal flow.
**WARN:** Suspicious situation.
**ERROR:** Failed business.

Rules:

**Configured record:** JSON format, searchability.
**PII prohibition:** Password and ID are not recorded.
**Rotation:** When the file grows, it is archived.

Example:

```
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Ödeme alındı: sipariş=%s", siparis_id)
```

Over-recording slows down the system, under-recording leaves it blind. INFO is opened in production and DEBUG is opened in case of a problem.

## Frequently Mixed Things

It is thought to be observability. However, logging is its building block: The log is the raw material, observation ability is the product.

## Use in Different Disciplines

**Black box:** Flight data recording.
**Journal:** Chronological notes.
**Camera recording:** Event archive.

## Frequently Asked Questions

**Is it good to save everything?**

No. Too much slows down and hides the important, keeping a balanced record.

**What is the level?**

It is the urgency tag of the record. It acts as a filter in the search.

**Where are the records written?**

File to central system or cloud service. Central collection is recommended in production.

**How long is it stored?**

It depends on the policy. Debugging takes weeks, auditing takes years.

## Related terms

- [Observability](https://trescout.com/en/dictionary/observability/)
- [Traces](https://trescout.com/en/dictionary/traces/)
- [Logs](https://trescout.com/en/dictionary/logs/)

## Related tools

- [OmniRoute](https://trescout.com/en/discover/omniroute/)
- [Spdlog](https://trescout.com/en/discover/spdlog/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/logging/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/logging/
