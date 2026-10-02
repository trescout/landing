# O que é LSP?

> Language Server Protocol

LSP (Language Server Protocol) é um protocolo aberto baseado em JSON-RPC que fornece comunicação padrão entre editores de código modernos e motores de análise de linguagens de programação.

## 1. Definição e o problema matemático que resolve: complexidade M × N
O Language Server Protocol (LSP) é um protocolo universal desenvolvido em 2016 sob a liderança da Microsoft (equipe do VS Code), Red Hat e Codenvy, que se tornou a pedra angular das ferramentas de desenvolvimento atuais.

## 2. Como o LSP funciona? Arquitetura de protocolo e JSON-RPC 2.0
LSP, editör (Client) ile dil analiz motoru (Server) arasında genellikle yerel standart girdi/çıktı (stdin/stdout) veya yerel soketler (IPC) üzerinden çalışan bir JSON-RPC 2.0 mesajlaşma protokolüdür.

## 3. Language Servers mais utilizados no ecossistema

## 4. LSP vs DAP vs LSIF / SCIP

## Perguntas frequentes
**O que significa LSP, qual é a sua definição?**
Significa Language Server Protocol (Protocolo de Servidor de Linguagem). É um protocolo aberto que padroniza a comunicação entre editores de código e os motores de sintaxe, verificação de tipos e preenchimento automático das linguagens de programação.

**Por que o LSP resolve o problema M × N?**
No modelo antigo, para M linguagens e N editores, era necessário escrever M × N plugins específicos para cada editor. Com o LSP, cada linguagem escreve um único servidor e cada editor escreve um único cliente, alcançando a fórmula de integração M + N.

**Como o LSP evita que o editor fique lento?**
A análise pesada da árvore de sintaxe abstrata (AST) da linguagem e as resoluções de tipos são executadas em processos de segundo plano isolados do processo principal do editor (via JSON-RPC); assim, a interface nunca trava.

**Qual é a diferença entre DAP e LSP?**
Enquanto o LSP analisa a escrita de código, o preenchimento de código e os erros de sintaxe, o DAP (Debug Adapter Protocol) permite que o código seja depurado passo a passo em tempo de execução, definindo pontos de interrupção (breakpoints).


## Termos relacionados
- [Agentic Coding Tool](/pt/dictionary/agentic-coding-tool/)
- [CLI](/pt/dictionary/cli/)
- [Keybindings](/pt/dictionary/keybindings/)
- [Code Snippets](/pt/dictionary/code-snippets/)
- [Runtime](/pt/dictionary/runtime/)

## Ferramentas relacionadas
- [Oh My Pi](/pt/discover/oh-my-pi/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/lsp/
