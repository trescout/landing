# Software de acompanhamento de treino executado no seu próprio servidor

O OpenGym é uma ferramenta de gestão de ginásio de código aberto para planear rotinas de treino e acompanhar exercícios com peso corporal. Permitindo que os utilizadores alojuem os seus próprios dados no seu próprio servidor, este software suporta a importação de dados de aplicações de fitness populares (Strong, Hevy).

- ★ 15.063
- JavaScript
- GitHub Trending · 2026-10-05

## Atualizações

- **23 de outubro de 2026:** Estrelas 14,645 → 15,063, versão mais recente v1.4.2 (23 de outubro de 2026).
- **22 de outubro de 2026:** Estrelas 13,304 → 14,645, versão mais recente v1.4.1 (10 de outubro de 2026).
- **18 de outubro de 2026:** Estrelas 12,021 → 13,304, versão mais recente v1.4.1 (10 de outubro de 2026).
- **15 de outubro de 2026:** Estrelas 10,912 → 12,021, versão mais recente v1.4.1 (10 de outubro de 2026).

## O que você ganha

- Pode armazenar os seus dados de treino num espaço seguro controlado por si, em vez de em servidores de empresas terceiras.
- Pode importar facilmente os seus dados de exercícios anteriores de aplicações de fitness populares como o Strong e o Hevy.
- Pode planear e acompanhar os seus treinos a partir do seu telemóvel ou computador, mesmo sem ligação à Internet.

## Instalação

**Com a plataforma de gestão de contentores Docker, p**

```
git clone https://github.com/DuarteSantos8/openGym
cd openGym
cp .env.example .env
docker compose pull      # prebuilt images, amd64 + arm64 (skip this to build from source)
docker compose up -d
```

## Se você não programa

Cole isto no seu agente (Claude Code · Codex · Antigravity)

Gostaria de instalar o software de acompanhamento de treino openGym na plataforma de gestão de contentores Docker. Poderia explicar passo a passo os passos de instalação que começam com o comando 'git clone https://github.com/DuarteSantos8/openGym', como configurar o ficheiro de variáveis de ambiente '.env' e como aceder à aplicação a partir do navegador após a conclusão da instalação?

Repositório: https://github.com/DuarteSantos8/openGym. Baseie-se nas instruções oficiais no arquivo README deste repositório para a instalação e execução.

Antes de começar, verifique em qual sistema operacional estamos e se as ferramentas necessárias (ex: Python, Node.js, Git, Docker) estão instaladas. Instale as que faltarem passo a passo de acordo com este sistema.

Crie uma pasta nova e vazia para trabalhar. Não toque em arquivos fora desta pasta e não exclua nada. Antes de executar cada comando, diga o que você vai fazer em uma frase.

Se uma chave de API for necessária, não me peça para digitá-la no chat. Mostre-me como adicioná-la ao arquivo .env e garanta que este arquivo não seja enviado ao Git.

Diga-me o que devo ver na tela ao final de cada etapa. Se ocorrer um erro, colarei a mensagem de erro para você exatamente como ela é, e vamos corrigi-la juntos.

## Termos relacionados do glossário

- [Clone](https://trescout.com/pt/dictionary/clone/)
- [API](https://trescout.com/pt/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Destina-se a entusiastas do desporto que valorizam a privacidade dos dados de treino e querem acompanhar gratuitamente as suas rotinas de ginásio no seu próprio servidor.
- **Licença:** AGPL-3.0

## Links

- [Repositório no GitHub →](https://github.com/DuarteSantos8/openGym)
- [Ler em turco →](https://trescout.com/discover/opengym/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-10-05: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. O texto de apresentação foi preparado com IA a partir da própria documentação do repositório e esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/opengym/
