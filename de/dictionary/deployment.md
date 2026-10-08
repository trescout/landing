# Was ist Deployment?

*Glossar · Dev · Zuletzt aktualisiert: 19. September 2026*

Deployment (Software-Deployment / Live-Schaltung) ist der Prozess, bei dem eine in einer lokalen Umgebung entwickelte und getestete Softwarekomponente kompiliert, auf Zielservern oder Cloud-Infrastrukturen installiert und für Endbenutzer zugänglich gemacht wird.

## Konzeptioneller Rahmen, Etymologie und historischer Wandel

Der Begriff Deployment leitet sich etymologisch aus der militärischen Terminologie ab und bezeichnet die Verlegung von Truppen, Munition oder Ausrüstung in strategische Gefechtspositionen, um sie einsatzbereit zu machen („to deploy“). In der Softwaretechnik begann er in den 1970er und 80er Jahren mit dem Laden von Lochkarten oder Magnetbändern auf Großrechner (Mainframes); er entwickelte sich in den 1990er Jahren zu manuell ausgeführten FTP/SSH-Dateiübertragungen und ist heute zu vollständig deklarativen und automatisierten Cloud-Pipelines (GitOps) mutiert.

In der modernen Softwaretechnik ist Deployment kein einmaliges, schmerzhaftes und mitten in der Nacht durchgeführtes Risikomanöver mehr. Dank Mechanismen für Continuous Integration und Continuous Delivery (CI/CD) ist es ein standardisierter Workflow, bei dem Code täglich hunderte Male sicher in die Produktionsumgebung übertragen wird.

***Analogie:** Es ähnelt dem Weichenwechsel eines Hochgeschwindigkeitszugs voller Passagiere. Bei der herkömmlichen Methode musste der Zug im Bahnhof angehalten und die Gleise zusammengeschweißt werden (Ausfallzeit / Downtime); modernes Deployment bedeutet hingegen, dass der Zug mit 300 Kilometern pro Stunde fährt, während eine automatische Weiche innerhalb von Millisekunden auf die neue Strecke umschaltet und die Passagiere nicht einmal einen Ruck spüren.*

## Strategien für unterbrechungsfreies Deployment (Zero-Downtime)

Die grundlegenden Deployment-Muster, die entwickelt wurden, damit Benutzer während der Aktualisierung von Anwendungen keine Dienstunterbrechungen erleben, sind folgende:

1. Blue-Green-Deployment: Es werden zwei identische Serverumgebungen vorgehalten, von denen eine den Live-Traffic bedient (Blau), während die sich andere im Leerlauf befindet (Grün). Der neue Code wird in der grünen Umgebung installiert, Smoketests werden durchgeführt und sobald alles einwandfrei funktioniert, leitet der Load Balancer den Traffic innerhalb von Millisekunden auf die grüne Umgebung um. Sollte ein Problem auftreten, wird sofort zu Blau zurückgewechselt (sofortiges Rollback).
2. Canary Deployment: Erhält seinen Namen daher, dass Bergleute im 19. Jahrhundert Kanarienvögel in Käfigen mit in die Kohleminen nahmen, um giftige Gase frühzeitig zu erkennen. Die neue Version wird zunächst nur für 1 bis 5 Prozent des gesamten Nutzertraffics freigegeben. Fehlerraten (HTTP 5xx), Speicherverbrauch und Antwortzeiten werden überwacht; läuft das System stabil, wird der Anteil schrittweise auf 25, 50 und 100 Prozent erhöht.
3. Rolling Deployment: Das nacheinander stattfindende Aktualisieren von Containern (z. B. in Portionen von 20 %) in Kubernetes-Clustern oder Serverflotten. Alte Pods werden der Reihe nach heruntergefahren und durch Pods der neuen Version ersetzt. Dies erfordert keine zusätzlichen Hardwarekosten für Backups, setzt jedoch die Verwaltung eines Übergangszeitraums voraus, in dem zwei verschiedene Versionen gleichzeitig live sind.
4. Dark Deployment (Shadow Deployment): Der Live-Benutzerverkehr wird dupliziert (Traffic Mirroring) und an die im Hintergrund laufende neue Version gesendet. Die von der neuen Version generierten Antworten werden jedoch nicht an den Benutzer übermittelt; stattdessen werden lediglich die Leistung des Systems unter realer Last und die Genauigkeit des Algorithmus gemessen.

## CI/CD-Pipeline, GitOps und Datenbankmigrationen

Eine erfolgreiche Bereitstellungsarchitektur baut auf drei kritischen technischen Säulen auf:

