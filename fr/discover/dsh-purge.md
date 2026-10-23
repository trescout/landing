# Tests de sécurité pour les modèles d'intelligence artificielle

YuJunZhiXue/dsh-purge est un outil JavaScript visant à contourner les restrictions de sécurité (jailbreak) à l'aide d'invites (prompts) personnalisables pour différents modèles d'IA. Le projet permet aux utilisateurs de définir leurs propres invites pour divers modèles et se concentre par défaut sur les modèles locaux.

- ★ 6 492
- JavaScript
- GitHub Trending · 2026-10-19

## Mises à jour

- **23 octobre 2026:** Étoiles 10,161 → 6,492, dernière version v1.1.73 (23 octobre 2026).
- **20 octobre 2026:** Étoiles 7,527 → 10,161, dernière version v1.1.71 (11 octobre 2026).
- **19 octobre 2026:** Étoiles 7,496 → 7,527, dernière version v1.1.71 (11 octobre 2026).

## Ce que ça vous apporte

- Vous pouvez tester localement les règles de sécurité et de modération sur l'environnement d'exécution d'IA DeepSeek Harness.
- Vous pouvez examiner directement les réponses du modèle et les filtres système en définissant des invites personnalisées pour différents modèles.
- Vous pouvez gérer les correctifs système appliqués via l'interface développeur et revenir à l'état antérieur à tout moment.

## Installation

**Clonage du dépôt dans le répertoire des extensions**

```
git clone https://github.com/YuJunZhiXue/dsh-purge.git "$DSH_HOME/plugins/dsh-purge"
```

**Passer au répertoire de profil correspondant et installer les dépendances**

```
cd "$DSH_HOME/profiles/web"   # 或 profiles/desktop
pnpm install
```

## Exécution

**Validation de la syntaxe du code**

```
node --check lib/index.js
node --check lib/core.js
node --check lib/rewind.js
node --check lib/skills.js
node --check client.js
```

## Si vous ne codez pas

Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Afin d'effectuer une évaluation de sécurité sur l'environnement d'exécution d'IA DeepSeek Harness, je souhaite installer et valider le plugin dsh-purge. Tout d'abord, exécutez la commande git clone https://github.com/YuJunZhiXue/dsh-purge.git "$DSH_HOME/plugins/dsh-purge" pour télécharger le dépôt avec le logiciel de contrôle de version Git. Ensuite, réalisez l'étape cd "$DSH_HOME/profiles/web" # 或 profiles/desktop
pnpm install pour installer les dépendances du profil avec le gestionnaire de paquets pnpm. Enfin, exécutez la commande node --check lib/index.js
node --check lib/core.js
node --check lib/rewind.js
node --check lib/skills.js
node --check client.js afin de vérifier les fichiers avec l'environnement d'exécution JavaScript Node.js.

Dépôt : https://github.com/YuJunZhiXue/dsh-purge. Base-toi sur les instructions officielles du fichier README de ce dépôt pour l'installation et l'exécution.

Avant de commencer, vérifie quel système d'exploitation nous utilisons et si les outils nécessaires (ex: Python, Node.js, Git, Docker) sont installés. Installe ceux qui manquent étape par étape selon ce système.

Crée un nouveau dossier vide pour travailler. Ne touche pas aux fichiers en dehors de ce dossier et ne supprime rien. Avant chaque commande, décris ce que tu vas faire en une phrase.

Dis-moi ce que je devrais voir à l'écran à la fin de chaque étape. Si une erreur survient, je te copierai le message d'erreur tel quel et nous la corrigerons ensemble.

## Termes liés du glossaire

- [Jailbreak](https://trescout.com/fr/dictionary/jailbreak/)
- [Harness](https://trescout.com/fr/dictionary/harness/)
- [Clone](https://trescout.com/fr/dictionary/clone/)
- [AI Skills](https://trescout.com/fr/dictionary/ai-skills/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Destiné aux chercheurs souhaitant vérifier les limites de sécurité et les filtres système des modèles d'intelligence artificielle dans leur propre environnement local.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/YuJunZhiXue/dsh-purge)
- [Lire en turc →](https://trescout.com/discover/dsh-purge/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-10-19 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Le texte de présentation a été préparé avec l’IA à partir de la propre documentation du dépôt et cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/dsh-purge/
