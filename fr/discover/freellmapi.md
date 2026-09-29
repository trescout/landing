# Combinez 34 fournisseurs LLM gratuits en une seule API

FreeLLMAPI fournit un routage intelligent et une tolérance aux pannes en regroupant 34 principaux fournisseurs de modèles de langage gratuits différents dans une seule API REST au format OpenAI.

- ★ 29 534
- TypeScript
- GitHub Trending · 2026-08-28

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
Pouvez-vous expliquer avec des exemples de code comment exécuter l'outil FreeLLMAPI sur mon serveur local avec Docker, comment faire pointer le SDK OpenAI Node.js vers ce point de terminaison local et comment activer l'utilisation d'un modèle de secours automatique en cas de défaillance d'un fournisseur ?

## Questions fréquemment posées
- Dois-je acheter une clé API pour utiliser FreeLLMAPI ? Non. Le système combine 34 modèles d’IA qui offrent des niveaux gratuits ou fournissent une inférence gratuite accessible au public.
- Quels sont les principaux modèles de langage pris en charge ? Les modèles à pondération ouverte comme Llama 3, Mistral, Gemma, Claude et les modèles populaires comme le niveau gratuit de Google Gemini sont pris en charge.
- Est-il adapté à la confidentialité des entreprises ? FreeLLMAPI est open source et fonctionne sur votre réseau local, mais les fournisseurs gratuits qui les sous-tendent ont leurs propres conditions d'utilisation et politiques de confidentialité.
- Est-il compatible avec LangChain ou CrewAI ? Oui. Puisqu'il fournit une émulation complète de l'API OpenAI REST, il peut être utilisé directement avec tous les frameworks LLM en définissant l'adresse baseURL sur localhost:3000/v1.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/freellmapi/
