# Qu'est-ce que Emitter ?

*Glossaire · Dev · Dernière mise à jour : 19 septembre 2026*

Emitter est un terme critique qui apparaît dans deux domaines fondamentaux du génie logiciel : le mécanisme qui annonce les changements d'état aux écouteurs dans les architectures événementielles (Event Emitter) et le module de génération de code (Code Emitter) qui convertit le code analysé en langage machine cible ou en bytecode dans la technologie de compilateur (Compiler).

## Origines conceptuelles : De la physique à l'architecture logicielle

Le mot « émetteur » dérive du verbe latin émettre, signifiant « jeter, libérer ». En électronique, les cathodes qui émettent des électrons ou en télécommunications, les émetteurs radio qui émettent des signaux sont appelés émetteurs. Le monde du logiciel a emprunté ce terme pour désigner « une ressource qui transfère une situation qui se produit en elle-même ou un résultat qu'elle produit vers le monde extérieur ».

Dans les logiciels, « émetteur » n'est pas une structure unique, mais représente deux immenses disciplines selon le contexte dans lequel il est utilisé : les flux d'événements et la conception du compilateur.

***Analogie :** Émetteur d'événements : bouton d'alarme incendie. Lorsque le bouton est enfoncé (émettre), le bouton ne sait pas combien de personnes se trouvent dans le bâtiment et quelles sirènes sonnent ; Il émet uniquement un signal et tous les systèmes d'alarme connectés (auditeurs) sont activés. Émetteur de code : C'est l'ingénieur en chef qui prend les plans techniques détaillés (AST) dessinés par un architecte et les transforme en instructions de coffrage et de ferraillage que les maîtres de chantier peuvent directement appliquer.*

## 1. Architecture basée sur les événements et émetteur d'événements

Dans la programmation basée sur les événements, Emitter est au cœur des modèles de conception Observer et Publish-Subscribe. Il permet aux composants du système de communiquer via des événements (couplage lâche) plutôt que de se reconnaître directement (couplage étroit).

La structure d'E/S réactive et asynchrone de Node.js est basée sur la classe EventEmitter au sein du module d'événements :

**émettre (événement, [...args]):** Déclenche l'événement avec le nom spécifié et alerte tous les auditeurs enregistrés.

**on(événement, auditeur):** Enregistre la fonction de rappel qui s'exécutera lorsque l'événement spécifié se produira.

**une fois(événement, auditeur):** Il capture l'événement une seule fois lorsqu'il se produit pour la première fois, puis supprime automatiquement l'enregistrement.

**Détail technique important :** Contrairement à la croyance populaire, Node.js EventEmitter exécute par défaut les écouteurs d'événements de manière synchrone. Si un auditeur bloque, les auditeurs suivants attendent. Pour l'exécution asynchrone, setImmediate() ou process.nextTick() est utilisé.

L'erreur la plus courante dans l'architecture Event Emitter est de ne pas supprimer les écouteurs (removeListener ou off) des objets dont le cycle de vie est terminé. Cela empêche les objets d'être nettoyés par Garbage Collector et provoque un avertissement MaxListenersExceededWarning dans Node.js.

## 2. Émetteur de code dans l'architecture du compilateur

La dernière et la plus cruciale étape d'un compilateur ou d'un transpilateur est la couche émetteur (générateur de code). La chaîne de compilation fonctionne dans cet ordre : Code source → Lexer (Tokens) → Analyseur (Arbre syntaxique - AST) → Analyse sémantique → Optimisation → Émetteur → Code cible

L'émetteur parcourt (généralement avec un modèle de visiteur) l'arbre de syntaxe abstraite (AST) optimisé ou la représentation intermédiaire (IR). Il distille chaque nœud en instructions que la plate-forme cible comprend : cette sortie peut être un langage machine brut (x86/ARM Assembly), un bytecode de machine virtuelle (JVM, V8 Bytecode) ou un autre langage de haut niveau (tel que la compilation TypeScript vers JavaScript).

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

- [Parser](https://trescout.com/fr/dictionary/parser/)
- [Compiler](https://trescout.com/fr/dictionary/compiler/)
- [Runtime](https://trescout.com/fr/dictionary/runtime/)
- [Assembly](https://trescout.com/fr/dictionary/assembly/)
- [API](https://trescout.com/fr/dictionary/api/)
- [Bundler](https://trescout.com/fr/dictionary/bundler/)

## Outils liés

- [YAML Cpp](https://trescout.com/fr/discover/yaml-cpp/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/emitter/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/emitter/
