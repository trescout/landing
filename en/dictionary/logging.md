# What is Logging?

Logging means writing down the program's events chronologically.

## Definition and Word Origin
"Log" means log, record. When the program silently fails, what it has done so far is read from the log. It is like the plane's black box: It is the first place checked after an accident.

## How to Know and Use in Daily Life?
Server: Debugging. Product: Usage monitoring. Security: Event logging.

## Technical Depth and Architecture
Levels:

## Frequently Mixed Things
It is thought to be observability. However, logging is its building block: The log is the raw material, observation ability is the product.

## Use in Different Disciplines
Black box: Flight data record. Log: Date sequence notes. Camera record: Event archive.

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
- [Observability](/en/dictionary/observability/)
- [Traces](/en/dictionary/traces/)
- [Logs](/en/dictionary/logs/)

## Related tools
- [OmniRoute](/en/discover/omniroute/)
- [Spdlog](/en/discover/spdlog/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/logging/
