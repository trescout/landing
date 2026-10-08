# Moteur d'exécution DeepSeek sur matériel natif

Développé par Salvatore Sanfilippo, le créateur de Redis, ds4 est un moteur d'inférence qui permet d'exécuter des modèles DeepSeek sur du matériel local. Cet outil, écrit en langage C, offre la possibilité d'exécuter des modèles performants sur différents processeurs graphiques grâce au support Metal, CUDA et ROCm.

- ★ 23 530
- C
- GitHub Trending · 2026-08-03

## Mises à jour

- **5 octobre 2026:** Étoiles 22,197 → 23,530.
- **10 septembre 2026:** Étoiles 21,134 → 22,197.
- **11 août 2026:** Étoiles 20,117 → 21,134.

## Ce que ça vous apporte

- Exécute des modèles d'IA hautes performances sur du matériel grand public
- Permet l'utilisation du modèle même avec une capacité de mémoire limitée en diffusant des données via SSD
- Permet de créer un serveur LLM de niveau entreprise avec prise en charge multi-GPU

## Installation

**Construisez en fonction de votre matériel**

```
make                  # macOS Metal
make cuda-spark       # Linux CUDA, DGX Spark / GB10
make cuda-generic     # Linux CUDA, other local CUDA GPUs
make strix-halo       # Linux ROCm, AMD Strix Halo
make cpu              # CPU-only diagnostics build
```

**Téléchargez le modèle**

```
./download_model.sh q2-imatrix   # 96/128 GB RAM machines, imatrix-tuned q2
./download_model.sh q2-q4-imatrix  # 96/128 GB RAM machines, q2 with last 6 layers q4
./download_model.sh q4-imatrix   # >= 256 GB RAM machines, imatrix-tuned q4
./download_model.sh pro-q2-imatrix  # 512 GB RAM machines, PRO q2 imatrix quant
```

## Exécution

**Initialiser le modèle**

```
./download_model.sh q2-imatrix

./ds4 \
  -m ./ds4flash.gguf \
  --ssd-streaming \
  --ssd-streaming-cache-experts 32GB \
  --ctx 32768 \
  --nothink
```

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Aidez-moi à choisir le modèle DeepSeek ou GLM le plus approprié en fonction des fonctionnalités matérielles de mon système. Quelle commande de téléchargement dois-je utiliser et comment puis-je surmonter le goulot d'étranglement de la mémoire en activant la fonction de streaming sur SSD ? Expliquez également les paramètres de configuration de base requis pour que j'utilise ce système d'intelligence artificielle que j'ai installé en tant que serveur local.

## Termes liés du glossaire

- [Inference Engine](https://trescout.com/fr/dictionary/inference-engine/)
- [Inference](https://trescout.com/fr/dictionary/inference/)
- [LLM](https://trescout.com/fr/dictionary/llm/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il s'adresse aux développeurs de logiciels et aux administrateurs système qui souhaitent exécuter des modèles d'intelligence artificielle hautes performances sur leur propre matériel local.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/antirez/ds4)
- [Lire en turc →](https://trescout.com/discover/ds4/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-08-03 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/ds4/
