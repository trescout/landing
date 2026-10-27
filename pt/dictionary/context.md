# O que é Context?

*Inteligência artificial · Última atualização: 19 de setembro de 2026*

Contexto é o conjunto de informações ambientais e semânticas de que um dado, comando ou processo necessita para ser interpretado e executado corretamente.

## 1. Contexto em Inteligência Artificial e LLMs

Grandes modelos de linguagem (LLM) não possuem uma memória permanente ou memória de experiência como os humanos; em cada consulta, eles apenas "lembram" dos dados incluídos na janela de contexto (context window) naquele momento.

### Transformer e Mecanismo de Atenção (Self-Attention)

Na arquitetura Transformer, o contexto é estabelecido ponderando a relação de uma palavra no início da frase com uma palavra no final (vetores de Consulta/Query, Chave/Key, Valor/Value). O modelo resolve se a palavra "banco" se refere a uma instituição financeira ou à margem de um rio apenas observando o contexto da frase em que ela aparece.

### Janela de Contexto (Context Window) e seus Limites

- Capacidade de Tokens: É o comprimento máximo que um modelo pode ler e gerar como resposta de uma só vez (por exemplo, 8K, 32K, 128K ou 1M+ tokens).
- Custo de Memória (KV Cache): À medida que o contexto aumenta, o requisito de memória da matriz de atenção cresce quadraticamente. Para aliviar essa carga, são utilizadas otimizações de FlashAttention e KV-Cache.
- Problema do Meio Perdido (Lost in the Middle): Pesquisas mostram que os LLMs focam melhor nas informações localizadas no início e no fim de textos longos do que nas informações contidas no meio.
- RAG (Geração Aumentada por Recuperação): Em vez de tentar encaixar milhões de páginas de dados corporativos na janela de contexto, apenas os parágrafos mais relevantes para a consulta são filtrados por meio de um mecanismo de busca ou banco de dados vetorial e transmitidos ao modelo como contexto.

***Analogia:** Ao conversar com um amigo, se você disser apenas "Sim, ele também disse isso", ele não o entenderá; no entanto, se você disser "Estou falando daquele filme sobre o qual conversamos ontem", você terá fornecido o contexto necessário.*

## 2. Contexto em Sistemas Operacionais e Programação

Na programação de sistemas, "contexto" refere-se a todos os valores de variáveis e registradores que refletem completamente o estado atual de um programa durante sua execução.

### Troca de Contexto (Context Switching)

Um sistema operacional que executa multitarefa (multitasking) compartilha o núcleo da CPU entre diferentes processos e threads:

1. Os registradores da CPU (RAX, RSP, RIP, etc.), o ponteiro de pilha e as páginas de memória do processo em execução são salvos no Bloco de Controle de Processo (PCB - Process Control Block).
2. Os registradores do próximo processo são restaurados na CPU.
3. Custo: A troca de contexto é muito custosa em nível de hardware, pois causa a invalidação (poluição de cache) dos caches L1/L2 da CPU e dos mapas de endereços TLB (Translation Lookaside Buffer).

### Gerenciamento de Contexto em Linguagens

- Go (context.Context): é utilizado para transmitir sinais de cancelamento, prazos (deadlines) e metadados de escopo de solicitação entre requisições de rede ou goroutines assíncronas.
- Python (blocos with): Os gerenciadores de contexto (Context Managers) tornam as operações de limpeza de recursos, como leitura de arquivos ou abertura/fechamento de conexões de banco de dados, mais seguras.
- React (Context API): É um método para transmitir o estado global profundamente na árvore de componentes sem precisar passar props individualmente para os componentes intermediários (sem prop drilling).

## Comparação: O Conceito de Contexto em Diferentes Disciplinas

| Área | Valor Representado pelo Contexto | Componentes Típicos | Problemas Encontrados |
|---|---|---|---|
| Inteligência Artificial (LLM) | Prompt de entrada + Histórico de chat + Documentos | Tokens, Máscaras de Atenção, Cache KV | Limite de tokens, Alucinação, Consumo de memória |
| Sistemas Operacionais | Estado instantâneo de hardware de um processo | Registradores, Contador de Programa, Tabelas de Páginas | Latência da CPU, falhas de cache, flush de TLB |
| Desenvolvimento de Software | Ciclo de vida da solicitação e dados de ambiente | Sinal de timeout, token de autorização | Vazamento de memória, chamadas assíncronas não canceladas |

## Perguntas e respostas

**O que significa Context e qual é a sua tradução para o português?**

A tradução para o português é "contexto". Refere-se ao conjunto de condições, plano de fundo e situações complementares relacionadas em que qualquer expressão, dado ou processo está inserido.

**Qual é a diferença entre Prompt e Contexto?**

O Prompt é a entrada, pergunta ou instrução de ação dada diretamente à inteligência artificial ("Explique este código"). O Contexto, por sua vez, é a informação adicional, o código completo, as variáveis de ambiente ou o histórico de conversas fornecidos para que o modelo execute essa instrução corretamente.

**Por que a Janela de Contexto (Context Window) é limitada?**

Na arquitetura Transformer, cada token é correlacionado com todos os outros tokens. Como esse cálculo matemático e a memória armazenada (KV-Cache) aumentam proporcionalmente ao quadrado do comprimento do contexto, a memória da GPU cria um limite de hardware.

**Por que a "Troca de Contexto" (Context Switch) no sistema operacional causa perda de desempenho?**

Ao alternar de um processo para outro, a CPU precisa salvar seus registradores, carregar o espaço de memória do novo processo e limpar e recarregar os caches do processador (L1/L2/L3 e TLB). Isso resulta em uma perda direta de processamento na ordem de microssegundos.

**Por que o pacote context na linguagem Go é passado como o primeiro parâmetro para cada função?**

O parâmetro ctx context.Context em Go evita o consumo desnecessário de recursos do servidor, garantindo que, quando uma solicitação HTTP é cancelada ou atinge o tempo limite, as consultas ao banco de dados e os trabalhos em segundo plano associados também sejam interrompidos.

## Termos relacionados

- [Context Window](https://trescout.com/pt/dictionary/context-window/)
- [Prompt](https://trescout.com/pt/dictionary/prompt/)
- [RAG](https://trescout.com/pt/dictionary/rag/)
- [Runtime](https://trescout.com/pt/dictionary/runtime/)

## Ferramentas relacionadas

- [REA](https://trescout.com/pt/discover/rea/)
- [Servers](https://trescout.com/pt/discover/servers/)
- [OmniRoute](https://trescout.com/pt/discover/omniroute/)
- [Goose](https://trescout.com/pt/discover/goose/)
- [Chrome Devtools MCP](https://trescout.com/pt/discover/chrome-devtools-mcp/)
- [Openclaude](https://trescout.com/pt/discover/openclaude/)
- [Context Mode](https://trescout.com/pt/discover/context-mode/)
- [Code Review Graph](https://trescout.com/pt/discover/code-review-graph/)

Esta explicação foi escrita em linguagem simples para a TreScout com IA e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/context/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/context/
