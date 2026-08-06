# Manage your travel plans together

TREK is a self-hosted travel planning application that offers features like real-time collaboration, interactive maps, and budget management. With progressive web application (PWA) support and single sign-on (SSO) integration, it allows users to organize their travel processes digitally.

- ★ 7,040
- GitHub Trending · 2026-06-26

## What you get
- Create daily travel routes and plans with drag and drop
- Tracking group expenses and dividing them per person
- Automatic travel and budget management with artificial intelligence integration

## Installation
**Quick installation with Docker**

```
ENCRYPTION_KEY=$(openssl rand -hex 32) docker run -d -p 3000:3000 \
  -e ENCRYPTION_KEY=$ENCRYPTION_KEY \
  -v ./data:/app/data -v ./uploads:/app/uploads mauriceboe/trek
```


## If you don't write code
You are a travel assistant. Using the MCP (Model Context Protocol) tools on TREK, create a 3-day Paris travel plan for me, adjust my budget based on daily spending limits, and create a packing list for what I need to take with me.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/trek/
