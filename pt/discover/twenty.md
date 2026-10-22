# CRM moderno e de código aberto

Twenty é uma alternativa de código aberto ao Salesforce que permite que equipes técnicas construam um CRM moderno que pode ser personalizado de acordo com seus processos de negócios. Você pode hospedar este sistema, que se concentra em fluxos de trabalho suportados por inteligência artificial, em seu próprio servidor.

- ★ 58.824
- TypeScript
- Lisans: özel
- GitHub Trending · 26 May 2026

## Atualizações

- **21 de outubro de 2026:** Estrelas 58,665 → 58,824, versão mais recente twenty/v2.50.0 (21 de outubro de 2026).
- **20 de outubro de 2026:** Estrelas 58,411 → 58,665, versão mais recente sdk/v2.49.0 (19 de outubro de 2026).
- **16 de outubro de 2026:** Estrelas 58,367 → 58,411, versão mais recente sdk/v2.48.0 (16 de outubro de 2026).
- **15 de outubro de 2026:** Estrelas 58,241 → 58,367, versão mais recente twenty/v2.47.0 (15 de outubro de 2026).

## O que você ganha

- Uma alternativa gratuita e de código aberto ao Salesforce.
- Controle total sobre seus dados com a opção de auto-hospedagem.
- Fluxos de trabalho modernos alimentados por IA.
- Blocos de construção flexíveis que podem ser adaptados às necessidades do seu negócio.

## Instalação

**Baixar modelo de ambiente**

```
curl -o .env https://raw.githubusercontent.com/twentyhq/twenty/refs/heads/main/packages/twenty-docker/.env.example
```

**Baixar arquivo Compose**

```
curl -o docker-compose.yml https://raw.githubusercontent.com/twentyhq/twenty/refs/heads/main/packages/twenty-docker/docker-compose.yml
```

**Gerar chave de criptografia**

```
openssl rand -base64 32
```

**Iniciar serviços**

```
docker compose up -d
```

## Execução

**Acessar interface local**

```
http://localhost:3000
```

## Como instalar?

Geralmente é instalado em seu próprio servidor com Docker; as etapas de instalação estão na documentação. Requer algum conhecimento técnico para gerenciar.

## Como instalar, como usar?

Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero instalar um CRM de código aberto chamado Twenty; crie um novo aplicativo no terminal com o comando 'npx create-twenty-app my-app' e publique-o em meu espaço de trabalho com 'npx twenty app:publish --private'. Diga-me também como executá-lo com Docker Compose para auto-hospedagem.

Repositório: https://github.com/twentyhq/twenty. Baseie-se nas instruções oficiais no arquivo README deste repositório para a instalação e execução.

Antes de começar, verifique em qual sistema operacional estamos e se as ferramentas necessárias (ex: Python, Node.js, Git, Docker) estão instaladas. Instale as que faltarem passo a passo de acordo com este sistema.

Crie uma pasta nova e vazia para trabalhar. Não toque em arquivos fora desta pasta e não exclua nada. Antes de executar cada comando, diga o que você vai fazer em uma frase.

Diga-me o que devo ver na tela ao final de cada etapa. Se ocorrer um erro, colarei a mensagem de erro para você exatamente como ela é, e vamos corrigi-la juntos.

## Termos relacionados do glossário

- [CRM](https://trescout.com/pt/dictionary/crm/)
- [SaaS](https://trescout.com/pt/dictionary/saas/)
- [Self-hosting](https://trescout.com/pt/dictionary/self-hosting/)
- [Open Source](https://trescout.com/pt/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Equipes técnicas que desejam estabelecer seu próprio CRM
- **Dificuldade:** Próximo · auto-host (desenvolvedor necessário)
- **O que oferece:** CRM personalizável com tecnologia de IA
- **Taxa:** Código aberto · auto-hospedado gratuitamente
- **Licença:** Fora do padrão (NOASSERTION) · detalhe abaixo

**Licença:** ⚠️ Sua licença não é padrão (GitHub 'NOASSERTION'). É referido como 'código aberto', mas o uso autônomo/auto-hospedado e a reentrega comercial/SaaS podem estar sujeitos a termos diferentes. Certifique-se de ler o arquivo LICENSE no repositório antes do uso comercial.

## Links

- [Repositório no GitHub →](https://github.com/twentyhq/twenty)
- [Ler em turco →](https://trescout.com/discover/twenty/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-05-26: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. O texto de apresentação foi preparado com IA a partir da própria documentação do repositório e esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/twenty/
