# Teste modelos de IA de forma autônoma

SIA é uma estrutura de IA de autoaperfeiçoamento desenvolvida para melhorar de forma autônoma o desempenho de modelos e agentes de IA em tarefas específicas de benchmark. Este sistema baseado em Python permite que sistemas de inteligência artificial otimizem seus processos analisando seus próprios resultados.

- ★ 1.478
- Python
- GitHub Trending · 2026-06-12

## O que você ganha
- Melhora de forma autônoma o desempenho das tarefas dos modelos de inteligência artificial.
- Meta fornece refinamento cíclico entre agentes alvo e de feedback.
- Oferece alta precisão e eficiência de velocidade de processamento em tarefas de benchmark.

## Instalação
**Instalação com Modelos Claude**

```
python3 -m venv .venv && source .venv/bin/activate
pip install 'sia-agent[claude]'
export ANTHROPIC_API_KEY="..."
```

**Configuração com vários provedores (OpenHands)**

```
python3 -m venv .venv && source .venv/bin/activate
pip install 'sia-agent[openhands]'

# Export the key(s) for the provider(s) you'll use:
export ANTHROPIC_API_KEY="..."   # for anthropic/* models
export GEMINI_API_KEY="..."      # for gemini/* models (or GOOGLE_API_KEY)
export OPENAI_API_KEY="..."      # for openai/* models
```


## Execução
**Iniciando o ciclo de autocura**

```
sia run --task gpqa --max_gen 5 --run_id 1
```

**Painel de visualização**

```
sia web
```


## Se você não programa
Quero melhorar o desempenho de um agente de IA usando a estrutura SIA. Após concluir a instalação, qual comando devo usar para iniciar o ciclo de autoaperfeiçoamento selecionando uma das tarefas disponíveis (por exemplo, gpqa) e como devo interpretar as saídas no final do processo (target_agent.py, agent_execution.json, melhoria.md)? Além disso, como posso incluir meu próprio diretório de tarefas personalizado no sistema?

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/sia/
