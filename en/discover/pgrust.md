# PostgreSQL rewritten with Rust

The pgrust project, in which the PostgreSQL database management system was rewritten with the Rust programming language, successfully completes all regression tests. This work aims to modernize the database architecture with a language focused on memory safety.

- ★ 3,957
- Rust
- GitHub Trending · 2026-07-12

## Update
- August 2, 2026: Star 2,171 → 3,957, final version v0.2-release (July 30, 2026).

## What you get
- Disk compatibility with Postgres 18.3
- More than 46 thousand regression test successes
- Modern architecture focused on memory security

## Installation
**Quick trial with Docker**

```
docker run -d --name pgrust -e POSTGRES_PASSWORD=secret malisper/pgrust:v0.1 && until docker exec -e PGPASSWORD=secret pgrust psql -h 127.0.0.1 -U postgres -c '\q' >/dev/null 2>&1; do sleep 1; done && docker exec -it -e PGPASSWORD=secret pgrust psql -h 127.0.0.1 -U postgres; docker rm -f pgrust
```


## If you don't write code
What is the main purpose of the Pgrust project, how is disk compatibility with existing PostgreSQL ensured, and how is artificial intelligence-supported programming used in the development of the project? Tell us about the compatibility of the current version of Pgrust with Postgres 18.3 and its success in regression testing.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/pgrust/
