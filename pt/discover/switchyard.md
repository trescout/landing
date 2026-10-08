# Roteador que gerencia tráfego de inteligência artificial

Desenvolvido pela NVIDIA, Switchyard é um mecanismo de inferência de inteligência artificial de alto desempenho escrito em linguagem Rust. Ele oferece um ambiente de tempo de execução otimizado para executar modelos de linguagem grandes (LLM) com eficiência em diferentes infraestruturas de hardware.

- ★ 3.227
- Rust
- GitHub Trending · 2026-08-13

## Atualizações

- **27 de setembro de 2026:** Estrelas 2,617 → 3,227, versão mais recente v0.3.0 (22 de setembro de 2026).
- **31 de agosto de 2026:** Estrelas 1,566 → 2,617, versão mais recente v0.2.0 (10 de agosto de 2026).
- **15 de agosto de 2026:** Estrelas 923 → 1,566, versão mais recente v0.2.0 (10 de agosto de 2026).

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

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Atue como um roteador de tráfego de IA para mim. Usando o Switchyard, quero que você distribua as solicitações dos meus agentes de codificação como Claude Code ou Codex entre diferentes modelos, traduza automaticamente entre os formatos OpenAI e API Anthropic e monitore todas as métricas operacionais. Gerencie solicitações recebidas com algoritmos de roteamento estruturados e realize testes A/B ou balanceamento de carga entre diferentes modelos quando necessário.

## Termos relacionados do glossário

- [Inference](https://trescout.com/pt/dictionary/inference/)
- [Runtime](https://trescout.com/pt/dictionary/runtime/)
- [LLM](https://trescout.com/pt/dictionary/llm/)
- [Rust](https://trescout.com/pt/dictionary/rust/)
- [API](https://trescout.com/pt/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Destina-se a desenvolvedores que desejam gerenciar com eficiência grandes modelos de linguagem em diferentes hardwares e provedores de serviços.
- **Licença:** Apache-2.0

## Links

- [Repositório no GitHub →](https://github.com/NVIDIA-NeMo/Switchyard)
- [Ler em turco →](https://trescout.com/discover/switchyard/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-08-13: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/switchyard/
