# Plataforma de suporte ao cliente de código aberto

Chatwoot é uma plataforma de código aberto que oferece chat ao vivo, suporte por e-mail e gerenciamento de mesa omnicanal. Desenvolvido como uma alternativa a softwares comerciais como Intercom e Zendesk, esta ferramenta permite gerenciar as interações com os clientes a partir de um único centro.

- ★ 38.153
- GitHub Trending · 2026-06-12

**Nota da TreScout:** Ele coleta mensagens dos clientes em uma única tela: chat do site, e-mail, WhatsApp. Serviços prontos que fazem o mesmo trabalho cobram uma taxa mensal por pessoa, mas como roda em seu próprio servidor não existe essa taxa, em troca o servidor e a manutenção passam a ser seu trabalho. Sua instalação não é monolítica, requer diversos utilitários e tem dificuldade com os pacotes de servidores mais baratos.

## Atualizações

- **24 de outubro de 2026:** Estrelas 38,048 → 38,153, versão mais recente v4.19.1 (24 de outubro de 2026).
- **21 de outubro de 2026:** Estrelas 36,927 → 38,048, versão mais recente v4.19.0 (20 de outubro de 2026).
- **18 de setembro de 2026:** Estrelas 36,253 → 36,927, versão mais recente v4.18.0 (18 de setembro de 2026).
- **27 de agosto de 2026:** Estrelas 36,001 → 36,253, versão mais recente v4.17.1 (27 de agosto de 2026).

## O que você ganha

- Ele combina todos os canais do cliente em uma única caixa de entrada.
- Responde automaticamente a perguntas de rotina com um assistente apoiado por inteligência artificial.
- Dá a você controle total sobre os dados do cliente, hospedando-os em seu próprio servidor.

## Instalação

**Baixar arquivo de ambiente**

```
wget -O .env https://raw.githubusercontent.com/chatwoot/chatwoot/develop/.env.example
```

**Baixar arquivo Docker Compose**

```
wget -O docker-compose.yaml https://raw.githubusercontent.com/chatwoot/chatwoot/develop/docker-compose.production.yaml
```

**Preparar banco de dados**

```
docker compose run --rm rails bundle exec rails db:chatwoot_prepare
```

## Execução

**Iniciar serviços**

```
docker compose up -d
```

## Se você não programa

Cole isto no seu agente (Claude Code · Codex · Antigravity)

Responda às perguntas fingindo ser um representante de suporte ao cliente. Como assistente do Capitão AI no Chatwoot, resolva automaticamente as perguntas mais frequentes e direcione questões complexas aos colegas de equipe relevantes. Melhore a experiência de suporte ao cliente, fornecendo sempre informações corteses, rápidas e precisas.

Repositório: https://github.com/chatwoot/chatwoot. Baseie-se nas instruções oficiais no arquivo README deste repositório para a instalação e execução.

Antes de começar, verifique em qual sistema operacional estamos e se as ferramentas necessárias (ex: Python, Node.js, Git, Docker) estão instaladas. Instale as que faltarem passo a passo de acordo com este sistema.

Crie uma pasta nova e vazia para trabalhar. Não toque em arquivos fora desta pasta e não exclua nada. Antes de executar cada comando, diga o que você vai fazer em uma frase.

Diga-me o que devo ver na tela ao final de cada etapa. Se ocorrer um erro, colarei a mensagem de erro para você exatamente como ela é, e vamos corrigi-la juntos.

## Termos relacionados do glossário

- [Omni-channel Desk](https://trescout.com/pt/dictionary/omni-channel-desk/)
- [Omni-channel](https://trescout.com/pt/dictionary/omni-channel/)
- [Deployment](https://trescout.com/pt/dictionary/deployment/)
- [Self-hosted](https://trescout.com/pt/dictionary/self-hosted/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** É adequado para empresas que desejam gerenciar as interações com os clientes a partir de um único centro e automatizar os processos de suporte.

## Links

- [Repositório no GitHub →](https://github.com/chatwoot/chatwoot)
- [Ler em turco →](https://trescout.com/discover/chatwoot/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-06-12: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. O texto de apresentação foi preparado com IA a partir da própria documentação do repositório e esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/chatwoot/
