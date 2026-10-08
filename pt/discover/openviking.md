# Memória do sistema de arquivos para agentes de inteligência artificial

Desenvolvido pela Volcengine, o OpenViking oferece um banco de dados de contexto que se aprimora automaticamente para agentes de IA. Este sistema combina memória do agente, processos e habilidades de recuperação de informações (RAG) sob o mesmo teto.

- ★ 39.151
- Python
- GitHub Trending · 2026-08-18

## Atualizações

- **3 de outubro de 2026:** Estrelas 38,859 → 39,151, versão mais recente v0.4.23 (2 de outubro de 2026).
- **28 de setembro de 2026:** Estrelas 38,733 → 38,859, versão mais recente v0.4.22 (28 de setembro de 2026).
- **27 de setembro de 2026:** Estrelas 37,128 → 38,733, versão mais recente v0.4.21 (20 de setembro de 2026).
- **14 de setembro de 2026:** Estrelas 36,182 → 37,128, versão mais recente v0.4.20 (14 de setembro de 2026).

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

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Construa gerenciamento de contexto para um agente de inteligência artificial usando o banco de dados OpenViking. Ele estrutura as informações por meio do protocolo viking://, separando as informações em resumo L0, visão geral L1 e camadas de detalhes L2. Ao colocar a memória, os recursos e as capacidades do agente neste sistema de arquivos virtual, ele permite navegar nos diretórios durante a interrogação e criar memória de longo prazo, aprendendo com sessões anteriores.

## Termos relacionados do glossário

- [RAG](https://trescout.com/pt/dictionary/rag/)
- [AI Skills](https://trescout.com/pt/dictionary/ai-skills/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** É para desenvolvedores que desejam combinar gerenciamento de memória, processos de recuperação de informações e recursos de agentes de IA em um sistema organizado.
- **Licença:** AGPL-3.0

## Links

- [Repositório no GitHub →](https://github.com/volcengine/OpenViking)
- [Ler em turco →](https://trescout.com/discover/openviking/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-08-18: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/openviking/
