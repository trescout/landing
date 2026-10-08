# Was ist Jailed?

*Glossar · Dev · Zuletzt aktualisiert: 29. September 2026*

Dabei handelt es sich um eine Situation, in der ein Programm in einem isolierten und eingeschränkten Bereich ausgeführt wird, sodass es nicht auf den Rest des Betriebssystems zugreifen kann.

## Definition

„Gesperrt“ bezieht sich auf den Sicherheitszustand, in dem ein Softwareprozess nur auf das Dateiverzeichnis, den Speicher und die Netzwerkressourcen zugreifen kann, für die er zulässig ist. Diese auf Betriebssystemebene angewendete Einschränkung verhindert, dass das Programm dem Hostsystem oder anderen Benutzern Schaden zufügt. Es schafft eine wichtige Verteidigungslinie beim Testen von nicht vertrauenswürdigem Code oder beim Eingrenzen des Malware-Risikos.

***Analogie:** Es ist, als ob man einen Gast im Haus nur im Gästezimmer sitzen lässt und alle anderen Türen verschließt, anstatt ihm den Zugang zu allen Zimmern zu erlauben.*

## So funktioniert es

Der Betriebssystemkern beschränkt den Stamm des Prozesses und seine Systemaufrufe auf spezielle Einschränkungen. Obwohl der Prozess denkt, dass er sich auf dem Hauptsystem befindet, kann er tatsächlich nur ein virtuelles Unterverzeichnis sehen. Wenn ein Programm in diesem isolierten Bereich abstürzt oder angegriffen wird, bleibt der Schaden nur in diesem eingeschränkten Bereich bestehen.

## Wo es eingesetzt wird

Es wird häufig zur Trennung von Benutzeraktionen auf Webservern, in Anwendungen, die Plug-Ins ausführen, und in Online-Codeausführungsplattformen verwendet.

## Häufig verwechselt mit

Es kommt dem Konzept der Sandbox sehr nahe; Jail ist jedoch ein traditionellerer Begriff, der sich im Allgemeinen auf die Dateisystemisolation auf Unix/Linux-Systemen konzentriert (wie Chroot oder FreeBSD Jail).

## Häufige Fragen

**Kann ein eingesperrtes Programm auf das Hauptsystem zugreifen?**

Unter normalen Umständen nein. Diese Grenzwerte können jedoch überschritten werden, wenn eine Schwachstelle auf Kernel-Ebene (Jailbreak-Schwachstelle) gefunden wird.

**Sind Container-Technologien auch Gefängnisse?**

Moderne Containerstrukturen (wie Docker) sind eine viel fortschrittlichere und funktionsreichere Weiterentwicklung der traditionellen Gefängnislogik.

## Verwandte Begriffe

- [Sandbox](https://trescout.com/de/dictionary/sandbox/)
- [Containers](https://trescout.com/de/dictionary/containers/)
- [Runtime](https://trescout.com/de/dictionary/runtime/)
- [Security Scanner](https://trescout.com/de/dictionary/security-scanner/)

## Verwandte Werkzeuge

- [Madeira](https://trescout.com/de/discover/madeira/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/jailed/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/jailed/
