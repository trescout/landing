# Teste de segurança para modelos de inteligência artificial

YuJunZhiXue/dsh-purge é uma ferramenta JavaScript que visa contornar restrições de segurança (jailbreak) usando prompts personalizáveis para diferentes modelos de IA. O projeto permite que os usuários definam seus próprios comandos para diferentes modelos e foquem, por padrão, em modelos locais.

- ★ 7.527
- JavaScript
- GitHub Trending · 2026-10-19

## Atualizações

- **19 de outubro de 2026:** Estrelas 7,496 → 7,527, versão mais recente v1.1.71 (11 de outubro de 2026).

## O que você ganha

- Você pode testar as regras de segurança e auditoria no ambiente de execução de IA DeepSeek Harness em um ambiente local.
- Ao definir prompts personalizados para diferentes modelos, você pode examinar diretamente as respostas do modelo e os filtros do sistema.
- Você pode gerenciar patches de sistema feitos através da interface do desenvolvedor e reverter para o estado anterior a qualquer momento.

## Instalação

**Clonar o repositório para o diretório de extensões**

```
git clone https://github.com/YuJunZhiXue/dsh-purge.git "$DSH_HOME/plugins/dsh-purge"
```

**Acessar o diretório de perfil correspondente e as dependências**

```
cd "$DSH_HOME/profiles/web"   # 或 profiles/desktop
pnpm install
```

## Execução

**Validar a sintaxe do código**

```
node --check lib/index.js
node --check lib/core.js
node --check lib/rewind.js
node --check lib/skills.js
node --check client.js
```

## Se você não programa

Cole isto no seu agente (Claude Code · Codex · Antigravity)

Para realizar uma avaliação de segurança no ambiente de execução de inteligência artificial DeepSeek Harness, desejo instalar e validar o plugin dsh-purge. Primeiro, execute o comando git clone https://github.com/YuJunZhiXue/dsh-purge.git "$DSH_HOME/plugins/dsh-purge" para baixar o repositório com o software de controle de versão Git. Em seguida, complete a etapa de instalação das dependências do perfil com o gerenciador de pacotes pnpm usando cd "$DSH_HOME/profiles/web" # ou profiles/desktop
pnpm install. Como última etapa, execute o comando node --check lib/index.js
node --check lib/core.js
node --check lib/rewind.js
node --check lib/skills.js
node --check client.js com o ambiente de execução JavaScript Node.js para verificar os arquivos.

Repositório: https://github.com/YuJunZhiXue/dsh-purge. Baseie-se nas instruções oficiais no arquivo README deste repositório para a instalação e execução.

Antes de começar, verifique em qual sistema operacional estamos e se as ferramentas necessárias (ex: Python, Node.js, Git, Docker) estão instaladas. Instale as que faltarem passo a passo de acordo com este sistema.

Crie uma pasta nova e vazia para trabalhar. Não toque em arquivos fora desta pasta e não exclua nada. Antes de executar cada comando, diga o que você vai fazer em uma frase.

Diga-me o que devo ver na tela ao final de cada etapa. Se ocorrer um erro, colarei a mensagem de erro para você exatamente como ela é, e vamos corrigi-la juntos.

## Termos relacionados do glossário

- [Jailbreak](https://trescout.com/pt/dictionary/jailbreak/)
- [Harness](https://trescout.com/pt/dictionary/harness/)
- [Clone](https://trescout.com/pt/dictionary/clone/)
- [AI Skills](https://trescout.com/pt/dictionary/ai-skills/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Destina-se a pesquisadores que desejam auditar os limites de segurança e os filtros de sistema de modelos de inteligência artificial em seu próprio ambiente local.
- **Licença:** MIT

## Links

- [Repositório no GitHub →](https://github.com/YuJunZhiXue/dsh-purge)
- [Ler em turco →](https://trescout.com/discover/dsh-purge/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-10-19: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. O texto de apresentação foi preparado com IA a partir da própria documentação do repositório e esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/dsh-purge/
