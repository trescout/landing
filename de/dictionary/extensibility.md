# Was ist Erweiterbarkeit (Extensibility)?

> Englisch: Extensibility · Wortherkunft: lateinisch extendere (ausdehnen, spannen)

**Kategorie:** Dev  
**Letzte Aktualisierung:** 2026-09-22

Erweiterbarkeit (Extensibility) ist ein Architekturprinzip der Softwaretechnik, das es ermöglicht, Anwendungen durch Module, Plugins und Schnittstellen um neue Funktionen zu ergänzen, ohne den bestehenden Kernquelltext zu modifizieren.

## Definition und Wortherkunft
Der Begriff geht auf das lateinische Wort extendere zurück, was ausdehnen bedeutet. In der Softwarearchitektur verkörpert dies das Open-Closed-Prinzip aus den SOLID-Leitsätzen: Systeme sollten offen für Erweiterungen, aber geschlossen für Änderungen sein. Anstatt neue Anforderungen direkt in das Fundament einzubauen, definieren Architekten Schnittstellen, an die Drittanbieter nahtlos andocken können.

## Alltägliche Anwendung und Praxis
Beispiele erweiterbarer Systeme im Entwickleralltag:
- **Code-Editoren:** VS Code bleibt schlank und schnell, lässt sich jedoch durch Marktplatz-Erweiterungen für beliebige Programmiersprachen anpassen.- **Webbrowser:** Firefox und Chrome ermöglichen die Installation von Werbeblockern und Passwort-Managern über offizielle Add-on-APIs.- **CMS-Plattformen:** WordPress stützt seinen weltweiten Erfolg auf Hook-Mechanismen, über die tausende Plugins integriert werden.

## Technische Tiefe und Architektur
Wichtige Architekturmuster für echte Erweiterbarkeit:
- **Plugin- und Hook-Systeme:** Feste Lebenszyklus-Ereignisse, an denen externe Skripte zusätzliche Logik einhängen können.- **Dependency Inversion:** Nutzung abstrakter Interfaces zur Entkopplung von Aufrufer und konkreter Implementierung.- **Ereignisgesteuerte Pub/Sub-Muster:** Das Kernsystem sendet Ereignisse, auf die registrierte Module unabhängig reagieren.- **WASM-Sandboxing:** Sichere Ausführung von Fremdcode in isolierten Speicherräumen ohne Zugriff auf das Betriebssystem.

## Interdisziplinäre Perspektiven
Vergleiche in anderen Lebensbereichen:
- **Bauwesen:** Ein modulares Gebäude, dessen Statik das Aufsetzen weiterer Etagen erlaubt, ohne tragende Wände zu zerstören.- **Werkzeuge:** Ein Akkuschrauber, auf den verschiedene Aufsätze zum Bohren, Sägen oder Polieren gesteckt werden.- **Brettspiele:** Ein Grundspiel, dessen Regelwerk von vornherein für thematische Erweiterungspakete ausgelegt ist.

## Als Analogie
Es ist wie ein Schweizer Taschenmesser: Der Grundkörper bleibt kompakt und unverändert, bietet jedoch passgenaue Fächer, um je nach Bedarf Spezialwerkzeuge auszuklappen oder anzustecken.

## Häufige Fragen

**Sollte jede Software von Beginn an erweiterbar sein?**  
Nein; verfrühte Erweiterbarkeitsschichten führen zu unnötiger Komplexität, wenn Anforderungen noch nicht klar umrissen sind.

**Worin liegt der Unterschied zwischen Erweiterbarkeit und Wartbarkeit?**  
Wartbarkeit beschreibt die Leichtigkeit der Fehlerbehebung im bestehenden Code; Erweiterbarkeit beschreibt das Hinzufügen neuer Funktionen ohne Änderung des Kerns.

**Wie schützt man das System vor fehlerhaften Plugins?**  
Indem Plugins in isolierten Sandboxes oder separaten Prozessen mit restriktiven Rechten ausgeführt werden.

**Welche Aufgabe haben SDKs bei erweiterbaren Plattformen?**  
Sie bieten Drittentwicklern standardisierte Klassen und Typprüfungen zur sicheren Kommunikation mit dem Host-System.

## Verwandte Begriffe
- [Plugin](/de/dictionary/plugin/)
- [Emitter](/de/dictionary/emitter/)
- [Tools](/de/dictionary/tools/)

---
Quelle: TreScout Tech-Glossar · https://trescout.com/de/dictionary/extensibility/
