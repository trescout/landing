# Apporter une expertise aux agents de codage IA

Développée pour Claude Code et divers agents de codage, cette bibliothèque propose plus de 330 packages de compétences et plus de 70 commandes spéciales dans différents domaines de l'ingénierie au marketing. Cet ensemble d'outils basés sur Python fournit des scripts personnalisables pour standardiser les flux de travail basés sur l'IA et augmenter la productivité.

- ★ 24 867
- Python
- GitHub Trending · 2026-07-05

## Ce que ça vous apporte
- Plus de 350 packs de compétences prêts à l'emploi
- Une vaste expertise de l’ingénierie au marketing
- Compatible avec 13 outils de codage différents

## Installation
**Installation de la CLI Gemini**

```
# Clone the repository
git clone https://github.com/alirezarezvani/claude-skills.git
cd claude-skills

# Run the setup script
./scripts/gemini-install.sh

# Start using skills
> activate_skill(name="senior-architect")
```

**Installation d'OpenClaw**

```
bash <(curl -s https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/scripts/openclaw-install.sh)
```


## Exécution
**Capacités de conversion pour le curseur**

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


## Si vous ne codez pas
Activez les packages de compétences de cette bibliothèque pour Claude Code ou l'agent de codage que vous utilisez. Standardisez mon flux de travail et augmentez ma productivité à l'aide de scripts spécialisés dans des domaines tels que l'ingénierie, le marketing ou le conseil de niveau C. Intégrer les capacités spécifiques dont j'ai besoin (par exemple, audit de sécurité ou développement de produits) dans mon projet.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/claude-skills/
