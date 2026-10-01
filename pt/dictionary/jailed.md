# O que é Jailed?

É a condição em que um programa é executado em uma área isolada e restrita, impedindo-o de acessar o restante do sistema operacional.

## Definição
Jailed refere-se ao estado de segurança em que um processo de software só pode acessar o diretório de arquivos, a memória e os recursos de rede que lhe foram permitidos. Essa limitação, aplicada ao nível do sistema operacional, impede que o programa cause danos ao sistema principal ou a outros usuários. Cria uma linha de defesa crítica ao testar códigos não confiáveis ou isolar riscos de malware.

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
- [Sandbox](/pt/dictionary/sandbox/)
- [Containers](/pt/dictionary/containers/)
- [Runtime](/pt/dictionary/runtime/)
- [Security Scanner](/pt/dictionary/security-scanner/)

## Ferramentas relacionadas
- [Madeira](/pt/discover/madeira/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/jailed/
