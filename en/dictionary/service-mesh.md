# What is Service Mesh?

Service mesh is the invisible infrastructure layer that manages the traffic of microservices.

## Definition and Word Origin
In a system with hundreds of parts, it is difficult for the parts to find each other and talk securely. Service mesh manages communication, regulates traffic, and ensures security. It enforces network policy without touching the code.

## How to Know and Use in Daily Life?
Cloud: Large applications with microservices. Bank: Tightly secured service traffic. E-commerce: Order line under campaign load.

## Technical Depth and Architecture
Parts:

## Use in Different Disciplines
Airport: The tower that does not collide planes. Traffic: The signal network that regulates the flow. Mail: The distribution center that separates the shipment.

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
- [Cloud Native](/en/dictionary/cloud-native/)
- [API](/en/dictionary/api/)
- [Proxy](/en/dictionary/proxy/)

## Related tools
- [Meshery](/en/discover/meshery/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/service-mesh/
