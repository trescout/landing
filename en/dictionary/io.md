# What is I/O?

*Dictionary · Dev · Last updated: September 22, 2026*

> Input/Output

I/O (Input/Output) is the system's data exchange with the outside world.

## Definition and Word Origin

Keyboard typing, downloaded file, result printed on the screen: All are I/O operations. The system talks to the outside world through this channel. It is like the senses and hands of the computer.

***Analogy:** It is like a person receiving information from the outside world and reacting to the outside world; eyes are input, speech is output.*

## How to Know and Use in Daily Life?

**Keyboard:** Text entry.
**Network:** File download.
**Screen:** Don't show results.

## Technical Depth and Architecture

Concepts:

**Blocking:** Don't wait until the process is finished.
**Non-blocking:** Don't wait, let me know when the results come.
**Buffer:** Intermediate tank that balances the speed difference.
**Bottleneck:** The slowest link slows down the entire line, usually disk or network.

File reading example:

```
const veri = await fs.readFile("not.txt", "utf8");
```

This line does not wait until the file arrives, other work continues. It continues when the result is ready.

## Use in Different Disciplines

**Person:** Eye-ear input, speech output.
**Restaurant:** Order entry, service exit.
**Factory:** Raw material input, product output.

## Frequently Asked Questions

**Why is I/O a bottleneck?**

Processor is fast, disk and network are slow. When the data does not catch up, the system waits and this is where the bottleneck occurs.

**What is blocking?**

It is a call that waits until the result comes. It crashes the interface, wastes work on the server.

**How to speed it up?**

With cache, batch read and asynchronous call. It is measured first, then the slowest ring is corrected.

**What does async have to do with it?**

It is another way of doing work while waiting. A lot of work can be done with a single thread.

## Related terms

- [API](https://trescout.com/en/dictionary/api/)
- [Data Pipeline](https://trescout.com/en/dictionary/data-pipeline/)
- [Streaming Applications](https://trescout.com/en/dictionary/streaming-applications/)

## Related tools

- [Asio](https://trescout.com/en/discover/asio/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/io/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/io/
