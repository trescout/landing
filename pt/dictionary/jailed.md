# O que é Jailed?

*Glossário · Dev · Última atualização: 29 de setembro de 2026*

É a condição em que um programa é executado em uma área isolada e restrita, impedindo-o de acessar o restante do sistema operacional.

## Definição

Jailed refere-se ao estado de segurança em que um processo de software só pode acessar o diretório de arquivos, a memória e os recursos de rede que lhe foram permitidos. Essa limitação, aplicada ao nível do sistema operacional, impede que o programa cause danos ao sistema principal ou a outros usuários. Cria uma linha de defesa crítica ao testar códigos não confiáveis ou isolar riscos de malware.

***Analogia:** É semelhante a permitir que um convidado em casa fique apenas no quarto de hóspedes e trancar todas as outras portas, em vez de permitir que ele circule por todos os cômodos.*

## Como funciona

O kernel do sistema operacional limita o diretório raiz e as chamadas de sistema do processo com restrições especiais. Mesmo que o processo pense que está no sistema principal, na verdade ele só consegue ver um subdiretório virtual. Se um programa nessa área isolada travar ou for atacado, o dano permanece apenas naquela área restrita.

## Onde é usado

É amplamente utilizado ao separar processos de usuários em servidores web, em aplicações que executam plugins e em plataformas de execução de código online.

## Costuma ser confundido com

É muito próximo do conceito de Sandbox; no entanto, jail é geralmente um termo mais tradicional focado no isolamento do sistema de arquivos em sistemas Unix/Linux (como chroot ou FreeBSD jail).

## Perguntas frequentes

**Um programa em estado jailed pode acessar o sistema principal?**

Em condições normais, não. No entanto, se houver uma vulnerabilidade ao nível do kernel (vulnerabilidade de jailbreak), esses limites podem ser ultrapassados.

**As tecnologias de contêiner também são um tipo de jail?**

As estruturas modernas de contêiner (como o Docker) são uma evolução muito mais avançada e rica em recursos da lógica tradicional de jail.

## Termos relacionados

- [Sandbox](https://trescout.com/pt/dictionary/sandbox/)
- [Containers](https://trescout.com/pt/dictionary/containers/)
- [Runtime](https://trescout.com/pt/dictionary/runtime/)
- [Security Scanner](https://trescout.com/pt/dictionary/security-scanner/)

## Ferramentas relacionadas

- [Madeira](https://trescout.com/pt/discover/madeira/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/jailed/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/jailed/
