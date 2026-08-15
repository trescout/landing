# Führen Sie riesige KI-Modelle mit 4 GB VRAM aus

AirLLM ermöglicht die Ausführung großer Sprachmodelle mit 70 Milliarden Parametern auf Grafikprozessoren mit nur 4 GB Videospeicher (VRAM). Diese Bibliothek nutzt Techniken zur Speicheroptimierung, um die Verwendung von Modellen mit hoher Kapazität und geringen Hardwareanforderungen zu ermöglichen.

- ★ 30.796
- Jupyter Notebook
- GitHub Trending · 2026-06-04

## Aktualisieren
- 12. August 2026: Star 29.265 → 30.796, neueste Version v3.1.0 (29. Juli 2026).
- 6. August 2026: Star 27.522 → 29.265, neueste Version v3.1.0 (29. Juli 2026).
- 4. August 2026: Star 25.416 → 27.522, neueste Version v3.1.0 (29. Juli 2026).
- 2. August 2026: Star 19.113 → 25.416, neueste Version v3.1.0 (29. Juli 2026).

## Was es bringt
- Möglichkeit, Modelle mit 70B-Parametern mit 4 GB VRAM zu betreiben.
- Möglichkeit zur Verwendung von 405B Llama3.1-Modellen mit 8 GB VRAM.
- Bis zu dreifache Geschwindigkeitssteigerung durch blockbasierte Komprimierung.

## Installation
**Paketinstallation**

```
pip install airllm
```


## Ausführung
**Laden Sie das Modell und führen Sie es aus**

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


## Wenn Sie nicht programmieren
Ich möchte ein Modell mit 70B-Parametern mithilfe der AirLLM-Bibliothek auf meiner Grafikkarte mit geringer VRAM-Kapazität ausführen. Für die Installation habe ich den Befehl pip install airllm verwendet. Wie kann ich mithilfe der AutoModel-Klasse die Python-Codestruktur erstellen, die zum Laden meines Modells und zur Ausgabe mit einer einfachen Texteingabe erforderlich ist? Ich weiß, dass ich sicherstellen muss, dass ich während des Vorgangs über genügend Speicherplatz verfüge. Können Sie mir die grundlegenden Schritte erklären, die ich befolgen muss, um den Vorgang zu starten?

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/airllm/
