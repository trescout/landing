# What is Hooks?

These are connection points that allow you to intervene at specific moments during the software's execution process and perform custom operations.

## Overview
They are special gateways left by developers so that they can inject their own code into the main flow while a software is running. This way, you can ensure your own commands run when a specific event occurs without modifying the main program. For example, you can use a hook to tell the system to automatically take a backup when a file is saved.

*Analogy: It is like a secret passage added to a building's security system; instead of entering through the main door, you set up a special mechanism that activates when a specific alarm goes off.*

## How it works
Software developers place markers inside the main code that say 'run this function when you reach here.' You then attach your own code to these markers to personalize the process. Thanks to this method, even if the main software is updated, the features you added continue to work.

## Where it is used
You frequently encounter them in the background of websites, application development frameworks, and plugin systems.

## Commonly confused with
They can be confused with plugins; while hooks are more of a code-level connection point, plugins offer broader features.

## Frequently asked questions
**Why don't we just change the main code directly?**
Changing the main code causes all your modifications to be deleted when the software is updated; hooks, on the other hand, are not affected by updates.


## Related terms
- [Plugin](/en/dictionary/plugin/)
- [Framework](/en/dictionary/framework/)
- [API](/en/dictionary/api/)

## Related tools
- [Everything Claude Code](/en/discover/everything-claude-code/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/hooks/
