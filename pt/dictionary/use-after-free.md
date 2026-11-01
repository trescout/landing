# O que é Use-After-Free?

*Desenvolvimento · Última atualização: 1 de novembro de 2026*

> UAF

É uma vulnerabilidade de segurança que surge quando o programa tenta aceder a uma área de memória após esta ter sido libertada.

## Definição

O use-after-free ocorre quando, durante a gestão de memória, uma estrutura de dados é eliminada ou libertada, mas o ponteiro continua a apontar para esse endereço. A leitura ou escrita do programa neste endereço inválido leva a falhas inesperadas ou à execução de código malicioso. Linguagens como o Rust, que verificam a segurança de memória em tempo de compilação, foram especialmente concebidas para prevenir este tipo de erros.

***Analogia:** É semelhante a devolver a chave de um quarto de hotel, entrar novamente no quarto e tentar mexer nos pertences do novo cliente que lá ficou.*

## Como funciona

O programador ou gestor de memória liberta um bloco de memória, mas não redefine a variável que aponta para esse bloco. Quando o programa tenta efetuar uma operação nos passos seguintes utilizando este ponteiro pendente, ocorre um erro de memória.

## Onde é usado

É frequentemente observado em linguagens de programação de sistemas que requerem gestão manual de memória, como C e C++, em vulnerabilidades detetadas e em análises de fragilidades.

## Costuma ser confundido com

Enquanto a vulnerabilidade de memory leak ocorre quando a memória não utilizada não é libertada, o use-after-free consiste na reutilização incorreta de memória já libertada.

## Perguntas e respostas

**Como prevenir esta vulnerabilidade de segurança?**

Pode ser evitada redefinindo os ponteiros imediatamente após a libertação da memória ou preferindo linguagens que garantam a segurança de memória.

**Esta falha permite a execução remota de código?**

Sim, os atacantes podem controlar o fluxo escrevendo os seus próprios dados na área de memória libertada.

## Termos relacionados

- [Vulnerability Scanning](https://trescout.com/pt/dictionary/vulnerability-scanning/)
- [Systems Programming](https://trescout.com/pt/dictionary/systems-programming/)
- [Rust](https://trescout.com/pt/dictionary/rust/)
- [Borrow Checker](https://trescout.com/pt/dictionary/borrow-checker/)
- [Remote Code Execution](https://trescout.com/pt/dictionary/rce/)

Esta explicação foi escrita em linguagem simples para a TreScout com IA e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/use-after-free/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/use-after-free/
