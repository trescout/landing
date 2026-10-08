# What is Gateway?

*Dictionary · Dev · Last updated: September 22, 2026*

A gateway is a connection point that manages traffic between different networks.

## Definition and Word Origin

Gate means door, and way means path. It is a bridge that allows two networks to communicate with each other: the device that connects the internet in your home to the outside world is a typical example. It examines incoming data and decides which network it should go to.

***Analogy:** It is like a border gate of a country; It controls the arrivals and ensures they go in the right direction.*

## How to Know and Use in Daily Life?

**Home modem:** Connects your home to the provider network.
**Corporate gateway:** The control point for office traffic.
**Cloudy:** The gateway between virtual networks.

## Technical Depth and Architecture

Functions of the gateway:

**Network Address Translation (NAT):** Maps internal addresses to a single external address.
**Filtering:** Keeps unwanted traffic at the door.
**Routing:** Delivers the packet to the correct network.

The default route information is as follows:

```
default via 192.168.1.1 dev eth0
```

This line indicates that unrecognized destinations will be sent via the modem. An API gateway, however, is at a different layer: it manages service requests, not network traffic.

## Frequently Mixed Things

It can be confused with an API Gateway. An API Gateway manages software services, while a network gateway operates at the network level. One is an application gateway, the other is a routing gateway.

## Use in Different Disciplines

**Border gateway:** Inspection and routing of arrivals.
**Port:** Customs clearance of ships.
**Reception:** Directing the visitor to the correct floor.

## Frequently Asked Questions

**Can one access the internet without a gateway?**

No. The local network cannot connect to the outside world and remains isolated.

**What is the difference from an API gateway?**

A network gateway carries packets, while an API gateway manages requests. One is the transport layer, the other is the application layer.

**Which one is used at home?**

The gateway inside your modem handles this. No additional settings are required, and addresses are distributed automatically.

**Can two networks be kept separate?**

Yes. By using firewall rules, traffic is blocked, and the networks operate in isolation.

## Related terms

- [API Gateway](https://trescout.com/en/dictionary/api-gateway/)
- [Network Stack](https://trescout.com/en/dictionary/network-stack/)
- [Proxy](https://trescout.com/en/dictionary/proxy/)

## Related tools

- [OmniRoute](https://trescout.com/en/discover/omniroute/)
- [Fanqiang](https://trescout.com/en/discover/fanqiang/)
- [Gitdiagram](https://trescout.com/en/discover/gitdiagram/)
- [OpenWA](https://trescout.com/en/discover/openwa/)
- [Grok2api](https://trescout.com/en/discover/grok2api/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/gateway/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/gateway/
