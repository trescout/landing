# What is Specification?

*Dictionary · Dev · Last updated: September 22, 2026*

Specification (spec for short, specification in Turkish) is a technical document that writes what the product will do and its rules.

## Definition and Word Origin

It is like the architectural project of the building: The software developer looks at the document before starting the code and understands what to build. It reduces errors and clarifies expectations. In the API world, OpenAPI, hardware datasheets do this job.

***Analogy:** It's like the ingredient list and cooking steps in a recipe; If you don't follow the recipe, the food will taste different.*

## How to Know and Use in Daily Life?

**Software:** Feature and rules document.
**Tender:** Technical specification file.
**Product:** Design and acceptance criteria.

## Technical Depth and Architecture

Good spec includes:

**Scope:** What is there, what is not.
**Acceptance criteria:** Testable conditions for it to be considered done.
**Borders:** Performance, security, compatibility.
**Version:** Change history.

Specification of API end:

```
paths:
  /siparis:
    post:
      summary: Yeni sipariş oluşturur
```

Rule: The item that cannot be measured is not a spec, it is a wish. Every item is written testable.

## Frequently Mixed Things

It is similar to Requirement. Requirement tells what is wanted, specification tells how to do it. One is the goal, the other is the plan.

## Use in Different Disciplines

**Recipe:** Material and step list.
**Assembly guide:** Part and sequence diagram.
**Tender:** Administrative and technical specifications.

## Frequently Asked Questions

**Can the spec change?**

Yes, but each change must be approved along with cost and schedule impact.

**Who writes the spec file?**

The product manager, engineer, or analyst writes. What matters is single owner and release discipline.

**How much detail is required?**

Enough to end the uncertainty. Too much will tire the writer, too little will clog the developer.

**Is there a spec in Agile?**

Yes, they are lighter. User stories and API contracts with acceptance criteria serve as specs.

## Related terms

- [Spec-driven Development](https://trescout.com/en/dictionary/spec-driven-development/)
- [Framework](https://trescout.com/en/dictionary/framework/)
- [Tech Stack](https://trescout.com/en/dictionary/tech-stack/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/specification/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/specification/
