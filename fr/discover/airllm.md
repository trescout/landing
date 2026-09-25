# Faites tourner des modèles d'IA géants avec 4 Go de VRAM

AirLLM est une bibliothèque open-source révolutionnaire qui permet d'exécuter des modèles de langage géants (LLM) de 70 milliards et 405 milliards de paramètres sur des cartes graphiques grand public disposant de seulement 4 Go de mémoire vidéo (VRAM), sans serveurs dédiés ni clusters GPU onéreux.

- ★ 33.755
- Jupyter Notebook
- GitHub Trending · 2026-06-04

## Mises à jour
- 6 septembre 2026: Étoiles 33 307 → 33 755, dernière version v4.0.0 (5 septembre 2026).
- 31 août 2026: Étoiles 31 598 → 33 307, dernière version v3.3.0 (28 août 2026).
- 19 août 2026: Étoiles 30 796 → 31 598, dernière version v3.2.0 (18 août 2026).
- 12 août 2026: Étoiles 29 265 → 30 796, dernière version v3.1.0 (29 juillet 2026).

## Ce que ça vous apporte
- Exécution de modèles 70B sur 4 Go de VRAM: Lancez des modèles massifs comme Llama 3 70B, Qwen ou DeepSeek sur des GPU d'entrée de gamme comme la GTX 1650 ou RTX 3050.
- Support de Llama 3.1 405B: Faites tourner le modèle phare de 405 milliards de paramètres sur un PC personnel à 8 Go de VRAM sans cluster de datacenter.
- Exécution couche par couche (Layer-wise Execution): Charge séquentiellement les couches depuis le disque vers la mémoire et les traite une à une pour pulvériser le goulot d'étranglement de la VRAM.
- Vitesse multipliée par 3 par compression de blocs: Lit les poids du modèle sur SSD NVMe par blocs optimisés pour accélérer le transfert disque vers GPU.
- Précision complète sans perte de quantification: Supprime l'obligation de compresser en 4-bit, permettant l'inférence en précision originale 16-bit (bfloat16).

## Installation

**Avec pip (PyPI)**

```
pip install airllm
```

## Architecture technique et principe de fonctionnement

Les moteurs d'inférence classiques (vLLM, Ollama ou HuggingFace) exigent que l'intégralité des poids d'un modèle tienne simultanément dans la mémoire vidéo (VRAM). Un modèle de 70B requiert environ 140 Go en 16-bit et au moins 35 à 40 Go en 4-bit. AirLLM révolutionne ce postulat fondamental :
- Nature séquentielle des couches Transformer: Un réseau Transformer compte environ 80 couches ordonnées. Chaque couche reçoit la sortie de la précédente. Conserver l'ensemble du réseau en VRAM à chaque instant n'est pas mathématiquement indispensable.
- Déchargement séquentiel des couches (Sequential Offloading): AirLLM ne charge en VRAM que l'unique couche en cours de calcul (~1.5 Go). Une fois le calcul terminé, la mémoire est libérée pour accueillir la couche suivante depuis le disque.
- Compromis vitesse et mémoire: Ce fonctionnement n'est pas pensé pour le chat instantané, mais constitue un atout économique exceptionnel pour l'analyse de données, le raisonnement approfondi, la traduction et l'évaluation de modèles.
- Lecture mémoire mappée (mmap): Relie les tenseurs PyTorch directement au disque NVMe via mmap pour exploiter la bande passante maximale du SSD sans saturer la RAM système.

## Exemple d'utilisation en Python

AirLLM offre une syntaxe Python particulièrement épurée, calquée sur l'API AutoModel de HuggingFace :

**Exécuter un modèle 70B en Python**

```python
from airllm import AutoModel

# Initialiser un modele 70B avec seulement 4 Go de VRAM
model = AutoModel.from_pretrained("meta-llama/Meta-Llama-3-70B-Instruct")

input_text = ["Resumez l avenir des agents d IA open source."]
input_tokens = model.tokenizer(input_text, return_tensors="pt", padding=True)

# Generation de texte (les couches sont executees sequentiellement)
generation_output = model.generate(
    input_tokens['input_ids'].cuda(),
    max_new_tokens=100,
    use_cache=True,
    return_dict_in_generate=True
)

output = model.tokenizer.decode(generation_output.sequences[0])
print(output)
```

## Si vous ne codez pas
🤖 Si vous ne codez pas
Je veux utiliser la bibliothèque AirLLM pour exécuter un modèle de 70 milliards de paramètres (ex. meta-llama/Llama-3-70B-Instruct) sur mon GPU local de 4 Go de VRAM. J'ai installé avec pip install airllm. Peux-tu me donner le code Python complet pour charger le modèle, générer une réponse et éviter les erreurs de mémoire ? Merci d'expliquer également l'espace disque requis et les étapes nécessaires.

- **Pour qui:** Chercheurs et développeurs disposant de GPU modestes souhaitant tester localement des modèles de 70B et 405B pour l'évaluation et l'analyse.
- **Licence:** Apache-2.0 (Licence open-source permissive)
- **Prérequis matériel:** GPU avec minimum 4 Go de VRAM et stockage SSD NVMe rapide
- **Écosystème:** Python, PyTorch et HuggingFace Transformers

## Questions fréquentes
- À quelle vitesse fonctionne AirLLM lors de l'exécution ? Comme AirLLM transfère en permanence les couches entre SSD et GPU, la vitesse dépend directement du débit de votre SSD NVMe. Sur un SSD Gen4, un modèle 70B génère environ 1 à 3 tokens par seconde. Ce débit est idéal pour les traitements par lots sans aucun surcoût matériel.
- Combien d'espace disque disponible est nécessaire ? Un modèle de 70B en float 16-bit demande environ 140 Go d'espace (ou 35-40 Go en 4-bit). Le modèle de 405B nécessite au moins 800 Go de stockage NVMe libre.
- Puis-je utiliser les poids originaux sans quantification ? Oui. C'est l'un des plus grands atouts d'AirLLM : la contrainte de quantification est levée car la mémoire est gérée couche par couche, préservant 100 % de la précision originale.
- AirLLM tourne-t-il sur Mac Apple Silicon ou uniquement sur CPU ? AirLLM est avant tout optimisé pour CUDA (GPU NVIDIA). Un support expérimental pour CPU et Apple Silicon Metal existe, mais les meilleures performances sont obtenues avec une carte NVIDIA et un SSD NVMe.

## Liens
- [GitHub →](https://github.com/lyogavin/airllm)

## Termes associés du glossaire
VRAM LLM Large Language Models Transformer Open Source

---
Source: TreScout Discover · https://trescout.com/fr/discover/airllm/
