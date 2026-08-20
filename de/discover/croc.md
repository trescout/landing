# Sichere und einfache Dateiübertragung

Croc ist ein Tool, das mittels Ende-zu-Ende-Verschlüsselung eine sichere Datei- und Datenübertragung zwischen zwei Computern ermöglicht. Diese mit der Programmiersprache Go entwickelte Software nutzt einen temporären Relay-Mechanismus, um den Übertragungsprozess zu erleichtern.

- ★ 39.973
- Go
- GitHub Trending · 2026-07-22

## Was es bringt
- Ende-zu-Ende verschlüsselte Datenübertragung
- Kompatibilität zwischen verschiedenen Betriebssystemen
- Unterbrochene Übertragungen dort fortsetzen, wo sie aufgehört haben

## Installation
**Allgemeine Installation**

```
curl https://getcroc.schollz.com | bash
```

**Installation auf macOS**

```
brew install croc
```


## Ausführung
**Datei senden**

```
croc send [file(s)-or-folder]
```

**Dateien empfangen**

```
croc code-phrase
```


## Wenn Sie nicht programmieren
Ich möchte Dateien mit dem Croc-Tool sicher zwischen zwei Computern übertragen. Wie kann ich den mir gegebenen Codeausdruck abgleichen, wenn ich den Befehl „croc send [Dateiname]“ auf der Senderseite mit dem Befehl „croc [Codeausdruck]“ auf der Empfängerseite ausführe und die Übertragung starte? Gibt es eine besondere Einstellung, auf die ich achten sollte, um sicherzustellen, dass bei der Übertragung eine Ende-zu-Ende-Verschlüsselung erfolgt und der Vorgang sicher ist?

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/croc/
