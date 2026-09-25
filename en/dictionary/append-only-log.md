# Append-Only Log Immutability, Write-Ahead Logs, and distributed storage


**Category:** Data & Infra  

**Last updated:** 2026-09-20


An append-only log is a fundamental data storage paradigm where new records can only be sequentially appended to the end of the file; existing data is strictly immutable and can never be modified or overwritten in place.


## Etymology and the Immutability Paradigm
The concept derives from classic financial bookkeeping ledgers: accountants never erase an incorrect entry with an eraser; they append a new compensating transaction. In computer science, an append-only log provides deterministic sequential write throughput by eliminating random disk write seeks.

## Technical Depth and System Architecture
Append-only structures form the backbone of modern data engineering:
- **Write-Ahead Logging (WAL):** Databases like PostgreSQL, MySQL, and SQLite append every transaction to a WAL file sequentially on disk before writing to complex B-Tree structures, guaranteeing ACID durability against power failures.- **Log-Structured Merge-Trees (LSM-Trees):** Storage engines (RocksDB, Cassandra) write updates to an append-only commit log and in-memory MemTable, periodically compacting immutable SSTables in the background.- **Distributed Event Streaming:** Apache Kafka and Apache Pulsar treat the append-only commit log as an unbounded event stream partitioned across distributed clusters.

## Sociological Dimension: Digital Memory and Audit Trails
In an era of deepfakes and data manipulation, append-only logs provide verifiable cryptographic integrity. In Git commits, certificate transparency logs, and public blockchains, every state modification produces a tamper-evident audit trail where historical truth cannot be silently altered.

## Common Mistakes and Engineering Pitfalls
Operating append-only architectures requires clear operational disciplines:
- **Unbounded Disk Growth:** Without log retention policies, rolling segment files, and compaction strategies, logs will eventually exhaust server storage.- **Read Amplification:** Reconstructing the current state of an entity requires replaying log records from the beginning unless periodic snapshot checkpoints are recorded.

## Analogy
An append-only log is like writing history in wet concrete or chisel on stone: once recorded, you cannot rub out past events; if you make a mistake, you must carve a new entry explaining the correction.

## Frequently asked questions

**What does append-only log mean in software?**  
It is a storage design where data is written strictly sequentially to the end of the file, making historical entries immutable and tamper-resistant.

**Why are append-only logs faster for disk writes?**  
Because sequential disk writes avoid the physical seek latency of random writes, maximizing NVMe and hard disk throughput.

**How do databases prevent append-only logs from filling up the disk?**  
Through log compaction, segment deletion, and periodic snapshotting where intermediate states are consolidated.

## Related terms
- [Distributed](/en/dictionary/distributed/)
- [Serialization](/en/dictionary/serialization/)
- [Local](/en/dictionary/local/)
- [Self-hosted](/en/dictionary/self-hosted/)
- [Runtime](/en/dictionary/runtime/)
- [Memory Management](/en/dictionary/memory-management/)

---
Source: TreScout Tech Dictionary · https://trescout.com/en/dictionary/append-only-log/
