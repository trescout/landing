# Qu'est-ce que Emitter ?

Emitter est un terme critique qui apparaît dans deux domaines fondamentaux du génie logiciel : le mécanisme qui annonce les changements d'état aux écouteurs dans les architectures événementielles (Event Emitter) et le module de génération de code (Code Emitter) qui convertit le code analysé en langage machine cible ou en bytecode dans la technologie de compilateur (Compiler).

## Origines conceptuelles : De la physique à l'architecture logicielle
Le mot « émetteur » dérive du verbe latin émettre, signifiant « jeter, libérer ». En électronique, les cathodes qui émettent des électrons ou en télécommunications, les émetteurs radio qui émettent des signaux sont appelés émetteurs. Le monde du logiciel a emprunté ce terme pour désigner « une ressource qui transfère une situation qui se produit en elle-même ou un résultat qu'elle produit vers le monde extérieur ».

## 1. Architecture basée sur les événements et émetteur d'événements
Dans la programmation basée sur les événements, Emitter est au cœur des modèles de conception Observer et Publish-Subscribe. Il permet aux composants du système de communiquer via des événements (couplage lâche) plutôt que de se reconnaître directement (couplage étroit).

## 2. Émetteur de code dans l'architecture du compilateur
La dernière et la plus cruciale étape d'un compilateur ou d'un transpilateur est la couche émetteur (générateur de code). La chaîne de compilation fonctionne dans cet ordre : Code source → Lexer (Tokens) → Analyseur (Arbre syntaxique - AST) → Analyse sémantique → Optimisation → Émetteur → Code cible

## Questions fréquentes
**Que signifie Emitter et quel est son équivalent turc ?**
Emitter signifie « émetteur » ou « émetteur » en anglais. Il est souvent utilisé comme « émetteur d'événements » dans les logiciels ou comme « émetteur de code » dans les compilateurs.

**Quel est le plus grand avantage de l’utilisation d’Event Emitter ?**
Il réduit à zéro la dépendance (couplage) entre les composants. Un module lance un événement ; Peu importe qui a commis l’incident, quand et comment. Cela augmente la modularité et la testabilité.

**Quel rôle Emitter joue-t-il dans les compilateurs ?**
C'est le composant final qui analyse le code source et produit la sortie cible (Assembly, code machine, bytecode ou code source converti) en prenant la structure arborescente optimisée (AST).

**Quelle est la différence entre RxJS Observable et Event Emitter ?**
L'émetteur d'événements effectue généralement des multidiffusions et est utilisé pour les notifications d'événements instantanées. RxJS Observable, quant à lui, offre le pouvoir de transformer des flux de données riches au fil du temps grâce à des opérateurs fonctionnels tels que le filtrage, le mappage et le retard.


## Termes liés
- [Parser](/fr/dictionary/parser/)
- [Compiler](/fr/dictionary/compiler/)
- [Runtime](/fr/dictionary/runtime/)
- [Assembly](/fr/dictionary/assembly/)
- [API](/fr/dictionary/api/)
- [Bundler](/fr/dictionary/bundler/)

## Outils liés
- [YAML Cpp](/fr/discover/yaml-cpp/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/emitter/
