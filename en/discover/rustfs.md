# High-performance object storage system

RustFS was developed as an S3-compatible high-performance object storage system. It offers interoperability and data migration support with other S3-compatible platforms such as MinIO and Ceph.

- ★ 33,264
- Rust
- GitHub Trending · 2026-09-19

## What you get
- Provides high speed and memory safety with the Rust language
- Works seamlessly with existing tools thanks to its S3-compatible structure
- Offers unrestricted commercial use with the Apache 2.0 license

## Installation
**Start with the installation script**

```
curl -O https://rustfs.com/install_rustfs.sh && bash install_rustfs.sh
```

**Run the latest version with Docker**

```
docker run -d -p 9000:9000 -p 9001:9001 -v $(pwd)/data:/data -v $(pwd)/logs:/logs rustfs/rustfs:latest
```


## Running it
**Start the system using Docker Compose**

```
docker compose -f docker-compose-simple.yml up -d
```


## If you don't write code
I want to set up a high-performance object storage environment using RustFS. How can I manage my data by leveraging the system's S3 compatibility, and what should I pay attention to when scaling on a distributed architecture? Provide me with a step-by-step guide on the installation and basic configuration settings of this Apache 2.0 licensed system.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/rustfs/
