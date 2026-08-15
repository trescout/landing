# Konfigurieren Sie AI-Ausgaben

Die Outlines-Bibliothek ermöglicht die Darstellung der Antworten großer Sprachmodelle als strukturierte Ausgaben nach vordefinierten Schemata. Mit diesem Python-basierten Tool schützen Entwickler die Datenintegrität, indem sie Modellausgaben mit regulären Ausdrücken oder kontextfreien Grammatikregeln einschränken.

- ★ 15.525
- Python
- GitHub Trending · 2026-07-22

## Aktualisieren
- 7. August 2026: Stern 15.477 → 15.525, letzte Version 1.3.3 (6. August 2026).
- 2. August 2026: Star 14.917 → 15.477, letzte Version 1.3.2 (20. Juli 2026).

## Was es bringt
- Schränkt Modellausgaben gemäß vordefinierten Schemata ein
- Vollständig kompatibel mit JSON- oder Python-Datentypen
- Eliminiert die Notwendigkeit, fehlerhafte Ausgaben zu debuggen

## Installation
**Installieren Sie die Bibliothek**

```
pip install outlines
```


## Ausführung
**Schließen Sie das Modell an**

```
import outlines
from transformers import AutoTokenizer, AutoModelForCausalLM


MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"
model = outlines.from_transformers(
    AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto"),
    AutoTokenizer.from_pretrained(MODEL_NAME)
)
```


## Wenn Sie nicht programmieren
Ich möchte die Antwort eines KI-Modells mithilfe der Outlines-Bibliothek auf eine bestimmte Pydantic-Datenstruktur oder einen bestimmten Python-Typ (z. B. int oder Literal) beschränken. Wie kann ich nach der Definition des Modellobjekts die Funktion model(request, output_type) verwenden, um sicherzustellen, dass die Ausgabe des Modells immer dem gewünschten Schema entspricht? Bitte erläutern Sie anhand eines Beispiels, wie Sie das Pydantic-Modell für komplexe Objekte definieren und diese Struktur auf die Modellausgabe anwenden.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/outlines/
