# Transformez votre PC en serveur IA local

Osmantic/ODS open source vous permet de configurer une inférence de modèle de langage étendu natif, des pipelines RAG basés sur la recherche vectorielle et des flux de travail d'agent autonomes exécutés sur votre matériel personnel.

- ★ 6 854
- Python
- GitHub Trending · 2026-08-31

## Mises à jour

- **27 septembre 2026:** Étoiles 5,181 → 6,854, dernière version v3.0.0 (24 septembre 2026).

## Ce que ça vous apporte

- Confidentialité totale des données et exécution locale : exécution sécurisée de l'IA sur le GPU et le CPU locaux sans envoyer vos données à des serveurs cloud externes.
- RAG (Search Aided Generation) intégré : Vectorisez vos notes personnelles, documents d'entreprise et référentiels de codes pour des recherches sémantiques instantanées.
- Capacités multimodales : Réunir la production de texte, la reconnaissance vocale (Whisper), la synthèse vocale et la production visuelle sous un même toit.
- API native compatible OpenAI : pointez vos clients et outils d'IA existants vers votre serveur ODS local avec une seule modification d'URL.
- Orchestration complète des agents : chaînes d'agents intelligentes qui appellent des outils locaux et résolvent des tâches en plusieurs étapes de manière autonome.

## Installation

**Clonage du référentiel et configuration de l'environnement**

```
git clone https://github.com/Osmantic/ODS.git
cd ODS
pip install -e .
```

## Exécution

**Démarrage du serveur AI local**

```
python -m ods.server --port 8000
# Web paneline http://localhost:8000 adresinden erişin
```

## Architecture technique et principe de fonctionnement

- Noyau d'inférence natif (llama.cpp et vLLM) : chargez et exécutez rapidement des modèles aux formats GGUF et GPU purs avec une empreinte mémoire minimale.
- Base de données vectorielles intégrée : regroupement et indexation de documents avec un stockage vectoriel léger basé sur ChromaDB et SQLite.
- File d'attente de tâches et machine d'état d'agent : gestionnaires asynchrones qui gèrent les requêtes en plusieurs étapes et les flux d'appels d'outils.

## Workflows RAG natifs et pipelines d’agents personnalisés

- Travailler avec des documents confidentiels de l'entreprise : interrogez les contrats, les états financiers et la correspondance interne avec le RAG local sans les extraire vers le cloud.
- Assistant d'analyse et de développement de code natif : fournissez la complétion du code IA natif sur VS Code ou Cursor en indexant vos projets logiciels personnalisés.
- Agents de traitement de données autonomes : définissez des tâches en arrière-plan qui lisent, résument et formatent les rapports de conversion dans le système de fichiers local.

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Pouvez-vous expliquer, avec le code et les étapes du terminal, comment importer les documents PDF de mon entreprise dans la base de données vectorielles locale en installant le serveur ODS sur mon ordinateur personnel, puis comment effectuer des requêtes Q&R RAG basées sur ces documents via un modèle Llama 3 local ?

## Questions fréquemment posées

- Est-ce que ça fonctionne complètement hors ligne sans connexion Internet ? Oui. Une fois les poids de modèle requis téléchargés, ODS peut fonctionner dans des environnements complètement hors ligne (avec espace d'air) sans nécessiter de connexion réseau.
- Quels formats de modèles prend-il en charge ? Prend en charge tous les modèles ouverts (Llama 3, Mistral, Qwen, DeepSeek) et les poids HuggingFace purs au format GGUF.
- Existe-t-il une interface Web disponible ? Oui. ODS est livré avec un panneau Web intégré ; Vous pouvez gérer des modèles, télécharger des fichiers et ouvrir des sessions de discussion.
- Est-ce que ça fonctionne avec CPU uniquement, sans GPU ? Oui. Grâce au noyau llama.cpp, il peut également fonctionner sur un processeur pur avec une grande efficacité en utilisant les jeux d'instructions AVX2/AVX-512.

## Termes liés du glossaire

- [Multimodal](https://trescout.com/fr/dictionary/multimodal/)
- [Vector Database](https://trescout.com/fr/dictionary/vector-database/)
- [GGUF](https://trescout.com/fr/dictionary/gguf/)
- [Whisper](https://trescout.com/fr/dictionary/whisper/)
- [CPU](https://trescout.com/fr/dictionary/cpu/)
- [RAG](https://trescout.com/fr/dictionary/rag/)

- **Pour qui:** Entreprises soucieuses de la confidentialité des données, développeurs locaux d’intelligence artificielle et administrateurs système.
- **Licence:** MIT (Özgür açık kaynak lisansı)
- **Toit:** Serveur IA local Python et lama.cpp
- **Plateformes:** Linux, macOS, Windows

## Liens

- [Dépôt GitHub →](https://github.com/Osmantic/ODS)
- [Lire en turc →](https://trescout.com/discover/ods/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-08-31 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/ods/
