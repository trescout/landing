# Qu'est-ce que Skill ?

*Glossaire · AI · Dernière mise à jour : 22 septembre 2026*

Une compétence (skill en anglais), dans sa correspondance turque, est une unité définie qui permet à un assistant d'intelligence artificielle d'accomplir des tâches à l'aide d'un outil externe.

## Définition et origine du mot

La conversation générale de l'assistant ne suffit pas ; il doit parfois lire des fichiers ou effectuer des recherches. Chacune de ces fonctions spécifiques est définie comme une compétence. Le concept est passé de l'ère des assistants vocaux à celle des agents : des compétences d'Alexa aux capacités des agents d'aujourd'hui.

***Analogie :** C'est comme les différents outils dans les mains d'un chef cuisinier ; le chef est unique et choisit le bon outil pour chaque tâche.*

## Comment connaître et utiliser dans la vie quotidienne ?

**Fichier :** Lecture et résumé de documents.
**Calendrier :** Planification de réunions.
**Recherche :** Récupération d'informations actualisées.

## Profondeur technique et architecture

Une compétence est écrite en trois parties :

**Nom :** Le nom court que le modèle appellera.
**Description :** Description du moment où il faut l'utiliser. Le modèle fait son choix en se basant sur cela.
**Schéma des paramètres :** Format d'entrée.

Exemple de définition :

```
{
  "name": "hava-durumu",
  "description": "Belirtilen şehrin güncel havasını verir",
  "parameters": { "sehir": "string" }
}
```

Flux : L'utilisateur formule une demande, le modèle sélectionne la compétence appropriée, remplit le paramètre, l'outil s'exécute, et le résultat est renvoyé au modèle. Pour les compétences dotées de privilèges d'écriture, l'approbation de l'utilisateur est requise.

## Choses fréquemment mélangées

On pense souvent qu'il s'agit d'une capacité générale du modèle. Pourtant, ce qui est visé ici, c'est la capacité de l'assistant à utiliser un outil externe. Le modèle comprend la langue, la compétence s'occupe de la tâche.

## Utilisation dans différentes disciplines

**Cuisine :** Le couteau et les techniques de sauce entre les mains du chef.
**Perceuse :** Fonction qui varie selon l'embout.
**Téléphone :** Chaque application installée.

## Foire aux questions

**Chaque modèle a-t-il une capacité ?**

Non. Les modèles de base génèrent du texte, la capacité est acquise lorsqu'un outil externe est ajouté à l'assistant.

**Comment développer les compétences ?**

Il est défini par une connexion API ou un bloc de code. La description est rédigée clairement, le modèle choisit correctement.

**Est-ce sécuritaire?**

Les capacités de lecture présentent un faible risque. Pour les opérations telles que l'écriture et le paiement, une validation et une limite de portée sont indispensables.

**Qui écrit les capacités ?**

Les développeurs les écrivent, les plates-formes les distribuent dans le store. Rédiger une bonne description représente la moitié du travail.

## Termes liés

- [AI Agent](https://trescout.com/fr/dictionary/ai-agent/)
- [AI Skill](https://trescout.com/fr/dictionary/ai-skills/)
- [Agent Skills](https://trescout.com/fr/dictionary/agent-skills/)
- [Tools](https://trescout.com/fr/dictionary/tools/)
- [AI Capabilities](https://trescout.com/fr/dictionary/ai-capabilities/)

## Outils liés

- [Anthropic Skills](https://trescout.com/fr/discover/anthropic-skills/)
- [Taste Skill](https://trescout.com/fr/discover/taste-skill/)
- [Archify](https://trescout.com/fr/discover/archify/)
- [Awesome Claude Skills](https://trescout.com/fr/discover/awesome-claude-skills/)
- [Last30days Skill](https://trescout.com/fr/discover/last30days-skill/)
- [I Have Adhd](https://trescout.com/fr/discover/i-have-adhd/)
- [Reverse Skill](https://trescout.com/fr/discover/reverse-skill/)
- [Book to Skill](https://trescout.com/fr/discover/book-to-skill/)

Cette explication a été rédigée en langage clair pour TreScout puis **traduite automatiquement** depuis l’original turc · la version turque fait foi. Si quelque chose vous semble erroné ou manquant, écrivez à [hello@trescout.com](mailto:hello@trescout.com). [Lire en turc →](https://trescout.com/dictionary/skill/)

---
Source : TreScout Glossaire · https://trescout.com/fr/dictionary/skill/
