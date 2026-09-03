# Seleção automática de ações para o mercado chinês

Sequoia-X é um software baseado em Python que realiza a seleção automática de ações com base em fórmulas de análise técnica, utilizando dados do mercado de ações chinês. Ele executa processos de varredura após o fechamento do mercado no final do dia e envia os resultados via Feishu, um aplicativo de mensagens corporativas.

- ★ 6.376
- Python
- GitHub Trending · 2026-09-03

## O que você ganha
- Armazena dados de ações em um banco de dados local
- Aplica automaticamente múltiplas estratégias de análise técnica
- Envia os resultados do final do dia através do aplicativo de mensagens Feishu

## Instalação
**Instalando as bibliotecas necessárias**

```
pip install .
```


## Execução
**Carregamento inicial de dados históricos**

```
python main.py --backfill
```

**Iniciar a varredura diária**

```
python main.py
```


## Se você não programa
Quero usar a ferramenta Sequoia-X para analisar ações no mercado chinês usando métodos de análise técnica. Após realizar as instalações necessárias no meu ambiente Python, usarei primeiro o modo backfill para carregar dados históricos e, em seguida, o modo de execução diária para realizar a varredura automática e receber notificações após o fechamento do mercado. Nesse processo, desejo garantir que os dados sejam armazenados no banco de dados SQLite local e que os resultados sejam enviados via Feishu.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/sequoia-x/
