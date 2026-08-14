# O que é Userspace?

Uma área segura onde os aplicativos do usuário são executados sem interferir no kernel do computador.

## Definição
Os sistemas operacionais são divididos em duas partes principais: kernel e espaço do usuário. O espaço do usuário é onde o navegador, o reprodutor de música ou os editores de código que você usa são executados. Um erro aqui não travará todo o computador, afetará apenas o aplicativo.

## Como funciona
Os aplicativos solicitam permissão do kernel para acessar os recursos subjacentes do sistema. Desta forma, o resto do sistema fica protegido.

## Onde é usado
É um conceito fundamental em desenvolvimento de software, segurança e arquitetura de sistemas.

## Costuma ser confundido com
É confundido com espaço do kernel; O kernel domina todo o sistema, enquanto o espaço do usuário é limitado.

## Perguntas frequentes
**Por que existe essa distinção?**
Para segurança e estabilidade; Para evitar que aplicativos corrompam o sistema.

**Onde o código que escrevi é executado?**
A maioria dos aplicativos e códigos são executados no espaço do usuário.


## Termos relacionados
- [Runtime](/pt/dictionary/runtime/)
- [Containers](/pt/dictionary/containers/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/userspace/
