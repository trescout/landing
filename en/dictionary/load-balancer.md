# What is Load Balancer?

*Development · Last updated: November 20, 2026*

It is a traffic router that prevents system crashes and improves performance by distributing incoming network traffic across multiple servers.

## Overview

A load balancer distributes user requests coming to a website or digital service evenly across a pool of backend servers. It prevents a single server from being overwhelmed under heavy load and instantly redirects traffic to healthy servers in case of hardware failures. This ensures your system provides uninterrupted, fast, and reliable service.

***Analogy:** It is similar to a queue management system in a busy bank branch that directs customers to available counters in order to prevent crowding in front of a single teller.*

## How it works

Instead of going directly to the server, the network request from the user first meets the load balancer. The system directs the request to the most appropriate server using algorithms such as Round Robin, least connections, or server response time. Simultaneously, it monitors the health status of the servers and automatically removes those that fail from the traffic flow.

## Where it is used

It is used in e-commerce platforms serving millions of users, microservice-based cloud architectures, and financial systems that cannot tolerate downtime.

## Commonly confused with

It can be confused with an API Gateway. While an API Gateway focuses on functions like authentication, request transformation, and API management, a load balancer primarily aims to distribute traffic efficiently among servers.

## Questions and answers

**Is using a load balancer mandatory?**

It is not mandatory for simple sites with low traffic, but it becomes indispensable for preventing outages when your application grows and a single server is no longer sufficient.

**What is the difference between software and hardware load balancers?**

Hardware models are dedicated physical devices placed in data centers. Software models, such as NGINX or HAProxy, are flexible programs that run in cloud environments and on standard servers.

## Related terms

- [API Gateway](https://trescout.com/en/dictionary/api-gateway/)
- [Reverse Proxy](https://trescout.com/en/dictionary/reverse-proxy/)
- [Microservices](https://trescout.com/en/dictionary/microservices/)
- [Cloud Computing](https://trescout.com/en/dictionary/cloud-computing/)

This explanation was written in plain language for TreScout with AI and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/load-balancer/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/load-balancer/
