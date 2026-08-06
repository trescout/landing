# What is Packet Fragmentation?

It is the process of dividing the data sent over the Internet into smaller pieces according to the carrying capacity of the network.

## Overview
When sending data on the Internet, each network has a maximum size it can carry. If the data you send is larger than this size, the system breaks it into small pieces, delivers it to the destination and reassembles it there.

*Analogy: It's like when you can't fit a very large cargo into a single truck, you divide it into smaller boxes, ship them on different trucks, and reassemble them at the destination.*

## How it works
As data is sent, network devices check the size of the packet. If the limit is exceeded, the packet is fragmented and each fragment is given a 'sequence number'. The receiving device looks at these numbers and assembles the parts in the correct order.

## Where it is used
It happens constantly in the background during internet protocols and networking processes.

## Commonly confused with
It may be confused with data loss, but this is a controlled partitioning process.

## Frequently asked questions
**What happens if parts are lost?**
The receiving device realizes that parts are missing and asks the sender to resend that part.


## Related terms
- [Networking Stack](/en/dictionary/networking-stack/)
- [DNS Tunneling](/en/dictionary/dns-tunneling/)

## Related tools
- [Zapret Discord Youtube](/en/discover/zapret-discord-youtube/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/packet-fragmentation/
