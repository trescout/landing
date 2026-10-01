# What is ab (ApacheBench)?

> ApacheBench

A simple performance testing tool to measure how many people a web server can handle at the same time.

## Overview
When you build a website, you wonder how many concurrent visitors it can handle. ApacheBench, or ab for short, runs from the command line and sends hundreds of fake requests to your server simultaneously. This way, you can see in advance when your server will crash or slow down.

*Analogy: It is like conducting an simultaneous entry test to see if the door of a newly opened café can withstand it when a hundred people pile up at the entrance at the same time.*

## How it works
You open the terminal screen and type the commands specifying the web address you want to test and how many requests you want to send. The tool provides you with a numerical report of how many transactions you can handle per second.

## Where it is used
It is used to measure server performance, run speed tests just before a massive traffic wave is expected, or after system optimization.

## Frequently asked questions
**Does it mimic a real user?**
Not entirely, it just bombards the target with requests in rapid succession.

**Does it only work on Apache servers?**
No, even though its name is ApacheBench, it can test any web address accessible on the internet.


## Related terms
- [Benchmark](/en/dictionary/benchmark/)
- [Load Generator](/en/dictionary/load-generator/)
- [CLI](/en/dictionary/cli/)

## Related tools
- [HEY](/en/discover/hey/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/apache-bench-ab/
