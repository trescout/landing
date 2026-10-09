# O que é Guardrails?

*Glossário · AI · Última atualização: 9 de outubro de 2026*

São limites de segurança e controle que impedem que modelos de inteligência artificial produzam saídas nocivas, enganosas ou que violem regras estabelecidas.

## Definição

Guardrails são mecanismos de controle programáticos que garantem que os aplicativos de inteligência artificial cumpram regras éticas, operacionais e jurídicas específicas durante a interação com o usuário. Eles monitoram em tempo real os prompts recebidos pelo modelo e as respostas geradas. Detectam riscos como conteúdo nocivo, vazamento de dados sensíveis, desvio de tópico ou alucinações, bloqueando a resposta ou ajustando-a para uma estrutura segura.

***Analogia:** São semelhantes às barreiras de aço na margem de uma curva. Não importa quão rápido seu veículo esteja andando, elas evitam fisicamente que ele saia da pista e caia no precipício.*

## Como funciona

Os desenvolvedores definem regras específicas, listas negras e controles semânticos. A solicitação do usuário passa por um filtro de entrada antes de chegar ao modelo; em seguida, a resposta gerada pelo modelo também é escaneada por um filtro de saída antes de ser entregue ao usuário final. Quando os limites de segurança definidos são ultrapassados, o sistema censa a resposta, retorna uma mensagem de erro padrão predeterminada ou obriga o modelo a gerar novamente uma resposta segura.

## Onde é usado

São amplamente utilizados em chatbots de atendimento ao cliente, setores regulamentados como finanças e saúde, motores de busca corporativos e agentes de inteligência artificial autônomos.

## Costuma ser confundido com

Podem ser confunde com a Aprendizagem por Reforço com Feedback Humano (RLHF) realizada durante o treinamento básico do modelo. Enquanto o treinamento básico define o caráter interno do modelo, os guardrails são um invólucro de segurança independente conectado externamente ao modelo.

## Perguntas frequentes

**O sistema de guardrails desacelera significativamente os tempos de resposta?**

As camadas de controle adicionais adicionam uma latência muito pequena ao sistema, mas, graças a regras leves e modelos menores otimizados, esse tempo dificilmente é percebido pelo usuário.

**O uso de guardrails bloqueia completamente os ataques de prompt injection?**

Não é uma solução mágica por si só, mas reduz drasticamente o nível de risco ao capturar a grande maioria das vulnerabilidades conhecidas e tentativas de desvio de comando.

## Termos relacionados

- [Prompt Injection](https://trescout.com/pt/dictionary/prompt-injection/)
- [Red Teaming](https://trescout.com/pt/dictionary/red-teaming/)
- [Hallucination](https://trescout.com/pt/dictionary/hallucination/)
- [Agent Governance Toolkit](https://trescout.com/pt/dictionary/agent-governance-toolkit/)
- [RLHF](https://trescout.com/pt/dictionary/rlhf/)

## Ferramentas relacionadas

- [Litellm](https://trescout.com/pt/discover/litellm/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/guardrails/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/guardrails/
