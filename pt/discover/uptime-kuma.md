# Ferramenta de monitoramento de status de servidores e serviços

O Uptime Kuma é uma ferramenta de monitoramento auto-hospedada com uma interface visual. Esta aplicação baseada em JavaScript, que permite acompanhar o status de funcionamento de sites e serviços, oferece uma experiência amigável.

- ★ 93.936
- JavaScript
- GitHub Trending · 2026-11-14

## Atualizações

- **14 de novembro de 2026:** Estrelas 93,934 → 93,936, versão mais recente 2.5.11 (12 de novembro de 2026).

## O que você ganha

- Acompanhe sites e serviços em tempo real
- Obtenha suporte a vários idiomas e notificações
- Crie páginas de status visual

## Instalação

**Instalação com Docker Compose**

```
mkdir uptime-kuma
cd uptime-kuma
curl -o compose.yaml https://raw.githubusercontent.com/louislam/uptime-kuma/master/compose.yaml
docker compose up -d
```

**Instalação com Comando Docker**

```
docker run -d --restart=always -p 3001:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:2
```

## Execução

**Executando com Docker**

```
docker compose up -d
```

## Se você não programa

Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero instalar a ferramenta de monitoramento chamada Uptime Kuma. Para usar o Docker Compose, preciso executar o seguinte comando: mkdir uptime-kuma
cd uptime-kuma
curl -o compose.yaml https://raw.githubusercontent.com/louislam/uptime-kuma/master/compose.yaml
docker compose up -d. Você pode me ajudar a concluir estas etapas?

Repositório: https://github.com/louislam/uptime-kuma. Baseie-se nas instruções oficiais no arquivo README deste repositório para a instalação e execução.

Antes de começar, verifique em qual sistema operacional estamos e se as ferramentas necessárias (ex: Python, Node.js, Git, Docker) estão instaladas. Instale as que faltarem passo a passo de acordo com este sistema.

Crie uma pasta nova e vazia para trabalhar. Não toque em arquivos fora desta pasta e não exclua nada. Antes de executar cada comando, diga o que você vai fazer em uma frase.

Diga-me o que devo ver na tela ao final de cada etapa. Se ocorrer um erro, colarei a mensagem de erro para você exatamente como ela é, e vamos corrigi-la juntos.

## Termos relacionados do glossário

- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Ideal para qualquer pessoa que queira monitorar se sites e servidores estão funcionando em seu próprio servidor.
- **Licença:** MIT

## Links

- [Repositório no GitHub →](https://github.com/louislam/uptime-kuma)
- [Ler em turco →](https://trescout.com/discover/uptime-kuma/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-11-14: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. O texto de apresentação foi preparado com IA a partir da própria documentação do repositório e esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/uptime-kuma/
