# What is In-process?

It is the execution of a process within the program's own workspace, without the need for outside help.

## Overview
It is a software that completes the operation within its own borders without connecting to another server or external service. This method offers speed and security advantages by ensuring that the data does not leave the application. Everything happens under one roof, in the same memory space.

*Analogy: It's like doing a job in your own office, with your own employees, instead of outsourcing it to someone else.*

## How it works
While the program is running, it uses the structures it keeps in its own memory instead of pulling the required data from an external database. In this way, no network traffic occurs and the transaction is completed much faster.

## Where it is used
It is frequently preferred in fast running applications and database operations.

## Commonly confused with
It can be confused with client-server architecture, where the system is completely self-contained.

## Frequently asked questions
**Should we always work in-process?**
No, if your data is very large or needs to be shared, external systems make more sense.

**Is there much difference in speed?**
Yes, since there is no time to retrieve data over the network, in-process operations are fast in milliseconds.


## Related terms
- [In-process Vector Database](/en/dictionary/in-process-vector-database/)
- [Runtime](/en/dictionary/runtime/)
- [Memory Management](/en/dictionary/memory-management/)

## Related tools
- [Turso](/en/discover/turso/)
- [Zvec](/en/discover/zvec/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/in-process/
