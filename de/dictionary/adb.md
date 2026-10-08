# Was ist ADB?

*Glossar · Dev · Zuletzt aktualisiert: 22. September 2026*

> Android Debug Bridge

ADB (Android Debug Bridge), ein Tool, das die Kommunikation für Befehle und das Debugging zwischen einem Computer und einem Android-Gerät ermöglicht.

## Definition und Wortherkunft

Debug bedeutet Fehlerbehebung, bridge bedeutet Brücke. ADB kommuniziert zwischen dem Client auf dem Computer und dem adb-Daemon auf dem Gerät; es wird für die Installation von Anwendungen, das Sammeln von Protokollen, das Debugging und für eingeschränkte Geräteverwaltungsaufgaben verwendet. Es ist Teil des Android SDK Platform-Tools-Pakets.

***Analogie:** Wenn Sie den Computer als Kontrollzentrum und das Gerät als Raumschiff betrachten, ist ADB das Signalkabel dazwischen.*

## Wie kann man es kennen und im täglichen Leben anwenden?

**Entwicklung:** Anwendungsinstallation und -protokollierung.
**Test:** Tests auf mehreren Geräten.
**Anpassung:** Erweiterte Einstellungen.

## Technische Tiefe und Architektur

Dreifaches Layout:

**Client:** Befehl auf dem Computer.
**Moderator:** Im Hintergrund laufender Administrator.
**Daemon:** Empfänger auf dem Gerät.

Stream:

```
adb devices
adb install uygulama.apk
```

Der erste listet verbundene Geräte auf, der zweite installiert das Anwendungspaket. USB-Debugging muss auf dem Gerät aktiviert sein. Da falsche Befehle zu Datenverlust führen können, ist es notwendig, das Zielgerät und den Befehl vor der Ausführung zu überprüfen.

## Häufig gemischte Dinge

Es wird für eine Dateiübertragung gehalten. Es kopiert nur, ADB greift in das System ein. Der Berechtigungsunterschied ist groß.

## Einsatz in verschiedenen Disziplinen

**Kabel:** Leitung, die ein Signal überträgt.
**Interpreter:** Die Sprache beider Seiten.
**Steuerung:** Fernverwaltung.

## Häufig gestellte Fragen

**Kann es jeder nutzen?**

Grundlegende Befehle sind leicht zu erlernen, aber insbesondere adb shell und Löschvorgänge erfordern technisches Fachwissen. Vor dem Ausführen eines Befehls sollte dessen Auswirkung überprüft werden.

**Geht das auch kabellos?**

Ja. Bei unterstützten Android-Versionen kann nach dem Koppeln mit dem Gerät eine Verbindung über WLAN hergestellt werden. Stabilität und Geschwindigkeit hängen von der Qualität des lokalen Netzwerks ab.

**Ist es sicher?**

Wenn Sie das Gerät besitzen, ja. Bei einem unbekannten Computer, an den das Gerät angeschlossen wird, wird keine Bestätigung erteilt.

**Was ist der Unterschied zu Fastboot?**

ADB kommuniziert mit dem Betriebssystem, während Android läuft. Fastboot hingegen wird verwendet, wenn sich das Gerät im Bootloader-Modus befindet, um Partitions-Images oder Firmware-Vorgänge durchzuführen; die unterstützten Befehle und der Entsperrvorgang variieren je nach Gerät.

## Verwandte Begriffe

- [CLI](https://trescout.com/de/dictionary/cli/)
- [SDK](https://trescout.com/de/dictionary/sdk/)
- [Emulator](https://trescout.com/de/dictionary/emulator/)

## Verwandte Werkzeuge

- [Universal Android Debloater Next Generation](https://trescout.com/de/discover/universal-android-debloater-next-generation/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/adb/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/adb/
