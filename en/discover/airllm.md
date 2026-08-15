# Run giant AI models with 4GB VRAM

AirLLM allows large language models with 70 billion parameters to be run on graphics processing units with only 4 GB of video memory (VRAM). This library uses memory optimization techniques to enable the use of high-capacity models with low hardware requirements.

- ★ 30,796
- Jupyter Notebook
- GitHub Trending · 2026-06-04

## What you get
- Possibility to run models with 70B parameters with 4GB VRAM.
- Ability to use 405B Llama3.1 models with 8GB VRAM.
- Up to 3x speed increase with block-based compression.

## Installation
**Package installation**

```
pip install airllm
```


## Running it
**Load and run the model**

```
from airllm import AutoModel

MAX_LENGTH = 128
# could use hugging face model repo id:
model = AutoModel.from_pretrained("garage-bAInd/Platypus2-70B-instruct")

# or use model's local path...
#model = AutoModel.from_pretrained("/home/ubuntu/.cache/huggingface/hub/models--garage-bAInd--Platypus2-70B-instruct/snapshots/b585e74bcaae02e52665d9ac6d23f4d0dbc81a0f")

input_text = [
        'What is the capital of United States?',
        #'I like',
    ]

input_tokens = model.tokenizer(input_text,
    return_tensors="pt", 
    return_attention_mask=False, 
    truncation=True, 
    max_length=MAX_LENGTH, 
    padding=False)
           
generation_output = model.generate(
    input_tokens['input_ids'].cuda(), 
    max_new_tokens=20,
    use_cache=True,
    return_dict_in_generate=True)

output = model.tokenizer.decode(generation_output.sequences[0])

print(output)
```


## If you don't write code
I want to run a model with 70B parameters using the AirLLM library on my graphics card with low VRAM capacity. I used the pip install airllm command for installation. How can I create the Python code structure needed to load my model and output it with a simple text input, using the AutoModel class? I know I need to make sure I have enough disk space during the process, can you explain the basic steps I need to follow to start the process?

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/airllm/
