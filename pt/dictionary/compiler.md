# O que é Compiler?

*Glossário · Dev · Última atualização: 22 de setembro de 2026*

Compiler (em turco, derleyici), é o programa que converte o código que você escreve para a linguagem de máquina que o computador pode executar.

## Definição e origem da palavra

"Compile" significa compilar, reunir. Os computadores entendem apenas sequências de 0 e 1. Já os programadores escrevem em linguagem legível. O compilador atua como tradutor entre esses dois mundos: analisa o código e, se não houver erros, converte-o em um arquivo executável.

***Analogia:** É como transformar uma receita escrita em inglês em instruções escritas para um chef que não fala inglês, numa língua que ele entende.*

## Como conhecer e usar no dia a dia?

**Instalação de aplicativos:** A versão compilada do programa que você baixou é executada.
**Mensagens de erro:** Quando você esquece um ponto e vírgula, o compilador avisa.
**Motores de jogos:** Uma saída de compilação separada para cada plataforma.

## Profundidade Técnica e Arquitetura

A compilação passa por quatro etapas:

**Análise léxica e sintática:** O código é dividido em partes, a estrutura da frase é extraída.
**Verificação semântica:** Procura-se por variáveis não definidas e incompatibilidade de tipos.
**Otimização:** Código equivalente, mas mais rápido, é gerado.
**Geração de código:** O código de máquina específico do processador é escrito.

A compilação na linguagem C funciona da seguinte forma:

```
gcc merhaba.c -o merhaba
./merhaba
```

A primeira linha traduz, a segunda executa. O interpretador, por sua vez, executa linha por linha e não produz um arquivo de saída separado.

## Use em diferentes disciplinas

**Interpretação:** A distinção entre tradução simultânea (intérprete) e tradução escrita (compilador).
**Impressão:** A conversão do rascunho em matriz de impressão.
**Culinária:** A transformação da receita em um prato pronto.

## Perguntas Frequentes

**O compilador de cada linguagem é diferente?**

Sim. Cada linguagem requer um compilador ou interpretador de acordo com suas próprias regras. Algumas linguagens usam ambos em conjunto.

**Qual é a diferença para o Interpretador (Interpreter)?**

O compilador traduz o código antecipadamente e gera um arquivo, e então o programa é executado rapidamente. O interpretador traduz linha por linha e executa, é flexível, mas geralmente lento.

**O que é JIT?**

A compilação just-in-time converte seções usadas com frequência em código de máquina durante a execução. É um meio-termo entre os dois, utilizado por Java e JavaScript.

**Quem compilou o primeiro compilador?**

É a questão do ovo e da galinha. Os primeiros compiladores foram escritos à mão em código de máquina, e os seguintes foram compilados pelo compilador anterior (bootstrapping).

## Termos relacionados

- [Rust](https://trescout.com/pt/dictionary/rust/)
- [Runtime](https://trescout.com/pt/dictionary/runtime/)
- [Compile-time](https://trescout.com/pt/dictionary/compile-time/)

## Ferramentas relacionadas

- [Llvm Project](https://trescout.com/pt/discover/llvm-project/)
- [SWC](https://trescout.com/pt/discover/swc/)
- [FMT](https://trescout.com/pt/discover/fmt/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/compiler/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/compiler/
