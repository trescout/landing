# Was ist Clone?

*Glossar · Dev · Zuletzt aktualisiert: 22. September 2026*

Ein Klon (auf Türkisch klonlama) ist der Prozess, bei dem eine lokale Kopie eines entfernten Git-Repositorys samt seiner gesamten Historie erstellt wird.

## Definition und Wortherkunft

"Clone" bedeutet auf Englisch exakte Kopie. In der Git-Welt wird es mit dem Befehl git clone verwendet: Sie laden damit nicht nur die aktuellen Dateien herunter, sondern die gesamte Commit-Historie, alle Branches und Tags des Projekts.

***Analogie:** Das ist so, als würde man nicht nur ein einziges Foto von einer Seite in der Bibliothek machen, sondern das gesamte Buch in Ihr eigenes Regal stellen.*

## Wie kann man es kennen und im täglichen Leben anwenden?

Wenn Sie ein Open-Source-Projekt untersuchen oder dazu beitragen möchten, ist der erste Schritt meistens das Klonen:

```
git clone https://github.com/kullanici/proje.git
```

Wenn der Befehl ausgeführt wird, wird im aktuellen Verzeichnis ein Projektordner erstellt. Wenn das Repository zu groß ist, wird ein flacher Klon verwendet, um nur einen Teil der Historie zu laden:

```
git clone --depth 1 https://github.com/kullanici/proje.git
```

## Technische Tiefe und Architektur

Das .git-Verzeichnis im geklonten Ordner ist das Gedächtnis des Repositories: Alle Commit-Objekte, Branch-Zeiger und Remote-Adressen befinden sich hier. Nach dem Klonen:

git fetch lädt Remoteverbesserungen herunter und berührt Ihre Dateien nicht.
git pull lädt Änderungen herunter und führt sie mit Ihrem aktuellen Branch zusammen.
git push sendet deine Commits an das Remote-Repository (sofern du die Berechtigung hast).
Ein Fork erstellt serverseitig eine Kopie. Ein Klon lädt diese Kopie oder das Original-Repository auf Ihren Computer herunter. Beides sind unterschiedliche Konzepte.

## Einsatz in verschiedenen Disziplinen

**Biologie:** Eine genetische Kopie eines Lebewesens. Ein Klon in der Software ist dagegen eine Kopie von Daten und hat nichts mit Lebewesen zu tun.
**Medien:** Ersatzkostüme, mit denen gearbeitet wird, während das Original geschont wird.
**Virtualisierung:** Erstellung einer neuen Maschine aus einer vorgefertigten Vorlage.

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

- [CLI](https://trescout.com/de/dictionary/cli/)
- [Open Source](https://trescout.com/de/dictionary/open-source/)
- [Self-Hosting](https://trescout.com/de/dictionary/self-hosting/)

## Verwandte Werkzeuge

- [MoneyPrinterTurbo](https://trescout.com/de/discover/moneyprinterturbo/)
- [VoxCPM](https://trescout.com/de/discover/voxcpm/)
- [Clone-Wars](https://trescout.com/de/discover/clone-wars/)
- [Univer](https://trescout.com/de/discover/univer/)
- [OpenStock](https://trescout.com/de/discover/openstock/)
- [Hermes WebUI](https://trescout.com/de/discover/hermes-webui/)
- [Production Agentic RAG Course](https://trescout.com/de/discover/production-agentic-rag-course/)
- [Flowsint](https://trescout.com/de/discover/flowsint/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/clone/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/clone/
