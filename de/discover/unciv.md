# Leichtes und quelloffenes Strategiespiel

Unciv ist eine quelloffene, minimalistische und plattformübergreifende Adaption von Civilization V für Desktop und Android. Entwickelt mit Kotlin und LibGDX, bietet das Projekt die originalen 4X-Strategiemechaniken bei minimalem Ressourcenverbrauch und umfassender Mod-Unterstützung.

- ★ 11.285
- Kotlin
- GitHub Trending · 2026-06-18

## Aktualisierungen
- 18. September 2026: Sterne 11.276 → 11.285, neueste Version 4.22.1 (17. September 2026).
- 15. September 2026: Sterne 11.257 → 11.276, neueste Version 4.22.0 (14. September 2026).
- 10. September 2026: Sterne 11.241 → 11.257, neueste Version 4.21.19 (9. September 2026).
- 8. September 2026: Sterne 11.223 → 11.241, neueste Version 4.21.18 (7. September 2026).

## Was es bringt
- Geringer Hardware- und Akkuverbrauch: Nutzt flüssige 2D-Vektor- und Pixelgrafik, um selbst auf schwachen Mobilgeräten ohne Hitzeentwicklung zu laufen.
- Originalgetreue Civilization V-Mechaniken: Städtebau, Technologiebaum, Sozialpolitiken, Diplomatie und Sechseck-Gitter-Kämpfe bleiben vollständig erhalten.
- Plattformübergreifende Spielstände und Mehrspieler: Übertragen Sie Spielstände zwischen Android und PC oder tragen Sie rundenbasierte Matches aus.
- Umfangreiches Community-Mod-Ökosystem: Neue Zivilisationen, Einheiten und Szenarien lassen sich mit einem Klick im Spielmenü aktivieren.
- Vollkommen frei und werbefrei: Veröffentlicht unter MPL-2.0 ohne In-App-Käufe, Tracking oder Werbung.

## Erste Schritte und Installationsoptionen

Unciv ist für mehrere Plattformen verfügbar. Auf Android können Sie die App über den Google Play Store oder F-Droid installieren. Auf Desktop-Systemen (Windows, Linux, macOS) stehen Standalone-ZIP-Dateien, Flatpak und itch.io bereit.
- [Google Play Store Seite →](https://play.google.com/store/apps/details?id=com.unciv.app)
- [F-Droid Open-Source-Repository →](https://f-droid.org/packages/com.unciv.app/)
- [itch.io Desktop-Versionen →](https://yairm210.itch.io/unciv)

## Technische Architektur und Funktionsweise

Unciv basiert auf LibGDX und Kotlin und baut auf eine deterministische, leichtgewichtige Zustandsverwaltung:
- Zustandsorientierte Spiel-Engine: Hex-Felder, Einheiten und Städte werden als reines JSON serialisiert; Spielstände bleiben winzig.
- Deklarative Modding-Engine: Zivilisationseigenschaften und Bauregeln werden in JSON definiert, ohne Quellcode neu zu kompilieren.
- Deterministische Rundenberechnung: KI-Züge und Kämpfe laufen mathematisch vorhersagbar ab, was Desynchronisationen verhindert.
- Plattformübergreifende Kompilierung: Eine einzige Kotlin-Codebasis läuft performant auf JVM-Desktop und Android.

## Gameplay-Strategien und 4X-Dynamik

Unciv setzt das klassische 4X-Prinzip perfekt um: eXplore, eXpand, eXploit und eXterminate:
- Erkundung in den ersten Runden: Verteilen Sie Späher früh auf der Karte, um Ruinen zu plündern und Gold von Stadtstaaten zu erhalten.
- Zufriedenheit und Nahrung im Gleichgewicht: Gründen Sie Städte in Reichweite von Luxusgütern, um Wachstumseinbußen zu vermeiden.
- Zielgerichteter Technologiepfad: Forschen Sie gezielt nach den militärischen oder kulturellen Stärken Ihrer Zivilisation.
- Geländevorteile im Kampf: Nutzen Sie Flussläufe und Hügel, um selbst mit kleinen Truppen große Armeen aufzuhalten.

## Wenn Sie nicht programmieren
🤖 Wenn Sie nicht programmieren
Ich möchte eine gültige JSON-Mod für Unciv erstellen. Kannst du mir eine Vorlage mit einem Anführer, der Wissenschaft und Kultur fördert, einer Kavallerie-Einheit und einem Bibliotheksgebäude erstellen? Erkläre bitte auch die Verzeichnisstruktur und wie man die Mod im Spiel testet.

- **Für wen:** Spieler und Mod-Entwickler, die klassische 4X-Strategie leichtgewichtig und werbefrei erleben wollen.
- **Lizenz:** MPL-2.0 (Mozilla Public License 2.0)
- **Spiel-Engine:** LibGDX (Kotlin-basiert)
- **Plattformen:** Android, Windows, Linux, macOS

## Häufig gestellte Fragen
- Wie ähnlich ist Unciv zu Civilization V? Mechaniken, Einheitenwerte und Technologiebäume entsprechen Civilization V mit Erweiterungen, umgesetzt in 2D.
- Wird eine Internetverbindung benötigt? Nein, Unciv ist im Einzelspieler komplett offline spielbar. Internet wird nur für Mods und Mehrspieler gebraucht.
- Wie werden Mods installiert? Im Mods-Menü des Spiels können Hunderte von Community-Mods mit einem Klick heruntergeladen werden.
- Können Spielstände zwischen PC und Smartphone getauscht werden? Ja, der Spielstand kann als Text in die Zwischenablage kopiert und auf dem anderen Gerät importiert werden.

## Links
- [GitHub →](https://github.com/yairm210/Unciv)
- [Read in Turkish →](https://trescout.com/discover/unciv/)

## Verwandte Begriffe aus dem Glossar
Open Source Offline

---
Source: TreScout Discover · https://trescout.com/de/discover/unciv/
