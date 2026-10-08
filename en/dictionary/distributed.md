# Distributed Systems: Fallacies, CAP theorem, consensus, and sagas

*Dictionary · Dev · Last updated: September 19, 2026*

A distributed system is a computing architecture where multiple independent machines (nodes) communicate and coordinate over a network, appearing to end users as a unified, coherent system.

## Etymology and the Nature of Distributed Systems

The term *distributed* comes from Latin *distribuere* (to divide, allocate, or apportion). As Leslie Lamport famously quipped: *"A distributed system is one in which the failure of a computer you did not even know existed can render your own computer unusable."* Unlike centralized mainframes, distributed networks trade simplicity for infinite horizontal scalability and geographic fault tolerance.

## The 8 Fallacies of Distributed Computing

Formulated by L. Peter Deutsch and Sun Microsystems engineers, these eight false assumptions lead to brittle architectures if ignored:

1. The network is reliable.
2. Latency is zero.
3. Bandwidth is infinite.
4. The network is secure.
5. Topology doesn't change.
6. There is one administrator.
7. Transport cost is zero.
8. The network is homogeneous.

## The CAP Theorem and PACELC Model

Eric Brewer's **CAP Theorem** dictates that a distributed data store can guarantee at most two of three properties under network partitions:

- **Consistency (C):** Every read receives the most recent write or an error.
- **Availability (A):** Every non-failing node returns a non-error response without guarantee of recent state.
- **Partition Tolerance (P):** The system continues to operate despite arbitrary message drops. Since network partitions cannot be avoided in real networks, systems must choose between CP (e.g., ZooKeeper, Google Spanner) or AP (e.g., Cassandra, DynamoDB).

Daniel Abadi's **PACELC model** refines this: *If there is a Partition (P), trade off Availability (A) and Consistency (C); Else (E), trade off Latency (L) and Consistency (C).*

## Consensus Protocols: Raft and Paxos

To agree on a single source of truth across untrusted networks, systems employ consensus algorithms:

- **Paxos:** Leslie Lamport's mathematically proven algorithm based on proposer, acceptor, and learner roles; notoriously difficult to implement in real software.
- **Raft:** Designed by Ongaro and Ousterhout for understandability, Raft decomposes consensus into explicit Leader Election, Log Replication, and Safety invariants, powering systems like etcd and HashiCorp Consul.

## The Problem of Time in Distributed Systems and Solutions

Without a single shared physical quartz clock, ordering events across machines is physically impossible due to clock drift (relativistic network delays):

- **Lamport Timestamps & Vector Clocks:** Logical counters establishing causal relationships ("happened-before") without relying on physical time.
- **Google TrueTime:** Hardware architecture integrating atomic clocks and GPS receivers into data centers, bounding clock uncertainty within small milliseconds intervals (used in Spanner).

## Distributed Data and Transaction Management: The Saga Pattern

Classic two-phase commit (2PC) locks database rows and fails under high scale. Modern microservice architectures utilize the **Saga Pattern**:

- A series of local transactions coordinated either through an orchestrator (central state machine) or choreography (event-driven pub/sub).
- If any step fails, the system executes explicit compensating transactions backwards to reverse completed actions safely without global locking.

*A centralized system is like a solitary chef cooking orders in a small food truck; a distributed system is like a global restaurant chain operating across five continents where hundreds of kitchens must fulfill matching recipes while handling phone disconnects and shipping delays.*

## Frequently asked questions

**What is a distributed system in computer science?**

It is an architecture where multiple independent computers connected by a network coordinate state and tasks to act as a single system.

**Why can a distributed database not have both C and A during a network split?**

Because if nodes cannot communicate, you must either accept writes and risk divergence (favoring Availability) or reject writes to maintain consistency (favoring Consistency).

**What is the difference between Raft and Paxos?**

Both achieve distributed consensus, but Raft was designed specifically to be easier for human engineers to understand and implement reliably.

**How does the Saga pattern replace distributed transactions?**

By executing a chain of independent local transactions and triggering backward compensating actions if any intermediate step fails.

## Related terms

- [Cloud Computing](https://trescout.com/en/dictionary/cloud-computing/)
- [Network Stack](https://trescout.com/en/dictionary/network-stack/)
- [Deployment](https://trescout.com/en/dictionary/deployment/)
- [Runtime](https://trescout.com/en/dictionary/runtime/)

## Related tools

- [Elasticsearch](https://trescout.com/en/discover/elasticsearch/)
- [Cassandra](https://trescout.com/en/discover/cassandra/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/distributed/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/distributed/
