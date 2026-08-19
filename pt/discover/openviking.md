# Memória do sistema de arquivos para agentes de inteligência artificial

Desenvolvido pela Volcengine, o OpenViking oferece um banco de dados de contexto que se aprimora automaticamente para agentes de IA. Este sistema combina memória do agente, processos e habilidades de recuperação de informações (RAG) sob o mesmo teto.

- ★ 29.066
- Python
- GitHub Trending · 2026-08-18

## O que você ganha
- Organiza as informações hierarquicamente como um sistema de arquivos.
- Reduz o custo da inteligência artificial com carregamento em camadas.
- Torna o histórico do agente rastreável e depurável.

## Instalação
**Instalação e inicialização do servidor**

```
pip install openviking --upgrade
openviking-server init      # interactive wizard: providers, models, ov.conf
openviking-server doctor    # validate setup
openviking-server           # start (background: nohup openviking-server > openviking.log 2>&1 &)
```


## Execução
**Inicie um bate-papo com suporte de bot**

```
pip install "openviking[bot]"
openviking-server --with-bot
ov chat   # in another terminal
```


## Se você não programa
Construa gerenciamento de contexto para um agente de inteligência artificial usando o banco de dados OpenViking. Ele estrutura as informações por meio do protocolo viking://, separando as informações em resumo L0, visão geral L1 e camadas de detalhes L2. Ao colocar a memória, os recursos e as capacidades do agente neste sistema de arquivos virtual, ele permite navegar nos diretórios durante a interrogação e criar memória de longo prazo, aprendendo com sessões anteriores.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/openviking/
