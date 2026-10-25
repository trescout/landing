# Leichtes und Open-Source-Strategiespiel

Unciv ist eine Open-Source-, minimalistische und plattformübergreifende Desktop- und Android-Adaption von Civilization V. Das Projekt wurde mit Kotlin- und LibGDX-Infrastruktur entwickelt und bietet originale 4X-Strategiemechaniken ohne Hardwarelast und hohe Mod-Unterstützung.

- ★ 11.486
- Kotlin
- GitHub Trending · 2026-06-18

## Aktualisierungen

- **25. Oktober 2026:** Sterne 11,477 → 11,486, neueste Version 4.22.13-patch1 (24. Oktober 2026).
- **22. Oktober 2026:** Sterne 11,464 → 11,477, neueste Version 4.22.13 (21. Oktober 2026).
- **19. Oktober 2026:** Sterne 11,458 → 11,464, neueste Version 4.22.12 (18. Oktober 2026).
- **18. Oktober 2026:** Sterne 11,452 → 11,458, neueste Version 4.22.11-patch1 (17. Oktober 2026).

## Was es bringt

- Niedrige Hardware und batteriefreundliche Architektur: Es funktioniert selbst auf den einfachsten Mobilgeräten ohne Erwärmung, indem es 2D-Vektor- und Pixelgrafiken anstelle schwerer 3D-Rendering-Engines verwendet.
- Die ursprüngliche Mechanik von Civilization V: Stadtplanung, Technologiebaum, Sozialpolitik, Diplomatie und taktisches Hex-Kampfsystem bleiben vollständig erhalten.
- Plattformübergreifende Speicherung und Multiplayer-Unterstützung: Sie können gespeicherte Dateien direkt zwischen Desktop und Android verschieben oder E-Mail-/serverbasierte Round-Robin-Multiplayer-Matches spielen.
- Community-gesteuertes, reichhaltiges Mod-Ökosystem: Neue Zivilisationen, Einheiten, Fantasy-Szenarien und Grafikthemen können mit einem einzigen Klick über die In-Game-Oberfläche installiert und aktiviert werden.
- Völlig kostenloses und werbefreies Erlebnis: Vertrieb unter MPL-2.0-Lizenz; enthält keine In-App-Käufe, Werbung, Tracking oder Datenerfassung.

## Erste Schritte und Installationsoptionen

Um das Unciv-Projekt auf Ihrem Gerät abzuspielen, können Sie den für Ihre Plattform geeigneten Vertriebskanal wählen. Auf der mobilen Seite können Android-Benutzer über den Google Play Store oder das datenschutzorientierte F-Droid-Repository installieren. Auf der Desktop-Seite können direkte MSI- oder portable ZIP-Dateien für Windows, Flatpak-Pakete oder itch.io-Distributionen für Linux bevorzugt werden.

- [Google Play Store Sayfası →](https://play.google.com/store/apps/details?id=com.unciv.app)
- [F-Droid Açık Kaynak Deposu →](https://f-droid.org/packages/com.unciv.app/)
- [itch.io Masaüstü Sürümleri →](https://yairm210.itch.io/unciv)

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

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte eine gültige JSON-Mod-Struktur für das Spiel Unciv vorbereiten. Können Sie eine Beispiel-Unciv-Mod-Vorlage erstellen, die eine spezielle Kavallerieeinheit und ein spezielles Bibliotheksgebäude enthält, das als Anführerfähigkeit einen Bonus auf Wissenschafts- und Kulturproduktion verleiht? Können Sie Schritt für Schritt erklären, welche JSON-Dateien ich in welcher Ordnerstruktur speichern soll und wie ich dies über die Mod-Manager-Oberfläche im Spiel testen kann?

Repository: https://github.com/yairm210/Unciv. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Häufig gestellte Fragen

- Wie ähnlich ist Unciv zu Civilization V? Spielmechanik, Einheitenstatistik, Technologiebaum und Siegbedingungen sind weitgehend kompatibel mit den Add-ons Civilization V Gods and Kings und Brave New World. Der Unterschied besteht im Wesentlichen in der Verwendung eines einfachen visuellen 2D-Designs anstelle von 3D-Grafiken.
- Ist zum Spielen eine Internetverbindung erforderlich? Nein. Unciv kann vollständig offline gespielt werden. Um im Einzelspielermodus gegen KI-Gegner zu spielen, ist keine Netzwerkverbindung erforderlich. Nur Mod-Downloads und Multiplayer-Matches erfordern eine Verbindung.
- Wie installiere ich Unciv-Mods? Wenn Sie im Hauptmenü auf die Registerkarte „Mods“ gehen, können Sie Hunderte von Mods auflisten, die von der Community hochgeladen wurden, und sie mit einem einzigen Klick auf Ihr Gerät herunterladen. Sie können die Installation auch direkt durchführen, indem Sie einen Link zu einem beliebigen Mod-Repository auf GitHub hinzufügen.
- Können Aufnahmedateien zwischen Desktop und Telefon übertragen werden? Ja. Sie können die gespeicherte Datei aus dem Aufnahmemenü im Spiel in die Zwischenablage kopieren, sie per E-Mail oder Nachricht im Textformat an Ihr anderes Gerät senden und dort mit der Option „Aus der Zwischenablage laden“ dort fortfahren, wo Sie aufgehört haben.

## Verwandte Begriffe aus dem Glossar

- [Exploit](https://trescout.com/de/dictionary/exploit/)
- [Runtime](https://trescout.com/de/dictionary/runtime/)
- [Open Source](https://trescout.com/de/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Für Gamer und unabhängige Modder, die klassische 4X-Strategiespiele auf einer leichten, werbefreien und Open-Source-Infrastruktur erleben möchten.
- **Lizenz:** MPL-2.0 (Mozilla Public License 2.0)
- **Spiel-Engine:** LibGDX (Kotlin-basierte plattformübergreifende Plattform)
- **Plattformen:** Android, Windows, Linux, macOS

## Links

- [GitHub-Repository →](https://github.com/yairm210/Unciv)
- [Auf Türkisch lesen →](https://trescout.com/discover/unciv/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-06-18 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/unciv/
