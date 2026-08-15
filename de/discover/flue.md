# TypeScript-Framework für KI-Agenten

Flue wurde vom Astro-Team entwickelt und zeichnet sich durch ein TypeScript-basiertes Sandbox-Agent-Framework aus. Diese Struktur ermöglicht es Entwicklern, Agenten für künstliche Intelligenz in sicheren und isolierten Umgebungen zu erstellen.

- ★ 7.625
- TypeScript
- GitHub Trending · 2026-06-06

## Was es bringt
- Erstellen programmierbarer und kopfloser Agenten basierend auf TypeScript.
- Schnelle und skalierbare Arbeitsumgebung mit virtueller Sandbox.
- Vielseitige Bereitstellung über Node.js-, Cloudflare- und CI/CD-Prozesse hinweg.

## Installation
**Node.js-Entwicklungsserver**

```
flue dev --target node
```

**Zusammenstellung**

```
flue build --target node          # Node.js server (single bundled .mjs)
flue build --target cloudflare    # Cloudflare Workers + Durable Objects
```


## Ausführung
**Ausführen des Hello World-Workflows**

```
flue run hello --target node \
  --payload '{"text": "Hello world", "language": "French"}'
```


## Wenn Sie nicht programmieren
Ich möchte mithilfe des Flue-Frameworks einen Agenten für künstliche Intelligenz entwickeln. Wie kann ich in meinem Projekt einen Workflow mit TypeScript definieren? Wie kann ich konkret das Modell mit der Funktion „createAgent“ konfigurieren und über session.prompt mit meinem Agenten interagieren? Können Sie anhand eines einfachen „Hallo Welt“-Beispiels Schritt für Schritt erklären, wie ich einen Agenten zur Laufzeit starten und Ergebnisse erzielen kann?

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/flue/
