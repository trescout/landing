# QUIC and HTTP/3 support with Rust

Developed by Cloudflare, quiche provides a Rust implementation of the QUIC transport protocol and the HTTP/3 network standard. Aimed at accelerating internet traffic, this library offers a low-level infrastructure for developers looking to optimize network performance.

- ★ 12,638
- GitHub Trending · 2026-09-20

## What you get
- Implementing the QUIC transport protocol
- Working on the HTTP/3 network standard
- Processing low-level network packets

## Installation
**Clone the project**

```
git clone https://github.com/cloudflare/quiche
```


## Running it
**Run the client**

```
cargo run --bin quiche-client -- https://cloudflare-quic.com/
```

**Run the server**

```
cargo run --bin quiche-server -- --cert apps/src/bin/cert.crt --key apps/src/bin/cert.key
```


## If you don't write code
I want to use this library, written in the Rust programming language, to process QUIC packets and manage network connection states. After cloning the project, what steps should I follow to run the client and the server?

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/quiche/
