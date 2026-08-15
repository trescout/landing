# Bereiten Sie PDF-Daten für KI vor

OpenDataLoader PDF ist ein Open-Source-PDF-Parser, der Daten für Modelle der künstlichen Intelligenz verfügbar macht. Dieses Java-basierte Projekt beschleunigt Datenverarbeitungsprozesse, indem es die Zugänglichkeit von PDF-Dokumenten automatisiert.

- ★ 28.095
- Java
- GitHub Trending · 2026-06-04

## Aktualisieren
- 2. August 2026: Star 23.530 → 28.095, neueste Version v2.5.0 (14. Juli 2026).

## Was es bringt
- Konvertiert PDF-Dateien in das Markdown-, JSON- oder HTML-Format für KI-Modelle.
- Bietet hochpräzise Datenextraktion für gescannte Dokumente und komplexe Tabellen.
- Markiert PDF-Dateien automatisch gemäß den Barrierefreiheitsstandards.

## Installation
**Installation mit Python**

```
pip install -U opendataloader-pdf
```

**Installation mit Hybridmodus**

```
pip install -U "opendataloader-pdf[hybrid]"
```


## Ausführung
**PDF-Konvertierungsprozess**

```
import opendataloader_pdf

# Batch all files in one call — each convert() spawns a JVM process, so repeated calls are slow
opendataloader_pdf.convert(
    input_path=["file1.pdf", "file2.pdf", "folder/"],
    output_dir="output/",
    format="markdown,json"
)
```


## Wenn Sie nicht programmieren
Ich möchte meine PDF-Dateien mit dem PDF-Tool OpenDataLoader analysieren und in strukturierte Datenformate (Markdown oder JSON) konvertieren, die ich in RAG- oder LLM-Prozessen verwenden kann. Können Sie mir helfen, mit dem Python SDK ein Skript zu erstellen, das auf meinem lokalen Computer ausgeführt wird und Tabellen, Überschriften und Text in der richtigen Lesereihenfolge aus meinen Dokumenten extrahiert? Erklären Sie außerdem Schritt für Schritt, wie Sie den Hybridmodus für komplexe Seiten aktivieren und die Ausgabe anpassen.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/opendataloader-pdf/
