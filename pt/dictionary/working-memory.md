# O que é Working Memory?

*Inteligência artificial · Última atualização: 22 de setembro de 2026*

A memória de trabalho (working memory) é a informação temporária que o modelo retém para a tarefa em questão.

## Definição e origem da palavra

Quando a tarefa termina ou o contexto muda, o conteúdo é limpo. O recipiente da janela de contexto é a informação ativa dentro da memória de trabalho. O histórico do chat e os resultados intermediários ficam aqui.

***Analogia:** É como notas temporárias feitas ao lado ao resolver matemática; quando o problema termina, não têm mais importância.*

## Como conhecer e usar no dia a dia?

**Chat:** Lembrar de mensagens anteriores.
**Raciocínio:** Manter passos intermediários.
**Veículo:** Manter resultados de chamadas em espera.

## Profundidade Técnica e Arquitetura

Cálculo de orçamento:

```
bağlam: 128K token
geçmiş: 100K → kalan 28K
```

Quando transborda, o modelo diz adeus ao antigo: poda, resumo ou deslocamento são aplicados. Diferença do RAG: o RAG traz informações de fora, a memória de trabalho mantém a informação atual. Ambos trabalham juntos.

## Coisas frequentemente misturadas

Pensa-se que é memória de longo prazo. Esse é o perfil permanente, este é o balcão temporário. Quando a sessão fecha, este espaço é esvaziado.

## Use em diferentes disciplinas

**Nota lateral:** Rascunho descartado quando o problema termina.
**Ficar em pé:** Ferramenta recolhida quando o trabalho termina.
**RAM:** Área apagada quando a energia é cortada.

## Perguntas Frequentes

**O que acontece se encher?**

Informações antigas são esquecidas, o contexto se perde. É gerenciado com resumo e poda.

**Como aumentar?**

Escolhe-se um modelo com janela maior ou adiciona-se conhecimento externo com RAG.

**Qual é a diferença do RAG?**

O RAG traz informações de fora, a memória mantém o momento atual. Ambos são complementares.

**Esquece?**

Sim. É uma área temporária, não se espera persistência. Informações persistentes são gravadas externamente.

## Termos relacionados

- [Memory](https://trescout.com/pt/dictionary/memory/)
- [Context Window](https://trescout.com/pt/dictionary/context-window/)
- [Long-term Memory](https://trescout.com/pt/dictionary/long-term-memory/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/working-memory/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/working-memory/
