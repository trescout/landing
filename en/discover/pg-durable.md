# Robust process management on PostgreSQL

Developed by Microsoft, pg_durable is a library designed to manage durable execution processes on PostgreSQL. Written in Rust, the tool enables complex workflows to run within the database in a fault-tolerant and persistent manner.

- ★ 2,781
- Rust
- GitHub Trending · 2026-06-08

## What you get
- It manages workflows within the database in a fault-tolerant and persistent manner.
- In case of crash or interruption, it continues operations from the last checkpoint.
- It runs directly on PostgreSQL without requiring additional infrastructure.

## Installation
**Activating the Plugin**

```
CREATE EXTENSION pg_durable;
```


## Running it
**Starting a Workflow**

```
SELECT df.start(
    'SELECT id FROM documents WHERE processed = false LIMIT 100' |=> 'batch'
    ~> 'UPDATE documents SET processed = true WHERE id = ANY($batch)'
);
```


## If you don't write code
I want to create a workflow using the pg_durable plugin on PostgreSQL. How should I configure the df.start() function to manage a fault-tolerant and persistent process within the database? How can I create a structure that processes data and can continue from where it left off in case of error, using the ~> and |=> operators that connect SQL steps? Please explain this process with examples using SQL commands.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/pg-durable/
