# What is Network Stack?

The Network Stack is the collection of hardware drivers, kernel, and user-space protocol layers that enable an operating system or hardware to transmit, route, and receive data packets over a network.

## 1. Layered architecture: OSI 7 Layer vs TCP/IP 4 Layer
In network communication, the OSI 7-Layer Model defined by ISO is used in theory, and in practice the TCP/IP Model, which forms the backbone of the Internet:

## 2. Packet encapsulation and decapsulation flow
When a client sends a request to a web server, as the data moves down the stack, each layer adds its own header:

## 3. Network Stack lifecycle in the Linux kernel

## 4. Kernel Bypass and next-generation networking: eBPF / XDP and DPDK

## Frequently asked questions
**What does 'network stack' mean, and what is its Turkish equivalent?**
In Turkish, it is called "ağ yığını" or "protokol yığını". It is a hierarchy of hardware and software rules layered on top of each other that enables a computer to communicate over a network.

**Where is the fundamental difference between TCP and UDP located within the network stack?**
It is located at the Transport Layer (L4). TCP guarantees that packets arrive complete and in order via an acknowledgment mechanism (ACK); UDP, on the other hand, fires packets at maximum speed without waiting for acknowledgment.

**What is MTU (Maximum Transmission Unit)?**
It is the largest packet size that a network interface can carry in a single frame without fragmentation. For standard Ethernet, the MTU value is 1500 bytes.

**Why is Kernel Bypass architecture used?**
It is used to eliminate the interrupt and memory copying overheads of the Linux kernel at extremely high data volumes such as 100 Gbps, and to process packets directly at the hardware level with zero latency using DPDK and eBPF/XDP.


## Related terms
- [VPN](/en/dictionary/vpn/)
- [Runtime](/en/dictionary/runtime/)
- [Memory Management](/en/dictionary/memory-management/)
- [Packet Fragmentation](/en/dictionary/packet-fragmentation/)
- [API](/en/dictionary/api/)

## Related tools
- [OpenFlux](/en/discover/openflux/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/network-stack/
