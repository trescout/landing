# O que é Durable Objects?

São pequenas unidades de software que rodam continuamente na Internet e podem armazenar dados sem perder seu estado.

## Definição
Normalmente, os programas na Internet são temporários, mas estas estruturas funcionam sem interrupção, mantendo os dados dentro de si. Eles não esquecem os dados mesmo quando a interação do usuário termina. Ideal para manter a consistência em sistemas distribuídos.

## Como funciona
Eles residem no servidor com uma identidade específica e processam cada solicitação recebida com o status atual em sua memória.

## Onde é usado
É usado em jogos em tempo real, aplicativos de bate-papo e serviços web cujo estado deve ser mantido.

## Costuma ser confundido com
Não deve ser confundido com funções de servidor temporário (sem servidor); porque eles sempre começam do zero.

## Perguntas frequentes
**Onde os dados são armazenados?**
Ele é armazenado no próprio volume, ou seja, diretamente como parte do ambiente operacional.


## Termos relacionados
- [Runtime](/pt/dictionary/runtime/)
- [State Management](/pt/dictionary/state-management/)
- [Distributed](/pt/dictionary/distributed/)

## Ferramentas relacionadas
- [Celld](/pt/discover/celld/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/durable-objects/
