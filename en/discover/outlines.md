# Configure AI outputs

The Outlines library enables the responses from large language models to be presented as structured outputs according to predefined schemas. With this Python-based tool, developers protect data integrity by restricting model outputs with regular expressions or context-free grammar rules.

- ★ 15,525
- Python
- GitHub Trending · 2026-07-22

## Updates

- **August 7, 2026:** Stars 15,477 → 15,525, latest release 1.3.3 (August 6, 2026).
- **August 2, 2026:** Stars 14,917 → 15,477, latest release 1.3.2 (July 20, 2026).

## What you get

- Constrains model outputs according to predefined schemas
- Fully compatible with JSON or Python data types
- Eliminates the need to debug erroneous outputs

## Installation

**Install the library**

```
pip install outlines
```

## Running it

**Connect the model**

```
import outlines
from transformers import AutoTokenizer, AutoModelForCausalLM


MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"
model = outlines.from_transformers(
    AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto"),
    AutoTokenizer.from_pretrained(MODEL_NAME)
)
```

## If you don't write code

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to restrict the response from an AI model to a specific Pydantic data structure or Python type (e.g. int or Literal) using the Outlines library. How can I use the model(request, output_type) function after defining the model object to ensure that the model's output always conforms to the schema I want? Please explain with example how to define the Pydantic model for complex objects and apply this structure to the model output.

## Related dictionary terms

- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is for developers who want to convert irregular text outputs from AI models into structured data that can be used directly in software processes.
- **License:** Apache-2.0

## Links

- [GitHub repository →](https://github.com/dottxt-ai/outlines)
- [Read in Turkish →](https://trescout.com/discover/outlines/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-07-22: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/outlines/
