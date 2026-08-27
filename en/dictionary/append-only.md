# What is Append-only?

It is a recording method in which data can only be appended, cannot be changed or deleted.

## Overview
When adding information to a database or file, it is the principle of adding each new piece of information to the end of the list rather than replacing old data. This method is critical to preserve the history and security of the data. Since no data is deleted, it is possible to trace all movements in the system.

*Analogy: It's like writing down each transaction with a ballpoint pen, instead of writing with a pencil in an accounting ledger; You can't black out old pages.*

## How it works
The system only accepts an 'add' command rather than a command that updates the data. In this way, the history of the data is always preserved.

## Where it is used
It is used in blockchain technologies, log keeping systems and auditable databases.

## Commonly confused with
Can be confused with traditional databases; traditional ones can update the data, this method never allows.

## Frequently asked questions
**What happens if I make a mistake?**
Instead of deleting the erroneous data, you add a new record that corrects the error.

**Why is it so safe?**
Since the data cannot be changed, it is almost impossible to manipulate the past.


## Related terms
- [Database](/en/dictionary/database/)
- [Logs](/en/dictionary/logs/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/append-only/
