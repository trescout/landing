# What is Offline-first?

It is a software design approach that allows an application to continue operating all its core functions uninterrupted even if the internet connection is lost.

## Overview
In this approach, the application primarily stores data on the user's own device and performs operations locally. As soon as an internet connection is established, the data on the device is silently synced in the background with the cloud server. As TreScout, we recommend this architecture to keep the user experience at the highest level and to avoid being affected by connection drops.

*Analogy: It is like a smart notebook whose text is not erased when the internet goes out: You keep writing, and when the internet returns, the notebook automatically copies what you wrote to your library in the cloud.*

## How it works
When the application is opened, instead of fetching data from a remote server, it reads it from the local database inside the device. All new records and changes made by the user are first written to this local database. A special synchronization mechanism running in the background continuously checks the internet connection and synchronizes the data bidirectionally with the server.

## Where it is used
It is frequently used in note-taking applications used while traveling on the subway, in job tracking systems where field workers enter data in places without internet reception, and in map applications.

## Commonly confused with
It is often confused with simply having an offline mode: While offline mode only aims to prevent errors when there is no internet, the offline-first approach completely builds the application's main operating principle on local data.

## Frequently asked questions
**What happens if changes made while offline conflict with other users' data when the internet connection is restored?**
Conflict resolution algorithms in the software come into play, safely merging the data either by preserving the most recent change or by asking the user.

**Do offline-first applications take up a lot of space on the device?**
No, since only text-based data and small files actively used by the user are stored on the device, it does not unnecessarily fill up storage space.


## Related terms
- [Local-first](/en/dictionary/local-first/)
- [Offline](/en/dictionary/offline/)
- [Database](/en/dictionary/database/)
- [State Management](/en/dictionary/state-management/)

## Related tools
- [LAP](/en/discover/lap/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/offline-first/
