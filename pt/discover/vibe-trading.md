# Negociação pessoal com inteligência artificial

A Vibe-Trading oferece um agente comercial pessoal desenvolvido para negociação nos mercados financeiros. O projeto permite aos usuários gerenciar estratégias de negociação automáticas com sua estrutura baseada em Python.

- ★ 34.287
- Python
- GitHub Trending · 2026-06-04

## Atualizações

- **29 de setembro de 2026:** Estrelas 33,083 → 34,287, versão mais recente v0.1.16 (29 de setembro de 2026).
- **9 de setembro de 2026:** Estrelas 32,899 → 33,083, versão mais recente v0.1.15 (9 de setembro de 2026).
- **7 de setembro de 2026:** Estrelas 31,295 → 32,899, versão mais recente v0.1.14 (20 de agosto de 2026).
- **20 de agosto de 2026:** Estrelas 30,558 → 31,295, versão mais recente v0.1.14 (20 de agosto de 2026).

## O que você ganha

- Gerenciamento automatizado de estratégia com agente comercial pessoal.
- Acesso a dados de mercado com suporte multi-corretagem.
- Autorização de transações orientada para segurança e livro de auditoria.

## Instalação

**Instalação Direta**

```
pip install vibe-trading-ai
```

**Configuração do ambiente do desenvolvedor**

```
git clone https://github.com/HKUDS/Vibe-Trading.git
cd Vibe-Trading
python -m venv .venv

# Activate
source .venv/bin/activate          # Linux / macOS
# .venv\Scripts\Activate.ps1       # Windows PowerShell

pip install -e .
cp agent/.env.example agent/.env   # Edit — set your LLM provider API key
vibe-trading                       # Launch interactive TUI
```

## Execução

**Pesquisa com Linguagem Natural**

```
vibe-trading run -p "Backtest a BTC-USDT 20/50 moving-average strategy for 2024, summarize return and drawdown, then export the report"
```

**Teste de Estratégia**

```
vibe-trading alpha bench --zoo gtja191 --universe csi300 --period 2018-2025 --top 20
```

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero negociar nos mercados financeiros com o agente Vibe-Trading. Por favor, ajude-me a analisar os dados atuais do mercado, testar as estratégias que identifiquei e gerenciar minhas conexões de corretagem com segurança. Explique passo a passo como posso configurar processos de negociação automatizados, determinando especificamente meus mandatos de negociação e limites de risco.

## Termos relacionados do glossário

- [Trading Agent](https://trescout.com/pt/dictionary/trading-agent/)
- [Agent](https://trescout.com/pt/dictionary/agent/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Ele foi projetado para usuários que desejam desenvolver e gerenciar estratégias de negociação automática nos mercados financeiros.
- **Licença:** MIT

## Links

- [Repositório no GitHub →](https://github.com/HKUDS/Vibe-Trading)
- [Ler em turco →](https://trescout.com/discover/vibe-trading/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-06-04: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/vibe-trading/
