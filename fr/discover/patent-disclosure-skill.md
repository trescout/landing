# Automatisez les descriptions d'inventions de brevets avec l'intelligence artificielle

Le Patent Disclosure Skill basé sur Python analyse les ébauches d'inventions techniques pour générer des descriptions techniques, des revendications (claims) et des comparaisons avec l'état de la technique (prior art) conformes aux formats de brevet officiels.

- ★ 10 360
- Python
- GitHub Trending · 2026-08-31

## Ce que ça vous apporte
- Génération de texte de brevet structuré : création des sections domaine technique, arrière-plan, résumé et description détaillée de l'invention conformément aux normes de brevet standard.
- Arbre de revendications indépendantes et dépendantes : formulation automatique de listes de revendications de brevet hiérarchisées maximisant la portée de la protection juridique.
- Analyse des écarts avec l'état de la technique (Prior Art) : mise en évidence claire des différences techniques et du degré d'inventivité entre les technologies existantes et l'invention.
- Accélération de la collaboration avec les conseils en brevets : économies de temps et d'argent en transformant les brouillons des ingénieurs en documents techniques rationalisés prêts pour les conseils en brevets.
- Prise en charge de la terminologie des brevets multilingues : conformité avec la terminologie anglaise, turque et celle des organismes internationaux de brevets (OMPI, OEB, USPTO).

## Installation
**Clonage du référentiel et installation des dépendances**

```
git clone https://github.com/handsomestWei/patent-disclosure-skill.git
cd patent-disclosure-skill
pip install -r requirements.txt
```


## Exécution
**Lancer l'analyse de brevet et la génération de divulgation**

```
python run_skill.py --input bulus_taslagi.txt --output patent_disclosure.md
```


## Architecture technique et principe de fonctionnement
- Moteur d'analyse d'inventions techniques : identifie les entrées, les sorties et la méthodologie clés dans les descriptions de logiciels, de matériel ou de procédés chimiques.
- Validateur de syntaxe de revendication : analyseur de langage juridique qui vérifie les expressions vagues et les erreurs formelles dans les revendications.
- Exportation de modèles et Markdown : Enregistrement du document au format Markdown divisé en sections standard pour une utilisation dans les dépôts de brevets officiels.

## Flux de travail d'analyse de brevets et préparation des revendications
- Convertir des algorithmes logiciels en un format brevetable : dériver des descriptions de méthodes et de systèmes acceptables par les autorités de brevets à partir de codes et de schémas d'architecture.
- Défense contre les Office Actions : rédaction de réponses listant les caractéristiques distinctives de l'invention pour contrer les objections des examinateurs de brevets.
- Audit du portefeuille de propriété intellectuelle : cartographie précoce des étapes inventives à potentiel de brevet des projets technologiques internes.

## Si vous ne codez pas
Je souhaite préparer un texte officiel de déclaration d'invention pour un algorithme de mise en cache de base de données distribuée que j'ai développé, en utilisant la compétence de divulgation de brevet (patent disclosure skill). Pourriez-vous m'expliquer étape par étape comment générer les revendications indépendantes, le domaine technique de l'invention et les différences par rapport à l'état de la technique en fournissant le flux de l'algorithme en entrée ?

## Questions fréquemment posées
- Cet outil remplace-t-il un conseil en brevets officiel ? Non. Patent Disclosure Skill est un outil de préparation et de productivité destiné aux ingénieurs pour structurer leurs projets d'invention et les préparer pour les conseils ; le dépôt juridique doit être effectué par un conseil.
- Avec quels modèles LLM fonctionne-t-il ? Il peut être configuré pour fonctionner avec Claude 3.5 Sonnet, GPT-4o ou des modèles locaux à poids ouverts (Qwen, Llama 3).
- Mes secrets techniques risquent-ils de fuiter sur Internet ? Lorsqu'ils sont exécutés avec un LLM local (Ollama ou vLLM), toutes les analyses de brevets sont effectuées entièrement sur votre ordinateur local et aucune donnée ne sort.
- Peut-il interpréter des dessins de brevets et des organigrammes ? Lorsqu'ils sont connectés à des modèles multimodaux, il peut également analyser l'architecture système et les schémas fonctionnels pour les transcrire en texte.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/patent-disclosure-skill/
