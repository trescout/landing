# What is Traces?

These are monitoring records that show step by step through which stages a transaction goes through in the system.

## Overview
Modern software consists of many parts. When you send a request, it goes through many services. Traces maps which paths this request took from beginning to end and where and how much time it wasted.

*Analogy: It's like tracking a cargo package; You will see step by step which branch the cargo went to, when it departed and where it is waiting.*

## How it works
A special identification tag is attached to each part in the system, and the journey is tracked thanks to this tag.

## Where it is used
It is used in complex software architectures and to solve performance problems.

## Commonly confused with
It is mixed with logs; Logs answer the question 'what happened' and traces answer the question 'where and how long did it take'.

## Frequently asked questions
**Why are traces important?**
It allows you to find out which part of a slow running application is blocked.


## Related terms
- [Observability](/en/dictionary/observability/)
- [Logs](/en/dictionary/logs/)
- [API Gateway](/en/dictionary/api-gateway/)

## Related tools
- [Grafana](/en/discover/grafana/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/traces/
