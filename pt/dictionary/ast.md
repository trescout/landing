# O que é Abstract Syntax Tree?

*Desenvolvimento · Última atualização: 22 de outubro de 2026*

> Abstract Syntax Tree

É um modelo de dados que representa a estrutura gramatical do código-fonte na forma de uma árvore hierárquica.

## Definição

A Abstract Syntax Tree (AST) é uma representação em formato de árvore, estruturada de acordo com regras de sintaxe, para que o código-fonte possa ser facilmente analisado por compiladores ou interpretadores. Cada variável, operação e função no seu código ocupa um nó nesta árvore. Ela simplifica a análise ao filtrar parênteses ou espaços desnecessários, preservando a integridade semântica do código.

***Analogia:** É semelhante a um diagrama de análise gramatical em que você divide os elementos de uma frase nos ramos de sujeito, predicado e objeto.*

## Como funciona

O analisador sintático (parser) de código lê o código em formato de texto e o converte em tokens por meio de análise léxica. Em seguida, organiza esses tokens em uma estrutura de árvore com nós superiores e inferiores de acordo com as regras de sintaxe. Compiladores, ferramentas de lint e mecanismos de análise de código realizam otimizações ou verificações de erros percorrendo esta árvore.

## Onde é usado

É frequentemente utilizado em compiladores de linguagens de programação, ferramentas de análise estática de código e de segurança. Ferramentas de formatação de código e sistemas de busca de código apoiados por inteligência artificial também utilizam esta estrutura.

## Costuma ser confundido com

Pode ser confuso com AST Parsing. O AST Parsing é a ação de construir esta árvore, enquanto a AST refere-se diretamente à estrutura de dados hierárquica resultante.

## Perguntas e respostas

**Por que a AST é mais vantajosa do que o código em texto simples?**

Enquanto é difícil rastrear relações estruturais em código de texto simples, a AST torna a hierarquia lógica do código clara e facilita a sua transformação programática.

**Quais ferramentas usam AST?**

Babel, o ESLint, o compilador TypeScript e os estágios de compilação das linguagens de programação modernas utilizam a infraestrutura AST.

## Termos relacionados

- [AST Parsing](https://trescout.com/pt/dictionary/ast-parsing/)
- [Parser](https://trescout.com/pt/dictionary/parser/)
- [Compiler](https://trescout.com/pt/dictionary/compiler/)
- [Clean Code](https://trescout.com/pt/dictionary/clean-code/)

Esta explicação foi escrita em linguagem simples para a TreScout com IA e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/ast/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/ast/
