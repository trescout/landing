# O que é Specification?

*Glossário · Dev · Última atualização: 22 de setembro de 2026*

Specification (abreviado como spec, ou especificação em português) é o documento técnico que descreve o que o produto fará e as suas regras.

## Definição e origem da palavra

É como o projeto arquitetônico de um edifício: o desenvolvedor consulta o documento antes de começar a codificar para entender o que deve construir. Reduz erros e esclarece expectativas. No mundo das APIs, o OpenAPI, e no hardware, as folhas de dados (datasheets) cumprem esse papel.

***Analogia:** É como a lista de ingredientes e as etapas de cozimento de uma receita; Se você não seguir a receita, a comida terá um sabor diferente.*

## Como conhecer e usar no dia a dia?

**Software:** Documento de características e regras.
**Licitação:** Arquivo de especificação técnica.
**Produto:** Critérios de design e aceitação.

## Profundidade Técnica e Arquitetura

Uma boa especificação inclui:

**Escopo:** O que está incluído e o que não está.
**Critério de aceitação:** Condições testáveis para ser considerado concluído.
**Limites:** Desempenho, segurança, compatibilidade.
**Versão:** Histórico de alterações.

Correspondência da especificação do endpoint da API:

```
paths:
  /siparis:
    post:
      summary: Yeni sipariş oluşturur
```

Regra: O que não pode ser medido não é uma especificação, é um desejo. Cada item deve ser escrito de forma testável.

## Coisas frequentemente misturadas

É semelhante ao requisito. O requisito diz o que é desejado, a especificação explica como deve ser feito. Um é o objetivo, o outro é o plano.

## Use em diferentes disciplinas

**Receita culinária:** Lista de materiais e etapas.
**Manual de montagem:** Esquema de peças e sequência.
**Licitação:** Especificação administrativa e técnica.

## Perguntas Frequentes

**As especificações podem mudar?**

Sim, mas cada alteração deve ser aprovada com o seu impacto no custo e no cronograma.

**Quem escreve o arquivo de especificação?**

O gerente de produto, o engenheiro ou o analista escreve. O importante é ter um único proprietário e disciplina de versão.

**Quanto detalhe é necessário?**

O suficiente para eliminar a ambiguidade. O excesso cansa quem escreve, a falta trava o desenvolvedor.

**Pode haver especificação dentro do Agile?**

Sim, versões leves. Histórias de usuário com critérios de aceitação e contratos de API funcionam como especificação.

## Termos relacionados

- [Spec-driven Development](https://trescout.com/pt/dictionary/spec-driven-development/)
- [Framework](https://trescout.com/pt/dictionary/framework/)
- [Tech Stack](https://trescout.com/pt/dictionary/tech-stack/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/specification/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/specification/
