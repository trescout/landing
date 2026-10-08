# Gerenciamento persistente de dados em sistemas distribuídos

Desenvolvido pela Deno, o Celld oferece uma infraestrutura de objetos duráveis ​​auto-hospedada para sistemas distribuídos. Esta tecnologia, escrita em linguagem Rust, permite distribuir o gerenciamento de estado entre diferentes nós de forma escalonável.

- ★ 4.937
- Rust
- GitHub Trending · 2026-08-08

## Atualizações

- **2 de outubro de 2026:** Estrelas 4,817 → 4,937, versão mais recente v0.6.1 (1 de outubro de 2026).
- **27 de setembro de 2026:** Estrelas 4,630 → 4,817, versão mais recente v0.6.0 (26 de setembro de 2026).
- **15 de setembro de 2026:** Estrelas 4,521 → 4,630, versão mais recente v0.5.0 (15 de setembro de 2026).
- **6 de setembro de 2026:** Estrelas 4,405 → 4,521, versão mais recente v0.4.1 (5 de setembro de 2026).

## O que você ganha

- Fornece gerenciamento de estado escalonável em sua própria infraestrutura.
- Ele armazena cada objeto como um banco de dados SQLite independente.
- Ele estabelece coordenação entre nós com armazenamento compatível com S3.

## Instalação

**Baixe a ferramenta para o seu computador**

```
curl -fsSL https://celld.dev/install.sh | sh
```

## Execução

**Nó restrito a recursos**

```
CELLD_MAX_RESIDENT_CELLS=1000 \
CELLD_RESIDENT_LOW_WATER=800 \
celld --bucket s3://my-cells-bucket --listen 0.0.0.0:8080 \
  --advertise node-a.internal:8080
```

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero construir um sistema distribuído usando Celld. Após criar um espaço de armazenamento compatível com S3, explique passo a passo como os nós usarão esse espaço e como distribuir pacotes Wrangler. Resuma os detalhes técnicos em linguagem simples, especialmente sobre como os nós se descobrem e garantem a consistência dos dados no S3.

## Termos relacionados do glossário

- [State Management](https://trescout.com/pt/dictionary/state-management/)
- [Durable Objects](https://trescout.com/pt/dictionary/durable-objects/)
- [Self-hosted](https://trescout.com/pt/dictionary/self-hosted/)
- [Rust](https://trescout.com/pt/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** É adequado para desenvolvedores que trabalham em sistemas distribuídos e desejam estabelecer gerenciamento de estado escalonável em seus próprios servidores.
- **Licença:** Apache-2.0

## Links

- [Repositório no GitHub →](https://github.com/denoland/celld)
- [Ler em turco →](https://trescout.com/discover/celld/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-08-08: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/celld/
