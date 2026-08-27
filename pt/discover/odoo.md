# Planejamento de recursos empresariais de código aberto

Odoo é uma plataforma de planejamento de recursos empresariais de código aberto que permite às empresas gerenciar todos os seus processos operacionais sob o mesmo teto. Desenvolvido em linguagem Python, este sistema oferece uma ampla gama de aplicações modulares de negócios, desde vendas até contabilidade.

- ★ 52.082
- GitHub Trending · 2026-06-04

## O que você ganha
- Ele gerencia processos de negócios como vendas, contabilidade e armazém a partir de um único centro.
- Oferece aplicativos de negócios modulares compatíveis entre si.
- Ele fornece uma infraestrutura de código aberto que pode ser customizada de acordo com a necessidade.

## Instalação
**Iniciar banco de dados PostgreSQL**

```
docker run -d --name odoo-db -e POSTGRES_DB=postgres -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=change_me postgres:15
```

**Iniciar Odoo conectado ao banco de dados**

```
docker run -d --name odoo --link odoo-db:db -p 127.0.0.1:8069:8069 odoo:latest
```


## Execução
**Acessar interface local**

```
http://localhost:8069
```


## Como começar
- Fonte oficial →

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/odoo/
