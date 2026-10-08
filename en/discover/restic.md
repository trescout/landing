# Back up your data safely by encrypting it

Developed with the Go language, Restic offers an open source backup program that backs up data quickly and efficiently by encrypting it. This tool, which supports different storage systems, saves storage space with the incremental backup method.

- ★ 35,302
- GitHub Trending · 2026-06-12

**TreScout note:** It stores your backups by encrypting them and does not take up space because it does not write the same file twice. It does not have a clickable interface, it runs from the command line and you set the task of cleaning old backups, otherwise the storage will swell over time. Try restoring a file the same day you installed it: you won't be able to tell otherwise that the backup actually worked.

## Updates

- **August 2, 2026:** Stars 34,273 → 35,302, latest release v0.19.1 (July 5, 2026).

## What you get

- Provides high security by encrypting data
- Saves storage space with incremental backup
- Compatible with different cloud and local storage systems

## Installation

**macOS · Homebrew**

```
brew install restic
```

**Windows · winget**

```
winget install restic.restic
```

## Running it

**Create Backup Repository**

```
restic init --repo /path/to/repo
```

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to back up my data securely using Restic. How can I export a local folder or specific directory to an encrypted backup storage? Can you please explain step by step how to create the backup store and start the initial backup process so that my data is encrypted?

## Related dictionary terms

- [Backup Program](https://trescout.com/en/dictionary/backup-program/)
- [Incremental Backup](https://trescout.com/en/dictionary/incremental-backup/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is suitable for all users who want to back up their data quickly and efficiently by encrypting it.
- **License:** BSD-2-Clause

## Links

- [GitHub repository →](https://github.com/restic/restic)
- [Read in Turkish →](https://trescout.com/discover/restic/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-06-12: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/restic/
