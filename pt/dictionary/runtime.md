# O que é Runtime?

*Glossário · Dev · Última atualização: 19 de setembro de 2026*

Tempo de execução refere-se ao período de tempo em que um programa é efetivamente executado no processador e na memória do computador após a fase de compilação, e à infraestrutura de software (Runtime Environment) que possibilita essa execução.

## 1. Dois significados básicos do conceito de tempo de execução

Na engenharia de software, a palavra “Tempo de execução” refere-se a dois conceitos diferentes dependendo do contexto:

1. Como Fase Temporal (Tempo de Execução): Após a fase em que o código é escrito (autoria) e passado pelo compilador (tempo de compilação), é o período que vai do momento em que o usuário final inicia o programa até o momento em que ele o fecha.
2. Como Camada de Execução (Ambiente de Execução): É o conjunto de bibliotecas, gerenciadores de memória, coletores de lixo e máquinas virtuais necessários para que o código escrito rode diretamente no sistema operacional e hardware. Por exemplo, Node.js, JVM (Java Virtual Machine) ou Go Runtime são ambientes de execução.

***Analogia:** O tempo de compilação é a verificação dos desenhos arquitetônicos e cálculos estáticos de um edifício pelo engenheiro à mesa; Se houver algum erro, ele será corrigido enquanto estiver no papel. O tempo de execução é o momento em que aquele edifício é construído e as pessoas nele se instalam; Eventos imprevistos como terremotos, inundações ou sobrecargas testam o edifício apenas nesta fase.*

## 2. Diferença entre tempo de compilação e tempo de execução

- Tempo de compilação: análise de sintaxe, verificações de tipo estático e conversão em código de máquina são realizadas antes da execução do código. Erros de erro de sintaxe e incompatibilidade de tipo são detectados nesta fase.
- Tempo de execução: a alocação de memória, as chamadas do sistema e o loop de eventos são gerenciados enquanto o usuário realmente executa o programa. Erros NullPointerException, Segmentation Fault (SIGSEGV) e Stack Overflow ocorrem durante esta fase.

## 3. Tempos de execução gerenciados versus não gerenciados

- Não gerenciado (C, C++, Rust, Zig): Converte diretamente em código de máquina nativo; Nenhuma máquina virtual pesada ou coletor de lixo em execução em segundo plano, apenas uma biblioteca C padrão leve (libc) é suficiente. Oferece velocidade máxima e atraso zero.
- Gerenciado (Java, C#, Go, JavaScript, Python): Executa na proteção de uma máquina virtual (JVM, CLR) ou tempo de execução. Inclui compiladores JIT, coletores de lixo automáticos e um agendador integrado que gerencia goroutines, como no Go.

## 4. Guerras modernas de tempo de execução de JavaScript: Node.js vs Deno vs Bun

- Node.js (2009): Padrão da indústria que combina o mecanismo Google V8 com o loop de eventos de E/S assíncrona libuv baseado em C++.
- Deno (2018): Plataforma moderna que combina o motor V8 com a infraestrutura Rust e Tokio, possui TypeScript integrado e sandbox de permissão segura.
- Bun (2023): É um ambiente de trabalho de nova geração que usa o mecanismo JavaScriptCore do Apple WebKit e é escrito inteiramente do zero na linguagem Zig, oferecendo E/S de arquivo/rede muitas vezes mais rápido que o Node.js.

## Perguntas frequentes

**O que significa tempo de execução, qual é o seu equivalente turco?**

Em turco, é chamado de "tempo de execução" ou "ambiente de execução". Ele descreve o período de tempo em que um programa deixa seu código-fonte e realmente é executado no hardware do computador e na camada de software que dá suporte a esse trabalho.

**O que é erro de tempo de execução?**

É um erro que passa com sucesso na fase de compilação, mas faz com que o aplicativo trave repentinamente devido a uma situação inesperada (divisão por zero, acesso a um objeto vazio, RAM insuficiente) durante a execução do programa.

**O Node.js é uma linguagem de programação ou um tempo de execução?**

Node.js não é uma linguagem; É um tempo de execução JavaScript de código aberto que permite que o código JavaScript seja executado em servidores e computadores sem a necessidade de um navegador.

**Como funciona o JIT (Just-In-Time) durante o tempo de execução da compilação?**

O compilador JIT detecta instantaneamente blocos de código usados ​​com frequência ("hot paths") enquanto o programa está em execução e converte esses blocos em código de máquina nativo em tempo de execução, aumentando o desempenho do aplicativo.

## Termos relacionados

- [Memory Management](https://trescout.com/pt/dictionary/memory-management/)
- [Assembly](https://trescout.com/pt/dictionary/assembly/)
- [Compilation](https://trescout.com/pt/dictionary/compilation/)
- [Bundler](https://trescout.com/pt/dictionary/bundler/)
- [Tech Stack](https://trescout.com/pt/dictionary/tech-stack/)

## Ferramentas relacionadas

- [Andrej Karpathy Skills](https://trescout.com/pt/discover/andrej-karpathy-skills/)
- [Node](https://trescout.com/pt/discover/node/)
- [Deno](https://trescout.com/pt/discover/deno/)
- [BUN](https://trescout.com/pt/discover/bun/)
- [Svelte](https://trescout.com/pt/discover/svelte/)
- [Wand-Enhancer](https://trescout.com/pt/discover/wand-enhancer/)
- [Univer](https://trescout.com/pt/discover/univer/)
- [Onnxruntime](https://trescout.com/pt/discover/onnxruntime/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/runtime/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/runtime/
