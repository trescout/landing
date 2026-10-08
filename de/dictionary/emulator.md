# Was ist Emulator?

*Glossar · Dev · Zuletzt aktualisiert: 19. September 2026*

Ein Emulator ist eine Systemschicht, die die physische Hardwarearchitektur eines Computers, Mobilgeräts oder einer Spielekonsole softwarebasiert nachbildet, sodass Sie Software von fremden Plattformen auf Ihrem eigenen Gerät ausführen können.

## Konzeptioneller Rahmen, Etymologie und der Unterschied zum Simulator

Der Begriff Emulator stammt vom lateinischen Verb „aemulari“ (nachahmen, wetteifern, versuchen gleichzukommen) ab. Im Türkischen wird er technisch als „Öykünücü“ oder „Donanım taklitçisi“ bezeichnet.

Um Begriffsverwirrungen in der IT-Welt zu vermeiden, muss man drei Begriffe voneinander unterscheiden:

- Simulator (Simulator): Modelliert lediglich das äußere Verhalten, physikalische Gesetze oder API-Aufrufe eines Systems; die zugrunde liegende Hardware wird nicht imitiert. Beispielsweise führt der iOS Simulator in Apple Xcode iOS-Code direkt nativ auf dem x86- oder Apple Silicon-Prozessor Ihres Computers aus; er imitiert keine Hardware-Chips.
- Emulator: Bildet den Prozessor (CPU), den Grafikchip (GPU), die Speicherbusse und die Hardwareregister (Register) des Zielsystems auf Befehlsebene (Instruction-Level) eins zu eins nach. Er übersetzt für eine fremde Architektur kompilierten binären Maschinencode (Binary) Zeile für Zeile in seine eigene Sprache.
- Virtualisierer (Virtualizer): Führt Systeme mit der gleichen Prozessorarchitektur wie der Host in isolierten Partitionen direkt auf der Hardware aus (KVM, VMware ESXi). Da keine Befehlsübersetzung stattfindet, ist er um ein Vielfaches schneller als Emulatoren.

***Analogie:** Das ist vergleichbar mit dem Lesen eines technischen Handbuchs, das in einer Fremdsprache verfasst ist. Ein Simulator ist ein Leitfaden, der zusammenfasst, worum es in dem Buch geht; ein interpreterbasierter Emulator ist ein Schüler, der ein Wörterbuch zur Hand nimmt und jeden Satz Wort für Wort langsam übersetzt; ein JIT-Emulator hingegen ist ein Simultandolmetscher, der die Kapitel des Buches professionell von vornherein in seine eigene Sprache übersetzt, Notizen macht und bei den folgenden Lesungen diesen deutschen Text direkt und fließend liest.*

## Computerarchitektur und der Kernzyklus: Fetch-Decode-Execute

Im Herzen eines Emulators befindet sich eine softwaremodellierte virtuelle CPU. Dieser virtuelle Prozessor führt in jedem Taktzyklus drei Schritte aus:

1. Holen (Fetch): Liest den nächsten Maschinenbefehl von der virtuellen Speicheradresse, auf die der virtuelle Programmzähler (Program Counter · PC) zeigt.
2. Dekodieren: Analysiert den Opcode und die Parameter des Befehls (zum Beispiel MOV RAX, 0x1 oder ADD R1, R2).
3. Ausführen (Execute): Simuliert die Logik der Zielhardware auf dem Host-Computer und aktualisiert die virtuellen Register und Flags.

Befehlsausführungsmethoden:

- Interpreter: Jeder Maschinenbefehl wird einzeln innerhalb einer switch-case-Schleife gelesen und der entsprechende C/Rust-Code aufgerufen. Die Entwicklung ist einfach und die Taktzyklusgenauigkeit ist hoch, jedoch wird die CPU übermäßig beansprucht (langsam).
- Dynamische Rekompilierung (JIT · Just-In-Time Recompiler): Das Geheimnis der hohen Leistung moderner Emulatoren (Dolphin, RPCS3, QEMU). Fremde Maschinencode-Blöcke werden zur Laufzeit analysiert, in einem Durchgang in den nativen Maschinencode der Haupt-CPU (Host-CPU) übersetzt und im Arbeitsspeicher zwischengespeichert. Dadurch sinken die Übersetzungskosten auf null, wenn dieselbe Schleife erneut ausgeführt wird.
- Taktgenauigkeit (Cycle Accuracy): Bei einigen Retro-Konsolen (Game Boy, SNES) haben Spieleentwickler den Sound-Chip und die Rasterzeilen auf Nanosekundenebene mit dem Hardware-Takt synchronisiert. Um diese Geräte fehlerfrei zu emulieren, muss jeder von einem Befehl verbrauchte CPU-Taktzyklus ohne Verzögerung berechnet werden.

