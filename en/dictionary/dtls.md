# What is DTLS?

*Development · Last updated: November 7, 2026*

> Datagram Transport Layer Security

It is a secure communication protocol adapted for situations requiring speed and continuity in data transmission.

## Overview

DTLS is a redesign of the TLS protocol, which normally runs on TCP, tailored for networks like UDP that offer continuity but carry the risk of packet loss. In situations where instant data streaming is vital, it minimizes latency without compromising security.

***Analogy:** It is like sending valuable documents by a fast motorcycle courier instead of regular mail; the order of the packets might sometimes get mixed up, but you gain speed.*

## How it works

It takes the encryption and security rules of the TLS logic, but flexes them to handle situations where packets might be lost or their order might change.

## Where it is used

It is used in voice and video call applications, online games, and live streaming protocols.

## Commonly confused with

It is confused with standard TLS; the main difference is that one is secure but slow, while the other is suitable for instant streaming.

## Questions and answers

**Why isn't standard TLS used?**

Standard TLS does not tolerate packet loss and causes stuttering during live broadcasts.

**What type of network does it operate on?**

It generally operates on UDP-based network protocols.

## Related terms

- [TLS](https://trescout.com/en/dictionary/tls/)
- [Network Stack](https://trescout.com/en/dictionary/network-stack/)
- [Streaming Applications](https://trescout.com/en/dictionary/streaming-applications/)

## Related tools

- [Openssl](https://trescout.com/en/discover/openssl/)

This explanation was written in plain language for TreScout with AI and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/dtls/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/dtls/
