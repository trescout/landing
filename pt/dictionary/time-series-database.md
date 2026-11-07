# O que é Time Series Database?

*Dados e infraestrutura · Última atualização: 7 de novembro de 2026*

Banco de dados especializado que armazena mudanças ao longo do tempo em ordem cronológica.

## Definição

Um Banco de Dados de Séries Temporais é um tipo de banco de dados de alta velocidade onde os dados são registrados com um carimbo de data/hora e as mudanças em segundos são analisadas. Diferente dos bancos de dados clássicos, em vez de atualizar os dados, ele adiciona continuamente um novo registro de tempo na parte inferior. É otimizado para monitorar o status instantâneo de milhões de sensores ou servidores.

***Analogia:** É como um atleta mantendo um caderno com cronômetro, onde ele anota sua frequência cardíaca e velocidade a cada segundo, um abaixo do outro, durante todo o treino.*

## Como funciona

Os sistemas enviam relatórios de status em intervalos específicos e este banco de dados grava esses relatórios em seu disco em ordem cronológica. Ao realizar consultas, ele permite que você visualize tendências históricas e mudanças instantâneas de forma muito rápida.

## Onde é usado

É utilizado em ferramentas de monitoramento de desempenho de servidores, fluxos de dados do mercado de ações e sistemas de sensores de casas inteligentes.

## Costuma ser confundido com

Pode ser confundido com bancos de dados relacionais; enquanto os bancos de dados relacionais atualizam estados instantâneos, esses sistemas acumulam todo o histórico ao longo do tempo.

## Perguntas e respostas

**Por que um banco de dados normal não é usado para isso?**

Bancos de dados normais ficam lentos sob o peso de enormes pilhas de dados acumulados ao longo do tempo, enquanto esses sistemas são projetados para processar dados temporais muito rapidamente.

**Os dados antigos são excluídos?**

Geralmente, após um determinado período, os dados antigos são automaticamente resumidos ou limpos do disco.

## Termos relacionados

- [Database](https://trescout.com/pt/dictionary/database/)
- [Monitoring Tool](https://trescout.com/pt/dictionary/monitoring-tool/)
- [Data Processing](https://trescout.com/pt/dictionary/data-processing/)

## Ferramentas relacionadas

- [Prometheus](https://trescout.com/pt/discover/prometheus/)

Esta explicação foi escrita em linguagem simples para a TreScout com IA e **traduzida automaticamente** do original em turco · a versão turca é a que vale. Se algo parecer errado ou faltando, escreva para [hello@trescout.com](mailto:hello@trescout.com). [Ler em turco →](https://trescout.com/dictionary/time-series-database/)

---
Fonte: TreScout Glossário · https://trescout.com/pt/dictionary/time-series-database/
