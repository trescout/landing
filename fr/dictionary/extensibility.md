# Qu'est-ce que Extensibility ?

*Glossaire · Dev · Dernière mise à jour : 22 septembre 2026*

L'extensibilité (ou extensibility en anglais) est la capacité d'un logiciel à acquérir de nouvelles fonctionnalités grâce à des extensions et des modules, sans modifier son code principal.

## Définition et origine du mot

Le terme « extensibilité » provient de la racine anglaise *extend* (étendre). En génie logiciel, il est étroitement lié au principe ouvert/fermé (Open-Closed Principle) : un module doit être ouvert à l'extension, mais fermé à la modification. En d'autres termes, lorsqu'une nouvelle fonctionnalité est requise, il suffit d'ajouter un nouveau composant au système plutôt que de perturber le code existant.

***Analogie :** C'est comme un couteau suisse ; le corps reste le même, vous pouvez y ajouter un nouveau tournevis ou un embout de lampe de poche.*

## Comment connaître et utiliser dans la vie quotidienne ?

En tant qu'utilisateur final, vous rencontrez l'extensibilité au quotidien :

**Extensions de navigateur :** L'installation d'un bloqueur de publicités ou d'un gestionnaire de mots de passe sur votre navigateur.
**Extensions d'éditeur :** L'ajout d'une extension Python ou Prettier dans VS Code.
**Systèmes de contenu :** d'installer un formulaire de contact ou un plugin de cache sur votre site WordPress.
**Outils de design :** de télécharger un pack de composants prêts à l'emploi depuis la communauté Figma.

## Profondeur technique et architecture

Le noyau d'un système extensible est petit, son environnement s'agrandit grâce aux extensions. Les parties typiques de cette architecture sont les suivantes :

**Interface de plugin (API de plugin) :** C'est la porte contrôlée que le noyau ouvre aux extensions. L'extension n'interagit avec le système que via cette interface.
**Système de crochets et d'événements (Hooks & Events) :** Le noyau diffuse des événements à des moments précis. Les extensions s'abonnent à ces événements.
**Fichier de notification (Manifeste) :** Chaque extension comporte un petit fichier indiquant son nom, sa version et les autorisations qu'elle demande. Le système ne charge pas une extension qui ne respecte pas les règles.
**Bac à sable (Sandbox) et autorisations :** L'accès des extensions est limité. Ainsi, une extension défectueuse ne peut pas faire planter l'ensemble du système.
**Compatibilité des versions :** Lors de la mise à jour du noyau, l'interface doit rester rétrocompatible. Sinon, les plugins risquent de ne plus fonctionner.

Voici un petit exemple, typique d'une déclaration de plugin :

```
{
  "name": "ornek-eklenti",
  "version": "1.0.0"
}
```

## Utilisation dans différentes disciplines

**Architecture :** Des structures préfabriquées où de nouveaux modules peuvent être ajoutés sans toucher aux murs porteurs.
**Production:** Des robots culinaires sur lesquels différents accessoires peuvent être fixés sur le même corps.
**Jeu:** Des communautés de modding qui ajoutent de nouvelles cartes et missions sans modifier le jeu de base.

## Foire aux questions

**Tous les logiciels sont-ils extensibles ?**

Non. Si le logiciel n'a pas été conçu avec cette souplesse dès le départ, ajouter par la suite un support pour les plugins s'avère généralement coûteux et risqué.

**Quelle est la différence entre un plugin et un fork (divergence) ?**

Avec un plugin, vous ne copiez pas le code principal, vous vous connectez au système de l'extérieur. Avec un fork, vous copiez l'intégralité du code et prenez une direction distincte.

**Les plugins sont-ils sûrs ?**

Cela dépend de la source. Préférez les plugins provenant de magasins officiels, à jour et largement utilisés. Méfiez-vous des plugins qui demandent des autorisations inutiles.

**L'extensibilité réduit-elle les performances ?**

Chaque extension apporte une certaine charge. Lorsque vous utilisez peu d'extensions et qu'elles sont bien entretenues, l'effet est généralement imperceptible.

## Termes liés

- [Plugin](https://trescout.com/fr/dictionary/plugin/)
- [API](https://trescout.com/fr/dictionary/api/)
- [Framework](https://trescout.com/fr/dictionary/framework/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/extensibility/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/extensibility/
