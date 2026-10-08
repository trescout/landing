# Apporter une expertise aux agents de codage IA

Développée pour Claude Code et divers agents de codage, cette bibliothèque propose plus de 330 packages de compétences et plus de 70 commandes spéciales dans différents domaines de l'ingénierie au marketing. Cet ensemble d'outils basés sur Python fournit des scripts personnalisables pour standardiser les flux de travail basés sur l'IA et augmenter la productivité.

- ★ 27 840
- Python
- GitHub Trending · 2026-07-05

## Mises à jour

- **8 octobre 2026:** Étoiles 26,514 → 27,840, dernière version v2.12.0 (25 août 2026).
- **27 septembre 2026:** Étoiles 25,061 → 26,514, dernière version v2.12.0 (25 août 2026).
- **27 août 2026:** Étoiles 24,867 → 25,061, dernière version v2.12.0 (25 août 2026).
- **24 août 2026:** Étoiles 23,654 → 24,867, dernière version v2.9.0 (28 mai 2026).

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

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Activez les packages de compétences de cette bibliothèque pour Claude Code ou l'agent de codage que vous utilisez. Standardisez mon flux de travail et augmentez ma productivité à l'aide de scripts spécialisés dans des domaines tels que l'ingénierie, le marketing ou le conseil de niveau C. Intégrer les capacités spécifiques dont j'ai besoin (par exemple, audit de sécurité ou développement de produits) dans mon projet.

## Termes liés du glossaire

- [AI Skills](https://trescout.com/fr/dictionary/ai-skills/)
- [CLI](https://trescout.com/fr/dictionary/cli/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il s'adresse aux développeurs de logiciels et aux équipes techniques qui souhaitent utiliser les outils de codage basés sur l'intelligence artificielle de manière plus efficace et plus experte dans leurs flux de travail professionnels.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/alirezarezvani/claude-skills)
- [Lire en turc →](https://trescout.com/discover/claude-skills/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-07-05 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/claude-skills/
