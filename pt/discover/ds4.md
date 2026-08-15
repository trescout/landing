# Mecanismo de execução DeepSeek em hardware nativo

Desenvolvido por Salvatore Sanfilippo, criador do Redis, o ds4 é um mecanismo de inferência que permite executar modelos DeepSeek em hardware local. Esta ferramenta, escrita em linguagem C, oferece a oportunidade de executar modelos de alto desempenho em diferentes processadores gráficos graças ao suporte Metal, CUDA e ROCm.

- ★ 21.134
- C
- GitHub Trending · 2026-08-03

## O que você ganha
- Executa modelos de IA de alto desempenho em hardware de consumo
- Permite o uso do modelo mesmo com capacidade de memória limitada, transmitindo dados via SSD
- Permite a criação de um servidor LLM de nível empresarial com suporte multi-GPU

## Instalação
**Construa para se adequar ao seu hardware**

```
make                  # macOS Metal
make cuda-spark       # Linux CUDA, DGX Spark / GB10
make cuda-generic     # Linux CUDA, other local CUDA GPUs
make strix-halo       # Linux ROCm, AMD Strix Halo
make cpu              # CPU-only diagnostics build
```

**Baixe o modelo**

```
./download_model.sh q2-imatrix   # 96/128 GB RAM machines, imatrix-tuned q2
./download_model.sh q2-q4-imatrix  # 96/128 GB RAM machines, q2 with last 6 layers q4
./download_model.sh q4-imatrix   # >= 256 GB RAM machines, imatrix-tuned q4
./download_model.sh pro-q2-imatrix  # 512 GB RAM machines, PRO q2 imatrix quant
```


## Execução
**Inicialize o modelo**

```
./download_model.sh q2-imatrix

./ds4 \
  -m ./ds4flash.gguf \
  --ssd-streaming \
  --ssd-streaming-cache-experts 32GB \
  --ctx 32768 \
  --nothink
```


## Se você não programa
Ajude-me a escolher o modelo DeepSeek ou GLM mais adequado de acordo com os recursos de hardware do meu sistema. Qual comando de download devo usar e como posso superar o gargalo de memória ativando o recurso de streaming por SSD? Além disso, explique as configurações básicas necessárias para usar este sistema de inteligência artificial que instalei como servidor local.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/ds4/
