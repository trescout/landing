# O que é Type Hints?

*Desenvolvimento · Última atualização: 23 de outubro de 2026*

São marcadores de código em linguagens de programação dinâmica que especificam o tipo de dado que as variáveis e os parâmetros de função devem ter.

## Definição

As dicas de tipo (type hints) são anotações adicionadas em linguagens de tipagem dinâmica, como o Python, para melhorar a legibilidade e a segurança do código. Elas não interrompem o fluxo do programa em tempo de execução, mas permitem que editores de código e ferramentas de análise detectem erros antecipadamente. Assim, evita-se erros inesperados de incompatibilidade de tipos em projetos grandes.

***Analogia:** É semelhante às etiquetas 'vidro frágil' ou 'apenas líquido' coladas em caixas sem alterar o seu conteúdo.*

## Como funciona

Ao definir uma função, o programador coloca dois pontos ao lado do parâmetro e especifica o tipo esperado (por exemplo, texto ou número inteiro). As ferramentas de análise de código estático examinam essas dicas. Se dados do tipo errado forem enviados a uma função, o sistema avisa o desenvolvedor antes de executar o código.

## Onde é usado

É amplamente utilizado em projetos Python de grande escala, bases de código corporativas e bibliotecas de código aberto colaborativas.

## Costuma ser confundido com

É frequentemente confundido com a tipagem estática. Na tipagem estática, a incompatibilidade de tipos leva a um erro de compilação; nas dicas de tipo, as marcações não são obrigatórias em tempo de execução, servindo apenas como orientação.

## Perguntas e respostas

**As dicas de tipo tornam o programa mais lento?**

Não, como essas dicas geralmente são ignoradas em tempo de execução, elas não afetam a velocidade de execução da aplicação.

**O uso de dicas de tipo é obrigatório?**

Não é obrigatório, mas é altamente recomendado nos padrões modernos de software, pois reduz erros no trabalho em equipe e na manutenção do código.

## Termos relacionados

- [Static Typing](https://trescout.com/pt/dictionary/static-typing/)
- [Type Safety](https://trescout.com/pt/dictionary/type-safety/)
- [Static Type Checking](https://trescout.com/pt/dictionary/static-type-checking/)
- [Clean Code](https://trescout.com/pt/dictionary/clean-code/)

## Ferramentas relacionadas

- [Fastapi](https://trescout.com/pt/discover/fastapi/)

Esta explicação foi escrita em linguagem simples para a TreScout com IA e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/type-hints/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/type-hints/
