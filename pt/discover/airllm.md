# Execute modelos gigantes de IA com 4GB de VRAM

O AirLLM é uma biblioteca de código aberto revolucionária que permite executar modelos de linguagem gigantes (LLM) de 70 e 405 bilhões de parâmetros em placas de vídeo de consumo com apenas 4 GB de memória de vídeo (VRAM), dispensando servidores corporativos ou clusters de GPUs caríssimos.

- ★ 33.755
- Jupyter Notebook
- GitHub Trending · 2026-06-04

## Atualizações
- 6 de setembro de 2026: Estrelas 33.307 → 33.755, versão mais recente v4.0.0 (5 de setembro de 2026).
- 31 de agosto de 2026: Estrelas 31.598 → 33.307, versão mais recente v3.3.0 (28 de agosto de 2026).
- 19 de agosto de 2026: Estrelas 30.796 → 31.598, versão mais recente v3.2.0 (18 de agosto de 2026).
- 12 de agosto de 2026: Estrelas 29.265 → 30.796, versão mais recente v3.1.0 (29 de julho de 2026).

## O que você ganha
- Execução de modelos 70B em 4GB de VRAM: Rode modelos de alto calibre como Llama 3 70B, Qwen ou DeepSeek em placas de entrada como GTX 1650 ou RTX 3050.
- Suporte ao Llama 3.1 405B: Carregue modelos monstruosos de 405 bilhões de parâmetros em computadores comuns com 8GB de VRAM sem clusters de data centers.
- Execução em camadas (Layer-wise Execution): Em vez de colocar o modelo inteiro na memória, transmite e processa camada por camada do disco para a GPU, quebrando a barreira da VRAM.
- Até 3x mais velocidade com compressão em blocos: Lê pesos no SSD NVMe em blocos otimizados para acelerar a transferência do disco para a GPU.
- Precisão total sem perda por quantização: Não força a compressão em 4 bits, permitindo rodar em precisão nativa de 16 bits (bfloat16).

## Instalação

**Com pip (PyPI)**

```
pip install airllm
```

## Arquitetura técnica e princípio de funcionamento

Motores de inferência tradicionais (como vLLM, Ollama ou HuggingFace) exigem que todos os parâmetros do modelo fiquem simultaneamente na memória de vídeo (VRAM). Um modelo de 70B consome cerca de 140 GB em 16 bits e pelo menos 35-40 GB mesmo quantizado em 4 bits. O AirLLM quebra completamente esse paradigma:
- Natureza sequencial dos modelos Transformer: Uma rede Transformer conta com cerca de 80 camadas sequenciais. Cada camada recebe como entrada a saída da camada anterior. Não há necessidade matemática de manter todas em memória ao mesmo tempo.
- Descarregamento sequencial (Sequential Offloading): O AirLLM carrega na VRAM apenas a camada ativa naquele milissegundo (~1.5 GB). Ao fim do cálculo, a memória é limpa e a próxima camada é lida do disco.
- Compensação entre velocidade e memória: A arquitetura não foi desenhada para chats interativos em tempo real com alta taxa de tokens, mas representa uma economia gigantesca para processamento em lote, análise de dados, raciocínio e avaliação de modelos.
- Leitura de arquivos mapeada em memória (mmap): Mapeia tensores PyTorch diretamente no SSD NVMe via mmap, aproveitando a largura de banda do disco sem superlotar a RAM do computador.

## Exemplo de uso em Python

O AirLLM oferece uma interface muito limpa em Python, inspirada na API AutoModel do HuggingFace:

**Executando modelo 70B em Python**

```python
from airllm import AutoModel

# Inicialize um modelo 70B com apenas 4GB de VRAM
model = AutoModel.from_pretrained("meta-llama/Meta-Llama-3-70B-Instruct")

input_text = ["Resuma as perspectivas da inteligencia artificial no Brasil."]
input_tokens = model.tokenizer(input_text, return_tensors="pt", padding=True)

# Geracao de texto (camadas executadas sequencialmente)
generation_output = model.generate(
    input_tokens['input_ids'].cuda(),
    max_new_tokens=100,
    use_cache=True,
    return_dict_in_generate=True
)

output = model.tokenizer.decode(generation_output.sequences[0])
print(output)
```

## Se você não programa
🤖 Se você não programa
Quero usar a biblioteca AirLLM para rodar um modelo de 70 bilhões de parâmetros (como meta-llama/Llama-3-70B-Instruct) na minha placa de vídeo local de 4GB de VRAM. Fiz a instalação com pip install airllm. Você pode me fornecer o código em Python para carregar o modelo, gerar respostas e evitar erros de falta de memória? Poderia detalhar o espaço em disco exigido e os passos que devo seguir?

- **Para quem:** Pesquisadores e desenvolvedores com GPUs de entrada que precisam testar modelos 70B e 405B localmente para avaliações e extração de dados.
- **Licença:** Apache-2.0 (Licença permissiva de código aberto)
- **Requisitos de Hardware:** GPU com no mínimo 4 GB de VRAM e disco SSD NVMe de alta velocidade
- **Ecossistema:** Python, PyTorch e HuggingFace Transformers

## Perguntas frequentes
- Qual é a velocidade de geração do AirLLM? Como o AirLLM move dados continuamente entre o disco e a GPU, a velocidade depende da leitura do seu SSD NVMe. Em um SSD Gen4, um modelo de 70B gera de 1 a 3 tokens por segundo. É mais lento para conversas em tempo real, mas viabiliza modelos gigantes com custo zero de hardware extra.
- Quanto espaço em disco é necessário? Um modelo de 70B em 16 bits requer em torno de 140 GB de disco (ou 35-40 GB em 4 bits). Para modelos 405B, reserve ao menos 800 GB livres no SSD NVMe.
- Posso usar os pesos originais sem aplicar quantização? Sim. Uma das principais vantagens do AirLLM é dispensar a perda de precisão da quantização. Como o gargalo é resolvido camada por camada, você pode rodar em 16 bits sem nenhuma degradação de acurácia.
- O AirLLM funciona em Mac Apple Silicon ou só com CPU? O AirLLM é primariamente otimizado para CUDA (placas NVIDIA). Existe suporte experimental a CPU e Apple Silicon MPS, mas o melhor desempenho vem de GPUs NVIDIA aliadas a SSDs NVMe velozes.

## Links
- [GitHub →](https://github.com/lyogavin/airllm)

## Termos relacionados do glossário
VRAM LLM Large Language Models Transformer Open Source

---
Source: TreScout Discover · https://trescout.com/pt/discover/airllm/
