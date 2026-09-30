# Suporte a quic e http3 com Rust

Desenvolvido pela Cloudflare, o quiche oferece uma implementação em linguagem Rust do protocolo de transporte QUIC e do padrão de rede HTTP/3. Com o objetivo de acelerar o tráfego de internet, esta biblioteca fornece uma infraestrutura de baixo nível para desenvolvedores que desejam otimizar o desempenho de rede.

- ★ 12.638
- GitHub Trending · 2026-09-20

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
Gostaria de processar pacotes QUIC e gerenciar estados de conexão de rede usando esta biblioteca escrita na linguagem de programação Rust. Depois de clonar o projeto, quais passos devo seguir para executar o cliente e o servidor?

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/quiche/
