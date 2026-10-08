# Configurer les sorties IA

La bibliothèque Outlines permet de présenter les réponses de grands modèles de langage sous forme de sorties structurées selon des schémas prédéfinis. Avec cet outil basé sur Python, les développeurs protègent l'intégrité des données en limitant les sorties du modèle avec des expressions régulières ou des règles de grammaire sans contexte.

- ★ 15 525
- Python
- GitHub Trending · 2026-07-22

## Mises à jour

- **7 août 2026:** Étoiles 15,477 → 15,525, dernière version 1.3.3 (6 août 2026).
- **2 août 2026:** Étoiles 14,917 → 15,477, dernière version 1.3.2 (20 juillet 2026).

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

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite restreindre la réponse d'un modèle d'IA à une structure de données Pydantic spécifique ou à un type Python (par exemple int ou Literal) à l'aide de la bibliothèque Outlines. Comment puis-je utiliser la fonction model(request, output_type) après avoir défini l'objet modèle pour garantir que la sortie du modèle est toujours conforme au schéma souhaité ? Veuillez expliquer avec un exemple comment définir le modèle Pydantic pour les objets complexes et appliquer cette structure à la sortie du modèle.

## Termes liés du glossaire

- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il s'adresse aux développeurs qui souhaitent convertir les sorties de texte irrégulières des modèles d'IA en données structurées pouvant être utilisées directement dans les processus logiciels.
- **Licence:** Apache-2.0

## Liens

- [Dépôt GitHub →](https://github.com/dottxt-ai/outlines)
- [Lire en turc →](https://trescout.com/discover/outlines/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-07-22 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/outlines/
