# Servidor de IA para computadores Mac

O Omlx é um servidor de inferência de grandes modelos de linguagem (LLM) local de última geração para Macs com Apple Silicon (M1/M2/M3/M4), oferecendo loteamento contínuo (continuous batching) e cache em SSD. Ele combina a base do Apple MLX com uma API compatível com a OpenAI e controle na barra de menus do macOS.

- ★ 21.147
- Python
- GitHub Trending · 2026-08-18

## Atualizações
- 31 de agosto de 2026: Estrelas 20.793 → 21.147, versão mais recente v0.6.4 (29 de agosto de 2026).
- 27 de agosto de 2026: Estrelas 20.069 → 20.793, versão mais recente v0.6.3rc3 (24 de agosto de 2026).
- 20 de agosto de 2026: Estrelas 19.758 → 20.069, versão mais recente v0.6.3rc2 (20 de agosto de 2026).
- 19 de agosto de 2026: Estrelas 19.519 → 19.758, versão mais recente v0.6.3rc1 (19 de agosto de 2026).

## O que você ganha
- Aceleração de hardware Apple MLX e Metal: Utiliza diretamente a Arquitetura de Memória Unificada (UMA) para eliminar totalmente gargalos de cópia de memória entre CPU e GPU.
- Loteamento contínuo (Continuous Batching): Consolida requisições simultâneas de múltiplos usuários e agentes em uma única passagem de cálculo, aumentando a taxa de transferência em até 3x.
- Cache em SSD e pré-preenchimento em blocos (Chunked Prefill): Armazena o cache chave-valor (KV) no SSD NVMe em janelas de contexto longas, evitando travamentos por falta de memória (OOM).
- API padrão compatível com OpenAI: Conecta-se sem atrito ao Cursor, Open WebUI, Continue e LangChain pelos endpoints /v1/chat/completions e /v1/models.
- Controle pela barra de menus do macOS: Inicie, pause, alterne modelos e acompanhe o consumo de memória em tempo real sem precisar abrir o terminal.

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

**Baixando e servindo um modelo específico**

```
omlx run mlx-community/Llama-3.2-3B-Instruct-4bit
```

## Arquitetura técnica e princípio de funcionamento

O Omlx foi construído sobre o framework de aprendizado de máquina MLX da Apple. Ele se apoia em três pilares arquiteturais projetados para superar as barreiras de inferência tradicionais no Mac (como llama.cpp ou Ollama):
- Aproveitamento total da Memória Unificada (UMA): Diferente de PCs com GPUs dedicadas, no Apple Silicon os núcleos gráficos acessam diretamente até 128 GB ou 192 GB de RAM. O Omlx processa esse espaço com latência zero por meio de kernels em Metal Shading Language (MSL).
- Gerenciamento dinâmico de cache KV (PagedAttention): Aloca tensores chave-valor em blocos paginados para evitar fragmentação de memória em múltiplas sessões, liberando espaço imediatamente ao término da resposta.
- Camada de cache com transbordo para SSD: Quando o cache KV em janelas de 32K ou 128K excede a RAM física, o Omlx pagina automaticamente para o SSD NVMe integrado de alta velocidade sem derrubar o modelo.

## Integração de API local compatível com OpenAI

Ao ser iniciado, o Omlx disponibiliza uma API REST compatível com OpenAI localmente (padrão em http://localhost:8000). Você pode alimentar diretamente seus editores de código e aplicações de IA:

**Teste de API com cURL**

```
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "default",
    "messages": [{"role": "user", "content": "Qual e a principal vantagem arquitetural do Apple Silicon?"}],
    "temperature": 0.7
  }'
```

## Se você não programa
🤖 Se você não programa
Quero executar um modelo de linguagem local no meu Mac Apple Silicon usando o Omlx. Depois de instalar via Homebrew, você pode me explicar passo a passo como iniciar o servidor em segundo plano, gerenciar modelos pela barra de menus e conectar o editor Cursor ou um script Python via biblioteca openai a esse modelo local?

- **Para quem:** Desenvolvedores de IA e usuários de Mac Apple Silicon que buscam velocidade máxima de inferência e total privacidade local.
- **Licença:** Apache-2.0 (Licença de código aberto)
- **Framework:** Motor de inferência local baseado em Apple MLX e Python
- **Hardware:** Apple Silicon séries M1, M2, M3, M4 (com suporte a Pro, Max e Ultra)

## Perguntas frequentes
- Qual é a principal diferença entre o Omlx e o Ollama? Enquanto o Ollama utiliza a infraestrutura llama.cpp em C++, o Omlx roda nativamente sobre o framework MLX da Apple. Essa integração direta com Metal e Neural Engine proporciona taxas mais altas de geração de tokens, especialmente com continuous batching e contextos longos.
- Quais modelos rodam com 16 GB ou 24 GB de RAM? Modelos de 8B com quantização de 4 bits (Llama 3, Qwen 2.5, Mistral) consomem cerca de 5 a 6 GB e rodam com fluidez em Macs de 16 GB. Já aparelhos com 24 GB ou 36 GB de memória unificada conseguem carregar modelos de 14B ou 32B.
- O cache em SSD desgasta o disco do Mac? Não. O Omlx adota buffers inteligentes para evitar ciclos desnecessários de escrita. Ele só é acionado quando o contexto se aproxima do teto da RAM física, minimizando o impacto no SSD.
- Funciona em Macs antigos com Intel ou em PCs Windows/Linux? Não. O Omlx é rigorosamente otimizado para a arquitetura ARM do Apple Silicon e a biblioteca Apple MLX. Não é compatível com processadores x86.

## Links
- [GitHub →](https://github.com/jundot/omlx)

## Termos relacionados do glossário
Apple Silicon Continuous Batching LLM Local Open Source

---
Source: TreScout Discover · https://trescout.com/pt/discover/omlx/
