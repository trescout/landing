# Was ist Open Weight?

> Öffentlich zugängliche Modellgewichte

**Kategorie:** AI  
**Letzte Aktualisierung:** 2026-09-22

Open Weight bezeichnet KI-Modelle, deren trainierte Parametergewichte frei heruntergeladen werden können, sodass Entwickler das neuronale Netz auf eigener Hardware ausführen, quantisieren und anpassen können.

## Definition und Wortherkunft
Im Unterschied zu geschlossenen Cloud-APIs, die den Zugriff auf kostenpflichtige Token-Aufrufe beschränken, stellen Open-Weight-Modelle die rohen Tensordateien bereit. Dies ermöglicht volle Datenhoheit, Unabhängigkeit von externen Schnittstellen und verlustarme lokale Inferenz.

## Alltägliche Anwendung und Praxis
- **Lokale Inferenz auf Arbeitsplatzrechnern:** Ausführung quantisierter Sprachmodelle auf Laptops ohne ständige Internetverbindung.
- **Strikter Datenschutz:** Sensible Unternehmensdaten und Programmcode verlassen niemals das lokale Firmennetzwerk.
- **Kosteneffizienz bei hohen Volumina:** Ersetzung laufender API-Abonnements durch einmalig amortisierte Serverhardware.

## Technische Tiefe und Architektur
Technische Funktionsweise von Open Weights:- **Tensor-Formate:** Bereitstellung in modernen Safetensors- oder GGUF-Archiven mit 4-Bit- oder 8-Bit-Ganzzahlquantisierung.
- **Laufzeit-Engines:** Hochperformante Ausführung über Tools wie vLLM, Ollama, llama.cpp und TGI.
- **Ressourcenschonende Anpassung (PEFT):** Verhaltensoptimierung über leichtgewichtige LoRA-Adapter ohne Neuberechnung des Basismodells.

## Häufig verwechselt mit
Wird häufig mit vollwertiger Open-Source-KI verwechselt. Open Source verlangt die vollständige Offenlegung des Trainingscodes und der Datensätze; Open Weight stellt primär das fertige Zahlenwerk der trainierten Gewichte bereit.

## Interdisziplinäre Perspektiven
- **Backen:** Einen fertigen Vorteig erhalten und im eigenen Ofen frisch ausbacken vs. ein verpacktes Brot im Supermarkt kaufen.
- **Software:** Eine native Binärdatei lokal installieren vs. eine Cloud-SaaS-Lösung im Browser mieten.
- **Musik:** Zugriff auf die Original-Tonspuren für ein Remix haben vs. einen Song über einen Streaming-Dienst anhören.

## Als Analogie
Es gleicht dem Bereitstellen von Zutaten und Anleitung, sodass jeder das Gericht in seiner eigenen Küche frisch zubereiten und nachwürzen kann.

## Häufige Fragen

**Welche Möglichkeiten eröffnen offene Modellgewichte?**  
Sie können Modelle auf eigenen Servern hosten, für Mobilgeräte optimieren, mit eigenen Daten nachtrainieren und offline nutzen.

**Worin liegt der Hauptvorteil gegenüber geschlossenen APIs?**  
Vollständige Datenhoheit, Ausfallsicherheit ohne Internet und planbare Betriebskosten bei großen Anfragemengen.

**Welche Hardware wird für gängige 8B-Modelle benötigt?**  
Ein handelsüblicher Rechner mit 16 GB Arbeitsspeicher oder eine Grafikkarte mit 8 bis 12 GB VRAM reicht für 4-Bit-Modelle völlig aus.

**Dürfen Open-Weight-Modelle kommerziell eingesetzt werden?**  
Die meisten modernen Modellfamilien (wie Llama, Mistral und Qwen) gestatten die kommerzielle Nutzung im Rahmen ihrer Lizenzbedingungen ausdrücklich.

## Verwandte Begriffe
- [Open Source AI](/de/dictionary/open-source-ai/)
- [Foundation Model](/de/dictionary/foundation-model/)
- [SLM](/de/dictionary/slm/)

---
Quelle: TreScout Tech-Glossar · https://trescout.com/de/dictionary/open-weight/
