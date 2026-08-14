# PostgreSQL reescrito com Rust

O projeto pgrust, no qual o sistema de gerenciamento de banco de dados PostgreSQL foi reescrito com a linguagem de programação Rust, conclui com êxito todos os testes de regressão. Este trabalho tem como objetivo modernizar a arquitetura de banco de dados com uma linguagem focada na segurança de memória.

- ★ 3.957
- Rust
- GitHub Trending · 2026-07-12

## Atualizar
- 2 de agosto de 2026: Star 2.171 → 3.957, versão final v0.2-release (30 de julho de 2026).

## O que você ganha
- Compatibilidade de disco com Postgres 18.3
- Mais de 46 mil sucessos em testes de regressão
- Arquitetura moderna focada na segurança da memória

## Instalação
**Teste rápido com Docker**

```
docker run -d --name pgrust -e POSTGRES_PASSWORD=secret malisper/pgrust:v0.1 && until docker exec -e PGPASSWORD=secret pgrust psql -h 127.0.0.1 -U postgres -c '\q' >/dev/null 2>&1; do sleep 1; done && docker exec -it -e PGPASSWORD=secret pgrust psql -h 127.0.0.1 -U postgres; docker rm -f pgrust
```


## Se você não programa
Qual é o objetivo principal do projeto Pgrust, como é garantida a compatibilidade do disco com o PostgreSQL existente e como é utilizada a programação suportada por inteligência artificial no desenvolvimento do projeto? Conte-nos sobre a compatibilidade da versão atual do Pgrust com o Postgres 18.3 e seu sucesso em testes de regressão.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/pgrust/
