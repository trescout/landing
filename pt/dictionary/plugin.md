# O que é Plugin?

Um plugin é um componente de software modular independente que adiciona novos recursos, ferramentas e funcionalidades a um sistema sem alterar o código principal do software ou exigir recompilação.

## Origem conceitual e filosofia arquitetural
O termo "plugin" deriva do verbo inglês "plug in" (conectar, ligar à tomada). Assim como um pedal de efeitos conectado a um amplificador de áudio ou um hardware conectado a um computador via USB, ele se refere a módulos que podem ser conectados e desconectados do software conforme a necessidade.

## Arquitetura de Microkernel e princípio de funcionamento
Sistemas baseados em plugins são geralmente construídos com a Arquitetura de Microkernel (Microkernel Pattern). Nessa arquitetura, o sistema consiste em duas partes principais:

## Conceitos semelhantes: Plugin, Extension, Add-on e Mod
Embora esses termos sejam frequentemente usados de forma intercambiável no ecossistema de software, eles possuem nuances:

## Na era da inteligência artificial, complementos e o Protocolo de Contexto de Modelo (MCP)
Com a revolução da inteligência artificial, a arquitetura de plugins ganhou uma dimensão totalmente nova. Os grandes modelos de linguagem (LLMs) deixaram de ser repositórios de conhecimento fechados e, graças aos plugins e aos mecanismos de "Chamada de Ferramentas/Funções" (Tool/Function Calling), transformaram-se em agentes autônomos capazes de pesquisar na web, consultar bancos de dados e realizar ações por meio de APIs. O Model Context Protocol (MCP), desenvolvido pela Anthropic, constitui o exemplo mais recente da arquitetura moderna de plugins, permitindo que os LLMs se conectem a diferentes fontes de dados e ferramentas por meio de um protocolo de plugin padronizado.

## Perguntas frequentes
**O que significa plugin e qual é o seu equivalente em português?**
Vem da raiz inglesa "plug in" (conectar) e é chamado de "extensão" ou "plugin" em português. É uma peça de software independente que adiciona funcionalidades extras a um software principal.

**Os plugins causam queda de desempenho ou vulnerabilidades de segurança?**
Sim. Plugins mal otimizados podem consumir memória e CPU em excesso. Além disso, como plugins de terceiros podem abrir portas para ataques à cadeia de suprimentos (supply chain attacks), eles devem ser instalados apenas a partir de fontes confiáveis.

**Qual é a diferença entre Plugin e Extension?**
Enquanto o termo plugin refere-se mais a módulos que expandem as capacidades principais e o motor de dados de uma aplicação (por exemplo, filtros de áudio/vídeo), o termo extension é frequentemente preferido para complementos que melhoram a interface e a interação do usuário.

**O Model Context Protocol (MCP) é um plugin?**
O MCP é um protocolo de plugin aberto que padroniza a forma como os modelos de inteligência artificial se comunicam com ferramentas externas, bancos de dados e serviços.


## Termos relacionados
- [SDK](/pt/dictionary/sdk/)
- [API](/pt/dictionary/api/)
- [LSP](/pt/dictionary/lsp/)
- [MCP](/pt/dictionary/mcp/)
- [Bundler](/pt/dictionary/bundler/)
- [Runtime](/pt/dictionary/runtime/)

## Ferramentas relacionadas
- [Superpowers](/pt/discover/superpowers/)
- [ECC](/pt/discover/ecc/)
- [Andrej Karpathy Skills](/pt/discover/andrej-karpathy-skills/)
- [Anthropic Skills](/pt/discover/anthropic-skills/)
- [Understand Anything](/pt/discover/understand-anything/)
- [Claude Plugins Official](/pt/discover/claude-plugins-official/)
- [Codex Plugin Cc](/pt/discover/codex-plugin-cc/)
- [Knowledge Work Plugins](/pt/discover/knowledge-work-plugins/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/plugin/
