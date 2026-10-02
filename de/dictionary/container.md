# Was ist Container?

Ein Container sorgt dafür, dass Code und Abhängigkeiten einer Anwendung in einem einzigen Paket in jeder Umgebung identisch ausgeführt werden.

## Definition und Wortherkunft
Container fassen den Code, die Bibliotheken und die Einstellungen einer Anwendung in einem einzigen Paket zusammen. Sie funktionieren auf dem Server genauso wie auf Ihrem Computer. Die Idee ist alt (chroot, LXC), wurde nach 2013 durch Docker populär gemacht und wird heute durch den OCI-Standard definiert.

## Wie kann man es kennen und im täglichen Leben anwenden?
Vertrieb: Dasselbe Paket vom Entwickler bis zur Live-Umgebung.Mikroservice: Jeder Dienst hat seine eigene Box.CI: Jeder Test läuft in einer sauberen Box ab.

## Technische Tiefe und Architektur
Konzepte:

## Häufig gemischte Dinge
Wird oft für eine virtuelle Maschine gehalten. Die Maschine enthält ein vollwertiges Betriebssystem, der Container nur die Anwendung. Die Isolierung ist bei der Maschine stärker, bei Containern ausreichend; die Wahl hängt von der Last ab.

## Einsatz in verschiedenen Disziplinen
Transport: Kompatibilität mit Schiffen, Zügen und Lastwagen durch standardisierte Containergrößen.Küche: Eine Fertiggerichte-Box mit allen Zutaten im Inneren.Camping: Ein ordentlich in seiner Tasche transportiertes Camping-Set.

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
- [Containers](/de/dictionary/containers/)
- [Virtual Machines](/de/dictionary/virtual-machines/)
- [Deployment](/de/dictionary/deployment/)

## Verwandte Werkzeuge
- [N8n](/de/discover/n8n/)
- [Stirling-PDF](/de/discover/stirling-pdf/)
- [Core](/de/discover/core/)
- [Container](/de/discover/container/)
- [Mattermost](/de/discover/mattermost/)
- [Keycloak](/de/discover/keycloak/)
- [Trivy](/de/discover/trivy/)
- [PPF Contact Solver](/de/discover/ppf-contact-solver/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/container/
