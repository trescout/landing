# Roteador que gerencia tráfego de inteligência artificial

Desenvolvido pela NVIDIA, Switchyard é um mecanismo de inferência de inteligência artificial de alto desempenho escrito em linguagem Rust. Ele oferece um ambiente de tempo de execução otimizado para executar modelos de linguagem grandes (LLM) com eficiência em diferentes infraestruturas de hardware.

- ★ 1.566
- Rust
- GitHub Trending · 2026-08-13

## O que você ganha
- Roteando o tráfego entre diferentes modelos de inteligência artificial
- Tradução entre formatos OpenAI e API Anthropic
- Rastreie métricas de transações e logs de erros

## Instalação
**Instalação como ferramenta de linha de comando**

```
curl -LsSf https://astral.sh/uv/install.sh | sh
source "$HOME/.local/bin/env"
uv tool install --python 3.10 "nemo-switchyard[cli]"
```

**Instalação como servidor**

```
cargo install --locked switchyard-server
switchyard-server --help
```


## Execução
**Verifique o status do servidor**

```
curl http://localhost:4000/health
```


## Se você não programa
Atue como um roteador de tráfego de IA para mim. Usando o Switchyard, quero que você distribua as solicitações dos meus agentes de codificação como Claude Code ou Codex entre diferentes modelos, traduza automaticamente entre os formatos OpenAI e API Anthropic e monitore todas as métricas operacionais. Gerencie solicitações recebidas com algoritmos de roteamento estruturados e realize testes A/B ou balanceamento de carga entre diferentes modelos quando necessário.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/switchyard/
