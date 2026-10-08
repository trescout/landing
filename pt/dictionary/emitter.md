# O que é Emitter?

*Glossário · Dev · Última atualização: 19 de setembro de 2026*

Emitter (emissor) é um termo crítico na engenharia de software que aparece em duas áreas fundamentais: o mecanismo que anuncia mudanças de estado aos ouvintes em arquiteturas orientadas a eventos (Event Emitter) e o módulo de geração de código que converte o código analisado na linguagem de máquina de destino ou bytecode em tecnologia de compiladores (Code Emitter).

## Origem conceitual: Da física à arquitetura de software

A palavra "emitter" deriva do verbo latino emittere, que significa "lançar para fora, soltar". Na eletrônica, o termo é usado para cátodos que emitem elétrons ou, nas telecomunicações, para transmissores de rádio que emitem sinais. O mundo do software tomou este termo emprestado com o sentido de "uma fonte que transfere para o mundo exterior um estado que ocorre nela ou uma saída que ela produz".

No software, o "emitter" não é uma estrutura única, mas representa duas disciplinas enormes dependendo do contexto em que é usado: fluxos de eventos e design de compiladores.

***Analogia:** Event Emitter: É o botão de alarme de incêndio. Quando o botão é pressionado (emit), ele não sabe quantas pessoas estão no prédio ou quais sirenes estão tocando; ele apenas emite um sinal e todos os sistemas de alarme conectados (listeners) são acionados.

Code Emitter: É o engenheiro-chefe que recebe os planos técnicos detalhados (AST) desenhados por um arquiteto e os converte em instruções de moldagem e armação de ferro que os mestres de obra podem aplicar diretamente.*

## 1. Arquitetura orientada a eventos e Event Emitter

Na programação orientada a eventos, o Emitter é o coração dos padrões de projeto Observer (Observador) e Publish-Subscribe (Publicar-Assinar). Ele permite que os componentes do sistema se comuniquem por meio de eventos (acoplamento fraco), em vez de se conhecerem diretamente (acoplamento forte).

A estrutura de I/O reativa e assíncrona do Node.js baseia-se na classe EventEmitter dentro do módulo events:

**emit(event, [...args]):** Aciona o evento com o nome especificado e notifica todos os ouvintes registrados.

**on(evento, ouvinte):** Registra a função de retorno de chamada (callback) que será executada quando o evento especificado ocorrer.

**once(evento, ouvinte):** Captura o evento apenas uma vez, na primeira ocorrência, e remove o registro automaticamente em seguida.

**Detalhe Técnico Importante:** Ao contrário da crença popular, o EventEmitter do Node.js executa ouvintes de eventos de forma síncrona por padrão. Se um ouvinte bloquear, os ouvintes subsequentes aguardarão. Para execução assíncrona, utiliza-se setImmediate() ou process.nextTick().

O erro mais comum na arquitetura Event Emitter é não remover os ouvintes (removeListener ou off) de objetos cujo ciclo de vida terminou. Isso impede que os objetos sejam limpos pelo Garbage Collector e causa o aviso MaxListenersExceededWarning no Node.js.

## 2. Code Emitter (Gerador de Código) na arquitetura de compiladores

A fase final e mais crucial de um compilador ou transpiler é a camada Emitter (Gerador de Código). A cadeia de compilação funciona na seguinte ordem: Código-fonte → Lexer (Tokens) → Parser (Árvore de Sintaxe - AST) → Análise Semântica → Otimização → Emitter → Código de Destino

O Emitter percorre a Árvore de Sintaxe Abstrata (AST) otimizada ou a Representação Intermediária (IR) de ponta a ponta (geralmente com o Padrão Visitor). Ele converte cada nó em instruções que a plataforma de destino entende: essa saída pode ser linguagem de máquina bruta (Assembly x86/ARM), bytecode de máquina virtual (JVM, V8 Bytecode) ou outra linguagem de alto nível (como a compilação de TypeScript para JavaScript).

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

- [Parser](https://trescout.com/pt/dictionary/parser/)
- [Compiler](https://trescout.com/pt/dictionary/compiler/)
- [Runtime](https://trescout.com/pt/dictionary/runtime/)
- [Assembly](https://trescout.com/pt/dictionary/assembly/)
- [API](https://trescout.com/pt/dictionary/api/)
- [Bundler](https://trescout.com/pt/dictionary/bundler/)

## Ferramentas relacionadas

- [YAML Cpp](https://trescout.com/pt/discover/yaml-cpp/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/emitter/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/emitter/
