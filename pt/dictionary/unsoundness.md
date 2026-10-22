# O que é Unsoundness?

*Desenvolvimento · Última atualização: 13 de outubro de 2026*

A situação em que as regras que uma linguagem de programação afirma serem seguras são, na verdade, defeituosas ou incompletas.

## Definição

Unsoundness refere-se a situações em linguagens de programação onde regras como segurança de tipos ou proteção de memória são violadas ou contêm brechas. Se uma situação perigosa que normalmente deveria ser impossível de acordo com as regras da linguagem se torna possível devido a uma falha na lógica da própria linguagem, isso é considerado unsound. Geralmente resulta de erros lógicos profundos no compilador ou na biblioteca padrão da linguagem.

***Analogia:** É semelhante a um cofre de aço considerado impossível de arrombar poder ser aberto com um grampo de cabelo devido a um pequeno erro de design no buraco da fechadura.*

## Como funciona

Os desenvolvedores podem ignorar alguns cenários extremos ao projetar ou otimizar a linguagem. Se um mecanismo que permite escrever código seguro fizer suposições erradas em segundo plano, o programa pode falhar inesperadamente ou apresentar uma vulnerabilidade de segurança.

## Onde é usado

É um conceito crítico abordado em processos de desenvolvimento de compiladores, projetos de linguagens de baixo nível e auditorias de segurança.

## Costuma ser confundido com

Difere de simples erros de programação (bugs); significa que a promessa fundamental de confiabilidade da linguagem foi abalada em sua base.

## Perguntas e respostas

**Isso ocorre em todas as linguagens de software?**

Especialmente em linguagens como Rust, que possuem alegações rigorosas de segurança, essas brechas são levadas muito a sério e corrigidas imediatamente.

**Como isso é resolvido?**

O compilador da linguagem é atualizado para fechar essas lacunas lógicas nas regras.

## Termos relacionados

- [Rust](https://trescout.com/pt/dictionary/rust/)
- [Compiler](https://trescout.com/pt/dictionary/compiler/)
- [Borrow Checker](https://trescout.com/pt/dictionary/borrow-checker/)
- [Vulnerability Scanning](https://trescout.com/pt/dictionary/vulnerability-scanning/)
- [Static Type Checking](https://trescout.com/pt/dictionary/static-type-checking/)

Esta explicação foi escrita em linguagem simples para a TreScout com IA e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/unsoundness/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/unsoundness/
