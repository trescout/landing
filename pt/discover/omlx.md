# Servidor AI para computadores Mac

Omlx é um servidor de inferência de grandes modelos de linguagem (LLM) local de próxima geração que oferece recursos de processamento em lote contínuo (continuous batching) e cache em SSD para computadores Mac com processadores Apple Silicon (M1/M2/M3/M4). Ele combina a infraestrutura Apple MLX com uma API compatível com OpenAI e uma interface na barra de menus do macOS.

- ★ 23.036
- Python
- GitHub Trending · 2026-08-18

## Atualizações

- **25 de outubro de 2026:** Estrelas 22,973 → 23,036, versão mais recente v0.7.3.dev2 (25 de outubro de 2026).
- **21 de outubro de 2026:** Estrelas 22,855 → 22,973, versão mais recente v0.7.2 (21 de outubro de 2026).
- **16 de outubro de 2026:** Estrelas 22,825 → 22,855, versão mais recente v0.7.1rc1 (15 de outubro de 2026).
- **15 de outubro de 2026:** Estrelas 22,655 → 22,825, versão mais recente v0.7.1.dev2 (15 de outubro de 2026).

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

Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero executar um grande modelo de linguagem localmente usando o servidor Omlx no meu Mac com Apple Silicon. Após concluir a instalação com o Homebrew, você poderia explicar passo a passo como executar o servidor em segundo plano, gerenciar a seleção de modelos na barra de menus e como me conectar a esse modelo local através do editor de código Cursor ou da biblioteca Python openai?

Repositório: https://github.com/jundot/omlx. Baseie-se nas instruções oficiais no arquivo README deste repositório para a instalação e execução.

Antes de começar, verifique em qual sistema operacional estamos e se as ferramentas necessárias (ex: Python, Node.js, Git, Docker) estão instaladas. Instale as que faltarem passo a passo de acordo com este sistema.

Crie uma pasta nova e vazia para trabalhar. Não toque em arquivos fora desta pasta e não exclua nada. Antes de executar cada comando, diga o que você vai fazer em uma frase.

Diga-me o que devo ver na tela ao final de cada etapa. Se ocorrer um erro, colarei a mensagem de erro para você exatamente como ela é, e vamos corrigi-la juntos.

## Perguntas frequentes

- Qual é a principal diferença entre o Omlx e o Ollama? Enquanto o Ollama utiliza geralmente a infraestrutura llama.cpp baseada em C++, o Omlx funciona diretamente sobre o framework MLX desenvolvido pela Apple. Graças a isso, ele estabelece uma integração mais profunda com as unidades Metal e o motor neural dos chips Apple Silicon, proporcionando uma velocidade de geração de tokens mais elevada, especialmente em processamento contínuo e contextos longos.
- Quais modelos podem ser executados com 16 GB ou 24 GB de RAM? Modelos de 8B parâmetros quantizados em 4 bits (Llama 3, Qwen 2.5, Mistral) ocupam cerca de 5-6 GB de memória e rodam de forma extremamente fluida em Macs de 16 GB. Em dispositivos com 24 GB ou 36 GB de memória unificada, modelos de 14B ou 32B podem ser carregados facilmente.
- O cache de SSD desgasta a vida útil do disco do Mac? Não. O Omlx utiliza algoritmos de buffer inteligentes para evitar ciclos de escrita desnecessários durante as operações de cache. Ele só é ativado quando a memória de contexto se aproxima do limite da RAM, mantendo o desgaste do disco no mínimo.
- Funciona em Macs antigos baseados em Intel? Não. O Omlx é otimizado especificamente para Apple Silicon (arquitetura ARM) e para o framework Apple MLX. Ele não funciona em Macs baseados em Intel ou em computadores Windows/Linux x86.

## Termos relacionados do glossário

- [Continuous Batching](https://trescout.com/pt/dictionary/continuous-batching/)
- [SSD Caching](https://trescout.com/pt/dictionary/ssd-caching/)
- [Context Window](https://trescout.com/pt/dictionary/context-window/)
- [Caching](https://trescout.com/pt/dictionary/caching/)
- [Apple Silicon](https://trescout.com/pt/dictionary/apple-silicon/)
- [RAM](https://trescout.com/pt/dictionary/ram/)

- **Para quem é:** É destinado a desenvolvedores de inteligência artificial que desejam executar grandes modelos de linguagem (LLM) em computadores Mac com processador Apple Silicon com a máxima velocidade e privacidade local.
- **Licença:** Apache-2.0 (licença de código aberto)
- **Framework:** Motor de inferência local baseado em Apple MLX e Python
- **Hardware:** Série Apple Silicon M1, M2, M3, M4 (com suporte a Pro, Max, Ultra)

## Links

- [Repositório no GitHub →](https://github.com/jundot/omlx)
- [Ler em turco →](https://trescout.com/discover/omlx/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-08-18: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. O texto de apresentação foi preparado com IA a partir da própria documentação do repositório e esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/omlx/
