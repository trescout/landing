# Manage bulk pull requests

Developed by GitHub, gh-stack is a command line tool that makes it easy to create and manage stacked pull requests during the software development process. It aims to speed up the review process by dividing complex code changes into small and independent parts.

- ★ 911
- Go
- GitHub Trending · 2026-08-02

## Update
- August 2, 2026: Star 860 → 911, latest version v0.1.0 (July 29, 2026).

## What you get
- Breaks large code changes into small and manageable pieces
- Automatically organizes dependencies between pull requests
- Facilitates rebase operations to keep branches within the stack up to date

## Installation
**Installing the tool**

```
gh extension install github/gh-stack
```

**Enable AI support**

```
gh skill install github/gh-stack
```


## Running it
**Starting a new stack**

```
gh stack init
```

**Adding a new layer to the stack**

```
gh stack add api-endpoints
```


## If you don't write code
I use the gh-stack tool to create stacked pull requests on GitHub. Include my existing working branches in a stack structure, manage dependencies between branches, and push the stack to GitHub to speed up the code review process.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/gh-stack/
