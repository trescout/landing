# What is Clone?

Clone is the process of creating a local copy of a remote Git repository along with its entire history.

## Definition and Word Origin
"Clone" means exact copy in English. In the Git world, it is used with the git clone command: You download not only the current files, but also the entire commit history, branches and tags of the project.

## How to Know and Use in Daily Life?
When you want to review or contribute to an open source project, the first step is usually to clone it:

## Technical Depth and Architecture
The .git directory inside the cloned folder is the memory of the repository: All commit objects, branch pointers, and the remote address reside here. After the clone:

## Use in Different Disciplines
Biology: The genetic copy of the living thing. The clone in the software is a copy of the data, it has nothing to do with the living thing. Media: Backup costumes to be used while the original remains. Virtualization: Producing a new machine from a ready-made mold.

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
- [CLI](/en/dictionary/cli/)
- [Open Source](/en/dictionary/open-source/)
- [Self-Hosting](/en/dictionary/self-hosting/)

## Related tools
- [MoneyPrinterTurbo](/en/discover/moneyprinterturbo/)
- [VoxCPM](/en/discover/voxcpm/)
- [Clone-Wars](/en/discover/clone-wars/)
- [OpenStock](/en/discover/openstock/)
- [Hermes WebUI](/en/discover/hermes-webui/)
- [Flowsint](/en/discover/flowsint/)
- [Production Agentic RAG Course](/en/discover/production-agentic-rag-course/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/clone/
