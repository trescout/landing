# Configure AI outputs

The Outlines library enables the responses from large language models to be presented as structured outputs according to predefined schemas. With this Python-based tool, developers protect data integrity by restricting model outputs with regular expressions or context-free grammar rules.

- ★ 15,525
- Python
- GitHub Trending · 2026-07-22

## Update
- August 7, 2026: Star 15,477 → 15,525, last version 1.3.3 (August 6, 2026).
- August 2, 2026: Star 14,917 → 15,477, last version 1.3.2 (July 20, 2026).

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
I want to restrict the response from an AI model to a specific Pydantic data structure or Python type (e.g. int or Literal) using the Outlines library. How can I use the model(request, output_type) function after defining the model object to ensure that the model's output always conforms to the schema I want? Please explain with example how to define the Pydantic model for complex objects and apply this structure to the model output.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/outlines/
