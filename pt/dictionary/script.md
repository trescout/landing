# O que é Script?

*Glossário · Dev · Última atualização: 22 de setembro de 2026*

Um script (com equivalente em turco betik) é uma breve sequência de comandos cuja única função é executar tarefas automaticamente.

## Definição e origem da palavra

Em vez de um grande projeto, resolve-se uma única tarefa: renomear arquivos, limpar dados, iniciar programas. Os comandos são escritos em um arquivo de texto e executados pelo interpretador. Não é necessária compilação, é o formato escreve-e-executa.

***Analogia:** É como dar uma lista de tarefas passo a passo em vez de explicar longamente.*

## Como conhecer e usar no dia a dia?

**Sistema:** Backup e limpeza.
**Dados:** Operações de arquivos em lote.
**Navegador:** Extensões de automação de páginas.

## Profundidade Técnica e Arquitetura

Fluxo de trabalho:

**Shebang:** A primeira linha do arquivo indica o interpretador.
**Permissão:** A flag de execução é fornecida.
**Parâmetro:** O arquivo e a opção são obtidos externamente.

Exemplo:

```
#!/bin/bash
for dosya in *.log; do
  gzip "$dosya"
done
```

Regra: O comando destrutivo é testado primeiro com uma execução seca, e um backup é feito.

## Coisas frequentemente misturadas

Acha-se que é uma aplicação. A aplicação é grande e precisa ser compilada, enquanto o script é leve e instantâneo. Ambos são ferramentas de escalas diferentes.

## Use em diferentes disciplinas

**Lista:** Descrição de trabalho passo a passo.
**Cartão de receita:** Instrução curta e medida.
**Autômato:** Mecanismo que funciona ao inserir uma ficha.

## Perguntas Frequentes

**Alguém pode escrever?**

Sim. Com a lógica básica, escrevem-se scripts simples; tarefas complexas vêm com a prática.

**Qual idioma deve ser escolhido?**

Bash é um começo prático para tarefas de sistema, e Python para tarefas gerais.

**Como é executado?**

Pelo nome do interpretador ou diretamente com permissão de execução. No Windows, usa-se WSL ou PowerShell.

**É seguro?**

Scripts de fontes confiáveis, sim. Um script obtido da internet não deve ser executado sem ser lido.

## Termos relacionados

- [CLI](https://trescout.com/pt/dictionary/cli/)
- [Tools](https://trescout.com/pt/dictionary/tools/)
- [Shell](https://trescout.com/pt/dictionary/shell/)

## Ferramentas relacionadas

- [NVM](https://trescout.com/pt/discover/nvm/)
- [Omarchy](https://trescout.com/pt/discover/omarchy/)
- [Cmux](https://trescout.com/pt/discover/cmux/)
- [Meshery](https://trescout.com/pt/discover/meshery/)
- [Tradingview MCP](https://trescout.com/pt/discover/tradingview-mcp/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/script/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/script/
