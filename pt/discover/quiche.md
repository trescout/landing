# Suporte a quic e http3 com Rust

Desenvolvido pela Cloudflare, o quiche oferece uma implementação em linguagem Rust do protocolo de transporte QUIC e do padrão de rede HTTP/3. Com o objetivo de acelerar o tráfego de internet, esta biblioteca fornece uma infraestrutura de baixo nível para desenvolvedores que desejam otimizar o desempenho de rede.

- ★ 12.638
- GitHub Trending · 2026-09-20

## Atualizações

- **27 de setembro de 2026:** Estrelas 12,452 → 12,638, versão mais recente 0.30.0 (17 de setembro de 2026).

## O que você ganha

- Implementar o protocolo de transporte QUIC
- Trabalhar no padrão de rede HTTP/3
- Processar pacotes de rede de baixo nível

## Instalação

**Clone o projeto**

```
git clone https://github.com/cloudflare/quiche
```

## Execução

**Execute o cliente**

```
cargo run --bin quiche-client -- https://cloudflare-quic.com/
```

**Execute o servidor**

```
cargo run --bin quiche-server -- --cert apps/src/bin/cert.crt --key apps/src/bin/cert.key
```

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Gostaria de processar pacotes QUIC e gerenciar estados de conexão de rede usando esta biblioteca escrita na linguagem de programação Rust. Depois de clonar o projeto, quais passos devo seguir para executar o cliente e o servidor?

## Termos relacionados do glossário

- [Rust](https://trescout.com/pt/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Desenvolvedores que desejam otimizar o desempenho de rede e fornecer suporte a HTTP/3.
- **Licença:** BSD-2-Clause

## Links

- [Repositório no GitHub →](https://github.com/cloudflare/quiche)
- [Ler em turco →](https://trescout.com/discover/quiche/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-09-20: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/quiche/
