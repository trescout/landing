# Leichtes und Open-Source-Strategiespiel

Unciv ist eine Open-Source-, minimalistische und plattformübergreifende Desktop- und Android-Adaption von Civilization V. Das Projekt wurde mit Kotlin- und LibGDX-Infrastruktur entwickelt und bietet originale 4X-Strategiemechaniken ohne Hardwarelast und hohe Mod-Unterstützung.

- ★ 11.376
- Kotlin
- GitHub Trending · 2026-06-18

## Was es bringt
- Niedrige Hardware und batteriefreundliche Architektur: Es funktioniert selbst auf den einfachsten Mobilgeräten ohne Erwärmung, indem es 2D-Vektor- und Pixelgrafiken anstelle schwerer 3D-Rendering-Engines verwendet.
- Die ursprüngliche Mechanik von Civilization V: Stadtplanung, Technologiebaum, Sozialpolitik, Diplomatie und taktisches Hex-Kampfsystem bleiben vollständig erhalten.
- Plattformübergreifende Speicherung und Multiplayer-Unterstützung: Sie können gespeicherte Dateien direkt zwischen Desktop und Android verschieben oder E-Mail-/serverbasierte Round-Robin-Multiplayer-Matches spielen.
- Community-gesteuertes, reichhaltiges Mod-Ökosystem: Neue Zivilisationen, Einheiten, Fantasy-Szenarien und Grafikthemen können mit einem einzigen Klick über die In-Game-Oberfläche installiert und aktiviert werden.
- Völlig kostenloses und werbefreies Erlebnis: Vertrieb unter MPL-2.0-Lizenz; enthält keine In-App-Käufe, Werbung, Tracking oder Datenerfassung.

## Erste Schritte und Installationsoptionen
- Google Play Store-Seite →
- F-Droid Open Source Repository →
- itch.io Desktop-Versionen →

## Technische Architektur und Funktionsweise
- Zustandsgesteuerte Spiel-Engine: Alle Hex-Kacheln, Einheiten, Städte und diplomatischen Beziehungen auf dem Spielbrett werden als reine JSON-Objekte gespeichert. Durch diese Struktur bleibt die Größe der Protokolldateien bei nur wenigen hundert Kilobyte.
- Deklarative Modding-Engine: Zivilisationsfunktionen, Technologiebäume und Baukosten werden über JSON-Dateien definiert, ohne den Quellcode zu berühren. Auf diese Weise benötigen Mod-Entwickler keinen externen Compiler.
- Deterministische Rundenberechnung: KI-Bewegungen und Kampfergebnisse werden mit vorhersehbaren Algorithmen berechnet. Dies verhindert Synchronisationsunterbrechungen in asynchronen Multiplayer-Spielen.
- Multiplattform-Kompilierung: Dank LibGDX wird eine einzige Kotlin-Codebasis mit nativer Leistung für Desktop (JVM) und Mobilgeräte (Android-Laufzeit) gepackt.

## Spielstrategien und 4X-Dynamik
- Kartenerkundung in den ersten Runden: Verteilen Sie Ihre Krieger- und Spähereinheiten frühzeitig auf der Karte, um antike Artefakte zu sammeln, ersten Kontakt mit Stadtstaaten aufzunehmen und Goldeinnahmen zu erzielen.
- Glück und Ernährungsbalance: Achten Sie bei der Gründung neuer Städte darauf, dass Sie sich in der Reichweite luxuriöser Ressourcen befinden. Wenn Ihre Zufriedenheitsrate negativ wird, verlangsamen sich Bevölkerungswachstum und Produktion deutlich.
- Technologie-Roadmap: Konzentrieren Sie sich auf die Stärken Ihrer Zivilisation und nicht auf zufällige Forschung. Folgen Sie den Wegen der Schmiedekunst und des Schießpulvers für den militärischen Sieg, der Philosophie und der Bildung für den kulturellen Sieg.
- Geländevorteile nutzen: Schlagen Sie große Armeen mit einer kleinen Anzahl von Einheiten ab, indem Sie Flussuferverteidigung, Hügelvorteile und enge Pässe schaffen.

## Wenn Sie nicht programmieren
Ich möchte eine gültige JSON-Mod-Struktur für das Spiel Unciv vorbereiten. Können Sie eine Beispiel-Unciv-Mod-Vorlage erstellen, die eine spezielle Kavallerieeinheit und ein spezielles Bibliotheksgebäude enthält, das als Anführerfähigkeit einen Bonus auf Wissenschafts- und Kulturproduktion verleiht? Können Sie Schritt für Schritt erklären, welche JSON-Dateien ich in welcher Ordnerstruktur speichern soll und wie ich dies über die Mod-Manager-Oberfläche im Spiel testen kann?

## Häufig gestellte Fragen
- Wie ähnlich ist Unciv zu Civilization V? Spielmechanik, Einheitenstatistik, Technologiebaum und Siegbedingungen sind weitgehend kompatibel mit den Add-ons Civilization V Gods and Kings und Brave New World. Der Unterschied besteht im Wesentlichen in der Verwendung eines einfachen visuellen 2D-Designs anstelle von 3D-Grafiken.
- Ist zum Spielen eine Internetverbindung erforderlich? Nein. Unciv kann vollständig offline gespielt werden. Um im Einzelspielermodus gegen KI-Gegner zu spielen, ist keine Netzwerkverbindung erforderlich. Nur Mod-Downloads und Multiplayer-Matches erfordern eine Verbindung.
- Wie installiere ich Unciv-Mods? Wenn Sie im Hauptmenü auf die Registerkarte „Mods“ gehen, können Sie Hunderte von Mods auflisten, die von der Community hochgeladen wurden, und sie mit einem einzigen Klick auf Ihr Gerät herunterladen. Sie können die Installation auch direkt durchführen, indem Sie einen Link zu einem beliebigen Mod-Repository auf GitHub hinzufügen.
- Können Aufnahmedateien zwischen Desktop und Telefon übertragen werden? Ja. Sie können die gespeicherte Datei aus dem Aufnahmemenü im Spiel in die Zwischenablage kopieren, sie per E-Mail oder Nachricht im Textformat an Ihr anderes Gerät senden und dort mit der Option „Aus der Zwischenablage laden“ dort fortfahren, wo Sie aufgehört haben.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/unciv/
