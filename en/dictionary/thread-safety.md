# What is Thread-safety?

*Dictionary · Dev · Last updated: September 22, 2026*

Thread safety means that a code does not corrupt data when executed by more than one thread at the same time.

## Definition and Word Origin

"Thread" means thread and "safety" means security. The security here is not to protect against hackers, but to keep the data consistent: If two processes update the same account at the same time, the result may be incorrect. Thread-safe code rules this race. Banking applications, web servers, and any multiprocessor software need it.

***Analogy:** It's like putting a lock on the door in a house with only one toilet; While one is inside, the other has to wait.*

## How to Know and Use in Daily Life?

**Banking:** Two withdrawal requests from the same account do not reduce the balance to negative.
**Ticket sales:** The last seat should not be sold to two people at once.
**Counters:** The visitor counter increments by a full increment with each request.

## Technical Depth and Architecture

Typical tools are:

**Lock (Mutex/Lock):** One thread enters the critical region at a time, the other one waits.
**Atomic operation:** Indivisible single-step reading and writing.
**Immutable data:** Data that cannot be changed does not enter the race, it is copied.
**Messaging:** Communication via queue instead of shared data (e.g. Go channels).

A small Python example:

```
import threading
kilit = threading.Lock()
with kilit:
    bakiye += 100
```

No other threads can intervene while locked rows are running. If the lock is forgotten or retrieved in the wrong order, the program may hang (deadlock). That's why the critical region is kept short.

## Frequently Mixed Things

It is not about cybersecurity. The issue is not hackers, but data consistency: Two processes touching the same data at the same time do not crush each other.

## Use in Different Disciplines

**Traffic:** Lights that determine the order of crossing on a single-lane bridge.
**Kitchen:** Cooks taking turns using a single knife.
**Library:** A single copy of the book changes hands with the loan book.

## Frequently Asked Questions

**What happens if it is not thread-safe?**

Data gets messed up, calculations turn out to be wrong, or the app crashes. It is difficult to debug because the error does not repeat on every try.

**Should a lock be added to every code?**

No. In single-threaded code, the lock introduces unnecessary overhead. Only concurrent partitions that touch common data are preserved.

**What is deadlock and how to prevent it?**

It means that two processes are stuck waiting for each other to unlock. Taking the locks in the same order and keeping the critical region short reduces the risk.

**Can it be caught by testing?**

It is difficult to catch, because the error depends on timing. Load testing and special race detectors are used.

## Related terms

- [Concurrency](https://trescout.com/en/dictionary/concurrency/)
- [System Programming Language](https://trescout.com/en/dictionary/system-programming-language/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/thread-safety/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/thread-safety/
