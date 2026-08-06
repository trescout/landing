# What is ARQ?

> Automatic Repeat Request

It is an error control mechanism that ensures that information is automatically re-sent when an error occurs during data transmission.

## Overview
When sending data over the Internet, sometimes packets can get lost or corrupted. ARQ checks whether the receiving party has received the data and if it detects an error, it tells the sender 'I did not receive this, send again'. In this way, it is ensured that the data is received completely and without errors.

*Analogy: While talking on the phone, the other party says 'I didn't understand, can you say it again?' It's like saying and you repeating that sentence.*

## How it works
The sender sends the data packet and waits for an acknowledgment. If confirmation is not received within a certain period of time, the package is considered damaged or lost and is sent again.

## Where it is used
It is used in the basic protocols and network protocols of the Internet, such as the TCP protocol.

## Frequently asked questions
**Why is it so important?**
Internet connections are not always perfect; ARQ ensures the reliability of the data.

**Will it cause delay?**
Yes, resending faulty packages can slow down the process a bit.


## Related terms
- [API](/en/dictionary/api/)
- [DNS Tunneling](/en/dictionary/dns-tunneling/)
- [Computer Science](/en/dictionary/computer-science/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/arq/
