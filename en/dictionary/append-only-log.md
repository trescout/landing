# What is Append-only log?

*Data & Infra · Last updated: September 20, 2026*

An append-only log is an immutable data structure architecture where data is never modified in place or deleted, and every new transaction is added to the end of the file in chronological order.

## Etymology and Immutability Paradigm

The concept of the append-only log was developed as a fundamental alternative to the "update-in-place" paradigm of traditional databases. In classic databases, when a balance or profile is updated, the old data on the disk is deleted and the new value is overwritten. This approach creates serious reliability issues due to half-written data corrupting the system during a crash, locking bottlenecks, and random disk access (random I/O).

In the append-only log architecture, however, the past is sacred and tamper-proof. Instead of directly changing a bank account balance, every deposit and withdrawal action is added to the end of the log as a new record. The current state of the system is a natural result of the chronological execution (fold/reduce) of all these events added from the past to the present. This principle forms the backbone of modern distributed systems, high-performance storage engines, and blockchain networks.

***Analogy:** Imagine an official general ledger kept by an accountant. When the accountant makes an error on a line, they cannot open previous pages and erase the old number with correction fluid. Instead, they add a new reverse entry line correcting the mistake to the very last blank line of the ledger. The ledger only grows forward, the past is never altered; when and how money moves can be audited retrospectively. An append-only log is precisely this digital ledger; it records data not as an instantaneous snapshot, but as a living history.*

## Technical Depth and System Architecture

At a technical level, the append-only log architecture is built upon three main foundations regarding hardware optimization and data consistency:

Sequential I/O and WAL: Magnetic disks (HDDs) and even modern solid-state drives (SSDs/NVMe) perform with significantly higher throughput when writing to sequential blocks rather than random addresses. For this reason, databases such as PostgreSQL, MySQL, and SQLite use Write-Ahead Logging (WAL). When a transaction arrives, an append-only log entry is first written sequentially to the disk and fsync'd. This ensures that even if the server loses power suddenly, the database can be restored to a fully consistent state within seconds upon restart by reading the log from the beginning.
LSM-Tree and Compaction: High-write-throughput NoSQL engines such as RocksDB, Apache Cassandra, and Bigtable utilize the Log-Structured Merge-Tree (LSM-Tree) architecture. All incoming data is first added to an in-memory sorted structure (MemTable) and a concurrent append-only log. When the MemTable is full, it is flushed to disk as immutable SSTable files. Over time, accumulated old or invalid data is cleaned up by background compaction processes.
Event Sourcing and Distributed Streaming (Kafka): In microservice architectures, distributed messaging platforms like Apache Kafka and Redpanda function as massive distributed append-only logs. Instead of storing application states in a database, generated events are written to immutable logs. Different services consume these logs at their own pace to build their own local states.
Cryptographic Immutability and Blockchain: Distributed ledger technologies (DLT) such as Bitcoin and Ethereum are distributed append-only logs where each block contains the cryptographic hash of the previous block. No node in the network can alter past blocks; only new blocks that comply with consensus rules can be appended to the end of the log.

## Sociological Dimension: Digital Memory and Audit Trail

Beyond being merely a software design pattern, an append-only log represents the philosophy of digital accountability and transparency. The ability to answer the question of "who changed what and when" with unalterable precision in the corporate world and public administration is the most critical safety valve preventing crises of trust.

In traditional systems, the ability of a database administrator to delete and rewrite history with a single SQL command makes corporate memory fragile. Append-only systems, on the other hand, guarantee that history cannot be rewritten, weaving a mathematical immunity shield against human error, insider threats, and abuse of authority.

## Common Mistakes and Misconceptions

Failing to Anticipate Disk Consumption: If appropriate data retention and compaction strategies are not established, forgetting that logs only grow will lead to rapid exhaustion of disk space.
Neglecting Read Performance: Scanning millions of rows of logs from start to finish (replay) to calculate the final state paralyzes read times; regular state snapshots must be taken.
Ignoring the GDPR Right to be Forgotten: When data protection laws mandate the right to erasure, deleting data from immutable logs poses architectural challenges; this issue should be resolved through crypto-shredding, a method where data is rendered unintelligible by deleting its encryption key.

## Questions and answers

**Why is the append-only log architecture faster than the update-in-place model?**

Instead of searching for random blocks on the disk, writing data sequentially at the end of the file at all times (sequential write) minimizes disk head movement and I/O latency, providing very high write speeds.

**How is disk space managed if the append-only log grows infinitely?**

Systems periodically take a snapshot of the current state and run background compaction or segment cleaning processes to safely delete or archive old logs.

**How is an append-only log used in distributed systems and Apache Kafka?**

Kafka topics are partitioned append-only logs where messages are appended in chronological order; multiple consumers read the log losslessly and at high speed using independent offset values.

**How is the GDPR right to be forgotten implemented in systems that maintain append-only logs?**

User data in the immutable log is encrypted with a specific key; when a user requests deletion, only that user's encryption key is destroyed (crypto-shredding), rendering the data unreadable without corrupting the log.

## Related terms

- [Distributed](https://trescout.com/en/dictionary/distributed/)
- [Serialization](https://trescout.com/en/dictionary/serialization/)
- [Local](https://trescout.com/en/dictionary/local/)
- [Self-hosted](https://trescout.com/en/dictionary/self-hosted/)
- [Runtime](https://trescout.com/en/dictionary/runtime/)
- [Memory Management](https://trescout.com/en/dictionary/memory-management/)

This explanation was written in plain language for TreScout with AI and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/append-only-log/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/append-only-log/
