# Exécutez des modèles d'IA géants avec 4 Go de VRAM

AirLLM permet d'exécuter de grands modèles de langage avec 70 milliards de paramètres sur des unités de traitement graphique avec seulement 4 Go de mémoire vidéo (VRAM). Cette bibliothèque utilise des techniques d'optimisation de la mémoire pour permettre l'utilisation de modèles haute capacité avec de faibles exigences matérielles.

- ★ 29 265
- Jupyter Notebook
- GitHub Trending · 2026-06-04

## Mise à jour
- 6 août 2026 : Étoile 27 522 → 29 265, dernière version v3.1.0 (29 juillet 2026).
- 4 août 2026 : Étoile 25 416 → 27 522, dernière version v3.1.0 (29 juillet 2026).
- 2 août 2026 : Étoile 19 113 → 25 416, dernière version v3.1.0 (29 juillet 2026).

## Ce que ça vous apporte
- Possibilité d'exécuter des modèles avec des paramètres 70B avec 4 Go de VRAM.
- Possibilité d'utiliser des modèles 405B Llama3.1 avec 8 Go de VRAM.
- Augmentation de la vitesse jusqu'à 3 fois avec la compression basée sur les blocs.

## Installation
**Installation du paquet**

```
pip install airllm
```


## Exécution
**Charger et exécuter le modèle**

```
from airllm import AutoModel

MAX_LENGTH = 128
# could use hugging face model repo id:
model = AutoModel.from_pretrained("garage-bAInd/Platypus2-70B-instruct")

# or use model's local path...
#model = AutoModel.from_pretrained("/home/ubuntu/.cache/huggingface/hub/models--garage-bAInd--Platypus2-70B-instruct/snapshots/b585e74bcaae02e52665d9ac6d23f4d0dbc81a0f")

input_text = [
        'What is the capital of United States?',
        #'I like',
    ]

input_tokens = model.tokenizer(input_text,
    return_tensors="pt", 
    return_attention_mask=False, 
    truncation=True, 
    max_length=MAX_LENGTH, 
    padding=False)
           
generation_output = model.generate(
    input_tokens['input_ids'].cuda(), 
    max_new_tokens=20,
    use_cache=True,
    return_dict_in_generate=True)

output = model.tokenizer.decode(generation_output.sequences[0])

print(output)
```


## Si vous ne codez pas
Je souhaite exécuter un modèle avec des paramètres 70B en utilisant la bibliothèque AirLLM sur ma carte graphique avec une faible capacité VRAM. J'ai utilisé la commande pip install airllm pour l'installation. Comment puis-je créer la structure de code Python nécessaire pour charger mon modèle et le générer avec une simple saisie de texte, à l'aide de la classe AutoModel ? Je sais que je dois m'assurer de disposer de suffisamment d'espace disque pendant le processus. Pouvez-vous expliquer les étapes de base que je dois suivre pour démarrer le processus ?

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/airllm/
