# What is Logs?

A log is a time-stamped line of system events.

## Definition and Word Origin
"Log" means ship's log: The captain writes down what happens in a notebook. Software also writes what it does in the background line by line. In case of an error, the notebook is opened, and the time is checked. It is the primary source of system health.

## How to Know and Use in Daily Life?
Server: Debug.Application: Crash report.Security: Event trace.

## Technical Depth and Architecture
Rules of good logging:

## Frequently Mixed Things
Often mistaken for trace. A log is a record of an event, trace is the path of the event. One is a photograph, the other is a film.

## Use in Different Disciplines
Black box: Flight data. Log: Chronological notes. Receipt: Transaction record.

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
- [Observability](/en/dictionary/observability/)
- [QA](/en/dictionary/qa/)
- [Traces](/en/dictionary/traces/)

## Related tools
- [Grafana](/en/discover/grafana/)
- [Modly](/en/discover/modly/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/logs/
