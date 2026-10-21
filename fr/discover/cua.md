# Contrôle informatique pour les agents d'intelligence artificielle

CUA fournit une infrastructure open source pour les agents d'intelligence artificielle informatiques. Il rassemble un bac à sable, un kit de développement logiciel (SDK) et des outils de référence sous un même toit dans le but de former et d'évaluer les agents capables de contrôler les systèmes d'exploitation de bureau.

- ★ 30 501
- HTML
- GitHub Trending · 2026-06-16

## Mises à jour

- **21 octobre 2026:** Étoiles 30,335 → 30,501, dernière version cua-sdk-v0.6.0 (21 octobre 2026).
- **20 octobre 2026:** Étoiles 30,189 → 30,335, dernière version cua-spaces-v0.11.0 (20 octobre 2026).
- **19 octobre 2026:** Étoiles 30,064 → 30,189, dernière version agent-v0.9.1 (19 octobre 2026).
- **18 octobre 2026:** Étoiles 29,921 → 30,064, dernière version cua-spaces-v0.9.4 (18 octobre 2026).

## Ce que ça vous apporte

- Contrôler les applications de bureau en arrière-plan
- Bacs à sable isolés pour différents systèmes d'exploitation
- Outils d'analyse comparative pour mesurer les performances des agents

## Installation

**Installation du pilote (macOS/Linux)**

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/cua-driver/scripts/install.sh)"
```

**Installation du SDK bac à sable**

```
pip install cua
```

## Exécution

**Démarrage de la machine virtuelle macOS**

```
# Install Lume
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh)"

# Pull & start a macOS VM
lume run macos-sequoia-vanilla:latest
```

## Si vous ne codez pas

Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite développer un agent d'utilisation informatique utilisant l'infrastructure CUA. Aidez-moi à configurer la structure Python de base qui permettra à mon agent d'interagir avec les applications de bureau en arrière-plan, d'effectuer des clics de souris et d'envoyer des saisies au clavier. Créez un exemple d'esquisse de code qui exécute des commandes et prend des captures d'écran dans un environnement Linux à l'aide du SDK CUA Sandbox.

Dépôt : https://github.com/trycua/cua. Base-toi sur les instructions officielles du fichier README de ce dépôt pour l'installation et l'exécution.

Avant de commencer, vérifie quel système d'exploitation nous utilisons et si les outils nécessaires (ex: Python, Node.js, Git, Docker) sont installés. Installe ceux qui manquent étape par étape selon ce système.

Crée un nouveau dossier vide pour travailler. Ne touche pas aux fichiers en dehors de ce dossier et ne supprime rien. Avant chaque commande, décris ce que tu vas faire en une phrase.

Dis-moi ce que je devrais voir à l'écran à la fin de chaque étape. Si une erreur survient, je te copierai le message d'erreur tel quel et nous la corrigerons ensemble.

## Termes liés du glossaire

- [Benchmark](https://trescout.com/fr/dictionary/benchmark/)
- [Sandbox](https://trescout.com/fr/dictionary/sandbox/)
- [SDK](https://trescout.com/fr/dictionary/sdk/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il convient aux développeurs de logiciels et aux chercheurs qui développent des agents d'intelligence artificielle qui effectuent des tâches autonomes sur l'ordinateur.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/trycua/cua)
- [Lire en turc →](https://trescout.com/discover/cua/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-06-16 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Le texte de présentation a été préparé avec l’IA à partir de la propre documentation du dépôt et cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/cua/
