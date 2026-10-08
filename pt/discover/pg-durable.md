# Gerenciamento robusto de processos no PostgreSQL

Desenvolvido pela Microsoft, pg_durable é uma biblioteca projetada para gerenciar processos de execução duráveis no PostgreSQL. Escrita em Rust, a ferramenta permite que fluxos de trabalho complexos sejam executados no banco de dados de maneira persistente e tolerante a falhas.

- ★ 2.831
- Rust
- GitHub Trending · 2026-06-08

## Atualizações

- **7 de outubro de 2026:** Estrelas 2,811 → 2,831, versão mais recente v0.2.9 (7 de outubro de 2026).
- **12 de setembro de 2026:** Estrelas 2,800 → 2,811, versão mais recente v0.2.8 (11 de setembro de 2026).
- **2 de setembro de 2026:** Estrelas 2,781 → 2,800, versão mais recente v0.2.7 (1 de setembro de 2026).
- **24 de agosto de 2026:** Estrelas 2,716 → 2,781, versão mais recente v0.2.6 (24 de agosto de 2026).

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

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero criar um fluxo de trabalho usando o plugin pg_durable no PostgreSQL. Como devo configurar a função df.start() para gerenciar um processo persistente e tolerante a falhas dentro do banco de dados? Como posso criar uma estrutura que processe dados e possa continuar de onde parou em caso de erro, usando os operadores ~> e |=> que conectam as etapas do SQL? Explique este processo com exemplos usando comandos SQL.

## Termos relacionados do glossário

- [Durable Execution](https://trescout.com/pt/dictionary/durable-execution/)
- [Rust](https://trescout.com/pt/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** É adequado para desenvolvedores de back-end, administradores de banco de dados e engenheiros de dados que desejam gerenciar processos de processamento de dados diretamente no PostgreSQL de forma persistente e tolerante a falhas.

## Links

- [Repositório no GitHub →](https://github.com/microsoft/pg_durable)
- [Ler em turco →](https://trescout.com/discover/pg-durable/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-06-08: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/pg-durable/
