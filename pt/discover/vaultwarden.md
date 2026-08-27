# Gerenciamento de senhas em seu próprio servidor

Não foi possível produzir um resumo para este item hoje. Consulte o link da fonte para obter detalhes.

- ★ 65.982
- Rust
- GitHub Trending · 2026-08-24

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
Ajude-me a instalar o Vaultwarden, uma ferramenta que fornece gerenciamento de senhas em meu próprio servidor. Esta ferramenta é um software de servidor compatível com clientes Bitwarden. Como irei instalar usando Docker, explique passo a passo como configurar os comandos de imagem para puxar e executar, montando um volume para persistir meus dados e levando em consideração os requisitos de HTTPS.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/vaultwarden/
