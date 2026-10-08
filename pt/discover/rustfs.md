# Sistema de armazenamento de objetos de alto desempenho

O RustFS foi desenvolvido como um sistema de armazenamento de objetos de alto desempenho compatível com S3. Oferece suporte à interoperabilidade e migração de dados com outras plataformas compatíveis com S3, como MinIO e Ceph.

- ★ 34.330
- Rust
- GitHub Trending · 2026-09-19

## Atualizações

- **3 de outubro de 2026:** Estrelas 33,264 → 34,330, versão mais recente 1.0.1 (3 de outubro de 2026).
- **19 de setembro de 2026:** Estrelas 33,264 → 33,264, versão mais recente 1.0.0 (16 de setembro de 2026).

## O que você ganha

- Proporciona alta velocidade e segurança de memória com a linguagem Rust
- Funciona perfeitamente com ferramentas existentes graças à sua estrutura compatível com S3
- Oferece uso comercial irrestrito com a licença Apache 2.0

## Instalação

**Iniciar com script de instalação**

```
curl -O https://rustfs.com/install_rustfs.sh && bash install_rustfs.sh
```

**Executar a versão mais recente com Docker**

```
docker run -d -p 9000:9000 -p 9001:9001 -v $(pwd)/data:/data -v $(pwd)/logs:/logs rustfs/rustfs:latest
```

## Execução

**Iniciar o sistema usando Docker Compose**

```
docker compose -f docker-compose-simple.yml up -d
```

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero configurar um ambiente de armazenamento de objetos de alto desempenho usando o RustFS. Como posso gerenciar meus dados aproveitando a compatibilidade S3 do sistema e a que devo estar atento ao escalar em uma arquitetura distribuída? Oriente-me passo a passo sobre a instalação e as configurações básicas deste sistema licenciado sob Apache 2.0.

## Termos relacionados do glossário

- [Object Storage System](https://trescout.com/pt/dictionary/object-storage-system/)
- [Rust](https://trescout.com/pt/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Destina-se a administradores de sistemas e desenvolvedores que buscam uma solução de armazenamento rápida, segura e compatível com S3 para cargas de trabalho de big data, projetos de inteligência artificial e data lakes.
- **Licença:** Apache-2.0

## Links

- [Repositório no GitHub →](https://github.com/rustfs/rustfs)
- [Ler em turco →](https://trescout.com/discover/rustfs/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-09-19: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/rustfs/
