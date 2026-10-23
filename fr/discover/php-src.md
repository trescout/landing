# Langage de script pour les sites Web

PHP est utilisé comme un langage de script généraliste, spécialement conçu pour les processus de développement web. Écrit en C, cet interpréteur alimente de nombreux sites Web à travers le monde.

- ★ 41 410
- C
- GitHub Trending · 2026-10-23

## Mises à jour

- **23 octobre 2026:** Étoiles 41,391 → 41,410, dernière version php-8.5.12 (21 octobre 2026).

## Ce que ça vous apporte

- Vous permet d'exécuter des sites Web dynamiques et des applications web.
- Offre la possibilité de tester la version la plus récente en la compilant directement à partir du code source.
- Vous aide à mesurer la stabilité du système grâce à des outils de test intégrés et complets.

## Installation

**Installer les outils de compilation pour Ubuntu**

```
sudo apt install -y pkg-config build-essential autoconf bison re2c libxml2-dev libsqlite3-dev
```

**Installer les outils de compilation pour Fedora**

```
sudo dnf install re2c bison autoconf make ccache libxml2-devel sqlite-devel
```

## Exécution

**Compiler le code source**

```
make -j4
```

**Exécutez les tests**

```
make TEST_PHP_ARGS=-j4 test
```

## Si vous ne codez pas

Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite compiler l'interpréteur PHP à partir du code source et le tester. Si j'utilise Ubuntu, exécutez la commande sudo apt install -y pkg-config build-essential autoconf bison re2c libxml2-dev libsqlite3-dev pour installer les outils de compilation nécessaires via le gestionnaire de paquets. Si j'utilise Fedora, utilisez la commande sudo dnf install re2c bison autoconf make ccache libxml2-devel sqlite-devel, et si j'utilise macOS, utilisez la commande brew install autoconf bison re2c libiconv libxml2 sqlite avec le gestionnaire de paquets Homebrew. Ensuite, exécutez la commande make -j4 pour compiler le projet. Une fois la compilation terminée, appliquez la commande make TEST_PHP_ARGS=-j4 test pour exécuter les tests simultanément, ou la commande make TESTS=tests/lang/ pour exécuter les tests de langage.

Dépôt : https://github.com/php/php-src. Base-toi sur les instructions officielles du fichier README de ce dépôt pour l'installation et l'exécution.

Avant de commencer, vérifie quel système d'exploitation nous utilisons et si les outils nécessaires (ex: Python, Node.js, Git, Docker) sont installés. Installe ceux qui manquent étape par étape selon ce système.

Crée un nouveau dossier vide pour travailler. Ne touche pas aux fichiers en dehors de ce dossier et ne supprime rien. Avant chaque commande, décris ce que tu vas faire en une phrase.

Dis-moi ce que je devrais voir à l'écran à la fin de chaque étape. Si une erreur survient, je te copierai le message d'erreur tel quel et nous la corrigerons ensemble.

## Termes liés du glossaire

- [Scripting Language](https://trescout.com/fr/dictionary/scripting-language/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Destiné aux développeurs qui créent des applications web et à ceux qui souhaitent analyser le code source du noyau PHP et le compiler directement à partir de la source.
- **Licence:** BSD-3-Clause

## Liens

- [Dépôt GitHub →](https://github.com/php/php-src)
- [Lire en turc →](https://trescout.com/discover/php-src/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-10-23 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Le texte de présentation a été préparé avec l’IA à partir de la propre documentation du dépôt et cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/php-src/
