# Was ist ADB?

> Android Debug Bridge

ADB (Android Debug Bridge), ein Tool, das die Kommunikation für Befehle und das Debugging zwischen einem Computer und einem Android-Gerät ermöglicht.

## Definition und Wortherkunft
Debug bedeutet Fehlerbehebung, bridge bedeutet Brücke. ADB kommuniziert zwischen dem Client auf dem Computer und dem adb-Daemon auf dem Gerät; es wird für die Installation von Anwendungen, das Sammeln von Protokollen, das Debugging und für eingeschränkte Geräteverwaltungsaufgaben verwendet. Es ist Teil des Android SDK Platform-Tools-Pakets.

## Wie kann man es kennen und im täglichen Leben anwenden?
Entwicklung: Anwendungsinstallation und -protokollierung.Test: Tests auf mehreren Geräten.Anpassung: Erweiterte Einstellungen.

## Technische Tiefe und Architektur
Dreifaches Layout:

## Häufig gemischte Dinge
Es wird für eine Dateiübertragung gehalten. Es kopiert nur, ADB greift in das System ein. Der Berechtigungsunterschied ist groß.

## Einsatz in verschiedenen Disziplinen
Kabel: Leitung, die ein Signal überträgt.Interpreter: Die Sprache beider Seiten.Steuerung: Fernverwaltung.

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
- [CLI](/de/dictionary/cli/)
- [SDK](/de/dictionary/sdk/)
- [Emulator](/de/dictionary/emulator/)

## Verwandte Werkzeuge
- [Universal Android Debloater Next Generation](/de/discover/universal-android-debloater-next-generation/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/adb/
