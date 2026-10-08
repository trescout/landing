# Combinez 34 fournisseurs LLM gratuits en une seule API

FreeLLMAPI fournit un routage intelligent et une tolérance aux pannes en regroupant 34 principaux fournisseurs de modèles de langage gratuits différents dans une seule API REST au format OpenAI.

- ★ 31 427
- TypeScript
- GitHub Trending · 2026-08-28

## Mises à jour

- **7 octobre 2026:** Étoiles 30,274 → 31,427, dernière version v0.13.6 (7 octobre 2026).
- **3 octobre 2026:** Étoiles 29,808 → 30,274, dernière version v0.13.4 (3 octobre 2026).
- **1 octobre 2026:** Étoiles 29,534 → 29,808, dernière version v0.13.3 (30 septembre 2026).
- **29 septembre 2026:** Étoiles 29,054 → 29,534, dernière version v0.13.2 (29 septembre 2026).

## Ce que ça vous apporte

- 34 fournisseurs de modèles gratuits : accès unique à des dizaines de fournisseurs gratuits, notamment Google Gemini, Groq, Cloudflare Workers AI et HuggingFace.
- Compatibilité de l'API OpenAI REST : travaillez avec LangChain, LlamaIndex et les applications d'IA existantes sans modifier le code, grâce au point de terminaison /v1/chat/completions.
- Routage intelligent et récupération en cas de panne : passez automatiquement à un autre fournisseur lorsqu'un fournisseur atteint la limite de débit ou tombe en panne.
- Prise en charge du streaming (événements envoyés par le serveur) : possibilité de recevoir les sorties du modèle sous forme de flux mot par mot en temps réel.
- Légère et facile à déployer : architecture qui peut être déployée sur un ordinateur ou un serveur local en quelques secondes avec Docker ou Node.js.

## Installation

**Clonage du référentiel et installation des dépendances**

```
git clone https://github.com/tashfeenahmed/freellmapi.git
cd freellmapi
npm install
```

## Exécution

**Démarrage du service et interrogation du modèle**

```
npm start
# OpenAI uyumlu istek:
curl http://localhost:3000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-4o-mini","messages":[{"role":"user","content":"Merhaba!"}]}'
```

## Architecture technique et principe de fonctionnement

- Couche d'adaptateur de fournisseur : architecture extensible qui normalise différentes API REST et WebSocket dans un format de réponse JSON commun.
- Équilibrage de charge dynamique et surveillance des quotas : surveillez les limites de vitesse actuelles de chaque fournisseur et dirigez les demandes vers le modèle actif qui répond le plus rapidement.
- Cache intégré et gestion des erreurs : mise en cache des requêtes répétées et mécanisme de nouvelle tentative automatique en cas d'expiration du délai.

## Mécanisme de routage et de tolérance aux pannes du modèle

- Comparaison multimodèle : mesurez la qualité de réponse et la latence en envoyant la même entrée utilisateur à différents modèles open source.
- Économisez sur le développement et le prototypage : obtenez rapidement des prototypes et des projets MVP basés sur l'IA sans définir de clés API payantes.
- Stratégie de sauvegarde (pipeline de repli) : assurez-vous que votre système redirige vers les modèles secondaires sans interruption lorsque le fournisseur principal tombe en panne.

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Pouvez-vous expliquer avec des exemples de code comment exécuter l'outil FreeLLMAPI sur mon serveur local avec Docker, comment faire pointer le SDK OpenAI Node.js vers ce point de terminaison local et comment activer l'utilisation d'un modèle de secours automatique en cas de défaillance d'un fournisseur ?

## Questions fréquemment posées

- Dois-je acheter une clé API pour utiliser FreeLLMAPI ? Non. Le système combine 34 modèles d’IA qui offrent des niveaux gratuits ou fournissent une inférence gratuite accessible au public.
- Quels sont les principaux modèles de langage pris en charge ? Les modèles à pondération ouverte comme Llama 3, Mistral, Gemma, Claude et les modèles populaires comme le niveau gratuit de Google Gemini sont pris en charge.
- Est-il adapté à la confidentialité des entreprises ? FreeLLMAPI est open source et fonctionne sur votre réseau local, mais les fournisseurs gratuits qui les sous-tendent ont leurs propres conditions d'utilisation et politiques de confidentialité.
- Est-il compatible avec LangChain ou CrewAI ? Oui. Puisqu'il fournit une émulation complète de l'API OpenAI REST, il peut être utilisé directement avec tous les frameworks LLM en définissant l'adresse baseURL sur localhost:3000/v1.

## Termes liés du glossaire

- [Pipeline](https://trescout.com/fr/dictionary/pipeline/)
- [Proxy](https://trescout.com/fr/dictionary/proxy/)
- [Localhost](https://trescout.com/fr/dictionary/localhost/)
- [SDK](https://trescout.com/fr/dictionary/sdk/)
- [LLM](https://trescout.com/fr/dictionary/llm/)
- [API](https://trescout.com/fr/dictionary/api/)

- **Pour qui:** Développeurs d'intelligence artificielle, chercheurs open source, ingénieurs full-stack et développeurs de prototypes.
- **Licence:** MIT (Özgür açık kaynak lisansı)
- **Toit:** Proxy inverse TypeScript / Node.js
- **Plateformes:** Docker, Linux, macOS, Windows

## Liens

- [Dépôt GitHub →](https://github.com/tashfeenahmed/freellmapi)
- [Lire en turc →](https://trescout.com/discover/freellmapi/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-08-28 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/freellmapi/
