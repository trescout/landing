# What is Serialization?

Serialization is the dynamic allocation of objects, data structures, and pointer graphics in the working memory (RAM) of a programming language; It is the process of converting data into a flat, linear byte stream or text format that can be transmitted over the network or stored on disk.

## What Does Serialization Mean and Why Is It Necessary? Memory Model
In modern operating systems, each process runs in its own isolated virtual address space. An object at runtime; It contains local variables on the stack, dynamically allocated memory blocks on the heap, function pointers (vtable) and reference addresses (0x7ffee4b2...).

## Serialization Formats: Text-Based vs Binary
Choosing the right serialization format in software architecture; It requires a balance between human readability, CPU parsing cost, network bandwidth, and type safety.

## Zero-Copy Deserialization Architecture
In classic serialization libraries (JSON parsers or standard Protobuf) the deserialization process is carried out with these steps:

## Security Dimension: Insecure Deserialization (CWE-502)
Catastrophic security vulnerabilities arise when serialization attempts to serialize object classes and runtime behaviors rather than just moving pure data. Insecure Deserialization (Insecure Reverse Serialization), which is in the OWASP Top 10 list, allows the attacker to run arbitrary code (Remote Code Execution - RCE) on the system.

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
- [API](/en/dictionary/api/)
- [Data Pipeline](/en/dictionary/data-pipeline/)
- [Memory Management](/en/dictionary/memory-management/)
- [Network Stack](/en/dictionary/network-stack/)

## Related tools
- [YAML Cpp](/en/discover/yaml-cpp/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/serialization/
