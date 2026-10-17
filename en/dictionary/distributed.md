# What is Distributed?

*Development · Last updated: September 19, 2026*

Distributed, in the world of computing, is the sharing of hardware, data and calculation processes across many independent servers (nodes) connected to each other over the network, instead of a single central machine, and this system serves the end user as if it were a single whole computer.

## Etymology and the Nature of Distributed Systems

The word "distributed" translates to "dağıtık" in Turkish. Leslie Lamport, one of the pioneers of computer science, defined distributed systems with this famous quote: "A distributed system is one in which the failure of a computer you didn't even know existed can render your own computer unusable."

In centralized (monolithic) architectures, all operations occur on a single main memory and processor. In distributed systems, hundreds of nodes physically spread across data centers on different continents of the world serve a common purpose by communicating over unreliable network cables.

## 8 Fallacies of Distributed Computing

In the 1990s, Sun Microsystems engineers L. Peter Deutsch and James Gosling listed the "8 Deadly Mistakes" made by software developers developing distributed systems. All defense lines of modern cloud and microservice architectures are built according to these misconceptions:

1. The network is reliable: In reality, packets are lost, fiber lines break, and routers crash.
2. Latency is zero: The speed of light and network switching delay between two machines are always present.
3. Bandwidth is infinite: As data volume increases, network pipes become congested.
4. The network is secure: All distributed communication passes through open lines and requires cryptographic protection.
5. Topology doesn't change: Servers are constantly coming online and offline, IP addresses change.
6. There is only one system administrator: Multiple teams and cloud providers are involved.
7. Transport cost is zero: Serialization and CPU packaging costs cannot be ignored.
8. The network is homogeneous: Linux, Windows, ARM, x86, and different protocols work together in the system.

## CAP Theorem and PACELC Model

The CAP Theorem, proposed by Eric Brewer, outlines the fundamental limitations of distributed data management. When a network partition (P) occurs, the system must choose between one of two options:

- CP (Consistency + Partition Tolerance): The system chooses consistency. Nodes with outdated data refuse to respond; availability is sacrificed (e.g., finance and banking transactions).
- AP (Availability + Partition Tolerance): The system prioritizes availability. Nodes continue to respond, but some users may see stale data from a few seconds prior (e.g., social media feeds).

Modern systems use Daniel Abadi's PACELC model: If there is a partition (P), does the system prioritize Availability (A) or Consistency (C); and else (E), when the system is running normally, is the goal Latency (L) or Consistency (C)?

## Consensus Protocols: Raft and Paxos

Consensus algorithms have been developed so that independent servers, which do not trust each other and can crash at any time, can agree on a single truth:

Paxos: A consensus algorithm developed by Leslie Lamport that is mathematically proven but extremely complex to implement in practice.
- Raft: A human-intelligent consensus protocol developed by Diego Ongaro and John Ousterhout to solve the complexity of Paxos. Leader Election is based on Log Replication and Safety state machines (it works at the heart of giant systems such as Etcd, Kubernetes, Consul).
Byzantine Fault Tolerance (BFT): The foundation of blockchain protocols that achieve consensus even in environments where some nodes intentionally propagate erroneous or malicious information.

## Time Problem and Solutions in Distributed Systems

In a centralized computer, the hardware clock represents a single fact. In distributed systems, server clocks show physical clock drift and NTP (Network Time Protocol) is insufficient for millisecond precision:

Lamport Timestamps: Defines the "order of events" instead of physical time.
Vector Clocks: Detects data conflicts by determining which piece of data is the cause or result of another.
Google TrueTime: A combination of atomic clocks and GPS antennas used in the Google Spanner distributed database. It enables ACID transactions on a global scale by reducing the margin of uncertainty to a few milliseconds.

## Distributed Data and Transaction Management: Saga Pattern

In monolithic systems, database operations (ACID transactions) are replaced by the Saga Pattern in microservices. Instead of locking long-running distributed steps with Two-Phase Commit (2PC), event-driven architectures are used, where each service performs its local transaction and Compensating Transactions are triggered in the event of an error.

## Frequently Asked Questions

**What does Distributed mean (Turkish meaning)?**

In IT terminology, it means 'distributed'. It is the sharing of computing power, memory space, or database among many independent machines communicating over a network, rather than a single server.

**What does the CAP Theorem mean in practice?**

It means that when there is a break or delay (split) in the network connection, the system must either guarantee the most up-to-date data and hold some requests (Consistency), or respond to every request immediately at the expense of providing stale data (Availability).

**Why is the Raft consensus algorithm used in distributed systems?**

Even if a few of the servers in the network go down, the remaining majority is used to ensure that the nodes (Quorum) elect a new leader from among them and the database logs are synchronized losslessly across the entire cluster.

**Why is Saga pattern preferred over Two-Phase Commitment (2PC)?**

2PC (Two-Phase Commit) locks database resources on distributed nodes and locks down the entire system when one machine becomes unresponsive. The Saga pattern, on the other hand, maintains the high availability of the system by using asynchronous events and compensation steps.

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
