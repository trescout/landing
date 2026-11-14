# Moteur d'intelligence artificielle local TensorFold

ashhart/TensorFold propose un moteur d'inférence prenant en charge Metal, CUDA et Vulkan pour les grands modèles de langage (LLM). Développé en Zig, cet outil permet d'exécuter des modèles directement sur les processeurs graphiques Apple Silicon et NVIDIA sans nécessiter l'installation de Python ou MLX.

- ★ 2 080
- Zig
- GitHub Trending · 2026-11-13

## Mises à jour

- **14 novembre 2026:** Étoiles 1,998 → 2,080, dernière version v1.2.8 (13 novembre 2026).
- **13 novembre 2026:** Étoiles 1,996 → 1,998, dernière version v1.2.7 (11 novembre 2026).

## Ce que ça vous apporte

- Exécute des grands modèles de langage directement sur les processeurs graphiques Apple Silicon et NVIDIA.
- Fournit un service via un fichier binaire sans avoir besoin d'installer Python ou MLX.
- Permet de sélectionner des modèles et de discuter avec une application web locale.

## Installation

**Installation sur Mac**

```
brew install ashhart/tensorfold/tensorfold
tensorfold pull mlx-community/Qwen3.5-2B-MLX-4bit@93760be4f1f69842a46bc13dbdc0f19e291392a3
tensorfold serve mlx-community/Qwen3.5-2B-MLX-4bit --name local-model --context 8192 --no-thinking
```

## Exécution

**Envoi d'une requête**

```
curl -fsS http://127.0.0.1:8080/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"local-model","messages":[{"role":"user","content":"Say hello in one sentence."}],"max_tokens":128,"temperature":0}'
```

## Si vous ne codez pas

Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite installer l'outil TensorFold sur mon Mac équipé d'une puce Apple Silicon, télécharger le modèle Qwen3.5-2B et lancer le serveur. Pour cela, tu dois exécuter les commandes suivantes dans l'ordre :

brew install ashhart/tensorfold/tensorfold
tensorfold pull mlx-community/Qwen3.5-2B-MLX-4bit@93760be4f1f69842a46bc13dbdc0f19e291392a3
tensorfold serve mlx-community/Qwen3.5-2B-MLX-4bit --name local-model --context 8192 --no-thinking

Ensuite, pour vérifier que le serveur fonctionne, tu peux envoyer une requête avec la commande suivante :

curl -fsS http://127.0.0.1:8080/v1/chat/completions \
-H 'Content-Type: application/json' \
-d '{"model":"local-model","messages":[{"role":"user","content":"Say hello in one sentence."}],"max_tokens":128,"temperature":0}'

Dépôt : https://github.com/ashhart/TensorFold. Base-toi sur les instructions officielles du fichier README de ce dépôt pour l'installation et l'exécution.

Avant de commencer, vérifie quel système d'exploitation nous utilisons et si les outils nécessaires (ex: Python, Node.js, Git, Docker) sont installés. Installe ceux qui manquent étape par étape selon ce système.

Crée un nouveau dossier vide pour travailler. Ne touche pas aux fichiers en dehors de ce dossier et ne supprime rien. Avant chaque commande, décris ce que tu vas faire en une phrase.

Dis-moi ce que je devrais voir à l'écran à la fin de chaque étape. Si une erreur survient, je te copierai le message d'erreur tel quel et nous la corrigerons ensemble.

## Termes liés du glossaire

- [Temperature](https://trescout.com/fr/dictionary/temperature/)
- [Application](https://trescout.com/fr/dictionary/application/)
- [Inference Engine](https://trescout.com/fr/dictionary/inference-engine/)
- [Apple Silicon](https://trescout.com/fr/dictionary/apple-silicon/)
- [Inference](https://trescout.com/fr/dictionary/inference/)
- [LLM](https://trescout.com/fr/dictionary/llm/)

- **Pour qui:** Il s'adresse aux développeurs qui souhaitent exécuter de grands modèles de langage sur des processeurs graphiques Apple Silicon ou NVIDIA sans installer Python.
- **Licence:** Apache-2.0

## Liens

- [Dépôt GitHub →](https://github.com/ashhart/TensorFold)
- [Lire en turc →](https://trescout.com/discover/tensorfold/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-11-13 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Le texte de présentation a été préparé avec l’IA à partir de la propre documentation du dépôt et cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/tensorfold/
