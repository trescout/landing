# What is Resolver Load Balancing?

It is the process of preventing system overload by distributing Internet address queries to multiple servers.

## Overview
When internet traffic is very heavy, a single server cannot keep up with all the queries. This method prevents the system from crashing by redirecting queries to different servers like a traffic cop. This ensures a fast and uninterrupted connection at all times.

*Analogy: It's like melting the queue in a supermarket by directing all customers to 10 different checkouts instead of going to one checkout.*

## How it works
Install a load balancer software and distribute incoming DNS queries equally among the servers you define.

## Where it is used
It is used on large websites and high-traffic network infrastructures.

## Commonly confused with
It may be confused with just server clustering, but this method focuses specifically on managing query traffic.

## Frequently asked questions
**Will the site speed up thanks to this system?**
Yes, response times are shorter as the load on the server is reduced.

**What happens if a single server goes down?**
The load balancer keeps the site running by redirecting to other servers.


## Related terms
- [Proxy](/en/dictionary/proxy/)
- [Reverse Proxy](/en/dictionary/reverse-proxy/)
- [Runtime](/en/dictionary/runtime/)

## Related tools
- [MasterDnsVPN](/en/discover/masterdnsvpn/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/resolver-load-balancing/
