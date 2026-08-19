# Execute modelos gigantes de IA com 4 GB de VRAM

AirLLM permite que grandes modelos de linguagem com 70 bilhões de parâmetros sejam executados em unidades de processamento gráfico com apenas 4 GB de memória de vídeo (VRAM). Esta biblioteca utiliza técnicas de otimização de memória para permitir o uso de modelos de alta capacidade com baixos requisitos de hardware.

- ★ 31.598
- Jupyter Notebook
- GitHub Trending · 2026-06-04

## O que você ganha
- Possibilidade de rodar modelos com parâmetros de 70B com 4GB VRAM.
- Capacidade de usar modelos 405B Llama3.1 com 8 GB VRAM.
- Aumento de velocidade de até 3x com compactação baseada em bloco.

## Instalação
**Instalação do pacote**

```
pip install airllm
```


## Execução
**Carregar e executar o modelo**

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


## Se você não programa
Quero rodar um modelo com parâmetros de 70B usando a biblioteca AirLLM na minha placa gráfica com baixa capacidade de VRAM. Usei o comando pip install airllm para instalação. Como posso criar a estrutura de código Python necessária para carregar meu modelo e produzi-lo com uma entrada de texto simples, usando a classe AutoModel? Eu sei que preciso ter espaço em disco suficiente durante o processo. Você pode explicar as etapas básicas que preciso seguir para iniciar o processo?

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/airllm/
