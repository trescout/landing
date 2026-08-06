# What is Serialization?

It is the process of converting complex data structures into a plain text or byte array that can be stored or transmitted.

## Overview
You need to translate objects held in a complex way in the computer's memory (for example, a user profile) into a straight line in order to send them over the Internet or save them in a file. This process is called serialization. When the other party receives this data, it performs 'deserialization' and restores it to its old complex structure.

*Analogy: Moving a piece of furniture is like taking it apart and placing it in a flat box; At destination you open the box and reassemble the furniture.*

## How it works
Data is usually converted to JSON, XML, or faster binary formats. In this way, the original structure of the data is preserved and it becomes portable between different systems.

## Where it is used
It is used in API communications, database records, and creating save files in games.

## Frequently asked questions
**Why do we need serialization?**
The data in the computer's memory is meaningful only for the current program. To send data to another computer or disk, we need to convert it to a universal format.


## Related terms
- [API](/en/dictionary/api/)
- [Data Pipeline](/en/dictionary/data-pipeline/)

## Related tools
- [YAML Cpp](/en/discover/yaml-cpp/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/serialization/
