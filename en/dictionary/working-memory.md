# What is Working Memory?

*Dictionary · AI · Last updated: September 22, 2026*

Working memory (in Turkish, çalışma belleği) is the temporary information the model holds for the task at hand.

## Definition and Word Origin

When the task is finished or the context changes, the content is cleared. The context window container is the active information within the working memory. Chat history and intermediate results reside here.

***Analogy:** It is like temporary notes taken on the side while solving math; once the problem is over, it loses its importance.*

## How to Know and Use in Daily Life?

**Chat:** Remembering previous messages.
**Reasoning:** Retaining intermediate steps.
**Vehicle:** Holding tool call results.

## Technical Depth and Architecture

Budget calculation:

```
bağlam: 128K token
geçmiş: 100K → kalan 28K
```

When it overflows, the model says goodbye to the old: pruning, summarization, or sliding is applied. RAG difference: RAG brings in external information, working memory holds the current information. The two work together.

## Frequently Mixed Things

It is mistaken for long-term memory. That is the permanent profile, this is the temporary workbench. When the session closes, this place gets emptied.

## Use in Different Disciplines

**Side note:** Scratches thrown away when the problem is solved.
**Stand:** Tools packed up when the job is done.
**RAM:** The area that gets erased when the power is cut.

## Frequently Asked Questions

**What happens if it gets full?**

Old information is forgotten, context shifts. It is managed through summarization and pruning.

**How is it expanded?**

A model with a large context window is chosen, or external information is added via RAG.

**What is the difference of RAG?**

RAG brings it from the outside, memory holds that moment. The two are complementary.

**Does it forget?**

Yes. It is a temporary area, persistence is not expected. Permanent information is written externally.

## Related terms

- [Memory](https://trescout.com/en/dictionary/memory/)
- [Context Window](https://trescout.com/en/dictionary/context-window/)
- [Long-term Memory](https://trescout.com/en/dictionary/long-term-memory/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/working-memory/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/working-memory/
