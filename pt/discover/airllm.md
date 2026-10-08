# Execute modelos gigantes de IA com 4 GB de VRAM

AirLLM é uma biblioteca de código aberto revolucionária que executa grandes modelos de linguagem (LLMs) massivos de 70 bilhões e 405 bilhões de parâmetros em placas de vídeo padrão de nível de consumidor com apenas 4 GB de memória de vídeo (VRAM), sem a necessidade de servidores corporativos ou caros clusters de GPU.

- ★ 35.481
- Jupyter Notebook
- GitHub Trending · 2026-06-04

## O que você ganha
- Executar modelos de 70B com 4GB de VRAM: A capacidade de rodar modelos de alto parâmetro, como Llama 3 70B, Qwen ou DeepSeek, mesmo em placas de vídeo de entrada como a GTX 1650 ou a RTX 3050.
- Suporte ao Llama 3.1 405B: Capacidade de executar modelos com 405 bilhões de parâmetros, que exigem clusters de GPU de centenas de milhares de dólares em data centers, em computadores pessoais com 8 GB de VRAM.
- Execução baseada em camadas (Layer-wise Execution): Em vez de carregar o modelo inteiro na VRAM, ele supera o gargalo da VRAM carregando e processando as camadas da unidade de disco para a memória sequencialmente.
- Velocidade até 3 vezes maior com compactação baseada em blocos: acelera a transferência de dados do disco para a GPU, lendo os pesos do modelo em blocos otimizados no SSD NVMe.
- Precisão total sem perda de qualidade por quantização: Oferece a capacidade de realizar inferência até mesmo na precisão original de 16 bits (bfloat16), se desejado, sem a necessidade de comprimir os pesos para 4 bits.

## Instalação
**com pip (PyPI)**

```
pip install airllm
```


## Arquitetura técnica e princípio de funcionamento
- A natureza sequencial das camadas Transformer: Uma rede Transformer é composta por 80 camadas independentes. Cada camada recebe a saída tensorial da camada anterior como entrada. Teoricamente, não é obrigatório que todo o modelo permaneça na memória.
- Descarte sequencial (Sequential Offloading): O AirLLM carrega apenas uma única camada que está sendo calculada no momento para a VRAM (cerca de 1,5 GB). Quando o cálculo de avanço (forward pass) da camada correspondente é concluído, a memória é liberada e a próxima camada é puxada do disco.
- Compromisso entre velocidade e memória (Trade-off): Esta arquitetura não foi desenvolvida para chats interativos que geram dezenas de tokens por segundo; ela é uma ferramenta de economia incomparável para processos de análise de dados em lote, raciocínio profundo, tradução, geração de dados sintéticos e avaliação de modelos (evals).
- Leitura de arquivos mapeados em memória (mmap): conecta tensores do PyTorch diretamente ao disco usando o método mmap, utilizando diretamente a largura de banda de SSDs NVMe sem sobrecarregar desnecessariamente a RAM do sistema.

## Exemplo de uso em Python
O AirLLM possui uma sintaxe Python extremamente simples, muito semelhante à API HuggingFace AutoModel:

## Se você não programa
Gostaria de executar um modelo de 70 bilhões de parâmetros (por exemplo, meta-llama/Llama-3-70B-Instruct) na minha placa gráfica local com capacidade de 4 GB de VRAM usando a biblioteca AirLLM. Usei o comando pip install airllm para a instalação. Você pode explicar o código Python necessário para carregar meu modelo, obter saídas com entrada de texto e evitar o estouro de memória? Sei que preciso garantir espaço em disco suficiente no processo, você pode detalhar os passos que devo seguir?

## Perguntas frequentes
- Quão rápido é executar um modelo com o AirLLM? Como o AirLLM transfere continuamente as camadas entre o disco e a GPU, a velocidade de geração de tokens depende diretamente da velocidade de leitura do seu SSD NVMe. Em um SSD Gen4 típico, um modelo de 70B roda a uma velocidade de 1 a 3 tokens por segundo. Embora essa velocidade seja lenta para um chat interativo, ela é incomparável para rodar modelos gigantescos localmente com custo de hardware zero.
- Quanto espaço de armazenamento livre é necessário para o AirLLM? Um modelo com 70B parâmetros no formato float de 16-bit requer cerca de 140 GB de espaço em disco. Nas versões quantizadas de 4-bit, esse espaço cai para o nível de 35-40 GB. Para o modelo de 405B, deve ser reservado pelo menos 800 GB de espaço livre em disco NVMe.
- Posso usar os pesos originais do modelo sem quantização? Sim. Uma das maiores vantagens do AirLLM é que ele elimina a necessidade de quantização. Como a restrição de VRAM é resolvida camada por camada, você pode executar os pesos originais de 16 bits sem sofrer nenhuma perda de raciocínio ou precisão.
- O AirLLM funciona em Mac com Apple Silicon ou apenas em CPU? O AirLLM é otimizado principalmente para aceleração CUDA (GPU NVIDIA). No entanto, ele também suporta de forma experimental a execução em CPU e camadas MPS (Apple Silicon Metal). A maior eficiência é obtida com um SSD NVMe rápido e uma placa de vídeo NVIDIA.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/airllm/
