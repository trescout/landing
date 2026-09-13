# What is Worktree?

It is a structure that allows you to work on different versions of a project simultaneously without changing the same project folder.

## Overview
Worktree allows you to open different branches of a project in separate folders without disrupting your main workspace while developing software. For example, while developing a feature in the main project, you can simultaneously fix an old bug in another folder. This eliminates the time loss and confusion caused by constantly switching branches.

*Analogy: It is like keeping two different books open on separate desks while working on them at the same time; you don't have to bother flipping pages to switch from one to the other.*

## How it works
You add a new worktree via version control systems like Git. The system links a copy of the project to a different directory for you, and you continue working there without touching the main directory.

## Where it is used
It is used in complex software projects in situations where urgent bug fixes are required during long-running feature developments.

## Commonly confused with
It is not the same as just copying folders; worktrees are connected to the same Git repository and work in synchronization with each other.

## Frequently asked questions
**Why don't we just copy separate folders?**
Copying wastes disk space and makes managing Git history difficult; worktree, on the other hand, is much more efficient.

**Does it work in every Git project?**
Yes, this feature is supported in all modern Git versions.


## Related terms
- [Source Control](/en/dictionary/source-control/)
- [Git Push](/en/dictionary/git-push/)
- [Repository Checkout](/en/dictionary/repository-checkout/)

## Related tools
- [Worktrunk](/en/discover/worktrunk/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/worktree/
