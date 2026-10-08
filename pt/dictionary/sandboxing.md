# O que é Sandboxing?

*Glossário · Dev · Última atualização: 3 de outubro de 2026*

Técnica de executar software ou código suspeito em um ambiente isolado para evitar danos ao sistema principal e ao ambiente.

## Definição

O sandboxing é a prática de executar pedaços de código não confiáveis ou em fase de teste em uma área controlada, isolando-os dos recursos do sistema. Esse mecanismo limita o acesso direto do aplicativo ao sistema de arquivos, rede local ou ao núcleo do sistema operacional. É uma camada de segurança indispensável para impedir a disseminação de vulnerabilidades de segurança no sistema e neutralizar o impacto de malwares.

***Analogia:** É semelhante a realizar um experimento químico potencialmente perigoso dentro de uma capela de exaustão de vidro resistente a explosões, em vez de no meio da sala.*

## Como funciona

Uma barreira de proteção é estabelecida utilizando restrições ao nível do sistema operacional ou ferramentas de virtualização. Quando o código é executado, ele pode usar apenas a memória restrita e o espaço em disco que lhe foram permitidos. As chamadas de sistema são monitoradas constantemente; quando se detecta uma tentativa de operação não autorizada, o software é interrompido imediatamente.

## Onde é usado

É utilizado na execução de scripts de terceiros em navegadores web, em softwares de segurança que analisam arquivos suspeitos em anexos de e-mail e em ambientes de desenvolvimento onde agentes de inteligência artificial executam código.

## Costuma ser confundido com

Enquanto o termo sandbox descreve o próprio espaço isolado, o sandboxing refere-se ao processo de criar, gerenciar e restringir este ambiente seguro.

## Perguntas frequentes

**O sandboxing reduz significativamente o desempenho do sistema?**

Embora a monitoração de chamadas de sistema introduza uma pequena carga de processamento, nos sistemas operacionais modernos essa perda geralmente é tão pequena que passa despercebida.

**Por que o sandboxing é necessário em ferramentas de inteligência artificial?**

Como o código gerado e executado por modelos de inteligência artificial pode apresentar o risco de excluir arquivos críticos no sistema operacional, essas operações são realizadas em uma camada de isolamento seguro.

## Termos relacionados

- [Sandbox](https://trescout.com/pt/dictionary/sandbox/)
- [Runtime](https://trescout.com/pt/dictionary/runtime/)
- [Virtual Machines](https://trescout.com/pt/dictionary/virtual-machines/)
- [Security Scanner](https://trescout.com/pt/dictionary/security-scanner/)

## Ferramentas relacionadas

- [Agent Governance Toolkit](https://trescout.com/pt/discover/agent-governance-toolkit/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/sandboxing/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/sandboxing/
