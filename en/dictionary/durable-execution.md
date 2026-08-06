# What is Durable Execution?

It is a system that allows a process to continue safely where it left off, even if there is an error or interruption.

## Overview
Normally, if a computer program loses power or fails while it's running, everything is deleted and you have to start over. Durable execution records each step of the program, remembering where it left off at the time of the interruption. In this way, transactions that take hours can be completed safely.

*Analogy: It's like putting a bookmark while reading a book so you don't forget the page; You can continue where you left off.*

## How it works
The system constantly backs up the state of the program to a database. When an error occurs, the system restarts the process from the last backed up point.

## Where it is used
It is used for bank transfers, long data processing processes and complex artificial intelligence workflows.

## Commonly confused with
It may be confused with autosave, but this preserves the entire program's operating logic, not just the file.

## Frequently asked questions
**Should every program be durable?**
It is not needed for short transactions, but is essential for critical transactions that last for hours.

**Why is it so important?**
In case of a mistake, starting the entire process from scratch is a waste of both time and money.


## Related terms
- [State Management](/en/dictionary/state-management/)
- [Runtime](/en/dictionary/runtime/)

## Related tools
- [Pg Durable](/en/discover/pg-durable/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/durable-execution/
