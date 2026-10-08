# O que é CI/CD?

*Glossário · Dev · Última atualização: 22 de setembro de 2026*

> Continuous Integration / Continuous Deployment

CI/CD (Integração Contínua/Implantação Contínua) é o teste e liberação automática do código.

## Definição e origem da palavra

É uma linha automática estabelecida para garantir que o código escrito chegue ao usuário sem erros. A CI monta e testa constantemente o código e o transfere para o live CD. A era das publicações manuais chega ao fim.

***Analogia:** É como uma fita que garante que a comida é preparada na cozinha do restaurante, passa no teste de sabor e é servida ao cliente.*

## Como conhecer e usar no dia a dia?

**Equipe:** Teste após cada commit.
**Móvel:** Liberação automática para armazenar.
**Web:** Solte quando combinado.

## Profundidade Técnica e Arquitetura

Estágios de linha:

**Fiapos:** Controle de estilo.
**Teste:** Unidade e ponta a ponta.
**Compilação:** Produção de pacotes.
**Lançamento:** Abertura gradual.

Etapa de exemplo:

```
steps:
  - run: npm ci
  - run: npm test
```

Uma porta de aprovação manual é colocada em publicações críticas. Diferença com entrega: a entrega prepara, a implantação imprime. O primeiro espera, o segundo vai.

## Coisas frequentemente misturadas

Pensa-se que seja um teste manual. Porém, a linha é totalmente automática: vem o código, o teste roda, sai o resultado. A pessoa apenas espera na porta.

## Use em diferentes disciplinas

**Fita de cozinha:** Preparação, degustação e serviço.
**Linha de montagem:** Peça, inspeção e pacote.
**Faixa de bagagem:** Registro, navegação e upload.

## Perguntas Frequentes

**Por que isso é tão importante?**

Ele traduz o código defeituoso ao vivo e aumenta a velocidade. A transmissão frequente é feita com segurança.

**Deveria ser sempre automático?**

Geralmente sim, a porta manual é adicionada na versão crítica.

**Qual é a diferença com Entrega?**

A entrega prepara e espera, a implantação vai e vem. O primeiro é aprovado, o segundo é totalmente automático.

**O que acontece se quebrar?**

A linha para e a transmissão é interrompida. É por isso que um plano de backup e uma recuperação rápida são essenciais.

## Termos relacionados

- [Continuous Integration](https://trescout.com/pt/dictionary/continuous-integration/)
- [Continuous Deployment](https://trescout.com/pt/dictionary/continuous-deployment/)
- [Deployment](https://trescout.com/pt/dictionary/deployment/)
- [QA](https://trescout.com/pt/dictionary/qa/)

## Ferramentas relacionadas

- [Free for Dev](https://trescout.com/pt/discover/free-for-dev/)
- [Strix](https://trescout.com/pt/discover/strix/)
- [Googletest](https://trescout.com/pt/discover/googletest/)
- [Trivy](https://trescout.com/pt/discover/trivy/)
- [Openship](https://trescout.com/pt/discover/openship/)
- [Ipatool](https://trescout.com/pt/discover/ipatool/)
- [Checkstyle](https://trescout.com/pt/discover/checkstyle/)
- [Flue](https://trescout.com/pt/discover/flue/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/ci-cd/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/ci-cd/
