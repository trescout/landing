# What is Proxy?

*Dictionary · Dev · Last updated: September 22, 2026*

Proxy (in Turkish, proxy server) is the intermediary that transmits your requests to the target on your behalf.

## Definition and Word Origin

"Proxy" means proxy. It acts like a guard between your computer and the internet: You connect to the site through a proxy, not directly. It is used for identity concealment and traffic management.

***Analogy:** It's like you convey the message through your friend rather than directly; The buyer sees the middleman, not you.*

## How to Know and Use in Daily Life?

**Company:** Control of exit traffic.
**Security:** Address hiding.
**Access:** Regional constraint exceedance.

## Technical Depth and Architecture

There are two directions:

**forward:** Hide the client, go out.
**Reverse:** It protects the server and lets it in. Nginx does this job.

Types: HTTP, HTTPS and SOCKS. Environment variable example:

```
export https_proxy="http://vekil:8080"
```

It also keeps the cache: Frequently requested content is delivered from the proxy, the line is relaxed.

## Frequently Mixed Things

It is considered a VPN. VPN tunnels the entire device, while proxy usually operates at the application or browser level. The depth of privacy varies.

## Use in Different Disciplines

**Friend:** The person who forwards the message on your behalf.
**Reception:** The officer who greets the visitor.
**Interpreter:** The medium that conveys the word.

## Frequently Asked Questions

**Is it safe?**

It depends on the proxy. Untrustworthy server may monitor traffic, so known provider is chosen.

**Why is it used?**

For control, privacy and access. All three are separate needs.

**What is Reverse?**

It is the direction that distributes what comes from outside to the server. Provides load balancing and protection.

**Does it speed up?**

On cached content yes, on encrypted and remote traffic it generally slows it down.

## Related terms

- [Self-Hosting](https://trescout.com/en/dictionary/self-hosting/)
- [Offline](https://trescout.com/en/dictionary/offline/)
- [VPN](https://trescout.com/en/dictionary/vpn/)

## Related tools

- [OmniRoute](https://trescout.com/en/discover/omniroute/)
- [Litellm](https://trescout.com/en/discover/litellm/)
- [FlClash](https://trescout.com/en/discover/flclash/)
- [Nginx](https://trescout.com/en/discover/nginx/)
- [Freellmapi](https://trescout.com/en/discover/freellmapi/)
- [Headroom](https://trescout.com/en/discover/headroom/)
- [User Scanner](https://trescout.com/en/discover/user-scanner/)
- [OpenFlux](https://trescout.com/en/discover/openflux/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/proxy/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/proxy/
