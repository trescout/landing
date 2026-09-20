# What is Object Storage System?

It is a large-scale storage method that stores data with unique identifiers instead of file folders.

## Overview
The file system on your traditional computer is like a tree structure; it proceeds in the form of folders within folders. Object storage, on the other hand, treats data as an object and gives it a unique identifier. This way, instead of following folder paths to reach the data, you can access it quickly by using that identifier directly.

*Analogy: It is like scanning a magic barcode pasted on a book in a library and having the book instantly teleported into your hand, instead of finding it with shelves and numbers.*

## How it works
When data is uploaded to the system, it becomes an object and some descriptions (metadata) are added to it. When you need it, you call this object via its identifier.

## Where it is used
It is used in cloud storage services, large data backups, and the delivery of media content.

## Commonly confused with
It can be confused with normal hard disk file systems; however, this system is designed for much larger data.

## Frequently asked questions
**Why doesn't it use folders?**
Because managing billions of pieces of data in a folder structure is very slow, while the object system is much faster.


## Related terms
- [Database](/en/dictionary/database/)
- [Cloud Computing](/en/dictionary/cloud-computing/)
- [Data Layer](/en/dictionary/data-layer/)

## Related tools
- [Rustfs](/en/discover/rustfs/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/object-storage-system/
