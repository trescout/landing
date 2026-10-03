# O que é Emitter?

Emitter (emissor) é um termo crítico na engenharia de software que aparece em duas áreas fundamentais: o mecanismo que anuncia mudanças de estado aos ouvintes em arquiteturas orientadas a eventos (Event Emitter) e o módulo de geração de código que converte o código analisado na linguagem de máquina de destino ou bytecode em tecnologia de compiladores (Code Emitter).

## Origem conceitual: Da física à arquitetura de software
A palavra "emitter" deriva do verbo latino emittere, que significa "lançar para fora, soltar". Na eletrônica, o termo é usado para cátodos que emitem elétrons ou, nas telecomunicações, para transmissores de rádio que emitem sinais. O mundo do software tomou este termo emprestado com o sentido de "uma fonte que transfere para o mundo exterior um estado que ocorre nela ou uma saída que ela produz".

## 1. Arquitetura orientada a eventos e Event Emitter
Na programação orientada a eventos, o Emitter é o coração dos padrões de projeto Observer (Observador) e Publish-Subscribe (Publicar-Assinar). Ele permite que os componentes do sistema se comuniquem por meio de eventos (acoplamento fraco), em vez de se conhecerem diretamente (acoplamento forte).

## 2. Code Emitter (Gerador de Código) na arquitetura de compiladores
A fase final e mais crucial de um compilador ou transpiler é a camada Emitter (Gerador de Código). A cadeia de compilação funciona na seguinte ordem: Código-fonte → Lexer (Tokens) → Parser (Árvore de Sintaxe - AST) → Análise Semântica → Otimização → Emitter → Código de Destino

## Perguntas frequentes
**O que significa Emitter e qual é a sua tradução para o português?**
Emitter significa "emissor" ou "transmissor" em inglês. No software, é geralmente usado como "emissor de eventos" (event emitter) ou em compiladores como "gerador de código / emissor" (code emitter).

**Qual é a maior vantagem de usar um Event Emitter?**
Reduz o acoplamento (coupling) entre componentes a zero. Um módulo dispara um evento; ele não se preocupa com quem, quando ou como o evento é processado. Isso aumenta a modularidade e a testabilidade.

**Qual função o Emitter assume nos compiladores?**
É o componente final que recebe a estrutura de árvore (AST) otimizada e analisada do código-fonte para produzir a saída de destino (Assembly, código de máquina, bytecode ou código-fonte convertido).

**Qual é a diferença entre um RxJS Observable e um Event Emitter?**
O Event Emitter geralmente faz multicast e é usado para notificações de eventos instantâneos. Já o RxJS Observable oferece o poder de transformar fluxos de dados ricos ao longo do tempo (streams) com operadores funcionais, como filtragem, mapeamento e atraso.


## Termos relacionados
- [Parser](/pt/dictionary/parser/)
- [Compiler](/pt/dictionary/compiler/)
- [Runtime](/pt/dictionary/runtime/)
- [Assembly](/pt/dictionary/assembly/)
- [API](/pt/dictionary/api/)
- [Bundler](/pt/dictionary/bundler/)

## Ferramentas relacionadas
- [YAML Cpp](/pt/discover/yaml-cpp/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/emitter/
