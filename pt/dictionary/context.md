# O que é Contexto (Context)? IA e Sistemas

> Inglês: Context · Etimologia: latim contexere (tecer junto, entrelaçar)

**Categoria:** AI  
**Última atualização:** 2026-09-19

Contexto (context) é um fundamento computacional que define ou a janela de tokens ativa utilizada por inteligências artificiais para responder a prompts, ou o estado interno de registradores e memória que um sistema operacional preserva ao alternar tarefas.

## Por analogia
Se você chegar para alguém e apenas disser 'Sim, ele aprovou', a pessoa não saberá do que se trata; ao dizer 'Sobre aquele projeto que discutimos ontem', você fornece o contexto indispensável para a conversa fazer sentido.

## 1. O Contexto na Inteligência Artificial e LLMs
Modelos de linguagem não guardam memórias vivas após cada execução. Para compreender e formular respostas coerentes, dependem integralmente da sua **janela de contexto**: o conjunto de tokens (instruções, mensagens passadas e documentos recuperados via RAG) enviados na requisição. A extensão dessa janela define quanta informação o modelo consegue processar simultaneamente.

## 2. O Contexto em Sistemas Operacionais e Programação
No nível do sistema operacional, o contexto representa o estado exato de um processador ao executar um programa: valores de registradores, ponteiro de instrução (PC) e tabela de páginas de memória. Quando o sistema suspende um processo para rodar outro, ocorre uma **troca de contexto (context switch)**, salvando o estado anterior e restaurando o novo.

## Perspectivas comparadas entre áreas da computação
Aplicações distintas do conceito de contexto :
- **Modelos de Linguagem:** Búfer de tokens e cache de atenção (KV Cache) que fornecem a memória de trabalho do raciocínio.- **Núcleo do Sistema Operacional:** Bloco de Controle de Processo (PCB) registrando estados de registradores na CPU.- **Desenvolvimento de Software:** Contextos em Go ou React que propagam sinais de cancelamento e variáveis globais na árvore de chamadas.

## Perguntas frequentes

**O que é o fenômeno 'lost in the middle' em LLMs?**  
É a tendência de modelos de linguagem reterem com mais precisão dados no início e no fim do prompt, perdendo detalhes colocados no meio de textos extensos.

**Por que a troca de contexto de CPU gera perda de performance?**  
Porque exige salvar e recarregar registradores do processador, invalidando linhas de memória cache rápida (TLB e L1/L2).

**Qual o papel do Context no ecossistema React?**  
Permite disponibilizar estados compartilhados (como tema escuro ou login) diretamente para componentes profundos sem repassar props manuais.

**Como a atenção do Transformer processa o contexto?**  
Calculando o produto escalar ponderado entre todos os tokens da sequência para ponderar a relevância de cada termo em relação aos outros.

## Termos relacionados
- [Context Window](/pt/dictionary/context-window/)
- [Working Memory](/pt/dictionary/working-memory/)
- [Attention Mechanism](/pt/dictionary/attention-mechanism/)

## Ferramentas relacionadas
- [Goose](/pt/discover/goose/)
- [Chrome Devtools MCP](/pt/discover/chrome-devtools-mcp/)
- [Openclaude](/pt/discover/openclaude/)
- [Code Review Graph](/pt/discover/code-review-graph/)
- [Fastmcp](/pt/discover/fastmcp/)
- [Context Mode](/pt/discover/context-mode/)
- [Unity MCP](/pt/discover/unity-mcp/)
- [DesktopCommanderMCP](/pt/discover/desktopcommandermcp/)

---
Fonte: Dicionário Técnico TreScout · https://trescout.com/pt/dictionary/context/
