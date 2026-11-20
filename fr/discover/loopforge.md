# Flux de travail gérables pour vos agents de codage

Développé par Tencent, LoopForge est un outil de flux de travail auto-hébergé utilisé pour gérer les processus de livraison des agents de codage. Il prend en charge les processus d'assistance au codage local en orchestrant des logiciels tels que CodeBuddy, Codex et Claude Code avec des scripts et des mécanismes d'approbation humaine.

- ★ 5 104
- Go
- GitHub Trending · 2026-11-15

## Mises à jour

- **20 novembre 2026:** Étoiles 3,785 → 5,104, dernière version v0.4.0 (17 novembre 2026).
- **18 novembre 2026:** Étoiles 2,090 → 3,785, dernière version v0.4.0 (17 novembre 2026).
- **16 novembre 2026:** Étoiles 986 → 2,090, dernière version v0.3.8 (12 novembre 2026).
- **15 novembre 2026:** Étoiles 983 → 986, dernière version v0.3.8 (12 novembre 2026).

## Ce que ça vous apporte

- Exécute en toute sécurité des outils de codage par intelligence artificielle dans des environnements isolés (sandboxes).
- Garantit des livraisons répétables grâce à des processus standard et des étapes d'approbation humaine.
- Attribue des tâches à des rôles ou exécute des flux de travail étape par étape à partir de l'interface de discussion.

## Installation

**Clonage du dépôt et démarrage du système**

```
git clone https://github.com/Tencent/LoopForge.git
cd LoopForge
./start.sh
```

**Démarrage avec une source d'image alternative**

```
MIRROR=ghcr.nju.edu.cn ./start.sh
```

## Exécution

**Installation d'un assistant de codage dans le projet**

```
# Run inside your target project, e.g. for Claude Code
npx -y loopforge-cli@latest install claude
```

## Si vous ne codez pas

Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Pour pouvoir gérer mes processus de livraison avec des agents de codage sur mon propre serveur, je souhaite installer le système LoopForge. Tout d'abord, clonez le dépôt et démarrez le système en exécutant la série de commandes `git clone https://github.com/Tencent/LoopForge.git
cd LoopForge
./start.sh`. Si vous rencontrez des blocages lors du téléchargement, utilisez la commande `MIRROR=ghcr.nju.edu.cn ./start.sh` pour récupérer les images depuis le serveur alternatif et terminer le démarrage. Pour installer l'assistant de codage au sein de votre projet cible, exécutez la commande `# Run inside your target project, e.g. for Claude Code
npx -y loopforge-cli@latest install claude`.

Dépôt : https://github.com/Tencent/LoopForge. Base-toi sur les instructions officielles du fichier README de ce dépôt pour l'installation et l'exécution.

Avant de commencer, vérifie quel système d'exploitation nous utilisons et si les outils nécessaires (ex: Python, Node.js, Git, Docker) sont installés. Installe ceux qui manquent étape par étape selon ce système.

Crée un nouveau dossier vide pour travailler. Ne touche pas aux fichiers en dehors de ce dossier et ne supprime rien. Avant chaque commande, décris ce que tu vas faire en une phrase.

Dis-moi ce que je devrais voir à l'écran à la fin de chaque étape. Si une erreur survient, je te copierai le message d'erreur tel quel et nous la corrigerons ensemble.

## Termes liés du glossaire

- [Self-hosted](https://trescout.com/fr/dictionary/self-hosted/)
- [Clone](https://trescout.com/fr/dictionary/clone/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Convient aux équipes qui souhaitent gérer des agents de codage alimentés par l'intelligence artificielle sur leur propre infrastructure, avec une approbation humaine et des flux de travail standard.

## Liens

- [Dépôt GitHub →](https://github.com/Tencent/LoopForge)
- [Lire en turc →](https://trescout.com/discover/loopforge/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-11-15 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Le texte de présentation a été préparé avec l’IA à partir de la propre documentation du dépôt et cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/loopforge/