- CI/CD-Automatisierung und DORA-Metriken: Wenn ein Entwickler einen Commit in ein Git-Repository pusht, wird der Code automatisch auf Linting geprüft, Unit- und Integrationstests werden ausgeführt, ein Docker-Container-Image wird erstellt und in der Zielumgebung bereitgestellt. Laut den Metriken von DevOps Research and Assessment (DORA) verkürzen hochleistungsfähige Teams die Bereitstellungshäufigkeit (Deployment Frequency) auf ein Niveau von Stunden, während sie die Durchlaufzeit für Änderungen (Lead Time) und die Fehlerrate auf ein Minimum reduzieren.
- GitOps-Prinzip: Infrastruktur und Anwendungsversionen werden direkt über ein Git-Repository mit Tools wie ArgoCD oder Flux deklariert. Das Git-Repository ist die einzige Wahrheitsquelle (Single Source of Truth); weicht der tatsächliche Zustand auf den Servern vom Zustand in Git ab, synchronisiert sich das System automatisch.
- Datenbank-Schema-Dilemma (Expand-Contract-Muster): Code kann mit null Ausfallzeit aktualisiert werden, aber das Löschen einer Spalte in Datenbanktabellen kann zum Absturz der alten Version führen. Aus diesem Grund wenden Ingenieure das „Expand-Contract“-Muster (Parallel Run) an: Zuerst wird die neue Spalte hinzugefügt und in beide Versionen geschrieben, und nachdem alle Server auf die neue Version umgestellt wurden, wird die alte Spalte sicher gelöscht.

## Fehlerbehandlung, Beobachtbarkeit und Rollback-Architektur

Selbst in den fortschrittlichsten Testumgebungen gibt es zwei wesentliche Rettungsringe für Produktionsfehler, die übersehen wurden:

- Automatisches Rollback: Sobald APM-Tools (Datadog, Prometheus) bei Fehlerschwellenwerten (z. B. wenn die Fehlerrate 1 % übersteigt) eine Anomalie erkennen, kehren sie ohne menschliches Eingreifen zum vorherigen stabilen Docker-Image oder Git-Tag zurück.
- Feature Flags (Funktions-Flags): Trennen Bereitstellung (Deployment) und Freigabe (Release) voneinander. Selbst wenn der Code auf dem Server läuft, kann ein neues Feature in der Benutzeroberfläche deaktiviert bleiben; bei einem riskanten Zwischenfall lässt es sich über einen einzigen Dashboard-Schalter sofort ausschalten.

## Häufig verwechselt mit

- Development vs Deployment: Development ist, wenn der Koch in der Küche das Gericht zubereitet und probiert; Deployment ist, wenn das Gericht an den Tisch serviert und dem Kunden zum Verzehr angeboten wird.
- Deployment vs. Release: Deployment ist ein technischer Vorgang und bezeichnet das Laden des Codes auf den Server. Ein Release hingegen bedeutet, dass eine Funktion für die Nutzer sichtbar gemacht, die Marketingankündigung durchgeführt und sie vom Fachbereich offiziell freigeschaltet wird.

## Häufige Fragen

**Was bedeutet Deployment und wie lautet die deutsche Entsprechung?**

Es ist ein aus dem Englischen stammendes Wort und bedeutet „Bereitstellung“ oder „Liveschaltung“. Es ist der Prozess, bei dem ein Softwarepaket kompiliert und auf Zielservern oder in einer Cloud-Umgebung lauffähig gemacht wird.

**Was ist der Unterschied zwischen Deployment und Release?**

Deployment ist die technische Installation und Ausführung des Codes auf dem Server. Ein Release hingegen ist die offizielle Freigabe des Features für den Endbenutzer durch Feature Flags oder Marketingmaßnahmen.

**Was ist der Hauptunterschied zwischen Blue-Green- und Canary-Deployment?**

Beim Blue-Green-Deployment gibt es zwei identische Umgebungen, und der Datenverkehr wird auf einen Schlag über einen Load Balancer zu 100 % auf die neue Umgebung umgeschaltet. Beim Canary-Deployment hingegen wird die neue Version schrittweise zuerst einer kleinen Benutzergruppe von 1-5 % zur Verfügung gestellt, und der Prozentsatz wird nach Beobachtung der Metriken erhöht.

**Wie werden Datenbank-Schemataänderungen bei einem Zero-Downtime-Deployment verwaltet?**

Sie werden mit dem Expand-Contract-Muster (Erweitern und Reduzieren) verwaltet. Zuerst werden abwärtskompatible neue Felder hinzugefügt; nachdem alle Server des Systems auf den neuen Code umgestellt wurden und der Datenfluss gewährleistet ist, werden die alten Felder bereinigt.

## Verwandte Begriffe

- [Runtime](https://trescout.com/de/dictionary/runtime/)
- [Compile-time](https://trescout.com/de/dictionary/compile-time/)
- [Cloud Computing](https://trescout.com/de/dictionary/cloud-computing/)
- [Production Pipeline](https://trescout.com/de/dictionary/production-pipeline/)
- [Tech Stack](https://trescout.com/de/dictionary/tech-stack/)
- [Git Push](https://trescout.com/de/dictionary/git-push/)

## Verwandte Werkzeuge

- [Rocket.Chat](https://trescout.com/de/discover/rocket-chat/)
- [Chatwoot](https://trescout.com/de/discover/chatwoot/)
- [Argo Cd](https://trescout.com/de/discover/argo-cd/)
- [Openship](https://trescout.com/de/discover/openship/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/deployment/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/deployment/
