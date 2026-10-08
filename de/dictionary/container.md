# Was ist Container?

*Glossar · Dev · Zuletzt aktualisiert: 22. September 2026*

Ein Container sorgt dafür, dass Code und Abhängigkeiten einer Anwendung in einem einzigen Paket in jeder Umgebung identisch ausgeführt werden.

## Definition und Wortherkunft

Container fassen den Code, die Bibliotheken und die Einstellungen einer Anwendung in einem einzigen Paket zusammen. Sie funktionieren auf dem Server genauso wie auf Ihrem Computer. Die Idee ist alt (chroot, LXC), wurde nach 2013 durch Docker populär gemacht und wird heute durch den OCI-Standard definiert.

***Analogie:** Es ist so, als würde man alle notwendigen Zutaten, Gewürze und Werkzeuge für ein Gericht in eine einzige Box packen und dorthin mitnehmen, wo immer man möchte; egal wo Sie sie öffnen, Sie kochen immer dasselbe Gericht.*

## Wie kann man es kennen und im täglichen Leben anwenden?

**Vertrieb:** Dasselbe Paket vom Entwickler bis zur Live-Umgebung.
**Mikroservice:** Jeder Dienst hat seine eigene Box.
**CI:** Jeder Test läuft in einer sauberen Box ab.

## Technische Tiefe und Architektur

Konzepte:

**Image:** Schreibgeschützte Vorlage, besteht aus Schichten.
**Container:** Die laufende Instanz des Images.
**Dockerfile:** Das Rezept für die Vorlage.
**Registry:** Ein Repository, in dem Images gespeichert werden.

Eine einfache Beschreibung:

```
FROM python:3.12-slim
COPY . /uygulama
WORKDIR /uygulama
CMD ["python", "app.py"]
```

Erstellen und Ausführen:

```
docker build -t ornek:1.0 .
docker run -p 8000:8000 ornek:1.0
```

Der Unterschied zur virtuellen Maschine: Die Maschine bringt ihr eigenes Betriebssystem mit, der Container teilt sich den Host-Kernel. Daher sind Container schlanker und starten schneller.

## Häufig gemischte Dinge

Wird oft für eine virtuelle Maschine gehalten. Die Maschine enthält ein vollwertiges Betriebssystem, der Container nur die Anwendung. Die Isolierung ist bei der Maschine stärker, bei Containern ausreichend; die Wahl hängt von der Last ab.

## Einsatz in verschiedenen Disziplinen

**Transport:** Kompatibilität mit Schiffen, Zügen und Lastwagen durch standardisierte Containergrößen.
**Küche:** Eine Fertiggerichte-Box mit allen Zutaten im Inneren.
**Camping:** Ein ordentlich in seiner Tasche transportiertes Camping-Set.

## Häufig gestellte Fragen

**Warum ist der Container so beliebt?**

Da es in jeder Umgebung dieselbe Arbeit und eine schnelle Einrichtung ermöglicht. Es ist zusammen mit Microservices und Cloud-Orchestrierung zum Standard geworden.

**Was ist der Unterschied zwischen einem Container und einer virtuellen Maschine?**

Die Maschine bringt ihr eigenes Betriebssystem mit, der Container teilt sich den Host-Kernel. Der Container ist leicht und schnell, die Maschine ist stark in der Isolation.

**Ist ein Container sicher?**

Da der Kernel geteilt wird, ist er nicht so isoliert wie eine Maschine. Sie müssen Images aus einer vertrauenswürdigen Quelle beziehen und aktuell halten.

**Wann wird eine virtuelle Maschine bevorzugt?**

Wenn ein anderes Betriebssystem oder eine starke Isolation erforderlich ist. Für die meisten anderen Workloads reicht ein Container aus.

## Verwandte Begriffe

- [Containers](https://trescout.com/de/dictionary/containers/)
- [Virtual Machines](https://trescout.com/de/dictionary/virtual-machines/)
- [Deployment](https://trescout.com/de/dictionary/deployment/)

## Verwandte Werkzeuge

- [N8n](https://trescout.com/de/discover/n8n/)
- [Stirling-PDF](https://trescout.com/de/discover/stirling-pdf/)
- [Core](https://trescout.com/de/discover/core/)
- [Container](https://trescout.com/de/discover/container/)
- [Mattermost](https://trescout.com/de/discover/mattermost/)
- [Keycloak](https://trescout.com/de/discover/keycloak/)
- [Trivy](https://trescout.com/de/discover/trivy/)
- [PPF Contact Solver](https://trescout.com/de/discover/ppf-contact-solver/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/container/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/container/
