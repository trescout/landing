# Open source enterprise resource planning

Odoo is an open source enterprise resource planning platform that allows businesses to manage all their operational processes under a single roof. Developed with Python language, this system offers a wide range of modular business applications from sales to accounting.

- ★ 54,692
- GitHub Trending · 2026-06-04

## Updates

- **September 27, 2026:** Stars 52,082 → 54,692.

## What you get

- It manages business processes such as sales, accounting and warehouse from a single center.
- It offers modular business applications that are compatible with each other.
- It provides an open source infrastructure that can be customized according to need.

## Installation

**Start PostgreSQL database**

```
docker run -d --name odoo-db -e POSTGRES_DB=postgres -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=change_me postgres:15
```

**Start Odoo with database connection**

```
docker run -d --name odoo --link odoo-db:db -p 127.0.0.1:8069:8069 odoo:latest
```

## Running it

**Access Local UI**

```
http://localhost:8069
```

## Getting started

- Official source →

## Related dictionary terms

- [Enterprise Resource Planning](https://trescout.com/en/dictionary/enterprise-resource-planning/)

- **Who it is for:** It is suitable for businesses that want to manage all their operational processes on a single platform.

## Links

- [GitHub repository →](https://www.odoo.com)
- [Read in Turkish →](https://trescout.com/discover/odoo/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-06-04: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/odoo/
