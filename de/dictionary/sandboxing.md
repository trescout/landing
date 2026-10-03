# Was ist Sandboxing?

Eine Technik, bei der Software oder verdächtiger Code in einer isolierten Umgebung ausgeführt wird, um Schäden am Hauptsystem und an der Umgebung zu verhindern.

## Definition
Sandboxing ist die Praxis, nicht vertrauenswürdige oder sich in der Testphase befindliche Code-Snippets von Systemressourcen abzukapseln und in einem kontrollierten Bereich auszuführen. Dieser Mechanismus schränkt den direkten Zugriff der Anwendung auf das Dateisystem, das lokale Netzwerk oder den Betriebssystemkern ein. Es ist eine unverzichtbare Sicherheitsebene, um die Ausbreitung von Sicherheitslücken im System zu verhindern und die Auswirkungen von Schadsoftware auf ein Minimum zu reduzieren.

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
- [Sandbox](/de/dictionary/sandbox/)
- [Runtime](/de/dictionary/runtime/)
- [Virtual Machines](/de/dictionary/virtual-machines/)
- [Security Scanner](/de/dictionary/security-scanner/)

## Verwandte Werkzeuge
- [Agent Governance Toolkit](/de/discover/agent-governance-toolkit/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/sandboxing/
