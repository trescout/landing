# Was ist Protocol Buffers?

> Protobuf

Dabei handelt es sich um eine Methode, die es unterschiedlicher Software ermöglicht, Daten sehr schnell und in kleinen Größen zu verpacken und zu transportieren, während sie miteinander kommunizieren.

## Definition
Software verwendet normalerweise Textdateien, wenn sie Daten untereinander senden, diese Dateien können jedoch manchmal sehr groß sein. Protokollpuffer wandeln Daten in ein Binärformat um, sodass sie viel weniger Platz beanspruchen und viel schneller übertragen werden können. Es wurde von Google entwickelt und gilt heute als Standard in der systemübergreifenden Kommunikation.

## So funktioniert es
Sie definieren zunächst die Struktur der Daten in einer Vorlagendatei. Anschließend verpackt Ihre Software die Daten mithilfe dieser Vorlage und sendet sie an die andere Partei. Die empfangende Seite stellt die Daten mithilfe derselben Vorlage wieder her.

## Wo es eingesetzt wird
Es wird in Microservice-Architekturen, der Kommunikation mobiler Anwendungen mit Servern und Systemen verwendet, die eine hohe Leistung erfordern.

## Häufig verwechselt mit
Es kann mit textbasierten Datenformaten wie JSON oder XML verwechselt werden, ist aber viel schneller und kleiner.

## Häufige Fragen
**Können Menschen lesen?**
Nein, die Daten können nicht direkt von Menschen gelesen werden, da sie im Binärformat vorliegen. Sie sind so konzipiert, dass nur Computer sie verstehen können.


## Verwandte Begriffe
- [API](/de/dictionary/api/)
- [Networking Stack](/de/dictionary/networking-stack/)
- [Serialization](/de/dictionary/serialization/)

## Verwandte Werkzeuge
- [Protobuf](/de/discover/protobuf/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/protocol-buffers/
