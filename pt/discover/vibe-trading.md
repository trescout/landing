# Negociação pessoal com inteligência artificial

A Vibe-Trading oferece um agente comercial pessoal desenvolvido para negociação nos mercados financeiros. O projeto permite aos usuários gerenciar estratégias de negociação automáticas com sua estrutura baseada em Python.

- ★ 31.295
- Python
- GitHub Trending · 2026-06-04

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
Quero negociar nos mercados financeiros com o agente Vibe-Trading. Por favor, ajude-me a analisar os dados atuais do mercado, testar as estratégias que identifiquei e gerenciar minhas conexões de corretagem com segurança. Explique passo a passo como posso configurar processos de negociação automatizados, determinando especificamente meus mandatos de negociação e limites de risco.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/vibe-trading/
