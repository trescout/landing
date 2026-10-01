# Was ist Clone?

Ein Klon (auf Türkisch klonlama) ist der Prozess, bei dem eine lokale Kopie eines entfernten Git-Repositorys samt seiner gesamten Historie erstellt wird.

## Definition und Wortherkunft
"Clone" bedeutet auf Englisch exakte Kopie. In der Git-Welt wird es mit dem Befehl git clone verwendet: Sie laden damit nicht nur die aktuellen Dateien herunter, sondern die gesamte Commit-Historie, alle Branches und Tags des Projekts.

## Wie kann man es kennen und im täglichen Leben anwenden?
Wenn Sie ein Open-Source-Projekt untersuchen oder dazu beitragen möchten, ist der erste Schritt meistens das Klonen:

## Technische Tiefe und Architektur
Das .git-Verzeichnis im geklonten Ordner ist das Gedächtnis des Repositories: Alle Commit-Objekte, Branch-Zeiger und Remote-Adressen befinden sich hier. Nach dem Klonen:

## Einsatz in verschiedenen Disziplinen
Biologie: Eine genetische Kopie eines Lebewesens. Ein Klon in der Software ist dagegen eine Kopie von Daten und hat nichts mit Lebewesen zu tun.Medien: Ersatzkostüme, mit denen gearbeitet wird, während das Original geschont wird.Virtualisierung: Erstellung einer neuen Maschine aus einer vorgefertigten Vorlage.

## Häufig gestellte Fragen
**Kann ich das Projekt nach dem Klonen ändern?**
Ja. Sie können in Ihrer eigenen Kopie beliebige Änderungen vornehmen. Das Original-Repository ist davon nicht betroffen. Wenn Sie Ihre Änderung für das Projekt vorschlagen möchten, öffnen Sie einen Pull Request.

**Was ist der Unterschied zwischen Fork und Clone?**
Ein Fork erstellt eine Kopie auf dem Server (in Ihrem Konto), ein Clone lädt diese Kopie auf Ihren Computer herunter. Der Beitrags-Workflow sieht in der Regel einen Fork gefolgt von einem Clone vor.

**Was sollte ich tun, wenn das Repository zu groß ist?**
Führen Sie einen flachen Klon mit --depth 1 durch oder laden Sie nur einen einzelnen Branch (--single-branch) herunter. Sie können den Verlauf später vertiefen, falls Sie ihn benötigen.

**Halte ich den Klon aktuell?**
Ja. Führen Sie einfach git pull im Ordner aus. Wenn Sie Änderungen haben, müssen Sie diese zuerst committen oder zwischenspeichern (git stash).


## Verwandte Begriffe
- [CLI](/de/dictionary/cli/)
- [Open Source](/de/dictionary/open-source/)
- [Self-Hosting](/de/dictionary/self-hosting/)

## Verwandte Werkzeuge
- [MoneyPrinterTurbo](/de/discover/moneyprinterturbo/)
- [VoxCPM](/de/discover/voxcpm/)
- [Clone-Wars](/de/discover/clone-wars/)
- [Univer](/de/discover/univer/)
- [OpenStock](/de/discover/openstock/)
- [Hermes WebUI](/de/discover/hermes-webui/)
- [Flowsint](/de/discover/flowsint/)
- [Production Agentic RAG Course](/de/discover/production-agentic-rag-course/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/clone/
