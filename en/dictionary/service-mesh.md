# What is Service Mesh?

*Dictionary · Dev · Last updated: September 22, 2026*

Service mesh is the invisible infrastructure layer that manages the traffic of microservices.

## Definition and Word Origin

In a system with hundreds of parts, it is difficult for the parts to find each other and talk securely. Service mesh manages communication, regulates traffic, and ensures security. It enforces network policy without touching the code.

***Analogy:** It is like the tower that manages flight traffic at a major airport; It allows shuttles to move safely without crashing into each other.*

## How to Know and Use in Daily Life?

**Cloudy:** Large applications with microservices.
**Bank:** Strictly secured service traffic.
**E-commerce:** Order line under campaign load.

## Technical Depth and Architecture

Parts:

**Sidecar:** Small proxy next to each service, traffic flows from here.
**Control plane:** The brain that distributes the rules.
**Data plane:** Delegates who do the work.
**mTLS:** Inter-service encrypted identity.
**Durability:** Retry and circuit breaker.

Retry rule:

```
retries:
  attempts: 3
  perTryTimeout: 2s
```

Istio and Linkerd are known applications. In a small system, the cost exceeds the benefit.

## Use in Different Disciplines

**Airport:** The tower that prevents planes from colliding.
**Traffic:** The signaling network that regulates flow.
**Mail:** Distribution center that sorts the shipment.

## Frequently Asked Questions

**Is it necessary for every project?**

No. It creates a burden on a low-service system. As chaos grows, it gains meaning.

**What does it cost?**

Adds memory and latency per proxy. Paid for observability gain.

**Is Kubernetes necessary?**

No, but often used together. There are versions that also run on virtual machines.

**Does it replace API gateway?**

No. Gateway is the external door, mesh is the internal traffic. The two work together.

## Related terms

- [Cloud Native](https://trescout.com/en/dictionary/cloud-native/)
- [API](https://trescout.com/en/dictionary/api/)
- [Proxy](https://trescout.com/en/dictionary/proxy/)

## Related tools

- [Meshery](https://trescout.com/en/discover/meshery/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/service-mesh/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/service-mesh/
