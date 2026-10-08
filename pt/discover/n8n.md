# Workflows visuais e automação com IA

O n8n combina canvas visual, código personalizado, agentes de IA e workflows em uma plataforma de automação fair-code. Ele oferece implantação self-hosted ou cloud e pode incluir diferentes provedores de modelos nos workflows.

- ★ 206.804
- GitHub Trending · 2026-08-23

## Atualizações

- **7 de outubro de 2026:** Estrelas 206,753 → 206,804, versão mais recente n8n@2.42.4 (7 de outubro de 2026).
- **6 de outubro de 2026:** Estrelas 206,694 → 206,753, versão mais recente n8n@2.42.3 (5 de outubro de 2026).
- **5 de outubro de 2026:** Estrelas 206,489 → 206,694, versão mais recente n8n@2.41.7 (5 de outubro de 2026).
- **2 de outubro de 2026:** Estrelas 206,409 → 206,489, versão mais recente n8n@2.41.6 (2 de outubro de 2026).

## Instalação

**Crie o volume de dados**

```
docker volume create n8n_data
```

## Execução

**Inicie o container Docker do n8n**

```
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

## O que esta ferramenta faz?

Com o n8n, você pode criar workflows em um canvas visual e estendê-los com JavaScript, Python e pacotes npm. As fontes oficiais listam flexibilidade de modelos entre OpenAI, Anthropic, Google e modelos de código aberto, além de aprovações humanas, observabilidade, acesso baseado em funções e trilhas de auditoria. A plataforma pode ser implantada de forma self-hosted ou na nuvem.

## Para quem é?

Equipes que querem combinar o desenho visual de workflows com código personalizado e agentes de IA.

## O que não esperar

Pessoas que procuram apenas produtos de licença proprietária ou não querem ampliar workflows com código ou configuração.

## Destaques

- Combina canvas visual, código personalizado e agentes de IA nos workflows.
- Pode ser estendido com JavaScript, Python e pacotes npm.
- Oferece implantação self-hosted e cloud.
- Lista aprovações humanas, observabilidade, acesso baseado em funções e trilhas de auditoria.

## Primeiro fluxo de uso

1. Siga o início rápido oficial com Docker para executar o n8n.
2. Abra o editor no navegador pela porta 5678.
3. Crie seu primeiro workflow no canvas visual.
4. Adicione código personalizado ou um provedor de modelos compatível conforme a sua necessidade.

## Início seguro

O n8n é source-available sob a Sustainable Use License. Consulte os termos oficiais da licença e configure o acesso e a operação da sua implantação self-hosted.

## Primeiro prompt

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Ajude-me a criar no canvas visual um workflow que receba uma entrada, a processe com um modelo de IA e passe o resultado para a próxima etapa.

## Termos relacionados do glossário

- [Self-hosting](https://trescout.com/pt/dictionary/self-hosting/)
- [Container](https://trescout.com/pt/dictionary/container/)
- [Open Source](https://trescout.com/pt/dictionary/open-source/)

## Links

- [Repositório no GitHub →](https://github.com/n8n-io/n8n)
- [Repositório GitHub oficial do n8n →](https://github.com/n8n-io/n8n)
- [Documentação oficial do n8n →](https://docs.n8n.io/)
- [Repositório de documentação do n8n →](https://github.com/n8n-io/n8n-docs)
- [Ler em turco →](https://trescout.com/discover/n8n/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-08-23: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/n8n/
