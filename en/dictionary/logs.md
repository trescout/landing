# What is Logs?

*Dictionary · Dev · Last updated: September 22, 2026*

A log is a time-stamped line of system events.

## Definition and Word Origin

"Log" means ship's log: The captain writes down what happens in a notebook. Software also writes what it does in the background line by line. In case of an error, the notebook is opened, and the time is checked. It is the primary source of system health.

***Analogy:** It is like an airplane's black box; it records throughout the flight, and in case of a problem, it is rewound.*

## How to Know and Use in Daily Life?

**Presenter:** Debugging.
**Application:** Crash report.
**Security:** Event trace.

## Technical Depth and Architecture

Rules of good logging:

**Timestamp:** Time on every line.
**Level:** Distinction between INFO and ERROR.
**Rotation:** Archive when the file grows.
**PII prohibition:** Personal data is not included in the log.

Sample line:

```
2026-09-22T10:00:01 sipariş=4521 sonuc=ok sure_ms=38
```

Searching becomes easier in this format. Scattered text cannot be searched, structured records can.

## Frequently Mixed Things

Often mistaken for trace. A log is a record of an event, trace is the path of the event. One is a photograph, the other is a film.

## Use in Different Disciplines

**Black box:** Flight data.
**Journal:** Chronological notes.
**Receipt:** Transaction log.

## Frequently Asked Questions

**Why are logs necessary?**

The cause of the crash is in the logs. A system without logs flies blind.

**Where should it be written?**

To a file or central system. Centralized collection is recommended for production.

**How long is it stored?**

It depends on the policy. Debugging takes weeks, auditing takes years.

**Is personal data recorded?**

No. Passwords and identities are not recorded; they are masked.

## Related terms

- [Observability](https://trescout.com/en/dictionary/observability/)
- [QA](https://trescout.com/en/dictionary/qa/)
- [Traces](https://trescout.com/en/dictionary/traces/)

## Related tools

- [Grafana](https://trescout.com/en/discover/grafana/)
- [Modly](https://trescout.com/en/discover/modly/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/logs/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/logs/
