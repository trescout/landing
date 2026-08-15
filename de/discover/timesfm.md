# KI-Prognose für Zeitreihen

Das von Google Research entwickelte Time Series Foundation Model bietet eine vorab trainierte Struktur für die Zeitreihenvorhersage. Das Modell ist darauf ausgelegt, allgemeine Vorhersagefunktionen für verschiedene Datensätze bereitzustellen.

- ★ 27.185
- Python
- GitHub Trending · 2026-06-18

## Aktualisieren
- 2. August 2026: Star 22.167 → 27.185, neueste Version v2.0.2 (2. Juli 2026).

## Was es bringt
- Schnelle Vorhersage mit vorab trainiertem Basismodell
- Unterstützung für 16 KB Kontextlänge
- Anpassung an unterschiedliche Datensätze mit flexibler Struktur

## Installation
**Installation über PyPI**

```
pip install timesfm[torch]
# Or with Flax
pip install timesfm[flax]
# And when XReg is needed
pip install timesfm[xreg]
```

**lokale Installation**

```
git clone https://github.com/google-research/timesfm.git
    cd timesfm
```


## Wenn Sie nicht programmieren
Ich möchte Zeitreihenvorhersagen mithilfe der TimesFM-Bibliothek durchführen. Wie kann ich die 200M-Parameterstruktur mit Version 2.5 dieses von Google entwickelten Basismodells konfigurieren? Wie sollte ich die Werte max_context und max_horizon bestimmen, insbesondere während der Kompilierungsphase des Modells, und in welchem ​​Format sollte ich Dateneingaben für die Prognosefunktion bereitstellen? Können Sie dies anhand einer Beispielcodestruktur erklären?

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/timesfm/
