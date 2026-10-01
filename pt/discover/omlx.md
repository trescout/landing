# Servidor AI para computadores Mac

Omlx é um servidor de inferência de grandes modelos de linguagem (LLM) local de próxima geração que oferece recursos de processamento em lote contínuo (continuous batching) e cache em SSD para computadores Mac com processadores Apple Silicon (M1/M2/M3/M4). Ele combina a infraestrutura Apple MLX com uma API compatível com OpenAI e uma interface na barra de menus do macOS.

- ★ 22.409
- Python
- GitHub Trending · 2026-08-18

## O que você ganha
- Aceleração de hardware Apple MLX e Metal: elimina completamente o gargalo de cópia de memória entre a CPU e a GPU ao utilizar diretamente a Arquitetura de Memória Unificada (UMA) dos processadores Apple Silicon.
- Continuous Batching: Aumenta o rendimento do servidor em até 3 vezes ao combinar um grande número de solicitações simultâneas de usuários e agentes em um único ciclo de computação.
- Cache de SSD e pré-preenchimento de partes (Chunked Prefill): Evita travamentos por falta de memória (OOM) ao armazenar o cache de chave-valor (KV) em SSDs NVMe em janelas de contexto longas.
- API padrão compatível com OpenAI: graças aos endpoints /v1/chat/completions e /v1/models, funciona com as ferramentas Cursor, Open WebUI, Continue e LangChain sem necessidade de configuração.
- Controle da barra de menus do macOS: oferece a praticidade de iniciar, parar, selecionar modelos e monitorar o consumo de memória com gráficos em tempo real, sem precisar acessar o Terminal.

## Instalação
**Instalação com Homebrew**

```
brew tap jundot/omlx https://github.com/jundot/omlx
brew install jundot/omlx/omlx
```


## Execução
**Iniciando o serviço em segundo plano**

```
omlx start
```

**Baixar e servir um modelo específico**

```
omlx run mlx-community/Llama-3.2-3B-Instruct-4bit
```


## Arquitetura técnica e princípio de funcionamento
- Aproveitamento total da memória unificada (UMA): Ao contrário dos PCs com placas de vídeo dedicadas, nos Macs com Apple Silicon, 128 GB ou 192 GB de RAM podem ser endereçados diretamente pelos núcleos da GPU. O Omlx processa esse enorme pool de memória com latência zero usando kernels da Metal Shading Language (MSL).
- Gerenciamento dinâmico de cache KV (PagedAttention): Aloca tensores de chave-valor em blocos paginados para evitar a fragmentação de memória em múltiplas sessões. Quando o prompt é concluído, a memória utilizada é liberada imediatamente.
- Camada de cache com overflow para SSD: Quando o cache KV excede a RAM em janelas de contexto massivas, como 32K e 128K, o Omlx realiza automaticamente o paging para o SSD integrado de alta velocidade da Apple. Assim, o modelo continua a inferência sem travar.

## Integração de API local compatível com OpenAI
**Teste de API com cURL**

```
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "default",
    "messages": [{"role": "user", "content": "Apple Silicon mimarisinin temel avantajı nedir?"}],
    "temperature": 0.7
  }'
```


## Se você não programa
Quero executar um grande modelo de linguagem localmente usando o servidor Omlx no meu Mac com Apple Silicon. Após concluir a instalação com o Homebrew, você poderia explicar passo a passo como executar o servidor em segundo plano, gerenciar a seleção de modelos na barra de menus e como me conectar a esse modelo local através do editor de código Cursor ou da biblioteca Python openai?

## Perguntas frequentes
- Qual é a principal diferença entre o Omlx e o Ollama? Enquanto o Ollama utiliza geralmente a infraestrutura llama.cpp baseada em C++, o Omlx funciona diretamente sobre o framework MLX desenvolvido pela Apple. Graças a isso, ele estabelece uma integração mais profunda com as unidades Metal e o motor neural dos chips Apple Silicon, proporcionando uma velocidade de geração de tokens mais elevada, especialmente em processamento contínuo e contextos longos.
- Quais modelos podem ser executados com 16 GB ou 24 GB de RAM? Modelos de 8B parâmetros quantizados em 4 bits (Llama 3, Qwen 2.5, Mistral) ocupam cerca de 5-6 GB de memória e rodam de forma extremamente fluida em Macs de 16 GB. Em dispositivos com 24 GB ou 36 GB de memória unificada, modelos de 14B ou 32B podem ser carregados facilmente.
- O cache de SSD desgasta a vida útil do disco do Mac? Não. O Omlx utiliza algoritmos de buffer inteligentes para evitar ciclos de escrita desnecessários durante as operações de cache. Ele só é ativado quando a memória de contexto se aproxima do limite da RAM, mantendo o desgaste do disco no mínimo.
- Funciona em Macs antigos baseados em Intel? Não. O Omlx é otimizado especificamente para Apple Silicon (arquitetura ARM) e para o framework Apple MLX. Ele não funciona em Macs baseados em Intel ou em computadores Windows/Linux x86.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/omlx/
