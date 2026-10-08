# Qu'est-ce que Clean Code ?

*Glossaire · Dev · Dernière mise à jour : 22 septembre 2026*

Le code propre est le code qui peut être lu par les humains.

## Définition et origine du mot

La machine exécute tous les codes, un humain ne peut pas lire tous les codes. Un nom significatif, une petite fonction et un flux simple apportent de la lisibilité. Robert Martin est le nom de référence de cette discipline.

***Analogie :** C'est comme si les étagères d'une bibliothèque étaient classées par genre et par auteur.*

## Comment connaître et utiliser dans la vie quotidienne ?

**Équipe:** Base de code commune.
**Examen :** Contrôle de lisibilité.
**Soins:** Revenir à l'ancien code.

## Profondeur technique et architecture

Principes :

**Nom:** Le nom qui exprime l'intention.
**Dimension:** Fonction d'emploi unique.
**Encore:** La pièce commune est au même endroit.

Exemple :

```
# önce
def h(a, b):
    return a + a*b
# sonra
def indirimli_fiyat(fiyat, oran):
    return fiyat + fiyat * oran
```

Règle : exécuter du code est la première étape, lire le code est la deuxième étape.

## Utilisation dans différentes disciplines

**Tableau:** Espace de travail bien rangé.
**Étagères:** Classés par genre et auteur.
**Jardin:** Disposition des branches taillées.

## Foire aux questions

**N'est-ce pas suffisant de travailler ?**

Ce n'est pas suffisant. Le code de travail enregistre aujourd'hui, le code lu enregistre demain.

**Est-ce que cela ralentit ?**

Au début oui, en maintenance non. Cela rapporte de l’argent au total.

**Comment se mesure-t-il ?**

Avec temps de révision et taux d’erreur. Le nombre seul ne suffit pas.

**Par où commencer ?**

Du nom et de la fonction. Le code touché est effacé.

## Termes liés

- [Refactoring](https://trescout.com/fr/dictionary/refactoring/)
- [Unit Testing](https://trescout.com/fr/dictionary/unit-testing/)
- [Engineering Skills](https://trescout.com/fr/dictionary/engineering-skills/)

## Outils liés

- [Clean Code Javascript](https://trescout.com/fr/discover/clean-code-javascript/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/clean-code/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/clean-code/
