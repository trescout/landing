# What is Logging?

It is the chronological recording of a program to keep track of the operations it performs or the errors it encounters while it is running.

## Overview
Programs sometimes silently error out. Thanks to logging, when an error occurs, you can see step by step what the program has done so far and what data it has processed. This is sort of the 'black box' of the program.

*Analogy: Just like the black box of an airplane that records all its data during flight, the program records all its movements in a log.*

## How it works
You add commands such as 'came here', 'this data was processed' into the code. As the program runs, this information is written to a file or monitoring system.

## Where it is used
It is used in server applications, large software systems and debugging processes.

## Commonly confused with
It can be confused with Observability; Logging is one of the fundamental building blocks of this observability.

## Frequently asked questions
**Is it good to save everything?**
No, too many logs can slow down the system and make it difficult to find critical errors; Balanced records should be kept.


## Related terms
- [Observability](/en/dictionary/observability/)
- [Traces](/en/dictionary/traces/)
- [Logs](/en/dictionary/logs/)

## Related tools
- [Spdlog](/en/discover/spdlog/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/logging/
