# Was ist Cloud Native?

Cloud Native ist ein Ansatz zur Anwendungsentwicklung, der die Flexibilität und Skalierbarkeit der Cloud voll ausschöpft.

## Definition und Wortherkunft
Das Konzept wird unter dem Dach der CNCF (Cloud Native Computing Foundation) zusammengefasst. Der entscheidende Unterschied hierbei ist: Eine Software in die Cloud hochzuladen, macht sie nicht zu Cloud Native. Cloud Native bedeutet, dass die Anwendung von Anfang an auf die dynamische Struktur der Cloud ausgerichtet und in kleine, unabhängige Teile zerlegt aufgebaut wird.

## Wie kann man es kennen und im täglichen Leben anwenden?
Verkehrsreiche Tage: Die automatische Kapazitätserweiterung, wenn sich der Traffic an Kampagnentagen vervielfacht.Fehlermoment: Die nahtlose Übernahme der Aufgaben durch eine andere Kopie, sollte ein Server abstürzen.Aktualisierung: Die schrittweise Erneuerung der Anwendung im laufenden Betrieb statt im abgeschlossenen Zustand.

## Technische Tiefe und Architektur
Teile des Cloud-Native-Stacks:

## Einsatz in verschiedenen Disziplinen
Fertigbauweise: Ein modulares Haus, das je nach Bedarf um Zimmer erweitert werden kann.Stromnetz: Kraftwerke, die sich je nach Bedarf zuschalten.Logistik: Verteilerlinien, die sich je nach Auslastung öffnen und schließen.

## Häufig gestellte Fragen
**Macht das Verlegen einer Anwendung in die Cloud diese zu einer Cloud-native-Anwendung?**
Nein. Das einfache Übertragen einer Altanwendung ändert nur den Standort. Für Cloud-native muss die Architektur in kleine Teile zerlegt und für die automatisierte Verwaltung geeignet sein.

**Ist das für ein kleines Projekt erforderlich?**
Nicht immer. Für einen Blog, der problemlos auf einem einzigen Server läuft, ist diese Einrichtung möglicherweise übertrieben. Sie ergibt Sinn, wenn der Traffic schwankt oder das Team wächst.

**Erhöht dies die Kosten?**
Es fallen Einrichtungs- und Einarbeitungskosten an. Im Gegenzug sinken die Ausfallzeiten und Skalierungskosten. Die Kalkulation muss an Ihre Workloads angepasst werden.

**Wo sollte man beginnen?**
Beginnen Sie damit, die Anwendung in einen Container zu packen. Fügen Sie dann Health Checks, Logging und automatisches Deployment hinzu. Orchestrierung ist der letzte Schritt.


## Verwandte Begriffe
- [Containers](/de/dictionary/containers/)
- [Virtual Machines](/de/dictionary/virtual-machines/)
- [Runtime](/de/dictionary/runtime/)

## Verwandte Werkzeuge
- [Meshery](/de/discover/meshery/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/cloud-native/
