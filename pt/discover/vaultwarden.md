# Gerenciamento de senhas em seu próprio servidor

Vaultwarden é um software de servidor de código aberto desenvolvido na linguagem Rust que funciona de forma compatível com a ferramenta de gerenciamento de senhas Bitwarden.

- ★ 68.594
- Rust
- GitHub Trending · 2026-08-24

## Atualizações

- **6 de outubro de 2026:** Estrelas 67,398 → 68,594, versão mais recente 1.37.4 (5 de outubro de 2026).
- **14 de setembro de 2026:** Estrelas 65,982 → 67,398, versão mais recente 1.37.3 (13 de setembro de 2026).
- **24 de agosto de 2026:** Estrelas 65,983 → 65,982, versão mais recente 1.37.2 (22 de agosto de 2026).

## O que você ganha

- Totalmente compatível com clientes oficiais da Bitwarden
- Pode ser hospedado em seu próprio servidor com baixo consumo de recursos
- Oferece autenticação de dois fatores e acesso de emergência

## Instalação

**Baixe e execute o contêiner**

```
docker pull vaultwarden/server:latest
docker run --detach --name vaultwarden \
  --env DOMAIN="https://vw.domain.tld" \
  --volume /vw-data/:/data/ \
  --restart unless-stopped \
  --publish 127.0.0.1:8000:80 \
  vaultwarden/server:latest
```

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Ajude-me a instalar o Vaultwarden, uma ferramenta que fornece gerenciamento de senhas em meu próprio servidor. Esta ferramenta é um software de servidor compatível com clientes Bitwarden. Como irei instalar usando Docker, explique passo a passo como configurar os comandos de imagem para puxar e executar, montando um volume para persistir meus dados e levando em consideração os requisitos de HTTPS.

## Termos relacionados do glossário

- [Rust](https://trescout.com/pt/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** É para usuários que desejam hospedar suas próprias senhas e dados confidenciais em seu próprio servidor, em vez de depender de serviços de nuvem de terceiros.
- **Licença:** AGPL-3.0

## Links

- [Repositório no GitHub →](https://github.com/dani-garcia/vaultwarden)
- [Ler em turco →](https://trescout.com/discover/vaultwarden/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-08-24: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/vaultwarden/
