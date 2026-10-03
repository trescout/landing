# Qu'est-ce que Bundler ?

Bundler (module bundler) est un outil de développement qui analyse les codes sources (JavaScript, TypeScript, CSS, HTML, ressources graphiques et de polices) et les dépendances de bibliothèques externes divisées en centaines de parties indépendantes dans l'écosystème moderne de développement Web et logiciel, et transforme ces actifs en packages de fichiers optimisés (bundles) que les navigateurs peuvent exécuter de la manière la plus rapide et la plus efficace.

## Que signifie Bundler et pourquoi est-il apparu ?
Dans les premières années du Web, les sites se composaient de quelques balises <script> ajoutées séquentiellement dans le HTML. Mais à mesure que les applications Web sont devenues aussi complexes que les logiciels de bureau et se sont transformées en bases de code massives composées de milliers de modules, de sérieux obstacles structurels sont apparus :

## Comment fonctionne le bundler ? L'architecture en profondeur
Le fonctionnement d’un emballeur moderne se compose essentiellement de trois étapes :

## Techniques d'optimisation critiques

## Comparaison de l'écosystème des emballeurs
Les principaux outils qui répondent aux différents besoins de l'écosystème Web sont :

## Questions fréquentes
**Qu'est-ce que Bundler et pourquoi est-il essentiel dans le développement Web moderne ?**
Regroupeur ; Il s'agit d'un outil qui convertit des centaines de fichiers sources modulaires, d'images et de fichiers de style écrits par le développeur en packages que le navigateur peut traiter de manière unique et optimisée. Il est considéré comme obligatoire dans les projets modernes pour l'optimisation de la taille des fichiers, la réduction des requêtes réseau et la compatibilité des navigateurs.

**Quelle est la principale différence entre Webpack et Vite ?**
Webpack compile également l'intégralité du projet dans l'environnement de développement et crée un seul package en mémoire ; À mesure que le projet grandit, le temps de démarrage augmente. Vite, d'autre part, utilise le support natif du module ES (Native ESM) du navigateur dans l'environnement de développement et compile les fichiers uniquement lorsque le navigateur les demande, de sorte qu'ils soient ouverts instantanément, quelle que soit la taille du projet.

**Qu'est-ce que le tremblement d'arbre et pourquoi cela ne fonctionne-t-il que dans les modules ES ?**
Le Tree-Shaking consiste à supprimer du package final des fonctions et des blocs de code qui ne sont jamais utilisés dans le projet. Cela ne peut être fait en toute sécurité qu'au format ESM avec une syntaxe statique telle que l'importation et l'exportation ; L'analyse complète des codes CommonJS (require()) appelables dynamiquement n'est pas possible pendant la phase de compilation.

**Quelle est la différence entre Transpiler (Babel, SWC) et Bundler ?**
Transpiler convertit simplement la syntaxe du code (par exemple, il traduit le code TypeScript ou ES6+ moderne en ES5). Bundler combine ces fichiers indépendants convertis en résolvant les relations de dépendance entre eux et les regroupe sous un même toit.

**À quoi sert le fractionnement de code ?**
Il permet de diviser le code de l'application en fichiers fragmentés au lieu d'un seul gros fichier. L'utilisateur télécharge uniquement le code de la page qu'il consulte actuellement, ce qui réduit considérablement le temps de chargement initial et améliore l'expérience utilisateur.


## Termes liés
- [Bundling](/fr/dictionary/bundling/)
- [Compilation](/fr/dictionary/compilation/)
- [Frontend Stack](/fr/dictionary/frontend-stack/)
- [Runtime](/fr/dictionary/runtime/)

## Outils liés
- [Webpack](/fr/discover/webpack/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/bundler/
