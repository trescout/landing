# Automate patent invention disclosures with artificial intelligence

The Python-based Patent Disclosure Skill analyzes technical invention drafts to generate technical descriptions, claims, and prior art comparisons in accordance with official patent formats.

- ★ 10,360
- Python
- GitHub Trending · 2026-08-31

## Updates

- **September 27, 2026:** Stars 6,058 → 10,360.

## What you get

- Structured patent text generation: Creating the technical field, background, abstract, and detailed description sections of an invention in accordance with standard patent norms.
- Independent and dependent claim tree: Automatically formulating hierarchical patent claim lists that maximize the scope of legal protection.
- Prior art gap analysis: Clearly highlighting the technical differences and the inventive step between existing technologies and the invention.
- Accelerating collaboration with patent attorneys: Saving time and money by transforming engineers' drafts into ready-to-use, organized technical documents for patent attorneys.
- Multilingual patent terminology support: Compliance with English, Turkish, and international patent office (WIPO, EPO, USPTO) terminology.

## Installation

**Cloning the repository and installing dependencies**

```
git clone https://github.com/handsomestWei/patent-disclosure-skill.git
cd patent-disclosure-skill
pip install -r requirements.txt
```

## Running it

**Initiating patent analysis and disclosure generation**

```
python run_skill.py --input bulus_taslagi.txt --output patent_disclosure.md
```

## Technical architecture and working principle

- Technical Invention Decomposition Engine: Identifies key inputs, outputs, and methodology in software, hardware, or chemical process descriptions.
- Claim Syntax Validator: A legal language analyzer that checks for vague expressions and formal errors in claims.
- Template and Markdown Export: Saving the document in a standard sectioned Markdown format for use in official patent applications.

## Patent analysis workflows and claim preparation

- Converting Software Algorithms into Patentable Formats: Deriving method and system descriptions acceptable to patent authorities from code and architectural diagrams.
- Defense Against Office Actions: Drafting responses that list the distinctive features of an invention in response to objections from patent examiners.
- Intellectual Property Portfolio Audit: Early mapping of the inventive steps within in-house technological projects that hold patent potential.

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to prepare a formal invention disclosure text for a distributed database caching algorithm I developed using the patent disclosure skill. Could you explain step-by-step how I can generate independent claims, the technical field of the invention, and the differences from prior art by providing the algorithm's flow as input?

## Frequently asked questions

- Does this tool replace a registered patent attorney? No. Patent Disclosure Skill is a preliminary preparation and productivity tool that helps engineers draft their inventions and prepare them for attorneys; legal filings must be handled by an attorney.
- Which LLM models does it work with? It can be configured to work with Claude 3.5 Sonnet, GPT-4o, or local open-weight models (Qwen, Llama 3).
- Will my confidential technical secrets leak to the internet? When running with a local LLM (Ollama or vLLM), all patent analyses are performed entirely on your local computer, and no data leaves your machine.
- Can it interpret patent drawings and flowcharts? When multimodal models are connected, it can also analyze system architecture and block diagram images and transcribe them into text.

## Related dictionary terms

- [Disclosure](https://trescout.com/en/dictionary/disclosure/)
- [patent disclosure](https://trescout.com/en/dictionary/patent-disclosure/)
- [Multimodal](https://trescout.com/en/dictionary/multimodal/)
- [Markdown](https://trescout.com/en/dictionary/markdown/)
- [Skill](https://trescout.com/en/dictionary/skill/)
- [LLM](https://trescout.com/en/dictionary/llm/)

- **Who it is for:** Patent attorneys, intellectual property managers, R&D engineers, and inventors.
- **License:** MIT (Özgür açık kaynak lisansı)
- **Framework:** Python-Based Patent Agent Skill
- **Platforms:** Linux, macOS, Windows

## Links

- [GitHub repository →](https://github.com/handsomestWei/patent-disclosure-skill)
- [Read in Turkish →](https://trescout.com/discover/patent-disclosure-skill/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-08-31: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/patent-disclosure-skill/
