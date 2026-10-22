# O que é Borrow Checker?

*Desenvolvimento · Última atualização: 13 de outubro de 2026*

O mecanismo que impede que programas escritos na linguagem Rust cometem erros de memória e controla como os dados são utilizados.

## Definição

O borrow checker é uma das partes mais importantes do compilador Rust e garante o uso seguro da memória. Ele examina minuciosamente se vários locais estão interferindo nos mesmos dados ao mesmo tempo no código que você escreve e se a vida útil dos dados é suficiente. Quando encontra uma situação que viola a regra de segurança, ele não permite que o programa seja executado e o avisa.

***Analogia:** É um livro de controle rigoroso que garante que, em um laboratório sensível, apenas um pesquisador por vez possa pegar emprestado um equipamento especial e devolvê-lo quando o trabalho terminar.*

## Como funciona

Ele entra em ação em segundo plano quando você tenta compilar seu código. Ele analisa as regras de propriedade das variáveis e os tempos de empréstimo. Se detectar um compartilhamento de dados que viole as regras, ele interrompe a compilação e mostra onde o erro está localizado.

## Onde é usado

Na programação de sistemas, ele opera ativamente durante a fase de compilação para projetos Rust que desejam prevenir vazamentos de memória e falhas desde o início.

## Costuma ser confundido com

É diferente dos depuradores normais; ele não é executado enquanto o programa está rodando, mas sim enquanto o código está sendo escrito e compilado.

## Perguntas frequentes

**Por que ele é tão rigoroso?**

Ele toma precauções antecipadas para eliminar completamente as falhas de memória em tempo de execução.

**Isso faz com que o programa funcione devagar?**

Não, ele funciona apenas na fase de compilação e não cria custos extras em tempo de execução.

## Termos relacionados

- [Rust](https://trescout.com/pt/dictionary/rust/)
- [Compiler](https://trescout.com/pt/dictionary/compiler/)
- [Thread-safety](https://trescout.com/pt/dictionary/thread-safety/)
- [Systems Programming](https://trescout.com/pt/dictionary/systems-programming/)
- [Memory Management](https://trescout.com/pt/dictionary/memory-management/)

Esta explicação foi escrita em linguagem simples para a TreScout com IA e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/borrow-checker/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/borrow-checker/
