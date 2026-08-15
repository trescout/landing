# Gerenciamento robusto de processos no PostgreSQL

Desenvolvido pela Microsoft, pg_durable é uma biblioteca projetada para gerenciar processos de execução duráveis no PostgreSQL. Escrita em Rust, a ferramenta permite que fluxos de trabalho complexos sejam executados no banco de dados de maneira persistente e tolerante a falhas.

- ★ 2.716
- Rust
- GitHub Trending · 2026-06-08

## O que você ganha
- Ele gerencia fluxos de trabalho no banco de dados de maneira persistente e tolerante a falhas.
- Em caso de travamento ou interrupção, continua as operações a partir do último ponto de verificação.
- Ele roda diretamente no PostgreSQL sem exigir infraestrutura adicional.

## Instalação
**Ativando o plug-in**

```
CREATE EXTENSION pg_durable;
```


## Execução
**Iniciando um fluxo de trabalho**

```
SELECT df.start(
    'SELECT id FROM documents WHERE processed = false LIMIT 100' |=> 'batch'
    ~> 'UPDATE documents SET processed = true WHERE id = ANY($batch)'
);
```


## Se você não programa
Quero criar um fluxo de trabalho usando o plugin pg_durable no PostgreSQL. Como devo configurar a função df.start() para gerenciar um processo persistente e tolerante a falhas dentro do banco de dados? Como posso criar uma estrutura que processe dados e possa continuar de onde parou em caso de erro, usando os operadores ~> e |=> que conectam as etapas do SQL? Explique este processo com exemplos usando comandos SQL.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/pg-durable/
