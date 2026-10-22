# Was ist Patch?

*Entwicklung · Zuletzt aktualisiert: 19. September 2026*

Ein Patch ist ein Code- und Datei-Update, das veröffentlicht wird, um Fehler in einer Software zu beheben, Sicherheitslücken zu schließen oder bestehende Funktionen zu verbessern.

## 1. Patch in der Software- und Spielewelt

Traditionell ist es ineffizient, bei einem Programmfehler die gesamte Software von Grund auf neu herunterzuladen und zu installieren, sowohl in Bezug auf die Bandbreite als auch auf die Zeit. Ein Patch wendet nur die geänderten Bytes oder Dateien auf das Zielsystem an.

- Sicherheits-Patches: Werden dringend bereitgestellt, um kritische Sicherheitslücken (CVE) und Zero-Day-Schwachstellen zu schließen.
- Fehlerbehebungen (Bug Fixes): Behebt logische Fehler, die die Stabilität beeinträchtigen oder zu unerwarteten Abstürzen führen.
- Spiel-Patches und Balancings: Updates in Online-Multiplayer-Spielen, die Charakterfähigkeiten ausbalancieren, neue Inhalte hinzufügen und die Leistung optimieren. Sie werden in der Regel zusammen mit detaillierten Patch-Notes veröffentlicht.
- Hotfix: Ein eng gefasster Patch, der unverzüglich veröffentlicht wird, um einen kritischen Fehler in der Produktionsumgebung zu beheben, ohne den Testzyklus abzuwarten.

***Analogie:** Es ist vergleichbar damit, ein passendes Stück Stoff auf einen kleinen Riss in Ihrer Kleidung zu nähen, anstatt das gesamte Kleidungsstück wegzuwerfen. Es ersetzt nur die fehlerhaften Teile, ohne die gesamte Software neu herunterladen zu müssen.*

## 2. Patches in Entwicklertools: UNIX patch und Git

In der Open-Source-Welt und in Versionskontrollsystemen ist ein Patch ein Klartextdokument, das den Unterschied (Diff) zwischen zwei Dateien oder Commits darstellt.

### Der UNIX patch-Befehl und seine Geschichte

Der Begriff „Patch“, der historisch auf der Metapher des Abklebens von Löchern in Lochkarten oder der Reparatur von Papierstreifen basiert, wurde 1985 durch den von Larry Wall geschriebenen patch-Befehl standardisiert. Ein mit dem Befehl diff -u alt.c neu.c > korrektur.patch erstellter Patch kann beim Empfänger mit patch \< korrektur.patch direkt auf den Quellcode angewendet werden.

### Verwendung von Patches in der Git-Umgebung

Git bietet fortschrittliche Werkzeuge, um Patches über Mailinglisten oder Offline-Kanäle zu übertragen:

- git format-patch: Wandelt bestimmte Commits zusammen mit Autoreninformationen, Commit-Nachricht und Code-Diff in E-Mail-freundliche .patch-Dateien um.
- git apply: Wendet eine Patch-Datei direkt auf das Arbeitsverzeichnis an, ohne einen Commit zu erstellen.
- git am: Liest Patches im E-Mail-Format und erstellt automatisch Commits unter Beibehaltung der ursprünglichen Autoren- und Zeitinformationen (besonders bei der Entwicklung des Linux-Kernels ein Standard).

## 3. Webarchitektur und HTTP PATCH in REST-APIs

Bei der Aktualisierung von Daten in RESTful-Services werden häufig die Methoden PUT und PATCH miteinander verglichen:

