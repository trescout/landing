# Konfigurieren Sie AI-Ausgaben

Die Outlines-Bibliothek ermöglicht die Darstellung der Antworten großer Sprachmodelle als strukturierte Ausgaben nach vordefinierten Schemata. Mit diesem Python-basierten Tool schützen Entwickler die Datenintegrität, indem sie Modellausgaben mit regulären Ausdrücken oder kontextfreien Grammatikregeln einschränken.

- ★ 15.525
- Python
- GitHub Trending · 2026-07-22

## Aktualisierungen

- **7. August 2026:** Sterne 15,477 → 15,525, neueste Version 1.3.3 (6. August 2026).
- **2. August 2026:** Sterne 14,917 → 15,477, neueste Version 1.3.2 (20. Juli 2026).

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

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte die Antwort eines KI-Modells mithilfe der Outlines-Bibliothek auf eine bestimmte Pydantic-Datenstruktur oder einen bestimmten Python-Typ (z. B. int oder Literal) beschränken. Wie kann ich nach der Definition des Modellobjekts die Funktion model(request, output_type) verwenden, um sicherzustellen, dass die Ausgabe des Modells immer dem gewünschten Schema entspricht? Bitte erläutern Sie anhand eines Beispiels, wie Sie das Pydantic-Modell für komplexe Objekte definieren und diese Struktur auf die Modellausgabe anwenden.

## Verwandte Begriffe aus dem Glossar

- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es richtet sich an Entwickler, die unregelmäßige Textausgaben von KI-Modellen in strukturierte Daten umwandeln möchten, die direkt in Softwareprozessen verwendet werden können.
- **Lizenz:** Apache-2.0

## Links

- [GitHub-Repository →](https://github.com/dottxt-ai/outlines)
- [Auf Türkisch lesen →](https://trescout.com/discover/outlines/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-07-22 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/outlines/
