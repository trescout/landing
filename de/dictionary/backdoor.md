# Was ist Backdoor?

*Entwicklung · Zuletzt aktualisiert: 22. Oktober 2026*

Eine Methode oder Software, die unbemerkt einen unbefugten Fernzugriff auf ein System ermöglicht, indem sie Standard-Authentifizierungsmechanismen umgeht.

## Definition

Eine Backdoor (Hintertür) ist ein versteckter Zugang, der von Softwareentwicklern absichtlich zu Debugging-Zwecken hinterlassen oder von Angreifern nachträglich im System platziert werden kann. Durch diese Methode werden herkömmliche Kontrollen von Benutzernamen, Passwörtern oder Verschlüsselungen außer Kraft gesetzt. Böswillige Akteure, die unbemerkt in das System eindringen, können die Hintertür nutzen, um über längere Zeit hinweg Verwaltungsrechte auszuüben.

***Analogie:** Das ist vergleichbar damit, dass am Haupteingang einer Burg Wachen stehen, während hinter der Mauer ein geheimes, niemandem bekanntes Tunnel gegraben wird.*

## So funktioniert es

Hintertüren werden durch eine im Quellcode versteckte Logikprüfung oder einen im System offen gelassenen, versteckten Netzwerkport eingerichtet. Manchmal werden sie über Updates in die Lieferkette eingeschleust oder durch ein kleines Kommandozeilentool ausgelöst, das mithilfe eines Exploits eingeschleust wurde. Wenn der Angreifer von außen ein spezielles Signal oder einen Schlüssel sendet, startet die Hintertür direkt eine Fernzugriffssitzung.

## Wo es eingesetzt wird

Sie sind häufig bei Lieferkettenangriffen, Fällen von Wirtschaftsspionage und Operationen mit fortgeschrittenen und beharrlichen Bedrohungen (APT) anzutreffen. Sie werden auch in Firmware oder in schädlichem Code entdeckt, der in Open-Source-Pakete eingeschleust wurde.

## Häufig verwechselt mit

Sie kann mit einem Trojaner verwechselt werden. Ein Trojaner ist eine trügerische Hülle, die zum Einschleusen von Schadsoftware verwendet wird; eine Backdoor hingegen ist die Funktion, die einen dauerhaften und verdeckten Zugriff auf das System ermöglicht.

## Fragen und Antworten

**Warum bauen Entwickler eine Hintertür in ein System ein?**

In einigen Fällen wird sie absichtlich zur erleichterten Wartung oder für den Notzugriff belassen, aber dieser Umstand setzt das System einem großen Sicherheitsrisiko aus.

**Wie wird eine Backdoor entdeckt?**

Sie kann durch die Überwachung abnormalen Netzwerkverkehrs, Integritätsprüfungen von Dateien und eingehende statische Quellcodeanalysen aufgespürt werden.

## Verwandte Begriffe

- [Exploit](https://trescout.com/de/dictionary/exploit/)
- [Remote Code Execution](https://trescout.com/de/dictionary/remote-code-execution/)
- [Penetration Testing](https://trescout.com/de/dictionary/penetration-testing/)
- [Vulnerability Scanning](https://trescout.com/de/dictionary/vulnerability-scanning/)

Diese Erklärung wurde für TreScout mit KI in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/backdoor/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/backdoor/
