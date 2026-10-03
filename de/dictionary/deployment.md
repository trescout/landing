# Was ist Deployment?

Deployment (Software-Deployment / Live-Schaltung) ist der Prozess, bei dem eine in einer lokalen Umgebung entwickelte und getestete Softwarekomponente kompiliert, auf Zielservern oder Cloud-Infrastrukturen installiert und für Endbenutzer zugänglich gemacht wird.

## Konzeptioneller Rahmen, Etymologie und historischer Wandel
Der Begriff Deployment leitet sich etymologisch aus der militärischen Terminologie ab und bezeichnet die Verlegung von Truppen, Munition oder Ausrüstung in strategische Gefechtspositionen, um sie einsatzbereit zu machen („to deploy“). In der Softwaretechnik begann er in den 1970er und 80er Jahren mit dem Laden von Lochkarten oder Magnetbändern auf Großrechner (Mainframes); er entwickelte sich in den 1990er Jahren zu manuell ausgeführten FTP/SSH-Dateiübertragungen und ist heute zu vollständig deklarativen und automatisierten Cloud-Pipelines (GitOps) mutiert.

## Strategien für unterbrechungsfreies Deployment (Zero-Downtime)
Die grundlegenden Deployment-Muster, die entwickelt wurden, damit Benutzer während der Aktualisierung von Anwendungen keine Dienstunterbrechungen erleben, sind folgende:

## CI/CD-Pipeline, GitOps und Datenbankmigrationen
Eine erfolgreiche Bereitstellungsarchitektur baut auf drei kritischen technischen Säulen auf:

## Fehlerbehandlung, Beobachtbarkeit und Rollback-Architektur
Selbst in den fortschrittlichsten Testumgebungen gibt es zwei wesentliche Rettungsringe für Produktionsfehler, die übersehen wurden:

## Häufig verwechselt mit

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
- [Runtime](/de/dictionary/runtime/)
- [Compile-time](/de/dictionary/compile-time/)
- [Cloud Computing](/de/dictionary/cloud-computing/)
- [Production Pipeline](/de/dictionary/production-pipeline/)
- [Tech Stack](/de/dictionary/tech-stack/)
- [Git Push](/de/dictionary/git-push/)

## Verwandte Werkzeuge
- [Rocket.Chat](/de/discover/rocket-chat/)
- [Chatwoot](/de/discover/chatwoot/)
- [Argo Cd](/de/discover/argo-cd/)
- [Openship](/de/discover/openship/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/deployment/
