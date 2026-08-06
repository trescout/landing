# What is Protocol Buffers?

> Protobuf

It is a method that allows different software to package and transport data very quickly and in small sizes while talking to each other.

## Overview
Software usually uses text files when sending data to each other, but these files can sometimes be very large. Protocol Buffers convert data into a binary format, allowing it to take up much less space and be transmitted much faster. It was developed by Google and is now considered the standard in inter-system communication.

*Analogy: Instead of sending a letter as it is, it is like compressing the information inside with a special encryption and fitting it into a box, and having the recipient open this box using the same method.*

## How it works
You first define the structure of the data in a template file. Then, your software packages the data using this template and sends it to the other party. The receiving side restores the data using the same template.

## Where it is used
It is used in microservice architectures, communication of mobile applications with servers and systems that require high performance.

## Commonly confused with
It may be confused with text-based data formats such as JSON or XML, but it is much faster and smaller.

## Frequently asked questions
**Can people read?**
No, the data cannot be directly read by humans as it is in binary format, it is designed so that only computers can understand it.


## Related terms
- [API](/en/dictionary/api/)
- [Networking Stack](/en/dictionary/networking-stack/)
- [Serialization](/en/dictionary/serialization/)

## Related tools
- [Protobuf](/en/discover/protobuf/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/protocol-buffers/
