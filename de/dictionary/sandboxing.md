# Was ist Sandboxing?

*Glossar · Dev · Zuletzt aktualisiert: 3. Oktober 2026*

Eine Technik, bei der Software oder verdächtiger Code in einer isolierten Umgebung ausgeführt wird, um Schäden am Hauptsystem und an der Umgebung zu verhindern.

## Definition

Sandboxing ist die Praxis, nicht vertrauenswürdige oder sich in der Testphase befindliche Code-Snippets von Systemressourcen abzukapseln und in einem kontrollierten Bereich auszuführen. Dieser Mechanismus schränkt den direkten Zugriff der Anwendung auf das Dateisystem, das lokale Netzwerk oder den Betriebssystemkern ein. Es ist eine unverzichtbare Sicherheitsebene, um die Ausbreitung von Sicherheitslücken im System zu verhindern und die Auswirkungen von Schadsoftware auf ein Minimum zu reduzieren.

***Analogie:** Das ist vergleichbar damit, ein potenziell gefährliches chemisches Experiment nicht mitten im Raum, sondern in einem explosionsgeschützten Glaskasten durchzuführen.*

## So funktioniert es

Durch betriebssystemnahe Einschränkungen oder den Einsatz von Virtualisierungswerkzeugen wird eine geschützte Barriere errichtet. Wenn der Code ausgeführt wird, kann er nur den ihm zugewiesenen, begrenzten Speicher- und Festplattenbereich nutzen. Systemaufrufe werden kontinuierlich überwacht; wird ein unerlaubter Handlungsversuch erkannt, wird die Software sofort gestoppt.

## Wo es eingesetzt wird

Es wird beim Ausführen von Skripten Dritter in Webbrowsern, in Sicherheitssoftware zur Untersuchung verdächtiger Dateien in E-Mail-Anhängen und in Entwicklungsumgebungen verwendet, in denen KI-Agenten Code ausführen.

## Häufig verwechselt mit

Während der Begriff Sandbox den isolierten Bereich selbst beschreibt, bezeichnet Sandboxing den Prozess der Erstellung, Verwaltung und Begrenzung dieser sicheren Umgebung.

## Häufige Fragen

**Verringert Sandboxing die Systemleistung spürbar?**

Obwohl die Überwachung von Systemaufrufen eine geringe Rechenlast verursacht, ist dieser Verlust in modernen Betriebssystemen meist so gering, dass er kaum auffällt.

**Warum ist Sandboxing bei KI-Werkzeugen erforderlich?**

Da von KI-Modellen generierter und ausgeführter Code das Risiko bergen kann, kritische Dateien im Betriebssystem zu löschen, werden diese Prozesse in einer sicheren Isolationsschicht ausgeführt.

## Verwandte Begriffe

- [Sandbox](https://trescout.com/de/dictionary/sandbox/)
- [Runtime](https://trescout.com/de/dictionary/runtime/)
- [Virtual Machines](https://trescout.com/de/dictionary/virtual-machines/)
- [Security Scanner](https://trescout.com/de/dictionary/security-scanner/)

## Verwandte Werkzeuge

- [Agent Governance Toolkit](https://trescout.com/de/discover/agent-governance-toolkit/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/sandboxing/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/sandboxing/
