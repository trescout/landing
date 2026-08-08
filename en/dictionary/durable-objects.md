# What is Durable Objects?

They are small software units that run continuously on the Internet and can store data without losing their state.

## Overview
Normally, programs on the Internet are temporary, but these structures operate without interruption by keeping the data within themselves. They don't forget the data even when a user interaction ends. Ideal for maintaining consistency in distributed systems.

*Analogy: Instead of an app that wakes up only when necessary, it's like a secretary who's always on alert and never leaves her notebook.*

## How it works
They live on the server with a specific identity and process every incoming request with the current status in their memory.

## Where it is used
It is used in real-time games, chat applications, and web services whose state must be maintained.

## Commonly confused with
Not to be confused with temporary server functions (serverless); because they start from scratch every time.

## Frequently asked questions
**Where is the data stored?**
It is stored within the volume itself, i.e. directly as part of the operating environment.


## Related terms
- [Runtime](/en/dictionary/runtime/)
- [State Management](/en/dictionary/state-management/)
- [Distributed](/en/dictionary/distributed/)

## Related tools
- [Celld](/en/discover/celld/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/durable-objects/
