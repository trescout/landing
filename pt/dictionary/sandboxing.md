# O que é Sandboxing?

Técnica de executar software ou código suspeito em um ambiente isolado para evitar danos ao sistema principal e ao ambiente.

## Definição
O sandboxing é a prática de executar pedaços de código não confiáveis ou em fase de teste em uma área controlada, isolando-os dos recursos do sistema. Esse mecanismo limita o acesso direto do aplicativo ao sistema de arquivos, rede local ou ao núcleo do sistema operacional. É uma camada de segurança indispensável para impedir a disseminação de vulnerabilidades de segurança no sistema e neutralizar o impacto de malwares.

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
- [Sandbox](/pt/dictionary/sandbox/)
- [Runtime](/pt/dictionary/runtime/)
- [Virtual Machines](/pt/dictionary/virtual-machines/)
- [Security Scanner](/pt/dictionary/security-scanner/)

## Ferramentas relacionadas
- [Agent Governance Toolkit](/pt/discover/agent-governance-toolkit/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/sandboxing/
