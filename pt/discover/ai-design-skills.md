# Regras de design prontas para assistentes de programação

elayadesign/ai-design-skills oferece uma coleção de habilidades de design composta por um arquivo de regras em markdown que ferramentas de programação de inteligência artificial (Claude Code, Cursor, Codex, Windsurf) podem ler. Este projeto fornece um recurso orientativo para ferramentas impulsionadas por IA para padronizar os processos de design.

- ★ 11.349
- GitHub Trending · 2026-10-28

## Atualizações

- **29 de outubro de 2026:** Estrelas 9,826 → 11,349.

## O que você ganha

- Permite que ferramentas de inteligência artificial gerem páginas de destino e sistemas visuais compatíveis do zero
- Reúne padrões de design como tipografia, cor, espaçamento e animação em um único arquivo
- Possibilita que os assistentes de programação escrevam interfaces mais consistentes com regras específicas do projeto

## Instalação

**Adicionar à pasta de regras do Claude Code**

```
mkdir -p .claude/skills
git clone https://github.com/elayadesign/ai-design-skills.git /tmp/ai-design-skills
cp -r /tmp/ai-design-skills/skills/<skill-name> .claude/skills/
```

**Instalar para o editor de código com IA Cursor**

```
mkdir -p .cursor/rules
curl -o .cursor/rules/<skill-name>.md \
  https://raw.githubusercontent.com/elayadesign/ai-design-skills/main/skills/<skill-name>/SKILL.md
```

## Se você não programa

Cole isto no seu agente (Claude Code · Codex · Antigravity)

Quero ensinar as regras de design à minha ferramenta de codificação de inteligência artificial. Para baixar o arquivo de regras necessário para o editor de código Cursor, execute os seguintes comandos em ordem: `mkdir -p .cursor/rules` e, em seguida, `curl -o .cursor/rules/\<skill-name>.md \
https://raw.githubusercontent.com/elayadesign/ai-design-skills/main/skills/\<skill-name>/SKILL.md`. Não se esqueça de substituir a parte `\<skill-name>` aqui por `landing-page-design`, que é a regra que queremos baixar.

Repositório: https://github.com/elayadesign/ai-design-skills. Baseie-se nas instruções oficiais no arquivo README deste repositório para a instalação e execução.

Antes de começar, verifique em qual sistema operacional estamos e se as ferramentas necessárias (ex: Python, Node.js, Git, Docker) estão instaladas. Instale as que faltarem passo a passo de acordo com este sistema.

Crie uma pasta nova e vazia para trabalhar. Não toque em arquivos fora desta pasta e não exclua nada. Antes de executar cada comando, diga o que você vai fazer em uma frase.

Diga-me o que devo ver na tela ao final de cada etapa. Se ocorrer um erro, colarei a mensagem de erro para você exatamente como ela é, e vamos corrigi-la juntos.

## Termos relacionados do glossário

- [Skill](https://trescout.com/pt/dictionary/skill/)
- [Markdown](https://trescout.com/pt/dictionary/markdown/)
- [AI Skills](https://trescout.com/pt/dictionary/ai-skills/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Destina-se a proprietários de produtos e programadores que pretendem desenvolver interfaces web estéticas e consistentes com editores de código alimentados por inteligência artificial.
- **Licença:** MIT

## Links

- [Repositório no GitHub →](https://github.com/elayadesign/ai-design-skills)
- [Ler em turco →](https://trescout.com/discover/ai-design-skills/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-10-28: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. O texto de apresentação foi preparado com IA a partir da própria documentação do repositório e esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/ai-design-skills/
