# O que é Task Runner?

*Glossário · Dev · Última atualização: 22 de setembro de 2026*

O executor de tarefas é uma ferramenta que executa tarefas repetitivas sequencialmente.

## Definição e origem da palavra

Tarefas como teste, compactação e implantação estão vinculadas a um único comando. A lista segue, o processo acelera, os erros diminuem.

***Analogia:** É como um robô que faz as tarefas da cozinha em ordem; A lista é dada, o processo funciona.*

## Como conhecer e usar no dia a dia?

**Web:** Compilação e compactação.
**CI:** Etapas de linha.
**Lançamento:** Implantação com um único comando.

## Profundidade Técnica e Arquitetura

Scripts NPM:

```
"scripts": {
  "test": "pytest",
  "build": "vite build"
}
```

A execução está no formato npm run test. Makefile e Just são alternativas. Regra: Três tarefas manuais são gravadas no script.

## Coisas frequentemente misturadas

É considerado um terminal. O terminal executa, o runner gerencia. Um é o palco, o outro é o diretor.

## Use em diferentes disciplinas

**Robô:** Tarefas de cozinha sequenciais.
**Máquina de lavar:** Lavagem programada.
**Piloto automático:** Rastreamento de rota.

## Perguntas Frequentes

**Em quais trabalhos é utilizado?**

Em testes, compilação e implantação. Qualquer trabalho recorrente é um candidato.

**Qual escolher?**

O ecossistema determina: npm é comum no lado JS, Make é comum no sistema.

**Qual é a diferença do IC?**

O Runner é executado localmente, o CI é executado na nuvem. Ambos são usados ​​juntos.

**Quando deve ser escrito?**

Na terceira repetição. A primeira é feita à mão, a segunda por anotação, a terceira por roteiro.

## Termos relacionados

- [CLI](https://trescout.com/pt/dictionary/cli/)
- [Continuous Integration](https://trescout.com/pt/dictionary/continuous-integration/)
- [Script](https://trescout.com/pt/dictionary/script/)

## Ferramentas relacionadas

- [Mise](https://trescout.com/pt/discover/mise/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/task-runner/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/task-runner/
