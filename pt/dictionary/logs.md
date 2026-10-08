# O que é Logs?

*Glossário · Dev · Última atualização: 22 de setembro de 2026*

Log, que significa registro em português, são linhas de eventos do sistema com carimbo de data/hora.

## Definição e origem da palavra

"Log" significa diário de bordo: o capitão escreve o que aconteceu no caderno. O software também escreve linha por linha o que está fazendo em segundo plano. No momento de um erro, o caderno é aberto e a hora é verificada. É a primeira fonte de saúde do sistema.

***Analogia:** É como a caixa-preta de um avião; mantém um registro durante todo o voo e, em caso de problema, retrocede-se para analisar.*

## Como conhecer e usar no dia a dia?

**Apresentador:** Depuração.
**Aplicação:** Relatório de falha.
**Segurança:** Rastreamento de eventos.

## Profundidade Técnica e Arquitetura

Regras de um bom registro:

**Carimbo de data/hora:** Hora em cada linha.
**Nível:** Distinção entre INFO e ERROR.
**Rotação:** Arquivamento quando o arquivo cresce.
**Proibição de PII:** Dados pessoais não entram no registro.

Linha de exemplo:

```
2026-09-22T10:00:01 sipariş=4521 sonuc=ok sure_ms=38
```

A pesquisa torna-se mais fácil neste formato. Texto desorganizado não pode ser pesquisado, registros organizados sim.

## Coisas frequentemente misturadas

Confundido com trace. Log é o registro do evento, trace é o caminho do evento. Um é uma foto, o outro é um filme.

## Use em diferentes disciplinas

**Caixa-preta:** Dados de voo.
**Diário:** Notas em ordem cronológica.
**Recibo de caixa:** Registro de transações.

## Perguntas Frequentes

**Por que o log é necessário?**

A causa da falha está no registro. Um sistema sem registros voa às cegas.

**Onde é gravado?**

Em um arquivo ou sistema centralizado. Em produção, recomenda-se a coleta centralizada.

**Por quanto tempo é armazenado?**

Depende da política. A depuração requer semanas, a auditoria requer anos.

**Dados pessoais são registrados?**

Não. Senhas e identificações não entram no registro, são mascaradas.

## Termos relacionados

- [Observability](https://trescout.com/pt/dictionary/observability/)
- [QA](https://trescout.com/pt/dictionary/qa/)
- [Traces](https://trescout.com/pt/dictionary/traces/)

## Ferramentas relacionadas

- [Grafana](https://trescout.com/pt/discover/grafana/)
- [Modly](https://trescout.com/pt/discover/modly/)

Esta explicação foi escrita em linguagem simples para a TreScout e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/logs/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/logs/
