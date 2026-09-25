# What is Serialization and How Does it Work?

> English: Serialization · Etymology: Latin series (row, succession) + facio (to make)

**Category:** Dev  
**Last updated:** 2026-09-19

Serialization is the process of converting dynamically allocated in-memory data structures, objects, and pointer graphs into a linear byte stream or standardized text format suitable for network transmission or persistent disk storage.

## What is Serialization and Why is it Necessary? Memory Model
In modern operating systems, every running process resides in an isolated virtual address space. Objects instantiated inside heap memory reference each other through memory pointers. Because pointers are merely raw virtual memory addresses valid only within that specific process context, they cannot be transferred across network sockets or saved to disk as-is. Serialization decomposes complex object graphs, resolves references, and flattens them into portable, self-contained data representations.

## Serialization Formats: Text-Based vs Binary Protocols
Choosing the appropriate format involves tradeoffs across human readability, CPU parsing overhead, network payload size, and schema rigor:
- **Text-Based (JSON, YAML, XML):** Human-readable, widely supported across programming languages, and simple to debug over HTTP APIs. However, they incur significant parsing overhead and payload inflation due to string encoding.- **Binary Formats (Protocol Buffers, MessagePack, Avro):** Compact binary representations featuring explicit field numbering, compact varints, and strong typing. They yield substantial bandwidth savings and rapid deserialization.- **Schema Evolution:** Enterprise protocols like Protobuf and Avro ensure backward and forward compatibility, allowing services to upgrade schemas without breaking older clients.

## Zero-Copy Deserialization Architecture
Conventional deserialization reads incoming bytes from a network buffer and reconstructs new heap objects in memory, requiring allocation and memory copies. Modern high-throughput frameworks (such as Cap'n Proto and FlatBuffers) utilize **Zero-Copy Deserialization**:
- **In-Place Traversal:** Data is organized with predetermined memory alignment and internal relative offsets.- **Direct Memory Mapping:** The application queries fields directly from memory-mapped disk files or network buffers without heap allocations, delivering orders of magnitude higher throughput.

## Security Dimensions: Insecure Deserialization (CWE-502)
When serialization formats serialize not just raw data fields but dynamic object classes, executable methods, or runtime closures (common in Python pickle, Java native serialization, or Ruby Marshal), severe security vulnerabilities emerge:
- **Remote Code Execution (RCE):** Malicious payloads can construct gadget chains that trigger arbitrary system execution during deserialization before business validation runs.- **Best Practice Defenses:** Treat untrusted network input strictly as structured data (preferring JSON, Protobuf, or strict schemas) and implement message integrity verification via HMAC or TLS.

## Analogy
It is like disassembling a piece of furniture into flat components to pack into a compact box for transport, and then following the instruction manual to reassemble it at the destination.

## Frequently Asked Questions

**What is the fundamental difference between serialization and deserialization?**  
Serialization flattens living memory structures into a linear byte sequence. Deserialization performs the reverse: reconstructing structured objects and pointer relationships from that byte stream.

**Why should Python's pickle never be used with untrusted data?**  
Pickle allows serialized streams to instantiate arbitrary Python objects and execute constructor functions, enabling attackers to execute system commands directly upon deserialization.

**How does FlatBuffers achieve zero-copy deserialization?**  
It lays out data in memory-aligned binary structures with relative offsets so consumers can read fields directly from the buffer without heap allocation.

**When is JSON preferred over Protobuf?**  
When human readability, quick exploratory debugging, and universal browser compatibility outweigh payload compression and CPU parsing efficiency.

## Related terms
- [API](/en/dictionary/api/)
- [Data Pipeline](/en/dictionary/data-pipeline/)
- [Buffer](/en/dictionary/buffer/)

## Related tools
- [YAML Cpp](/en/discover/yaml-cpp/)

---
Source: TreScout Tech Dictionary · https://trescout.com/en/dictionary/serialization/