- PUT (Vollständige Ersetzung): Sendet die gesamte Ressource erneut. Nicht angegebene Felder werden in der Regel auf den Standardwert zurückgesetzt oder gelöscht. Der PUT-Vorgang ist idempotent (das wiederholte Senden derselben Anfrage führt zum gleichen Ergebnis).
- PATCH (Teilweises Update – RFC 5789): Sendet einen Body, der nur die zu ändernden Felder enthält. Um beispielsweise nur die E-Mail-Adresse eines Benutzers zu aktualisieren, reicht es aus, nur das entsprechende Feld zu übermitteln, anstatt das gesamte Profilobjekt zu senden.
- JSON Patch (RFC 6902) ist eine Struktur, die Sequenzen atomarer Operationen wie add, remove, replace, move, copy und test definiert, um Änderungen zu standardisieren.

## Vergleichende Zusammenfassung: "Patch" in verschiedenen Kontexten

| Kontext | Was bedeutet es? | Hauptzweck | Typisches Beispiel |
|---|---|---|---|
| Software & Betriebssystem | Update-Paket | Schließen von Sicherheitslücken, Stabilität | Windows Update KB-Patch, Zero-Day-Patch |
| Spielewelt | Inhalts- und Balance-Update | Gameplay-Balance, Performance, Meta-Änderung | Saison-Patch (Patch 14.2), Balancing-Update |
| Git & Versionskontrolle | Zeilenbasierte Änderungsdatei | Code-Sharing, Code-Review, Mitwirkung | git format-patch HEAD~1, linux-kernel.patch |
| Web-API / HTTP | Partielle Update-Methode | Netzwerkeinsparung, partielle Änderung an der Ressource | PATCH /api/users/42 body: {"status": "active"} |

## Fragen und Antworten

**Was bedeutet Patch, was ist die türkische Entsprechung?**

Die deutsche Entsprechung ist „Patch“ oder „Fehlerbehebung“. Es bezieht sich auf Code-Fragmente, die einen bestimmten Teil eines Systems oder einer Software reparieren oder aktualisieren, ohne das gesamte System auszutauschen.

**Was ist der Unterschied zwischen einem Hotfix und einem Patch?**

Ein Patch wird in der Regel mit geplanten Releases (z. B. monatliche Sicherheitsbulletins) nach umfassenden Tests veröffentlicht. Ein Hotfix hingegen ist ein ungeplanter, schneller Eingriff, der erstellt wurde, um einen dringenden Absturz oder eine Sicherheitslücke in der Produktionsumgebung sofort zu beheben.

**Was ist der grundlegende Unterschied zwischen HTTP PUT und HTTP PATCH?**

PUT zielt auf den vollständigen Austausch (Replace) der Ressource ab und liefert bei Wiederholung derselben Anfrage das gleiche Ergebnis (idempotent). PATCH hingegen ändert nur die angegebenen Felder der Ressource teilweise (Partial Update) und muss nicht in jedem Szenario idempotent sein.

**Warum werden in Git-Umgebungen immer noch Patch-Dateien verwendet, obwohl es PRs (Pull Requests) gibt?**

Der Linux-Kernel, der Entwicklungsprozess von Git selbst und etablierte Open-Source-Projekte wie Postgres behalten den E-Mail-basierten Patch-Workflow bei, um nicht von zentralen Webplattformen (wie GitHub usw.) abhängig zu sein.

**Was ist der Patch Tuesday?**

Dies ist die Bezeichnung für den branchenüblichen Kalender, an dem Microsoft jeden zweiten Dienstag im Monat regelmäßig gesammelte Sicherheits-Patches für Windows und Unternehmensprodukte verteilt.

## Verwandte Begriffe

- [Vulnerability Scanning](https://trescout.com/de/dictionary/vulnerability-scanning/)
- [Security Scanner](https://trescout.com/de/dictionary/security-scanner/)
- [Deployment](https://trescout.com/de/dictionary/deployment/)
- [Git Push](https://trescout.com/de/dictionary/git-push/)

## Verwandte Werkzeuge

- [PLFM RADAR](https://trescout.com/de/discover/plfm-radar/)
- [PhotoGIMP](https://trescout.com/de/discover/photogimp/)

Diese Erklärung wurde für TreScout mit KI in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/patch/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/patch/
