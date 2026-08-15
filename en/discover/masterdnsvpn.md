# Bypass censorship blocks with DNS tunneling

MasterDnsVPN is a low-load domain name system tunneling (DNS tunneling) virtual private network (VPN) solution developed to bypass censorship barriers. Written in Go language, the tool offers high packet loss stability and resolver load balancing features in data transmission.

- ★ 6,870
- Go
- GitHub Trending · 2026-06-11

## What you get
- It provides data transmission in censored networks via DNS tunneling method.
- It offers multipathing and load balancing for low packet loss and high speed.
- Optimized for stable connection even under restricted network conditions.

## Installation
**Automatic Server Setup**

```
bash <(curl -Ls https://raw.githubusercontent.com/masterking32/MasterDnsVPN/main/server_linux_install.sh)
```

**Running with Docker**

```
docker run -d \
  --name masterdnsvpn \
  --restart unless-stopped \
  -e DOMAIN=v.example.com \
  -v $(pwd)/data:/data \
  -p 53:53/tcp \
  -p 53:53/udp \
  ghcr.io/masterking32/masterdnsvpn:latest
```


## If you don't write code
I want to establish a secure connection via DNS tunneling in a censored network using the MasterDnsVPN tool. How can I configure the server side using the shared auto-install script and what basic steps should I follow to ensure the connection on the client side? Please detail the network requirements I should pay attention to during the installation process and the method of running it via Docker.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/masterdnsvpn/
