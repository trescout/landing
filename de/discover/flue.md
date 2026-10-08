# TypeScript-Framework für KI-Agenten

Flue wurde vom Astro-Team entwickelt und zeichnet sich durch ein TypeScript-basiertes Sandbox-Agent-Framework aus. Diese Struktur ermöglicht es Entwicklern, Agenten für künstliche Intelligenz in sicheren und isolierten Umgebungen zu erstellen.

- ★ 8.393
- TypeScript
- GitHub Trending · 2026-06-06

## Aktualisierungen

- **29. September 2026:** Sterne 8,374 → 8,393, neueste Version @flue/cli@2.2.2 (28. September 2026).
- **27. September 2026:** Sterne 8,295 → 8,374, neueste Version @flue/cli@2.1.1 (23. September 2026).
- **19. September 2026:** Sterne 8,255 → 8,295, neueste Version @flue/cli@2.1.0 (18. September 2026).
- **17. September 2026:** Sterne 8,244 → 8,255, neueste Version @flue/cli@2.0.8 (16. September 2026).

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

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte mithilfe des Flue-Frameworks einen Agenten für künstliche Intelligenz entwickeln. Wie kann ich in meinem Projekt einen Workflow mit TypeScript definieren? Wie kann ich konkret das Modell mit der Funktion „createAgent“ konfigurieren und über session.prompt mit meinem Agenten interagieren? Können Sie anhand eines einfachen „Hallo Welt“-Beispiels Schritt für Schritt erklären, wie ich einen Agenten zur Laufzeit starten und Ergebnisse erzielen kann?

## Verwandte Begriffe aus dem Glossar

- [Sandbox Agent Framework](https://trescout.com/de/dictionary/sandbox-agent-framework/)
- [Prompt](https://trescout.com/de/dictionary/prompt/)
- [CI/CD](https://trescout.com/de/dictionary/ci-cd/)
- [Sandbox](https://trescout.com/de/dictionary/sandbox/)
- [Runtime](https://trescout.com/de/dictionary/runtime/)
- [Framework](https://trescout.com/de/dictionary/framework/)

- **Für wen es gedacht ist:** Es eignet sich für Softwareentwickler, die mit TypeScript eigene autonome Agenten für künstliche Intelligenz entwickeln und auf verschiedenen Plattformen ausführen möchten.
- **Lizenz:** Apache-2.0

## Links

- [GitHub-Repository →](https://github.com/withastro/flue)
- [Auf Türkisch lesen →](https://trescout.com/discover/flue/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-06-06 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/flue/
