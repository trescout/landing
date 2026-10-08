# What is Clone?

*Dictionary · Dev · Last updated: September 22, 2026*

Clone is the process of creating a local copy of a remote Git repository along with its entire history.

## Definition and Word Origin

"Clone" means exact copy in English. In the Git world, it is used with the git clone command: You download not only the current files, but also the entire commit history, branches and tags of the project.

***Analogy:** It's like taking a photo of not just one page of a book in the library, but having the entire copy of the book on your own shelf.*

## How to Know and Use in Daily Life?

When you want to review or contribute to an open source project, the first step is usually to clone it:

```
git clone https://github.com/kullanici/proje.git
```

When the command runs, a project folder is created in your current directory. If the repository is very large, a shallow clone is used to fetch only a portion of the history:

```
git clone --depth 1 https://github.com/kullanici/proje.git
```

## Technical Depth and Architecture

The .git directory inside the cloned folder is the memory of the repository: All commit objects, branch pointers, and the remote address reside here. After the clone:

git fetch downloads remote changes but does not touch your files.
git pull downloads and merges into your current branch.
git push sends your commits to the remote (if you have permission).
A fork creates a copy on the server side. A clone downloads that copy or the original repository to your computer. The two are different concepts.

## Use in Different Disciplines

**Biology:** The genetic copy of the living thing. The clone in the software is a copy of the data, it has nothing to do with the living organism.
**Media:** Spare costumes to work on while the original remains.
**Virtualization:** Producing a new machine from a ready-made mold.

## Frequently Asked Questions

**Can I change the project after cloning?**

Yes. You can make any changes you wish to your own copy. The original repository is not affected. If you want to propose your change to the project, you open a pull request.

**What is the difference between fork and clone?**

Fork creates a copy on the server (in your account), clone downloads that copy to your computer. The contribution flow is usually in the form of fork, then clone.

**What should I do if the warehouse is too large?**

Shallow clone with --depth 1 or download only single branch (--single-branch). You can deepen the history later if you need it.

**Do I keep the clone updated?**

Yes. Just run git pull inside the folder. If you have changes, you need to commit or stash them first.

## Related terms

- [CLI](https://trescout.com/en/dictionary/cli/)
- [Open Source](https://trescout.com/en/dictionary/open-source/)
- [Self-Hosting](https://trescout.com/en/dictionary/self-hosting/)

## Related tools

- [MoneyPrinterTurbo](https://trescout.com/en/discover/moneyprinterturbo/)
- [VoxCPM](https://trescout.com/en/discover/voxcpm/)
- [Clone-Wars](https://trescout.com/en/discover/clone-wars/)
- [Univer](https://trescout.com/en/discover/univer/)
- [OpenStock](https://trescout.com/en/discover/openstock/)
- [Hermes WebUI](https://trescout.com/en/discover/hermes-webui/)
- [Production Agentic RAG Course](https://trescout.com/en/discover/production-agentic-rag-course/)
- [Flowsint](https://trescout.com/en/discover/flowsint/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/clone/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/clone/
