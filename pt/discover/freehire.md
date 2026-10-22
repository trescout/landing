# Mecanismo de busca de empregos de código aberto

Desenvolvido em Go, o freehire é um mecanismo de busca de código aberto (com código-fonte aberto para acesso e desenvolvimento de todos) projetado para quem busca emprego. Ele oferece uma plataforma que permite aos usuários pesquisar e encontrar vagas de emprego.

- ★ 2.661
- Go
- GitHub Trending · 2026-10-22

## Atualizações

- **22 de outubro de 2026:** Estrelas 2,643 → 2,661, versão mais recente extension-v0.1.10 (21 de outubro de 2026).

## O que você ganha

- Você acessa vagas de tecnologia coletadas diretamente das páginas de carreira das empresas, de forma atualizada e sem intermediários.
- Você analisa vagas duplicadas em diferentes sites de carreira de forma deduplicada, em uma lista limpa e filtrável.
- Você gerencia seu processo de busca de emprego com a análise de compatibilidade de currículo e o painel de rastreamento de candidaturas impulsionado por inteligência artificial.

## Instalação

**Configurar todo o sistema em um ambiente de contêiner e**

```
make up        # build + start the whole stack in Docker:
               # api, web, postgres, meilisearch, redis, s3
curl localhost:8080/health
curl localhost:8080/api/v1/jobs
```

## Execução

**Com uma porta diferente se a porta padrão estiver ocupada**

```
HIRE_HOST_PORT=8090 make up
```

## Se você não programa

Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero executar a aplicação Freehire, uma plataforma de busca de empregos de código aberto, no meu próprio sistema. Para iniciar todos os serviços usando o software de gerenciamento de contêineres Docker e a ferramenta de automação Make, e para verificar o status da API, execute os seguintes comandos em ordem: make up # build + start the whole stack in Docker:
# api, web, postgres, meilisearch, redis, s3
curl localhost:8080/health
curl localhost:8080/api/v1/jobs

Repositório: https://github.com/strelov1/freehire. Baseie-se nas instruções oficiais no arquivo README deste repositório para a instalação e execução.

Antes de começar, verifique em qual sistema operacional estamos e se as ferramentas necessárias (ex: Python, Node.js, Git, Docker) estão instaladas. Instale as que faltarem passo a passo de acordo com este sistema.

Crie uma pasta nova e vazia para trabalhar. Não toque em arquivos fora desta pasta e não exclua nada. Antes de executar cada comando, diga o que você vai fazer em uma frase.

Diga-me o que devo ver na tela ao final de cada etapa. Se ocorrer um erro, colarei a mensagem de erro para você exatamente como ela é, e vamos corrigi-la juntos.

## Termos relacionados do glossário

- [Localhost](https://trescout.com/pt/dictionary/localhost/)
- [API](https://trescout.com/pt/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Destina-se àqueles que desejam acompanhar anúncios de software e tecnologia diretamente nas páginas de carreira das próprias empresas, sem intermediários, ou executar seu próprio motor de busca de empregos independente.
- **Licença:** MIT

## Links

- [Repositório no GitHub →](https://github.com/strelov1/freehire)
- [Ler em turco →](https://trescout.com/discover/freehire/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-10-22: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. O texto de apresentação foi preparado com IA a partir da própria documentação do repositório e esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/freehire/
