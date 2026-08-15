# Traga experiência para agentes de codificação de IA

Desenvolvida para Claude Code e diversos agentes de codificação, esta biblioteca oferece mais de 330 pacotes de habilidades e mais de 70 comandos especiais em diferentes áreas, da engenharia ao marketing. Este conjunto de ferramentas baseado em Python fornece scripts personalizáveis ​​para padronizar fluxos de trabalho baseados em IA e aumentar a produtividade.

- ★ 23.654
- Python
- GitHub Trending · 2026-07-05

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
Ative os pacotes de habilidades nesta biblioteca para Claude Code ou o agente de codificação que você usa. Padronize meu fluxo de trabalho e aumente minha produtividade usando scripts especializados em áreas como engenharia, marketing ou consultoria de nível C. Integre os recursos específicos necessários (por exemplo, auditoria de segurança ou desenvolvimento de produtos) ao meu projeto.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/claude-skills/
