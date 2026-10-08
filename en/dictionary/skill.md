# What is Skill?

*Dictionary · AI · Last updated: September 22, 2026*

Skill is the defined unit that enables the artificial intelligence assistant to do work with an external tool.

## Definition and Word Origin

The assistant's general speech is not enough; Sometimes it needs to read files and make searches. Each of these special functions is defined as a skill. The concept has moved from the voice assistant era to the agent era: from Alexa skills to today's agent skills.

***Analogy:** It is like different tools in the hands of the kitchen chef; The chef is unique; he chooses the right tool for each job.*

## How to Know and Use in Daily Life?

**File:** Document reading and summarizing.
**Calendar:** Set up a meeting.
**Call:** Getting current information.

## Technical Depth and Architecture

The skill is written in three parts:

**Name:** The short name that the model will call.
**Explanation:** Recipe for when to use it. Model selection is made by looking at this.
**Parameter chart:** Input format.

Example definition:

```
{
  "name": "hava-durumu",
  "description": "Belirtilen şehrin güncel havasını verir",
  "parameters": { "sehir": "string" }
}
```

Flow: The user requests, the model selects the appropriate skill, fills the parameter, the tool runs, the result is returned to the model. User approval is required for skills that have write permissions.

## Frequently Mixed Things

It is thought to be general modeling ability. However, what is meant here is the assistant's ability to use external tools. The model understands the language, the skill does the work.

## Use in Different Disciplines

**Kitchen:** Knife and sauce techniques in the chef's hand.
**Drill:** Function varying depending on tip.
**Telephone:** Every application installed.

## Frequently Asked Questions

**Does every model have the ability?**

No. Basic models generate text, the ability is gained when external tools are added to the assistant.

**How to develop skills?**

Identified by API connection or code block. The description is written clearly, the model chooses correctly.

**Is it safe?**

Reading abilities are at low risk. Approval and scope limit are essential for transactions such as writing and payment.

**Who writes talent?**

Developers write it, platforms distribute it in the store. Writing a good description is half the job.

## Related terms

- [AI Agent](https://trescout.com/en/dictionary/ai-agent/)
- [AI Skill](https://trescout.com/en/dictionary/ai-skills/)
- [Agent Skills](https://trescout.com/en/dictionary/agent-skills/)
- [Tools](https://trescout.com/en/dictionary/tools/)
- [AI Capabilities](https://trescout.com/en/dictionary/ai-capabilities/)

## Related tools

- [Anthropic Skills](https://trescout.com/en/discover/anthropic-skills/)
- [Taste Skill](https://trescout.com/en/discover/taste-skill/)
- [Archify](https://trescout.com/en/discover/archify/)
- [Awesome Claude Skills](https://trescout.com/en/discover/awesome-claude-skills/)
- [Last30days Skill](https://trescout.com/en/discover/last30days-skill/)
- [I Have Adhd](https://trescout.com/en/discover/i-have-adhd/)
- [Reverse Skill](https://trescout.com/en/discover/reverse-skill/)
- [Book to Skill](https://trescout.com/en/discover/book-to-skill/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/skill/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/skill/
