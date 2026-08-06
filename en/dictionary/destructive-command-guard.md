# What is Destructive Command Guard?

It is a security shield that stops you before you run commands that risk deleting data or corrupting the system.

## Overview
It is a security layer designed to prevent you from making irreversible errors on the system. When you type a dangerous command, the system detects it and asks if you really want to do it. This mechanism is used to reduce the margin of error, especially on critical servers.

*Analogy: It is like a warning system that prevents your car from accidentally shifting into park mode when shifting into reverse gear or reminds you that the doors are locked.*

## How it works
When you enter a command such as 'delete everything' on a command line, the system does not directly process this command. It first performs a security check and says 'This action will delete all your data, are you sure?' It displays a checkbox or warning message. The command will never run unless you approve it.

## Where it is used
It is commonly found in terminal applications, advanced software development tools, and server management panels.

## Commonly confused with
It can be confused with a firewall; It blocks attacks from outside, which prevents mistakes you make from inside.

## Frequently asked questions
**Should this protection always be on?**
Yes, having this protection turned on prevents major data losses, especially when performing critical operations.


## Related terms
- [Security Scanner](/en/dictionary/security-scanner/)
- [Linux Server Security](/en/dictionary/linux-server-security/)
- [Terminal Control](/en/dictionary/terminal-control/)

## Related tools
- [Destructive Command Guard](/en/discover/destructive-command-guard/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/destructive-command-guard/
