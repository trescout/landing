# Gerenciamento persistente de dados em sistemas distribuídos

Desenvolvido pela Deno, o Celld oferece uma infraestrutura de objetos duráveis ​​auto-hospedada para sistemas distribuídos. Esta tecnologia, escrita em linguagem Rust, permite distribuir o gerenciamento de estado entre diferentes nós de forma escalonável.

- ★ 4.405
- Rust
- GitHub Trending · 2026-08-08

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
Quero construir um sistema distribuído usando Celld. Após criar um espaço de armazenamento compatível com S3, explique passo a passo como os nós usarão esse espaço e como distribuir pacotes Wrangler. Resuma os detalhes técnicos em linguagem simples, especialmente sobre como os nós se descobrem e garantem a consistência dos dados no S3.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/celld/
