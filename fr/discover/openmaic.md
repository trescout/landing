# Simulation de classe interactive avec des agents d'intelligence artificielle multiples

Développé par des chercheurs de l'Université Tsinghua, OpenMAIC réunit des agents d'IA multiples dans les rôles d'enseignant, d'élève et d'observateur au sein d'un environnement de classe interactif.

- ★ 39 969
- TypeScript
- GitHub Trending · 2026-08-31

## Mises à jour

- **5 octobre 2026:** Étoiles 39,351 → 39,969, dernière version v1.1.3 (5 octobre 2026).
- **28 septembre 2026:** Étoiles 39,156 → 39,351, dernière version v1.1.2 (28 septembre 2026).
- **27 septembre 2026:** Étoiles 25,572 → 39,156, dernière version v1.1.1 (26 septembre 2026).

## Ce que ça vous apporte

- Architecture multi-agent basée sur les rôles : interaction dynamique d'agents LLM agissant en tant que professeur, étudiant questionneur, débatteur et résumé.
- Interface de classe visuelle et audio : une expérience pédagogique immersive grâce au tableau virtuel, au flux de questions-réponses instantané et à la synthèse vocale (TTS).
- Programme de cours personnalisable : créez instantanément des cours interactifs en téléchargeant vos propres documents PDF ou vos notes de cours textuelles.
- Lancement de simulation en un clic : gérez une orchestration d'agents complexe via une interface Web moderne sans compétences en codage technique.
- Compatibilité avec les modèles à poids ouverts : la liberté de connecter le modèle d'intelligence artificielle de votre choix via Ollama, vLLM ou des fournisseurs de LLM dans le cloud.

## Installation

**Clonage du référentiel et installation des dépendances**

```
git clone https://github.com/THU-MAIC/OpenMAIC.git
cd OpenMAIC
pnpm install
```

## Exécution

**Démarrage du serveur de développement**

```
pnpm run dev
# Tarayıcıda http://localhost:3000 adresini açın
```

## Architecture technique et principe de fonctionnement

- Moteur d'orchestration de conversation : Contrôleur central qui gère quel agent parle et quand, l'ordre de prise de parole et le contexte de la discussion.
- Gestion de la mémoire et du contexte : Conservation du contenu du tableau partagé et des questions des élèves dans la mémoire à court/long terme tout au long du cours.
- Diffusion en temps réel via WebSocket : transmission sans latence des textes de conversation, des expressions émotionnelles et des animations vers l'interface frontend.

## Dynamique de classe multi-agents et simulations de rôles

- Environnements de débat socratique : Des agents dotés de perspectives différentes débattent d'un sujet afin de stimuler la pensée critique de l'utilisateur.
- Support Pédagogique Personnalisé : des tuteurs IA dédiés qui ajustent automatiquement le niveau de difficulté en fonction de la vitesse de compréhension de l'utilisateur.
- Recherches sur l'interaction sociale inter-agents : analyse de la manière dont les grands modèles de langage coopèrent et partagent des informations dans des environnements de groupes peuplés.

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite simuler un environnement de discussion socratique sur la plateforme OpenMAIC en y chargeant mes propres notes de cours. Pourrais-tu m'expliquer étape par étape comment définir les rôles des agents (professeur, étudiant curieux, questionneur critique) et comment lancer cette classe avec un modèle Ollama local ?

## Questions fréquemment posées

- Faut-il un GPU pour utiliser OpenMAIC ? Si vous exécutez votre propre modèle local (Ollama/vLLM), un GPU est recommandé ; cependant, il peut être utilisé directement sur un ordinateur standard via des API cloud (OpenAI, Gemini, Groq).
- L'utilisateur peut-il participer à la simulation par la voix ? Oui. Grâce à WebRTC et au module de reconnaissance vocale, l'utilisateur peut participer aux discussions en classe en parlant dans son microphone.
- Combien d'agents peuvent être présents simultanément dans la classe ? Dans la configuration par défaut, une interaction idéale est obtenue entre 3 et 8 agents ; des classes plus peuplées peuvent être configurées en fonction des ressources système.
- Dans quels formats le contenu du cours peut-il être téléchargé ? Des documents en texte brut, Markdown et PDF peuvent être directement importés dans la base de connaissances du système.

## Termes liés du glossaire

- [Markdown](https://trescout.com/fr/dictionary/markdown/)
- [GPU](https://trescout.com/fr/dictionary/gpu/)
- [PDF](https://trescout.com/fr/dictionary/pdf/)
- [LLM](https://trescout.com/fr/dictionary/llm/)
- [API](https://trescout.com/fr/dictionary/api/)
- [Open Source](https://trescout.com/fr/dictionary/open-source/)

- **Pour qui:** Éducateurs, chercheurs en intelligence artificielle, entrepreneurs EdTech et étudiants.
- **Licence:** Apache-2.0 (Açık kaynak lisansı)
- **Toit:** Simulateur multi-agents TypeScript & Next.js
- **Plateformes:** Navigateur Web, Linux, macOS, Windows

## Liens

- [Dépôt GitHub →](https://github.com/THU-MAIC/OpenMAIC)
- [Lire en turc →](https://trescout.com/discover/openmaic/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-08-31 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/openmaic/