## Entwickler-, Sicherheits- und Unternehmensanwendungsbereiche

Emulatoren bringen nicht nur Retro-Konsolenspiele auf moderne Bildschirme; sie sind auch entscheidende Werkzeuge der modernen Softwaretechnik:

- Mobile App-Entwicklung: Der Android Studio Emulator nutzt im Hintergrund den QEMU-Hypervisor und ermöglicht es Entwicklern, ihren Code auf Hunderten verschiedener Hardware- und Bildschirmkonfigurationen zu testen, ohne ein echtes Telefon kaufen zu müssen.
- Cross-Architektur-Übergänge (Binary Translation): Rosetta 2, das Apple beim Wechsel von Intel-Prozessoren auf die ARM-Architektur eingeführt hat, ist im Grunde eine hochentwickelte AOT- (Ahead-of-Time) und JIT-Binärübersetzungs-Engine. Sie führt für Intel geschriebene x86_64-Anwendungen auf Apple Silicon mit nahezu verlustfreier Geschwindigkeit aus.
- Cybersicherheit und Schadsoftware-Analyse (Sandbox-Emulation): Sicherheitsanalysten führen eine verdächtige Ransomware auf einer emulierten virtuellen CPU aus, anstatt sie direkt auf einem physischen Computer zu öffnen. Speicherzugriffe und Systemaufrufe (Syscalls) werden dabei Schritt für Schritt überwacht.
- Legacy-Modernisierung: In den Bereichen Bankwesen, Verteidigung und öffentliche Infrastruktur werden IBM-Mainframes oder DEC-VAX-Systeme aus den 1980er-Jahren mithilfe von Emulatoren auf modernen Linux-Servern ohne Betriebsunterbrechung weiterbetrieben.

## Rechtlicher Aspekt und Urheberrechte

Die Legalität der Emulatorenentwicklung wurde weltweit durch Präzedenzfälle anerkannt:

- Sony v. Connectix (2000) und Sony v. Bleem!: Die Gerichte entschieden, dass es rechtmäßig ist und unter den Begriff der fairen Verwendung (Fair Use) fällt, die Funktionsweise einer Hardware durch Reverse Engineering mittels Clean-Room-Verfahren in Software zu übertragen.
- Urheberrechtlicher Hinweis: Die Emulationssoftware selbst ist legal. Das unbefugte Kopieren oder Herunterladen von urheberrechtlich geschützten BIOS-Dateien des Zielgeräts oder von urheberrechtlich geschützten Spiel- bzw. Software-ROMs aus dem Internet stellt jedoch eine Urheberrechtsverletzung dar.

## Häufige Fragen

**Was bedeutet Emulator und wie lautet die türkische Entsprechung?**

Der vom englischen Wort „Emulator“ abgeleitete Begriff bedeutet im Türkischen Emulator oder Hardware-Nachahmer. Es handelt sich um ein System, das die Hardware-Komponenten eines Geräts durch Software nachahmt, um Software fremder Plattformen auszuführen.

**Was ist der Hauptunterschied zwischen einem Emulator und einem Simulator?**

Während ein Simulator lediglich das Verhalten und die Logik des Systems nachahmt, kopiert ein Emulator den Prozessor, den Speicherbus und den Maschinencode der Zielhardware auf Befehlsebene eins zu eins in Software.

**Wie funktioniert ein JIT-Compiler (Just-In-Time) bei der Emulation?**

Er übersetzt die Maschinencodeblöcke des fremden Prozessors zur Laufzeit in den lokalen Maschinencode des eigenen Computers und speichert sie im Cache. Dadurch wird der Code bei der zweiten Ausführung mit nativer Geschwindigkeit ausgeführt.

**Ist die Entwicklung und Nutzung von Emulatoren legal?**

Ja, Emulatoren, die nach dem Prinzip des Clean-Room-Reverse-Engineering geschrieben wurden, sind völlig legal. Das unbefugte Verteilen urheberrechtlich geschützter BIOS-Dateien des Geräts oder urheberrechtlich geschützter ROM-Kopien von Spielen stellt jedoch eine Urheberrechtsverletzung dar.

## Verwandte Begriffe

- [ROM](https://trescout.com/de/dictionary/rom/)
- [Sandbox](https://trescout.com/de/dictionary/sandbox/)
- [Virtual Machines](https://trescout.com/de/dictionary/virtual-machines/)
- [Assembly](https://trescout.com/de/dictionary/assembly/)
- [Runtime](https://trescout.com/de/dictionary/runtime/)
- [Apple Silicon](https://trescout.com/de/dictionary/apple-silicon/)

## Verwandte Werkzeuge

- [Cool Retro Term](https://trescout.com/de/discover/cool-retro-term/)
- [Sharpemu](https://trescout.com/de/discover/sharpemu/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/emulator/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/emulator/
