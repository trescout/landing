# Was ist LSP?

> Language Server Protocol

LSP (Language Server Protocol) ist ein JSON-RPC-basiertes offenes Protokoll, das eine Standardkommunikation zwischen modernen Code-Editoren und Analyse-Engines von Programmiersprachen ermöglicht.

## 1. Definition und das mathematische Problem, das sie löst: M × N-Komplexität
Language Server Protocol (LSP) ist ein universelles Protokoll, das 2016 unter der Leitung von Microsoft (VS Code-Team), Red Hat und Codenvy entwickelt wurde und heute zum Eckpfeiler der Entwicklertools geworden ist.

## 2. Wie funktioniert LSP? Protokollarchitektur und JSON-RPC 2.0
LSP ist ein JSON-RPC 2.0-Nachrichtenprotokoll zwischen dem Editor (Client) und der Sprachanalyse-Engine (Server), das normalerweise über lokale Standardeingabe/-ausgabe (stdin/stdout) oder lokale Sockets (IPC) funktioniert.

## 3. Die am häufigsten verwendeten Sprachserver im Ökosystem

## 4. LSP vs. DAP vs. LSIF/SCIP

## Häufige Fragen
**Was bedeutet LSP und wofür steht es?**
Es steht für Language Server Protocol. Es handelt sich um ein offenes Protokoll, das die Kommunikation zwischen Code-Editoren und den Syntax-, Typprüfungs- und Autovervollständigungs-Engines von Programmiersprachen standardisiert.

**Warum löst LSP das M × N-Problem?**
Im alten Modell mussten für M-Sprachen und N-Editoren M × N-Plug-Ins speziell für jeden Editor geschrieben werden. Mit LSP schreibt jede Sprache einen einzelnen Server und jeder Editor schreibt einen einzelnen Client, wodurch die M + N-Integrationsformel erreicht wird.

**Wie verhindert LSP, dass der Editor langsamer wird?**
Die Analyse des schweren Syntaxbaums (AST) und die Typanalyse der Sprache werden in Hintergrundprozessen (über JSON-RPC) ausgeführt, die vom Haupteditorprozess isoliert sind. Daher stürzt die Schnittstelle nie ab.

**Was ist der Unterschied zwischen DAP und LSP?**
Während LSP Code-Schreib-, Code-Vervollständigungs- und Syntaxfehler analysiert; DAP (Debug Adapter Protocol) ermöglicht das schrittweise Debuggen des Codes durch das Setzen von Haltepunkten zur Laufzeit.


## Verwandte Begriffe
- [Agentic Coding Tool](/de/dictionary/agentic-coding-tool/)
- [CLI](/de/dictionary/cli/)
- [Keybindings](/de/dictionary/keybindings/)
- [Code Snippets](/de/dictionary/code-snippets/)
- [Runtime](/de/dictionary/runtime/)

## Verwandte Werkzeuge
- [Oh My Pi](/de/discover/oh-my-pi/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/lsp/
