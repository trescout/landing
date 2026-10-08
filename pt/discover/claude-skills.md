# Traga experiência para agentes de codificação de IA

Desenvolvida para Claude Code e diversos agentes de codificação, esta biblioteca oferece mais de 330 pacotes de habilidades e mais de 70 comandos especiais em diferentes áreas, da engenharia ao marketing. Este conjunto de ferramentas baseado em Python fornece scripts personalizáveis ​​para padronizar fluxos de trabalho baseados em IA e aumentar a produtividade.

- ★ 27.840
- Python
- GitHub Trending · 2026-07-05

## Atualizações

- **8 de outubro de 2026:** Estrelas 26,514 → 27,840, versão mais recente v2.12.0 (25 de agosto de 2026).
- **27 de setembro de 2026:** Estrelas 25,061 → 26,514, versão mais recente v2.12.0 (25 de agosto de 2026).
- **27 de agosto de 2026:** Estrelas 24,867 → 25,061, versão mais recente v2.12.0 (25 de agosto de 2026).
- **24 de agosto de 2026:** Estrelas 23,654 → 24,867, versão mais recente v2.9.0 (28 de maio de 2026).

## O que você ganha

- Mais de 350 pacotes de habilidades prontos
- Ampla experiência da engenharia ao marketing
- Compatível com 13 ferramentas de codificação diferentes

## Instalação

**Instalação CLI do Gemini**

```
# Clone the repository
git clone https://github.com/alirezarezvani/claude-skills.git
cd claude-skills

# Run the setup script
./scripts/gemini-install.sh

# Start using skills
> activate_skill(name="senior-architect")
```

**Instalação do OpenClaw**

```
bash <(curl -s https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/scripts/openclaw-install.sh)
```

## Execução

**Converter recursos para cursor**

```
# 1. Convert all skills to all tools (takes ~15 seconds)
./scripts/convert.sh --tool all

# 2. Install into your project (with confirmation)
./scripts/install.sh --tool cursor --target /path/to/project

# Or use --force to skip confirmation:
./scripts/install.sh --tool aider --target . --force

# 3. Verify
find .cursor/rules -name "*.mdc" | wc -l  # Should show 346
```

## Se você não programa

🤖 Cole isto no seu agente (Claude Code · Codex · Antigravity)

Ative os pacotes de habilidades nesta biblioteca para Claude Code ou o agente de codificação que você usa. Padronize meu fluxo de trabalho e aumente minha produtividade usando scripts especializados em áreas como engenharia, marketing ou consultoria de nível C. Integre os recursos específicos necessários (por exemplo, auditoria de segurança ou desenvolvimento de produtos) ao meu projeto.

## Termos relacionados do glossário

- [AI Skills](https://trescout.com/pt/dictionary/ai-skills/)
- [CLI](https://trescout.com/pt/dictionary/cli/)
- [Artificial Intelligence](https://trescout.com/pt/dictionary/artificial-intelligence/)

- **Para quem é:** Destina-se a desenvolvedores de software e equipes técnicas que desejam usar ferramentas de codificação suportadas por inteligência artificial de forma mais eficiente e especializada em seus fluxos de trabalho profissionais.
- **Licença:** MIT

## Links

- [Repositório no GitHub →](https://github.com/alirezarezvani/claude-skills)
- [Ler em turco →](https://trescout.com/discover/claude-skills/)

A TreScout não desenvolveu esta ferramenta · nós a encontramos nas tendências do GitHub e a apresentamos. Esta página descreve o repositório em 2026-07-05: A contagem de estrelas e o nosso texto são daquele dia, o repositório pode ter mudado desde então. Consulte o link do repositório para ver o estado atual. Esta página foi **traduzida automaticamente** do original em turco · a versão turca é a que vale.

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/claude-skills/
