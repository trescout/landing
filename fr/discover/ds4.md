# Moteur d'exécution DeepSeek sur matériel natif

Développé par Salvatore Sanfilippo, le créateur de Redis, ds4 est un moteur d'inférence qui permet d'exécuter des modèles DeepSeek sur du matériel local. Cet outil, écrit en langage C, offre la possibilité d'exécuter des modèles performants sur différents processeurs graphiques grâce au support Metal, CUDA et ROCm.

- ★ 21 134
- C
- GitHub Trending · 2026-08-03

## Mise à jour
- 11 août 2026 : Étoile 20 117 → 21 134.

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
Aidez-moi à choisir le modèle DeepSeek ou GLM le plus approprié en fonction des fonctionnalités matérielles de mon système. Quelle commande de téléchargement dois-je utiliser et comment puis-je surmonter le goulot d'étranglement de la mémoire en activant la fonction de streaming sur SSD ? Expliquez également les paramètres de configuration de base requis pour que j'utilise ce système d'intelligence artificielle que j'ai installé en tant que serveur local.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/ds4/
