# Was ist Bindings?

Sie sind Brücken, die es verschiedenen Programmiersprachen ermöglichen, die Bibliotheken der jeweils anderen zu nutzen.

## Definition
Eine Bibliothek ist normalerweise in einer einzigen Sprache geschrieben (z. B. C++). Wenn Sie jedoch Python verwenden, können Sie diese Bibliothek nicht direkt verwenden. Binding ist eine Schnittstelle, die diese Bibliothek in eine Sprache übersetzt, die Python versteht. Auf diese Weise können Sie Sprachgrenzen überwinden und die besten Tools in der gewünschten Sprache nutzen.

## So funktioniert es
Entwickler erstellen eine kleine Codeschicht, die die Funktionen der Hauptbibliothek in die Zielsprache portiert. So funktionieren komplexe Operationen in der Hauptbibliothek wie ein einfacher Befehl in Ihrer eigenen Sprache.

## Wo es eingesetzt wird
Die meisten KI-Modelle sind in C++ geschrieben, aber dank Python-Bindungen können wir sie problemlos mit Python verwenden.

## Häufig verwechselt mit
Es kann mit der API verwechselt werden, aber während die API über das Netzwerk kommuniziert, handelt es sich bei der Bindung um eine Verbindung auf Speicherebene innerhalb desselben Computers.

## Häufige Fragen
**Warum ist nicht jede Bibliothek in jeder Sprache geschrieben?**
Low-Level-Sprachen (C++) werden aus Leistungsgründen bevorzugt, High-Level-Sprachen (Python) aus Gründen der Benutzerfreundlichkeit.

**Verlangsamt sich die Bindung?**
Obwohl es in der Regel zu leichten Leistungseinbußen kommt, lohnt sich der Komfort, den es bietet.


## Verwandte Begriffe
- [API](/de/dictionary/api/)
- [Framework](/de/dictionary/framework/)
- [Runtime](/de/dictionary/runtime/)

## Verwandte Werkzeuge
- [Turbovec](/de/discover/turbovec/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/bindings/
