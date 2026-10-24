# Was ist Shellcode?

*Entwicklung · Zuletzt aktualisiert: 24. Oktober 2026*

Es handelt sich um einen kleinen Maschinencode, der Sicherheitslücken in Systemen ausnutzt, um Befehlszeilenzugriff auf dem Zielrechner zu erlangen oder spezifische Befehle auszuführen.

## Definition

Dieses spezielle Code-Fragment, das in der Welt der Cybersicherheit und bei Penetrationstests verwendet wird, wird direkt in den Systemspeicher injiziert. Seinen Namen verdankt es historisch dem Ziel, eine Befehls-Shell auf dem Zielsystem zu öffnen. Heutzutage ist es nicht mehr nur darauf ausgelegt, eine Shell zu öffnen, sondern jede beliebige Anweisung auf dem System auszuführen.

***Analogie:** Man kann es mit einer kleinen Schlüsselkarte vergleichen, die sich heimlich durch die verschlossene Tür eines Gebäudes schleicht und das Bedienfeld des Sicherheitsraums übernimmt.*

## So funktioniert es

Sicherheitsforscher oder Angreifer identifizieren Schwachstellen wie Pufferüberläufe in der Software. Anschließend platzieren sie den von ihnen vorbereiteten kleinen Maschinencode als Byte-Sequenz, die der Prozessor direkt versteht, im Speicher. Wenn der Prozessor diese Befehle ausführt, wird die unbefugte Kontrolle über das Zielsystem erlangt.

## Wo es eingesetzt wird

Es begegnet Ihnen bei Sicherheitsanalysen, Penetrationstests und der Untersuchung von Schadsoftware.

## Häufig verwechselt mit

Es sollte nicht mit Shell-Skripten verwechselt werden. Während Shell-Skripte textbasierter Code auf hoher Ebene sind, handelt es sich bei diesem Konzept um binären Byte-Code, der direkt auf Prozessorebene ausgeführt wird.

## Fragen und Antworten

**Wird Shellcode nur für schädliche Zwecke verwendet?**

Sicherheitsexperten verwenden diese Codes auch, um die Verteidigungsresistenz von Systemen zu testen und Sicherheitslücken zu schließen.

**Warum werden diese Code-Fragmente so klein geschrieben?**

Sie werden so klein wie möglich konzipiert, um in begrenzte Speicherbereiche eindringen zu können und zu funktionieren, ohne von Sicherheitsfiltern erkannt zu werden.

## Verwandte Begriffe

- [Exploit](https://trescout.com/de/dictionary/exploit/)
- [Penetration Testing](https://trescout.com/de/dictionary/penetration-testing/)
- [Vulnerability Scanning](https://trescout.com/de/dictionary/vulnerability-scanning/)
- [Backdoor](https://trescout.com/de/dictionary/backdoor/)

Diese Erklärung wurde für TreScout mit KI in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/shellcode/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/shellcode/
