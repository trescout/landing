# Configurer les sorties IA

La bibliothèque Outlines permet de présenter les réponses de grands modèles de langage sous forme de sorties structurées selon des schémas prédéfinis. Avec cet outil basé sur Python, les développeurs protègent l'intégrité des données en limitant les sorties du modèle avec des expressions régulières ou des règles de grammaire sans contexte.

- ★ 15 525
- Python
- GitHub Trending · 2026-07-22

## Ce que ça vous apporte
- Contraint les sorties du modèle selon des schémas prédéfinis
- Entièrement compatible avec les types de données JSON ou Python
- Élimine le besoin de déboguer les sorties erronées

## Installation
**Installer la bibliothèque**

```
pip install outlines
```


## Exécution
**Connecter le modèle**

```
import outlines
from transformers import AutoTokenizer, AutoModelForCausalLM


MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"
model = outlines.from_transformers(
    AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto"),
    AutoTokenizer.from_pretrained(MODEL_NAME)
)
```


## Si vous ne codez pas
Je souhaite restreindre la réponse d'un modèle d'IA à une structure de données Pydantic spécifique ou à un type Python (par exemple int ou Literal) à l'aide de la bibliothèque Outlines. Comment puis-je utiliser la fonction model(request, output_type) après avoir défini l'objet modèle pour garantir que la sortie du modèle est toujours conforme au schéma souhaité ? Veuillez expliquer avec un exemple comment définir le modèle Pydantic pour les objets complexes et appliquer cette structure à la sortie du modèle.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/outlines/
