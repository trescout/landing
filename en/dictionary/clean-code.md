# What is Clean Code?

*Dictionary · Dev · Last updated: September 22, 2026*

Clean code is the code that can be read by humans.

## Definition and Word Origin

The machine runs every code, a human cannot read every code. Meaningful name, small function and simple flow bring readability. Robert Martin is the reference name of this discipline.

***Analogy:** It's like having library shelves arranged by genre and author.*

## How to Know and Use in Daily Life?

**Team:** Common code base.
**Review:** Readability check.
**Care:** Reverting to old code.

## Technical Depth and Architecture

Principles:

**Name:** The name that expresses the intention.
**Dimension:** Single job function.
**Again:** The common piece is in one place.

Example:

```
# önce
def h(a, b):
    return a + a*b
# sonra
def indirimli_fiyat(fiyat, oran):
    return fiyat + fiyat * oran
```

Rule: Running code is the first step, read code is the second step.

## Use in Different Disciplines

**Table:** Tidy work area.
**Shelves:** Sorted by genre and author.
**Garden:** Pruned branch arrangement.

## Frequently Asked Questions

**Isn't it enough to work?**

It's not enough. Working code saves today, read code saves tomorrow.

**Does it slow down?**

In the beginning yes, in maintenance no. It makes money in total.

**How is it measured?**

With review time and error rate. Number alone is not enough.

**Where to start?**

From name and function. The touched code is cleared.

## Related terms

- [Refactoring](https://trescout.com/en/dictionary/refactoring/)
- [Unit Testing](https://trescout.com/en/dictionary/unit-testing/)
- [Engineering Skills](https://trescout.com/en/dictionary/engineering-skills/)

## Related tools

- [Clean Code Javascript](https://trescout.com/en/discover/clean-code-javascript/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/clean-code/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/clean-code/
