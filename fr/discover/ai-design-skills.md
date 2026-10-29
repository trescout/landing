# Règles de design prêtes pour les assistants de codage

elayadesign/ai-design-skills propose une collection de compétences en design composée d'un fichier de règles au format markdown que les outils de codage par IA (Claude Code, Cursor, Codex, Windsurf) peuvent lire. Ce projet fournit une ressource de référence pour les outils assistés par IA afin de standardiser les processus de design.

- ★ 11 349
- GitHub Trending · 2026-10-28

## Mises à jour

- **29 octobre 2026:** Étoiles 9,826 → 11,349.

## Ce que ça vous apporte

- Permet aux outils d'IA de générer des pages d'atterrissage et des systèmes visuels conformes à partir de zéro
- Rassemble les normes de design telles que la typographie, les couleurs, l'espacement et l'animation dans un seul fichier
- Permet aux assistants de codage d'écrire des interfaces plus cohérentes grâce à des règles spécifiques au projet

## Installation

**Ajouter au dossier de règles de Claude Code**

```
mkdir -p .claude/skills
git clone https://github.com/elayadesign/ai-design-skills.git /tmp/ai-design-skills
cp -r /tmp/ai-design-skills/skills/<skill-name> .claude/skills/
```

**Installer pour l'éditeur de code IA Cursor**

```
mkdir -p .cursor/rules
curl -o .cursor/rules/<skill-name>.md \
  https://raw.githubusercontent.com/elayadesign/ai-design-skills/main/skills/<skill-name>/SKILL.md
```

## Si vous ne codez pas

Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite enseigner mes règles de design à mon outil de codage par intelligence artificielle. Pour télécharger le fichier de règles nécessaire pour l'éditeur de code Cursor, veuillez exécuter tour à tour les commandes suivantes : `mkdir -p .cursor/rules` puis `curl -o .cursor/rules/\<skill-name>.md \
https://raw.githubusercontent.com/elayadesign/ai-design-skills/main/skills/\<skill-name>/SKILL.md`. N'oubliez pas de remplacer `\<skill-name>` par la règle que nous souhaitons télécharger, à savoir `landing-page-design`.

Dépôt : https://github.com/elayadesign/ai-design-skills. Base-toi sur les instructions officielles du fichier README de ce dépôt pour l'installation et l'exécution.

Avant de commencer, vérifie quel système d'exploitation nous utilisons et si les outils nécessaires (ex: Python, Node.js, Git, Docker) sont installés. Installe ceux qui manquent étape par étape selon ce système.

Crée un nouveau dossier vide pour travailler. Ne touche pas aux fichiers en dehors de ce dossier et ne supprime rien. Avant chaque commande, décris ce que tu vas faire en une phrase.

Dis-moi ce que je devrais voir à l'écran à la fin de chaque étape. Si une erreur survient, je te copierai le message d'erreur tel quel et nous la corrigerons ensemble.

## Termes liés du glossaire

- [Skill](https://trescout.com/fr/dictionary/skill/)
- [Markdown](https://trescout.com/fr/dictionary/markdown/)
- [AI Skills](https://trescout.com/fr/dictionary/ai-skills/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il s'adresse aux propriétaires de produits et aux développeurs qui souhaitent créer des interfaces web esthétiques et cohérentes à l'aide d'éditeurs de code alimentés par l'intelligence artificielle.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/elayadesign/ai-design-skills)
- [Lire en turc →](https://trescout.com/discover/ai-design-skills/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-10-28 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Le texte de présentation a été préparé avec l’IA à partir de la propre documentation du dépôt et cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/ai-design-skills/
