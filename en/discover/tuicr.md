# Reviewing code with Vim in the terminal

Developed with the Rust language, tuicr is a terminal user interface-based code review tool that supports Vim keyboard shortcuts. It allows developers to manage their code review process directly from the terminal.

- ★ 2,795
- Rust
- GitHub Trending · 2026-07-31

## What you get
- Quick code review in terminal with Vim shortcuts
- Post comments directly to GitHub and GitLab
- Structured output support for AI tools

## Installation
**Standard installation**

```
curl -fsSL tuicr.dev/install.sh | sh
# or
brew install agavra/tap/tuicr
```

**Alternative package managers**

```
# Cargo
cargo install tuicr

# Mise
mise use github:agavra/tuicr

# Nix
nix run github:agavra/tuicr
```


## Running it
**Review local changes**

```
tuicr -w
```

**Review a specific PR**

```
tuicr pr 125
```


## If you don't write code
Review this code review and prepare a structured list of any bugs or improvement suggestions you find, with each comment identified by file path and line number. While doing the review, provide concrete suggestions that will increase the readability and performance of the code, based on the data in markdown format that I copied from tuicr.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/tuicr/
