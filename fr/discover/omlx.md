# Serveur d'IA pour ordinateurs Mac

Omlx est un serveur d'inférence de grands modèles de langage (LLM) local de nouvelle génération conçu pour les Mac Apple Silicon (M1/M2/M3/M4), offrant le traitement par lots continu (continuous batching) et la mise en cache SSD. Il combine le framework Apple MLX avec une API compatible OpenAI et une interface dans la barre des menus macOS.

- ★ 21.147
- Python
- GitHub Trending · 2026-08-18

## Mises à jour
- 31 août 2026: Étoiles 20 793 → 21 147, dernière version v0.6.4 (29 août 2026).
- 27 août 2026: Étoiles 20 069 → 20 793, dernière version v0.6.3rc3 (24 août 2026).
- 20 août 2026: Étoiles 19 758 → 20 069, dernière version v0.6.3rc2 (20 août 2026).
- 19 août 2026: Étoiles 19 519 → 19 758, dernière version v0.6.3rc1 (19 août 2026).

## Ce que ça vous apporte
- Accélération matérielle Apple MLX et Metal: Exploite directement l'architecture de mémoire unifiée (UMA) pour supprimer tout goulot d'étranglement de copie mémoire entre CPU et GPU.
- Traitement par lots continu (Continuous Batching): Combine les requêtes simultanées de plusieurs utilisateurs ou agents IA dans une seule passe de calcul, triplant le débit du serveur.
- Mise en cache SSD et pré-remplissage fractionné (Chunked Prefill): Déporte le cache clé-valeur (KV) sur le SSD NVMe lors des longs contextes pour éviter tout plantage par manque de mémoire (OOM).
- API standard compatible OpenAI: Fonctionne sans configuration complexe avec Cursor, Open WebUI, Continue et LangChain via les points de terminaison /v1/chat/completions et /v1/models.
- Contrôle dans la barre des menus macOS: Démarrez, arrêtez, changez de modèle et observez la consommation mémoire en temps réel sans ouvrir le terminal.

## Installation

**Installation avec Homebrew**

```
brew tap jundot/omlx https://github.com/jundot/omlx
brew install jundot/omlx/omlx
```

## Exécution

**Démarrer le service en arrière-plan**

```
omlx start
```

**Télécharger et servir un modèle spécifique**

```
omlx run mlx-community/Llama-3.2-3B-Instruct-4bit
```

## Architecture technique et principe de fonctionnement

Omlx s'appuie sur le framework d'apprentissage automatique MLX d'Apple. Il repose sur trois piliers conçus pour dépasser les limitations des moteurs d'inférence classiques (comme llama.cpp ou Ollama) sur Mac :
- Exploitation totale de la mémoire unifiée (UMA): Contrairement aux PC équipés de cartes graphiques dédiées, les Mac Apple Silicon permettent aux cœurs GPU d'adresser directement 128 Go ou 192 Go de RAM. Omlx traite cette immense réserve sans latence via des noyaux Metal Shading Language (MSL).
- Gestion dynamique du cache KV (PagedAttention): Alloue les tenseurs clé-valeur en blocs paginés pour éliminer la fragmentation mémoire lors des sessions multi-utilisateurs et libère la mémoire immédiatement après réponse.
- Débordement du cache vers le SSD: Lorsque le cache KV dépasse la mémoire vive dans des contextes de 32K ou 128K tokens, Omlx bascule automatiquement les pages sur le SSD NVMe haute vitesse sans interrompre l'inférence.

## Intégration d'API locale compatible OpenAI

Une fois lancé, Omlx expose une API REST compatible OpenAI sur votre machine (par défaut http://localhost:8000). Vous pouvez connecter directement vos éditeurs de code et outils d'IA :

**Test d'API avec cURL**

```
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "default",
    "messages": [{"role": "user", "content": "Quel est le principal avantage de l architecture Apple Silicon ?"}],
    "temperature": 0.7
  }'
```

## Si vous ne codez pas
🤖 Si vous ne codez pas
Je souhaite faire tourner un grand modèle de langage local avec Omlx sur mon Mac Apple Silicon. Après avoir effectué l'installation via Homebrew, peux-tu m'expliquer pas à pas comment lancer le serveur en arrière-plan, choisir un modèle depuis la barre des menus et relier l'éditeur Cursor ou un script Python via la bibliothèque openai à ce modèle local ?

- **Pour qui:** Développeurs IA et utilisateurs de Mac Apple Silicon souhaitant une inférence ultra-rapide et une confidentialité totale en local.
- **Licence:** Apache-2.0 (Licence open-source)
- **Framework:** Moteur d'inférence local basé sur Apple MLX et Python
- **Matériel:** Série Apple Silicon M1, M2, M3, M4 (support Pro, Max, Ultra)

## Questions fréquentes
- Quelle est la différence fondamentale entre Omlx et Ollama ? Tandis qu'Ollama s'appuie sur le moteur llama.cpp en C++, Omlx est optimisé nativement sur le framework MLX d'Apple. Cette intégration étroite avec Metal et le Neural Engine offre une génération de tokens plus rapide, en particulier avec le batching continu et les longs contextes.
- Quels modèles tourneront avec 16 Go ou 24 Go de mémoire unifiée ? Les modèles 8B quantifiés en 4-bit (Llama 3, Qwen 2.5, Mistral) occupent environ 5 à 6 Go et fonctionnent avec une grande fluidité sur 16 Go. Avec 24 Go ou 36 Go, des modèles de 14B ou 32B s'exécutent confortablement.
- La mise en cache SSD use-t-elle le disque du Mac ? Non. Omlx emploie des tampons intelligents pour éviter les cycles d'écriture inutiles. Il n'intervient que si le cache approche la saturation de la RAM physique, réduisant l'usure au strict minimum.
- Fonctionne-t-il sur les anciens Mac Intel ou sur Windows/Linux ? Non. Omlx est exclusivement optimisé pour Apple Silicon (architecture ARM) et Apple MLX. Il n'est pas compatible avec les processeurs Intel x86.

## Liens
- [GitHub →](https://github.com/jundot/omlx)

## Termes associés du glossaire
Apple Silicon Continuous Batching LLM Local Open Source

---
Source: TreScout Discover · https://trescout.com/fr/discover/omlx/
