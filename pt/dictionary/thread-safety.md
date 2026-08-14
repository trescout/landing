# O que é Thread-safety?

Um recurso de segurança de um programa que evita que os dados sejam corrompidos ao executar várias operações ao mesmo tempo.

## Definição
Os computadores fazem muitas coisas ao mesmo tempo. Se dois processos diferentes tentarem alterar os mesmos dados ao mesmo tempo, ocorrerá o caos. Este recurso permite que os processos esperem uns pelos outros ou sejam executados sequencialmente.

## Como funciona
As regras de acesso a dados são determinadas enquanto o programa está sendo escrito. Embora um processo use os dados, os outros parecem ter um status 'bloqueado'.

## Onde é usado
É obrigatório para aplicações bancárias, servidores web e todos os softwares multitarefa.

## Costuma ser confundido com
Não se trata apenas de segurança (hacking), trata-se de consistência de dados.

## Perguntas frequentes
**O que acontece se não for thread-safe?**
Seus dados ficam confusos, aplicativos travam ou ocorrem erros de cálculo.


## Termos relacionados
- [Concurrency](/pt/dictionary/concurrency/)
- [System Programming Language](/pt/dictionary/system-programming-language/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/thread-safety/
