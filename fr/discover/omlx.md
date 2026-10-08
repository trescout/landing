# Serveur IA pour ordinateurs Mac

Omlx est un serveur d'inférence LLM (Large Language Model) natif de nouvelle génération qui offre des capacités de traitement par lots continu et de mise en cache SSD pour les ordinateurs Mac équipés de processeurs Apple Silicon (M1/M2/M3/M4). Il combine l'infrastructure Apple MLX avec une API compatible OpenAI et une interface de barre de menu macOS.

- ★ 22 409
- Python
- GitHub Trending · 2026-08-18

## Mises à jour

- **1 octobre 2026:** Étoiles 22,280 → 22,409, dernière version v0.7.0 (30 septembre 2026).
- **27 septembre 2026:** Étoiles 21,147 → 22,280, dernière version v0.7.0rc1 (24 septembre 2026).
- **31 août 2026:** Étoiles 20,793 → 21,147, dernière version v0.6.4 (29 août 2026).
- **27 août 2026:** Étoiles 20,069 → 20,793, dernière version v0.6.3rc3 (24 août 2026).

## Ce que ça vous apporte

- Accélération matérielle Apple MLX et Metal : élimine complètement le goulot d'étranglement de la copie de mémoire entre le CPU et le GPU en utilisant directement l'architecture de mémoire unifiée (UMA) des processeurs Apple Silicon.
- Traitement par lots continu : augmente l'efficacité du serveur jusqu'à 3 fois en combinant plusieurs demandes simultanées d'utilisateurs et d'agents en un seul cycle de calcul.
- Mise en cache SSD et pré-remplissage de morceaux : évite les pannes de mémoire insuffisante en stockant le cache clé-valeur (KV) sur le SSD NVMe pendant les longues fenêtres contextuelles.
- API standard compatible OpenAI : Fonctionne sans configuration avec les outils Cursor, Open WebUI, Continue et LangChain grâce aux points de terminaison /v1/chat/completions et /v1/models.
- Contrôle de la barre de menu macOS : offre la commodité de démarrer, d'arrêter, de sélectionner des modèles et de surveiller la consommation de mémoire avec des graphiques en direct sans entrer dans le terminal.

## Installation

**Installation avec Homebrew**

```
brew tap jundot/omlx https://github.com/jundot/omlx
brew install jundot/omlx/omlx
```

## Exécution

**Démarrage du service en arrière-plan**

```
omlx start
```

**Téléchargez et soumettez un modèle spécifique**

```
omlx run mlx-community/Llama-3.2-3B-Instruct-4bit
```

## Architecture technique et principe de fonctionnement

- Utilisation complète de la mémoire unifiée (UMA) : contrairement aux PC dotés de graphiques discrets, dans les Mac Apple Silicon, 128 Go ou 192 Go de RAM peuvent être adressés directement par les cœurs GPU. Omlx traite cet énorme pool de mémoire avec une latence nulle avec des cœurs Metal Shading Language (MSL).
- Gestion dynamique du cache KV (PagedAttention) : alloue des tenseurs clé-valeur sous forme de blocs paginés pour empêcher la fragmentation de la mémoire sur plusieurs sessions. La mémoire utilisée est immédiatement libérée à la fin de la requête.
- Couche de cache débordant sur le SSD : lorsque le cache KV dépasse la RAM dans d'énormes fenêtres contextuelles telles que 32 Ko et 128 Ko, Omlx page automatiquement le disque SSD intégré haute vitesse d'Apple. Ainsi, le modèle continue l’inférence sans planter.

## Intégration d'API native compatible OpenAI

**Test d'API avec cURL**

```
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "default",
    "messages": [{"role": "user", "content": "Apple Silicon mimarisinin temel avantajı nedir?"}],
    "temperature": 0.7
  }'
```

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite exécuter un modèle de langage étendu natif à l'aide du serveur Omlx sur mon Mac Apple Silicon. Après avoir terminé l'installation avec Homebrew, pouvez-vous expliquer étape par étape comment exécuter le serveur en arrière-plan, gérer la sélection du modèle depuis la barre de menu et vous connecter à ce modèle local via l'éditeur de code Cursor ou la bibliothèque openai Python ?

## Questions fréquemment posées

- Quelle est la principale différence entre Omlx et Ollama? Alors qu'Ollama utilise généralement l'infrastructure llama.cpp basée sur C++, Omlx s'exécute directement sur le framework MLX développé par Apple. De cette manière, il offre une intégration plus profonde avec les unités motrices métalliques et neuronales des puces Apple Silicon, offrant un taux de génération de jetons plus élevé, en particulier dans l'empilement continu et les contextes longs.
- Quels modèles peuvent fonctionner avec 16 Go ou 24 Go de RAM ? Les modèles avec des paramètres 8B quantifiés sur 4 bits (Llama 3, Qwen 2.5, Mistral) occupent environ 5 à 6 Go de mémoire et fonctionnent de manière extrêmement fluide sur les Mac de 16 Go. Sur les appareils dotés de 24 Go ou 36 Go de mémoire combinée, les modèles 14B ou 32B peuvent être facilement installés.
- La mise en cache SSD épuise-t-elle la durée de vie du disque Mac ? Non. Omlx utilise des algorithmes de mise en mémoire tampon intelligents pour éviter les cycles d'écriture inutiles dans les opérations de mise en cache. Il n'intervient que lorsque la mémoire contextuelle approche de la limite de RAM, minimisant ainsi l'usure du disque.
- Est-ce que cela fonctionne sur les anciens ordinateurs Mac à processeur Intel ? Non. Omlx est optimisé spécifiquement pour Apple Silicon (architecture ARM) et le framework Apple MLX. Il ne fonctionne pas sur les Mac à processeur Intel ou sur les ordinateurs Windows/Linux x86.

## Termes liés du glossaire

- [Continuous Batching](https://trescout.com/fr/dictionary/continuous-batching/)
- [SSD Caching](https://trescout.com/fr/dictionary/ssd-caching/)
- [Context Window](https://trescout.com/fr/dictionary/context-window/)
- [Caching](https://trescout.com/fr/dictionary/caching/)
- [Apple Silicon](https://trescout.com/fr/dictionary/apple-silicon/)
- [RAM](https://trescout.com/fr/dictionary/ram/)

- **Pour qui:** Pour les développeurs d'IA qui souhaitent exécuter des modèles de langage étendus (LLM) à vitesse maximale et avec une confidentialité native sur des ordinateurs Mac équipés de processeurs Apple Silicon.
- **Licence:** Apache-2.0 (Açık kaynak lisansı)
- **Toit:** Moteur d'inférence natif basé sur Apple MLX et Python
- **Matériel:** Apple Silicon séries M1, M2, M3, M4 (Pro, Max, Ultra pris en charge)

## Liens

- [Dépôt GitHub →](https://github.com/jundot/omlx)
- [Lire en turc →](https://trescout.com/discover/omlx/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-08-18 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/omlx/
